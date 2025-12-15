from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from pydantic import StrictBool
from yapily.models.account_api_list_response import AccountApiListResponse
from yapily.models.api_list_response_of_account_statement import (
    ApiListResponseOfAccountStatement,
)
from yapily.models.api_list_response_of_beneficiary import ApiListResponseOfBeneficiary
from yapily.models.api_list_response_of_category import ApiListResponseOfCategory
from yapily.models.api_list_response_of_direct_debit_response import (
    ApiListResponseOfDirectDebitResponse,
)
from yapily.models.api_list_response_of_payment_response import (
    ApiListResponseOfPaymentResponse,
)
from yapily.models.api_list_response_of_real_time_transaction import (
    ApiListResponseOfRealTimeTransaction,
)
from yapily.models.api_list_response_of_transaction import ApiListResponseOfTransaction
from yapily.models.api_response_of_account import ApiResponseOfAccount
from yapily.models.api_response_of_account_statement import (
    ApiResponseOfAccountStatement,
)
from yapily.models.api_response_of_balances import ApiResponseOfBalances
from yapily.models.api_response_of_identity import ApiResponseOfIdentity
from yapily.models.sort_enum import SortEnum
from yapily.api_client import ApiClient, RequestSerialized
from yapily.api_response import ApiResponse
from yapily.rest import RESTResponseType


class FinancialDataApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def get_account(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponseOfAccount:
        _param = self._get_account_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfAccount",
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
    async def get_account_with_http_info(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiResponseOfAccount]:
        _param = self._get_account_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfAccount",
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
    async def get_account_without_preload_content(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_account_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfAccount",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_account_serialize(
        self,
        account_id,
        consent,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
        sub_application,
        raw,
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
        if raw is not None:
            _query_params.append(("raw", raw))
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
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}",
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
    async def get_account_balances(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponseOfBalances:
        _param = self._get_account_balances_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfBalances",
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
    async def get_account_balances_with_http_info(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiResponseOfBalances]:
        _param = self._get_account_balances_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfBalances",
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
    async def get_account_balances_without_preload_content(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_account_balances_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfBalances",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_account_balances_serialize(
        self,
        account_id,
        consent,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
        sub_application,
        raw,
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
        if raw is not None:
            _query_params.append(("raw", raw))
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
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/balances",
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
    async def get_account_direct_debits(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiListResponseOfDirectDebitResponse:
        _param = self._get_account_direct_debits_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfDirectDebitResponse",
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
    async def get_account_direct_debits_with_http_info(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiListResponseOfDirectDebitResponse]:
        _param = self._get_account_direct_debits_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfDirectDebitResponse",
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
    async def get_account_direct_debits_without_preload_content(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_account_direct_debits_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfDirectDebitResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_account_direct_debits_serialize(
        self,
        account_id,
        consent,
        sub_application,
        limit,
        raw,
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
        if limit is not None:
            _query_params.append(("limit", limit))
        if raw is not None:
            _query_params.append(("raw", raw))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/direct-debits",
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
    async def get_account_periodic_payments(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiListResponseOfPaymentResponse:
        _param = self._get_account_periodic_payments_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfPaymentResponse",
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
    async def get_account_periodic_payments_with_http_info(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiListResponseOfPaymentResponse]:
        _param = self._get_account_periodic_payments_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfPaymentResponse",
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
    async def get_account_periodic_payments_without_preload_content(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_account_periodic_payments_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfPaymentResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_account_periodic_payments_serialize(
        self,
        account_id,
        consent,
        sub_application,
        limit,
        raw,
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
        if limit is not None:
            _query_params.append(("limit", limit))
        if raw is not None:
            _query_params.append(("raw", raw))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/periodic-payments",
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
    async def get_account_scheduled_payments(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiListResponseOfPaymentResponse:
        _param = self._get_account_scheduled_payments_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfPaymentResponse",
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
    async def get_account_scheduled_payments_with_http_info(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiListResponseOfPaymentResponse]:
        _param = self._get_account_scheduled_payments_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfPaymentResponse",
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
    async def get_account_scheduled_payments_without_preload_content(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_account_scheduled_payments_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            limit=limit,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfPaymentResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_account_scheduled_payments_serialize(
        self,
        account_id,
        consent,
        sub_application,
        limit,
        raw,
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
        if limit is not None:
            _query_params.append(("limit", limit))
        if raw is not None:
            _query_params.append(("raw", raw))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/scheduled-payments",
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
    async def get_accounts(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> AccountApiListResponse:
        _param = self._get_accounts_serialize(
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "AccountApiListResponse",
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
    async def get_accounts_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[AccountApiListResponse]:
        _param = self._get_accounts_serialize(
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "AccountApiListResponse",
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
    async def get_accounts_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_accounts_serialize(
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "AccountApiListResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_accounts_serialize(
        self,
        consent,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
        sub_application,
        raw,
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
        if raw is not None:
            _query_params.append(("raw", raw))
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
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts",
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
    async def get_beneficiaries(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiListResponseOfBeneficiary:
        _param = self._get_beneficiaries_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfBeneficiary",
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
    async def get_beneficiaries_with_http_info(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiListResponseOfBeneficiary]:
        _param = self._get_beneficiaries_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfBeneficiary",
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
    async def get_beneficiaries_without_preload_content(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_beneficiaries_serialize(
            account_id=account_id,
            consent=consent,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfBeneficiary",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_beneficiaries_serialize(
        self,
        account_id,
        consent,
        sub_application,
        raw,
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
        if raw is not None:
            _query_params.append(("raw", raw))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/beneficiaries",
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
    async def get_categories(
        self,
        country: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The 2 letter country code e.g. 'GB'."),
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
    ) -> ApiListResponseOfCategory:
        _param = self._get_categories_serialize(
            country=country,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfCategory",
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
    async def get_categories_with_http_info(
        self,
        country: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The 2 letter country code e.g. 'GB'."),
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
    ) -> ApiResponse[ApiListResponseOfCategory]:
        _param = self._get_categories_serialize(
            country=country,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfCategory",
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
    async def get_categories_without_preload_content(
        self,
        country: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The 2 letter country code e.g. 'GB'."),
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
        _param = self._get_categories_serialize(
            country=country,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfCategory",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_categories_serialize(
        self,
        country,
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
        if country is not None:
            _path_params["country"] = country
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/categories/{country}",
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
    async def get_identity(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponseOfIdentity:
        _param = self._get_identity_serialize(
            consent=consent,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfIdentity",
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
    async def get_identity_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiResponseOfIdentity]:
        _param = self._get_identity_serialize(
            consent=consent,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfIdentity",
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
    async def get_identity_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_identity_serialize(
            consent=consent,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfIdentity",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_identity_serialize(
        self,
        consent,
        sub_application,
        raw,
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
        if raw is not None:
            _query_params.append(("raw", raw))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/identity",
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
    async def get_real_time_transactions(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        psu_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_corporate_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_ip_address: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        var_from: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        before: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. The cursor token supplied by a previous call. The cursor represents a location in the data set."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiListResponseOfRealTimeTransaction:
        _param = self._get_real_time_transactions_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            var_from=var_from,
            before=before,
            cursor=cursor,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfRealTimeTransaction",
            "401": "ApiResponseError",
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
    async def get_real_time_transactions_with_http_info(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        psu_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_corporate_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_ip_address: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        var_from: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        before: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. The cursor token supplied by a previous call. The cursor represents a location in the data set."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiListResponseOfRealTimeTransaction]:
        _param = self._get_real_time_transactions_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            var_from=var_from,
            before=before,
            cursor=cursor,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfRealTimeTransaction",
            "401": "ApiResponseError",
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
    async def get_real_time_transactions_without_preload_content(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        psu_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_corporate_id: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        psu_ip_address: Annotated[
            Optional[StrictStr],
            Field(
                description="__Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required."
            ),
        ] = None,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        var_from: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        before: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ)."
            ),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(
                description="__Optional__. The cursor token supplied by a previous call. The cursor represents a location in the data set."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_real_time_transactions_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            var_from=var_from,
            before=before,
            cursor=cursor,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfRealTimeTransaction",
            "401": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_real_time_transactions_serialize(
        self,
        account_id,
        consent,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
        sub_application,
        var_from,
        before,
        cursor,
        raw,
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
        if var_from is not None:
            _query_params.append(("from", var_from))
        if before is not None:
            _query_params.append(("before", before))
        if cursor is not None:
            _query_params.append(("cursor", cursor))
        if raw is not None:
            _query_params.append(("raw", raw))
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
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/real-time/transactions",
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
    async def get_statement(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        statement_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The statement Id of the statement file."),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponseOfAccountStatement:
        _param = self._get_statement_serialize(
            consent=consent,
            account_id=account_id,
            statement_id=statement_id,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfAccountStatement",
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
    async def get_statement_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        statement_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The statement Id of the statement file."),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiResponseOfAccountStatement]:
        _param = self._get_statement_serialize(
            consent=consent,
            account_id=account_id,
            statement_id=statement_id,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfAccountStatement",
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
    async def get_statement_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        statement_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The statement Id of the statement file."),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_statement_serialize(
            consent=consent,
            account_id=account_id,
            statement_id=statement_id,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfAccountStatement",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_statement_serialize(
        self,
        consent,
        account_id,
        statement_id,
        sub_application,
        raw,
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
        if statement_id is not None:
            _path_params["statementId"] = statement_id
        if raw is not None:
            _query_params.append(("raw", raw))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/statements/{statementId}",
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
    async def get_statement_file(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        statement_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The statement Id of the statement file."),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> bytearray:
        _param = self._get_statement_file_serialize(
            consent=consent,
            account_id=account_id,
            statement_id=statement_id,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "bytearray",
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
    async def get_statement_file_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        statement_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The statement Id of the statement file."),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[bytearray]:
        _param = self._get_statement_file_serialize(
            consent=consent,
            account_id=account_id,
            statement_id=statement_id,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "bytearray",
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
    async def get_statement_file_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        statement_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The statement Id of the statement file."),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_statement_file_serialize(
            consent=consent,
            account_id=account_id,
            statement_id=statement_id,
            sub_application=sub_application,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "bytearray",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_statement_file_serialize(
        self,
        consent,
        account_id,
        statement_id,
        sub_application,
        raw,
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
        if statement_id is not None:
            _path_params["statementId"] = statement_id
        if raw is not None:
            _query_params.append(("raw", raw))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/pdf", "application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/statements/{statementId}/file",
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
    async def get_statements(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
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
        sort: Annotated[
            Optional[SortEnum],
            Field(
                description="__Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending"
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiListResponseOfAccountStatement:
        _param = self._get_statements_serialize(
            consent=consent,
            account_id=account_id,
            sub_application=sub_application,
            var_from=var_from,
            before=before,
            limit=limit,
            sort=sort,
            offset=offset,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfAccountStatement",
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
    async def get_statements_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
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
        sort: Annotated[
            Optional[SortEnum],
            Field(
                description="__Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending"
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiListResponseOfAccountStatement]:
        _param = self._get_statements_serialize(
            consent=consent,
            account_id=account_id,
            sub_application=sub_application,
            var_from=var_from,
            before=before,
            limit=limit,
            sort=sort,
            offset=offset,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfAccountStatement",
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
    async def get_statements_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The sub-application ID to which event type is being subscribed to"
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
        sort: Annotated[
            Optional[SortEnum],
            Field(
                description="__Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending"
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_statements_serialize(
            consent=consent,
            account_id=account_id,
            sub_application=sub_application,
            var_from=var_from,
            before=before,
            limit=limit,
            sort=sort,
            offset=offset,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfAccountStatement",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_statements_serialize(
        self,
        consent,
        account_id,
        sub_application,
        var_from,
        before,
        limit,
        sort,
        offset,
        raw,
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
        if var_from is not None:
            _query_params.append(("from", var_from))
        if before is not None:
            _query_params.append(("before", before))
        if limit is not None:
            _query_params.append(("limit", limit))
        if sort is not None:
            _query_params.append(("sort", sort.value))
        if offset is not None:
            _query_params.append(("offset", offset))
        if raw is not None:
            _query_params.append(("raw", raw))
        if consent is not None:
            _header_params["consent"] = consent
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/statements",
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
    async def get_transactions(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        var_with: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Acceptable value: `categorisation`. When set, will include enrichment data in the transactions returned. <br><br>Enrichment data is optional, e.g. when 'categorisation' enrichment data is requested, the enrichment response will include categorisation data and merchant name, only if it can be evaluated from the transaction. This service is limited for UK institution transactions currently. __This is a legacy feature and will be deprecated. Date TBC__"
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
        sort: Annotated[
            Optional[SortEnum],
            Field(
                description="__Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending"
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(description="__Optional__. This property is not currently in use."),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiListResponseOfTransaction:
        _param = self._get_transactions_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            var_with=var_with,
            var_from=var_from,
            before=before,
            limit=limit,
            sort=sort,
            offset=offset,
            cursor=cursor,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfTransaction",
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
    async def get_transactions_with_http_info(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        var_with: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Acceptable value: `categorisation`. When set, will include enrichment data in the transactions returned. <br><br>Enrichment data is optional, e.g. when 'categorisation' enrichment data is requested, the enrichment response will include categorisation data and merchant name, only if it can be evaluated from the transaction. This service is limited for UK institution transactions currently. __This is a legacy feature and will be deprecated. Date TBC__"
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
        sort: Annotated[
            Optional[SortEnum],
            Field(
                description="__Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending"
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(description="__Optional__. This property is not currently in use."),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiListResponseOfTransaction]:
        _param = self._get_transactions_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            var_with=var_with,
            var_from=var_from,
            before=before,
            limit=limit,
            sort=sort,
            offset=offset,
            cursor=cursor,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfTransaction",
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
    async def get_transactions_without_preload_content(
        self,
        account_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The account Id of the user's bank account."
            ),
        ],
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
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
        var_with: Annotated[
            Optional[List[StrictStr]],
            Field(
                description="__Optional__. Acceptable value: `categorisation`. When set, will include enrichment data in the transactions returned. <br><br>Enrichment data is optional, e.g. when 'categorisation' enrichment data is requested, the enrichment response will include categorisation data and merchant name, only if it can be evaluated from the transaction. This service is limited for UK institution transactions currently. __This is a legacy feature and will be deprecated. Date TBC__"
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
        sort: Annotated[
            Optional[SortEnum],
            Field(
                description="__Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending"
            ),
        ] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description="__Optional__. The number of transaction records to be skipped. Used primarily with paginated results."
            ),
        ] = None,
        cursor: Annotated[
            Optional[StrictStr],
            Field(description="__Optional__. This property is not currently in use."),
        ] = None,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._get_transactions_serialize(
            account_id=account_id,
            consent=consent,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            var_with=var_with,
            var_from=var_from,
            before=before,
            limit=limit,
            sort=sort,
            offset=offset,
            cursor=cursor,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiListResponseOfTransaction",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_transactions_serialize(
        self,
        account_id,
        consent,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
        sub_application,
        var_with,
        var_from,
        before,
        limit,
        sort,
        offset,
        cursor,
        raw,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {
            "with": "multi",
        }
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
        if var_with is not None:
            _query_params.append(("with", var_with))
        if var_from is not None:
            _query_params.append(("from", var_from))
        if before is not None:
            _query_params.append(("before", before))
        if limit is not None:
            _query_params.append(("limit", limit))
        if sort is not None:
            _query_params.append(("sort", sort.value))
        if offset is not None:
            _query_params.append(("offset", offset))
        if cursor is not None:
            _query_params.append(("cursor", cursor))
        if raw is not None:
            _query_params.append(("raw", raw))
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
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/accounts/{accountId}/transactions",
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
