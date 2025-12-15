from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from pydantic import StrictBool
from yapily.models.api_list_response_of_consent import ApiListResponseOfConsent
from yapily.models.api_response_of_consent import ApiResponseOfConsent
from yapily.models.api_response_of_consent_delete_response import (
    ApiResponseOfConsentDeleteResponse,
)
from yapily.models.consent import Consent
from yapily.models.consent_auth_code_request import ConsentAuthCodeRequest
from yapily.models.extend_consent_request import ExtendConsentRequest
from yapily.models.one_time_token_request import OneTimeTokenRequest
from yapily.api_client import ApiClient, RequestSerialized
from yapily.api_response import ApiResponse
from yapily.rest import RESTResponseType


class ConsentsApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def create_consent_with_code(
        self,
        consent_auth_code_request: ConsentAuthCodeRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Consent:
        _param = self._create_consent_with_code_serialize(
            consent_auth_code_request=consent_auth_code_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "Consent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    async def create_consent_with_code_with_http_info(
        self,
        consent_auth_code_request: ConsentAuthCodeRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Consent]:
        _param = self._create_consent_with_code_serialize(
            consent_auth_code_request=consent_auth_code_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "Consent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    async def create_consent_with_code_without_preload_content(
        self,
        consent_auth_code_request: ConsentAuthCodeRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        _param = self._create_consent_with_code_serialize(
            consent_auth_code_request=consent_auth_code_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "Consent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_consent_with_code_serialize(
        self,
        consent_auth_code_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None
        if consent_auth_code_request is not None:
            _body_params = consent_auth_code_request
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="POST",
            resource_path="/consent-auth-code",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def delete(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        force_delete: Annotated[
            Optional[StrictBool],
            Field(description="__Optional__. Whether to force the deletion."),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponseOfConsentDeleteResponse:
        _param = self._delete_serialize(
            consent_id=consent_id,
            force_delete=force_delete,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsentDeleteResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    async def delete_with_http_info(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        force_delete: Annotated[
            Optional[StrictBool],
            Field(description="__Optional__. Whether to force the deletion."),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiResponseOfConsentDeleteResponse]:
        _param = self._delete_serialize(
            consent_id=consent_id,
            force_delete=force_delete,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsentDeleteResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    async def delete_without_preload_content(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        force_delete: Annotated[
            Optional[StrictBool],
            Field(description="__Optional__. Whether to force the deletion."),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        _param = self._delete_serialize(
            consent_id=consent_id,
            force_delete=force_delete,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsentDeleteResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _delete_serialize(
        self,
        consent_id,
        force_delete,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None
        if consent_id is not None:
            _path_params["consentId"] = consent_id
        if force_delete is not None:
            _query_params.append(("forceDelete", force_delete))
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="DELETE",
            resource_path="/consents/{consentId}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def extend_consent(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        extend_consent_request: ExtendConsentRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponseOfConsent:
        _param = self._extend_consent_serialize(
            consent_id=consent_id,
            extend_consent_request=extend_consent_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsent",
            "400": "ApiErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    async def extend_consent_with_http_info(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        extend_consent_request: ExtendConsentRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiResponseOfConsent]:
        _param = self._extend_consent_serialize(
            consent_id=consent_id,
            extend_consent_request=extend_consent_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsent",
            "400": "ApiErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    async def extend_consent_without_preload_content(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        extend_consent_request: ExtendConsentRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        _param = self._extend_consent_serialize(
            consent_id=consent_id,
            extend_consent_request=extend_consent_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsent",
            "400": "ApiErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _extend_consent_serialize(
        self,
        consent_id,
        extend_consent_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None
        if consent_id is not None:
            _path_params["consentId"] = consent_id
        if extend_consent_request is not None:
            _body_params = extend_consent_request
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json;charset=UTF-8"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="POST",
            resource_path="/consents/{consentId}/extend",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def get_consent_by_id(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponseOfConsent:
        _param = self._get_consent_by_id_serialize(
            consent_id=consent_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    async def get_consent_by_id_with_http_info(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiResponseOfConsent]:
        _param = self._get_consent_by_id_serialize(
            consent_id=consent_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    async def get_consent_by_id_without_preload_content(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        _param = self._get_consent_by_id_serialize(
            consent_id=consent_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfConsent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_consent_by_id_serialize(
        self,
        consent_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None
        if consent_id is not None:
            _path_params["consentId"] = consent_id
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/consents/{consentId}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def get_consent_by_single_access_consent(
        self,
        one_time_token_request: OneTimeTokenRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Consent:
        _param = self._get_consent_by_single_access_consent_serialize(
            one_time_token_request=one_time_token_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "Consent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    async def get_consent_by_single_access_consent_with_http_info(
        self,
        one_time_token_request: OneTimeTokenRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Consent]:
        _param = self._get_consent_by_single_access_consent_serialize(
            one_time_token_request=one_time_token_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "Consent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    async def get_consent_by_single_access_consent_without_preload_content(
        self,
        one_time_token_request: OneTimeTokenRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        _param = self._get_consent_by_single_access_consent_serialize(
            one_time_token_request=one_time_token_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "Consent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_consent_by_single_access_consent_serialize(
        self,
        one_time_token_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None
        if one_time_token_request is not None:
            _body_params = one_time_token_request
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="POST",
            resource_path="/consent-one-time-token",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def get_consents(
        self,
        filter_application_user_id: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `applicationUserId` users provided."
            ),
        ] = None,
        filter_user_uuid: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `userUuid` users provided."
            ),
        ] = None,
        filter_institution: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `Institution` provided."
            ),
        ] = None,
        filter_status: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `Consent` [statuses](https://docs.yapily.com/api/reference/#operation/getConsents!c=200&path=data/status&t=response)."
            ),
        ] = None,
        var_from: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). "
            ),
        ] = None,
        before: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiListResponseOfConsent:
        _param = self._get_consents_serialize(
            filter_application_user_id=filter_application_user_id,
            filter_user_uuid=filter_user_uuid,
            filter_institution=filter_institution,
            filter_status=filter_status,
            var_from=var_from,
            before=before,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfConsent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    async def get_consents_with_http_info(
        self,
        filter_application_user_id: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `applicationUserId` users provided."
            ),
        ] = None,
        filter_user_uuid: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `userUuid` users provided."
            ),
        ] = None,
        filter_institution: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `Institution` provided."
            ),
        ] = None,
        filter_status: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `Consent` [statuses](https://docs.yapily.com/api/reference/#operation/getConsents!c=200&path=data/status&t=response)."
            ),
        ] = None,
        var_from: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). "
            ),
        ] = None,
        before: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiListResponseOfConsent]:
        _param = self._get_consents_serialize(
            filter_application_user_id=filter_application_user_id,
            filter_user_uuid=filter_user_uuid,
            filter_institution=filter_institution,
            filter_status=filter_status,
            var_from=var_from,
            before=before,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfConsent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    async def get_consents_without_preload_content(
        self,
        filter_application_user_id: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `applicationUserId` users provided."
            ),
        ] = None,
        filter_user_uuid: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `userUuid` users provided."
            ),
        ] = None,
        filter_institution: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `Institution` provided."
            ),
        ] = None,
        filter_status: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Filter records based on the list of `Consent` [statuses](https://docs.yapily.com/api/reference/#operation/getConsents!c=200&path=data/status&t=response)."
            ),
        ] = None,
        var_from: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). "
            ),
        ] = None,
        before: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        _param = self._get_consents_serialize(
            filter_application_user_id=filter_application_user_id,
            filter_user_uuid=filter_user_uuid,
            filter_institution=filter_institution,
            filter_status=filter_status,
            var_from=var_from,
            before=before,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfConsent",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_consents_serialize(
        self,
        filter_application_user_id,
        filter_user_uuid,
        filter_institution,
        filter_status,
        var_from,
        before,
        limit,
        offset,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {
            "filter[applicationUserId]": "multi",
            "filter[userUuid]": "multi",
            "filter[institution]": "multi",
            "filter[status]": "multi",
        }
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None
        if filter_application_user_id is not None:
            _query_params.append(
                ("filter[applicationUserId]", filter_application_user_id)
            )
        if filter_user_uuid is not None:
            _query_params.append(("filter[userUuid]", filter_user_uuid))
        if filter_institution is not None:
            _query_params.append(("filter[institution]", filter_institution))
        if filter_status is not None:
            _query_params.append(("filter[status]", filter_status))
        if var_from is not None:
            _query_params.append(("from", var_from))
        if before is not None:
            _query_params.append(("before", before))
        if limit is not None:
            _query_params.append(("limit", limit))
        if offset is not None:
            _query_params.append(("offset", offset))
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/consents",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
