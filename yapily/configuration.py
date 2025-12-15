import copy
import http.client as httplib
import logging
from logging import FileHandler
import sys
from typing import Any, ClassVar, Dict, List, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired, Self
import urllib3

JSON_SCHEMA_VALIDATION_KEYWORDS = {
    "multipleOf",
    "maximum",
    "exclusiveMaximum",
    "minimum",
    "exclusiveMinimum",
    "maxLength",
    "minLength",
    "pattern",
    "maxItems",
    "minItems",
}
ServerVariablesT = Dict[str, str]
GenericAuthSetting = TypedDict(
    "GenericAuthSetting",
    {
        "type": str,
        "in": str,
        "key": str,
        "value": str,
    },
)
OAuth2AuthSetting = TypedDict(
    "OAuth2AuthSetting",
    {
        "type": Literal["oauth2"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": str,
    },
)
APIKeyAuthSetting = TypedDict(
    "APIKeyAuthSetting",
    {
        "type": Literal["api_key"],
        "in": str,
        "key": str,
        "value": Optional[str],
    },
)
BasicAuthSetting = TypedDict(
    "BasicAuthSetting",
    {
        "type": Literal["basic"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": Optional[str],
    },
)
BearerFormatAuthSetting = TypedDict(
    "BearerFormatAuthSetting",
    {
        "type": Literal["bearer"],
        "in": Literal["header"],
        "format": Literal["JWT"],
        "key": Literal["Authorization"],
        "value": str,
    },
)
BearerAuthSetting = TypedDict(
    "BearerAuthSetting",
    {
        "type": Literal["bearer"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": str,
    },
)
HTTPSignatureAuthSetting = TypedDict(
    "HTTPSignatureAuthSetting",
    {
        "type": Literal["http-signature"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": None,
    },
)
AuthSettings = TypedDict(
    "AuthSettings",
    {
        "basicAuth": BasicAuthSetting,
    },
    total=False,
)


class HostSettingVariable(TypedDict):
    description: str
    default_value: str
    enum_values: List[str]


class HostSetting(TypedDict):
    url: str
    description: str
    variables: NotRequired[Dict[str, HostSettingVariable]]


class Configuration:
    _default: ClassVar[Optional[Self]] = None

    def __init__(
        self,
        host: Optional[str] = None,
        api_key: Optional[Dict[str, str]] = None,
        api_key_prefix: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_token: Optional[str] = None,
        server_index: Optional[int] = None,
        server_variables: Optional[ServerVariablesT] = None,
        server_operation_index: Optional[Dict[int, int]] = None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]] = None,
        ignore_operation_servers: bool = False,
        ssl_ca_cert: Optional[str] = None,
        retries: Optional[int] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ) -> None:
        self._base_path = "https://api.yapily.com" if host is None else host
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        self.ignore_operation_servers = ignore_operation_servers
        self.temp_folder_path = None
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        self.username = username
        self.password = password
        self.access_token = access_token
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("yapily")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = "%(asctime)s %(levelname)s %(message)s"
        self.logger_stream_handler = None
        self.logger_file_handler: Optional[FileHandler] = None
        self.logger_file = None
        if debug is not None:
            self.debug = debug
        else:
            self.__debug = False
        """Debug switch
        """
        self.verify_ssl = True
        self.ssl_ca_cert = ssl_ca_cert
        self.ca_cert_data = ca_cert_data
        self.cert_file = None
        self.key_file = None
        self.assert_hostname = None
        self.tls_server_name = None
        self.connection_pool_maxsize = 100
        self.proxy: Optional[str] = None
        self.proxy_headers = None
        self.safe_chars_for_path_param = ""
        self.retries = retries
        self.client_side_validation = True
        self.socket_options = None
        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        self.date_format = "%Y-%m-%d"

    def __deepcopy__(self, memo: Dict[int, Any]) -> Self:
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ("logger", "logger_file_handler"):
                setattr(result, k, copy.deepcopy(v, memo))
        result.logger = copy.copy(self.logger)
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default: Optional[Self]) -> None:
        cls._default = default

    @classmethod
    def get_default_copy(cls) -> Self:
        return cls.get_default()

    @classmethod
    def get_default(cls) -> Self:
        if cls._default is None:
            cls._default = cls()
        return cls._default

    @property
    def logger_file(self) -> Optional[str]:
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value: Optional[str]) -> None:
        self.__logger_file = value
        if self.__logger_file:
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, value: bool) -> None:
        self.__debug = value
        if self.__debug:
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            httplib.HTTPConnection.debuglevel = 1
        else:
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self) -> str:
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value: str) -> None:
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(
        self, identifier: str, alias: Optional[str] = None
    ) -> Optional[str]:
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(
            identifier, self.api_key.get(alias) if alias is not None else None
        )
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key
        return None

    def get_basic_auth_token(self) -> Optional[str]:
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(basic_auth=username + ":" + password).get(
            "authorization"
        )

    def auth_settings(self) -> AuthSettings:
        auth: AuthSettings = {}
        if self.username is not None and self.password is not None:
            auth["basicAuth"] = {
                "type": "basic",
                "in": "header",
                "key": "Authorization",
                "value": self.get_basic_auth_token(),
            }
        return auth

    def to_debug_report(self) -> str:
        return (
            "Python SDK Debug Report:\n"
            "OS: {env}\n"
            "Python Version: {pyversion}\n"
            "Version of the API: 7.2.0\n"
            "SDK Package Version: 1.0.0".format(env=sys.platform, pyversion=sys.version)
        )

    def get_host_settings(self) -> List[HostSetting]:
        return [
            {
                "url": "https://api.yapily.com",
                "description": "No description provided",
            }
        ]

    def get_host_from_settings(
        self,
        index: Optional[int],
        variables: Optional[ServerVariablesT] = None,
        servers: Optional[List[HostSetting]] = None,
    ) -> str:
        if index is None:
            return self._base_path
        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers
        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers))
            )
        url = server["url"]
        for variable_name, variable in server.get("variables", {}).items():
            used_value = variables.get(variable_name, variable["default_value"])
            if "enum_values" in variable and used_value not in variable["enum_values"]:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name], variable["enum_values"]
                    )
                )
            url = url.replace("{" + variable_name + "}", used_value)
        return url

    @property
    def host(self) -> str:
        return self.get_host_from_settings(
            self.server_index, variables=self.server_variables
        )

    @host.setter
    def host(self, value: str) -> None:
        self._base_path = value
        self.server_index = None
