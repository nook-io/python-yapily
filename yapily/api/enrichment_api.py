from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from yapily.models.get_accounts_transactions_categorised200_response import (
    GetAccountsTransactionsCategorised200Response,
)
from yapily.models.get_categorisation_account_type200_response import (
    GetCategorisationAccountType200Response,
)
from yapily.models.post_accounts_account_id_transactions_categorisation201_response import (
    PostAccountsAccountIdTransactionsCategorisation201Response,
)
from yapily.models.post_accounts_account_id_transactions_categorisation_request import (
    PostAccountsAccountIdTransactionsCategorisationRequest,
)
from yapily.api_client import ApiClient, RequestSerialized
from yapily.api_response import ApiResponse
from yapily.rest import RESTResponseType


class EnrichmentApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def get_accounts_transactions_categorised(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr, Field(description="Unique identifier for account")
        ],
        categorisation_id: Annotated[
            StrictStr,
            Field(
                description="Unique identifier for transaction categorisation request"
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[Annotated[int, Field(le=1000, strict=True, ge=100)]],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 100 and 1000. If not specified will default to 100."
            ),
        ] = None,
        page: Annotated[
            Optional[Annotated[int, Field(strict=True, ge=1)]],
            Field(
                description="__Optional__. The page number to be returned. If not specified will default to 1."
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
    ) -> GetAccountsTransactionsCategorised200Response:
        _param = self._get_accounts_transactions_categorised_serialize(
            consent=consent,
            account_id=account_id,
            categorisation_id=categorisation_id,
            sub_application=sub_application,
            limit=limit,
            page=page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetAccountsTransactionsCategorised200Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "404": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
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
    async def get_accounts_transactions_categorised_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr, Field(description="Unique identifier for account")
        ],
        categorisation_id: Annotated[
            StrictStr,
            Field(
                description="Unique identifier for transaction categorisation request"
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[Annotated[int, Field(le=1000, strict=True, ge=100)]],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 100 and 1000. If not specified will default to 100."
            ),
        ] = None,
        page: Annotated[
            Optional[Annotated[int, Field(strict=True, ge=1)]],
            Field(
                description="__Optional__. The page number to be returned. If not specified will default to 1."
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
    ) -> ApiResponse[GetAccountsTransactionsCategorised200Response]:
        _param = self._get_accounts_transactions_categorised_serialize(
            consent=consent,
            account_id=account_id,
            categorisation_id=categorisation_id,
            sub_application=sub_application,
            limit=limit,
            page=page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetAccountsTransactionsCategorised200Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "404": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
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
    async def get_accounts_transactions_categorised_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr, Field(description="Unique identifier for account")
        ],
        categorisation_id: Annotated[
            StrictStr,
            Field(
                description="Unique identifier for transaction categorisation request"
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[Annotated[int, Field(le=1000, strict=True, ge=100)]],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 100 and 1000. If not specified will default to 100."
            ),
        ] = None,
        page: Annotated[
            Optional[Annotated[int, Field(strict=True, ge=1)]],
            Field(
                description="__Optional__. The page number to be returned. If not specified will default to 1."
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
        _param = self._get_accounts_transactions_categorised_serialize(
            consent=consent,
            account_id=account_id,
            categorisation_id=categorisation_id,
            sub_application=sub_application,
            limit=limit,
            page=page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetAccountsTransactionsCategorised200Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "404": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_accounts_transactions_categorised_serialize(
        self,
        consent,
        account_id,
        categorisation_id,
        sub_application,
        limit,
        page,
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
        if account_id is not None:
            _path_params["accountId"] = account_id
        if categorisation_id is not None:
            _path_params["categorisationId"] = categorisation_id
        if limit is not None:
            _query_params.append(("limit", limit))
        if page is not None:
            _query_params.append(("page", page))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json", "application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/transactions/categorisation/{categorisationId}",
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
    async def get_categorisation_account_type(
        self,
        account_type: Annotated[
            StrictStr, Field(description="type of bank account (consumer or business)")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
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
    ) -> GetCategorisationAccountType200Response:
        _param = self._get_categorisation_account_type_serialize(
            account_type=account_type,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetCategorisationAccountType200Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "404": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
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
    async def get_categorisation_account_type_with_http_info(
        self,
        account_type: Annotated[
            StrictStr, Field(description="type of bank account (consumer or business)")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
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
    ) -> ApiResponse[GetCategorisationAccountType200Response]:
        _param = self._get_categorisation_account_type_serialize(
            account_type=account_type,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetCategorisationAccountType200Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "404": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
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
    async def get_categorisation_account_type_without_preload_content(
        self,
        account_type: Annotated[
            StrictStr, Field(description="type of bank account (consumer or business)")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
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
        _param = self._get_categorisation_account_type_serialize(
            account_type=account_type,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetCategorisationAccountType200Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "404": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_categorisation_account_type_serialize(
        self,
        account_type,
        sub_application,
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
        if account_type is not None:
            _path_params["accountType"] = account_type
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json", "application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/transactions/categorisation/categories/{accountType}",
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
    async def post_accounts_account_id_transactions_categorisation(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr, Field(description="Unique identifier for account")
        ],
        psu_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_corporate_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_ip_address: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        post_accounts_account_id_transactions_categorisation_request: Optional[
            PostAccountsAccountIdTransactionsCategorisationRequest
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
    ) -> PostAccountsAccountIdTransactionsCategorisation201Response:
        _param = self._post_accounts_account_id_transactions_categorisation_serialize(
            consent=consent,
            account_id=account_id,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            post_accounts_account_id_transactions_categorisation_request=post_accounts_account_id_transactions_categorisation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "PostAccountsAccountIdTransactionsCategorisation201Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
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
    async def post_accounts_account_id_transactions_categorisation_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr, Field(description="Unique identifier for account")
        ],
        psu_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_corporate_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_ip_address: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        post_accounts_account_id_transactions_categorisation_request: Optional[
            PostAccountsAccountIdTransactionsCategorisationRequest
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
    ) -> ApiResponse[PostAccountsAccountIdTransactionsCategorisation201Response]:
        _param = self._post_accounts_account_id_transactions_categorisation_serialize(
            consent=consent,
            account_id=account_id,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            post_accounts_account_id_transactions_categorisation_request=post_accounts_account_id_transactions_categorisation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "PostAccountsAccountIdTransactionsCategorisation201Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
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
    async def post_accounts_account_id_transactions_categorisation_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr, Field(description="Unique identifier for account")
        ],
        psu_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_corporate_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_ip_address: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        post_accounts_account_id_transactions_categorisation_request: Optional[
            PostAccountsAccountIdTransactionsCategorisationRequest
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
        _param = self._post_accounts_account_id_transactions_categorisation_serialize(
            consent=consent,
            account_id=account_id,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            post_accounts_account_id_transactions_categorisation_request=post_accounts_account_id_transactions_categorisation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "PostAccountsAccountIdTransactionsCategorisation201Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _post_accounts_account_id_transactions_categorisation_serialize(
        self,
        consent,
        account_id,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
        sub_application,
        post_accounts_account_id_transactions_categorisation_request,
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
        if account_id is not None:
            _path_params["accountId"] = account_id
        if consent is not None:
            _header_params["consent"] = consent
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if post_accounts_account_id_transactions_categorisation_request is not None:
            _body_params = post_accounts_account_id_transactions_categorisation_request
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json", "application/json;charset=UTF-8"]
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
            resource_path="/accounts/{accountId}/transactions/categorisation",
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
