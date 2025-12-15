from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from pydantic import StrictBool
from yapily.models.account_authorisation_request import AccountAuthorisationRequest
from yapily.models.api_response_of_account_authorisation_response import (
    ApiResponseOfAccountAuthorisationResponse,
)
from yapily.models.api_response_of_embedded_account_authorisation_response import (
    ApiResponseOfEmbeddedAccountAuthorisationResponse,
)
from yapily.models.api_response_of_payment_authorisation_request_response import (
    ApiResponseOfPaymentAuthorisationRequestResponse,
)
from yapily.models.api_response_of_payment_embedded_authorisation_request_response import (
    ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse,
)
from yapily.models.api_response_of_pre_authorisation_response import (
    ApiResponseOfPreAuthorisationResponse,
)
from yapily.models.bulk_payment_authorisation_request import (
    BulkPaymentAuthorisationRequest,
)
from yapily.models.bulk_payment_embedded_authorisation_request import (
    BulkPaymentEmbeddedAuthorisationRequest,
)
from yapily.models.embedded_account_authorisation_request import (
    EmbeddedAccountAuthorisationRequest,
)
from yapily.models.payment_authorisation_request import PaymentAuthorisationRequest
from yapily.models.payment_embedded_authorisation_request import (
    PaymentEmbeddedAuthorisationRequest,
)
from yapily.models.payment_pre_authorisation_request import (
    PaymentPreAuthorisationRequest,
)
from yapily.models.pre_authorisation_request import PreAuthorisationRequest
from yapily.api_client import ApiClient, RequestSerialized
from yapily.api_response import ApiResponse
from yapily.rest import RESTResponseType


class AuthorisationsApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def create_bulk_payment_authorisation(
        self,
        bulk_payment_authorisation_request: BulkPaymentAuthorisationRequest,
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
    ) -> ApiResponseOfPaymentAuthorisationRequestResponse:
        _param = self._create_bulk_payment_authorisation_serialize(
            bulk_payment_authorisation_request=bulk_payment_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPaymentAuthorisationRequestResponse",
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
    async def create_bulk_payment_authorisation_with_http_info(
        self,
        bulk_payment_authorisation_request: BulkPaymentAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentAuthorisationRequestResponse]:
        _param = self._create_bulk_payment_authorisation_serialize(
            bulk_payment_authorisation_request=bulk_payment_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPaymentAuthorisationRequestResponse",
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
    async def create_bulk_payment_authorisation_without_preload_content(
        self,
        bulk_payment_authorisation_request: BulkPaymentAuthorisationRequest,
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
        _param = self._create_bulk_payment_authorisation_serialize(
            bulk_payment_authorisation_request=bulk_payment_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPaymentAuthorisationRequestResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_bulk_payment_authorisation_serialize(
        self,
        bulk_payment_authorisation_request,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
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
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if bulk_payment_authorisation_request is not None:
            _body_params = bulk_payment_authorisation_request
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
            resource_path="/bulk-payment-auth-requests",
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
    async def create_embedded_bulk_payment_authorisation(
        self,
        bulk_payment_embedded_authorisation_request: BulkPaymentEmbeddedAuthorisationRequest,
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
    ) -> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse:
        _param = self._create_embedded_bulk_payment_authorisation_serialize(
            bulk_payment_embedded_authorisation_request=bulk_payment_embedded_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
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
    async def create_embedded_bulk_payment_authorisation_with_http_info(
        self,
        bulk_payment_embedded_authorisation_request: BulkPaymentEmbeddedAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]:
        _param = self._create_embedded_bulk_payment_authorisation_serialize(
            bulk_payment_embedded_authorisation_request=bulk_payment_embedded_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
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
    async def create_embedded_bulk_payment_authorisation_without_preload_content(
        self,
        bulk_payment_embedded_authorisation_request: BulkPaymentEmbeddedAuthorisationRequest,
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
        _param = self._create_embedded_bulk_payment_authorisation_serialize(
            bulk_payment_embedded_authorisation_request=bulk_payment_embedded_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_embedded_bulk_payment_authorisation_serialize(
        self,
        bulk_payment_embedded_authorisation_request,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
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
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if bulk_payment_embedded_authorisation_request is not None:
            _body_params = bulk_payment_embedded_authorisation_request
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
            resource_path="/embedded-bulk-payment-auth-requests",
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
    async def create_embedded_payment_authorisation(
        self,
        payment_embedded_authorisation_request: PaymentEmbeddedAuthorisationRequest,
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
    ) -> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse:
        _param = self._create_embedded_payment_authorisation_serialize(
            payment_embedded_authorisation_request=payment_embedded_authorisation_request,
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
            "201": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
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
    async def create_embedded_payment_authorisation_with_http_info(
        self,
        payment_embedded_authorisation_request: PaymentEmbeddedAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]:
        _param = self._create_embedded_payment_authorisation_serialize(
            payment_embedded_authorisation_request=payment_embedded_authorisation_request,
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
            "201": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
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
    async def create_embedded_payment_authorisation_without_preload_content(
        self,
        payment_embedded_authorisation_request: PaymentEmbeddedAuthorisationRequest,
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
        _param = self._create_embedded_payment_authorisation_serialize(
            payment_embedded_authorisation_request=payment_embedded_authorisation_request,
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
            "201": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_embedded_payment_authorisation_serialize(
        self,
        payment_embedded_authorisation_request,
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
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if payment_embedded_authorisation_request is not None:
            _body_params = payment_embedded_authorisation_request
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
            resource_path="/embedded-payment-auth-requests",
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
    async def create_payment_authorisation(
        self,
        payment_authorisation_request: PaymentAuthorisationRequest,
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
    ) -> ApiResponseOfPaymentAuthorisationRequestResponse:
        _param = self._create_payment_authorisation_serialize(
            payment_authorisation_request=payment_authorisation_request,
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
            "201": "ApiResponseOfPaymentAuthorisationRequestResponse",
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
    async def create_payment_authorisation_with_http_info(
        self,
        payment_authorisation_request: PaymentAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentAuthorisationRequestResponse]:
        _param = self._create_payment_authorisation_serialize(
            payment_authorisation_request=payment_authorisation_request,
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
            "201": "ApiResponseOfPaymentAuthorisationRequestResponse",
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
    async def create_payment_authorisation_without_preload_content(
        self,
        payment_authorisation_request: PaymentAuthorisationRequest,
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
        _param = self._create_payment_authorisation_serialize(
            payment_authorisation_request=payment_authorisation_request,
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
            "201": "ApiResponseOfPaymentAuthorisationRequestResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_payment_authorisation_serialize(
        self,
        payment_authorisation_request,
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
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if payment_authorisation_request is not None:
            _body_params = payment_authorisation_request
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
            resource_path="/payment-auth-requests",
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
    async def create_payment_pre_authorisation_request(
        self,
        payment_pre_authorisation_request: PaymentPreAuthorisationRequest,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponseOfPreAuthorisationResponse:
        _param = self._create_payment_pre_authorisation_request_serialize(
            payment_pre_authorisation_request=payment_pre_authorisation_request,
            raw=raw,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPreAuthorisationResponse",
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
    async def create_payment_pre_authorisation_request_with_http_info(
        self,
        payment_pre_authorisation_request: PaymentPreAuthorisationRequest,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
    ) -> ApiResponse[ApiResponseOfPreAuthorisationResponse]:
        _param = self._create_payment_pre_authorisation_request_serialize(
            payment_pre_authorisation_request=payment_pre_authorisation_request,
            raw=raw,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPreAuthorisationResponse",
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
    async def create_payment_pre_authorisation_request_without_preload_content(
        self,
        payment_pre_authorisation_request: PaymentPreAuthorisationRequest,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
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
        _param = self._create_payment_pre_authorisation_request_serialize(
            payment_pre_authorisation_request=payment_pre_authorisation_request,
            raw=raw,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPreAuthorisationResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_payment_pre_authorisation_request_serialize(
        self,
        payment_pre_authorisation_request,
        raw,
        psu_ip_address,
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
        if raw is not None:
            _query_params.append(("raw", raw))
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if payment_pre_authorisation_request is not None:
            _body_params = payment_pre_authorisation_request
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
            resource_path="/payment-pre-auth-requests",
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
    async def create_pre_authorisation_request(
        self,
        pre_authorisation_request: PreAuthorisationRequest,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
            ),
        ] = None,
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
    ) -> ApiResponseOfPreAuthorisationResponse:
        _param = self._create_pre_authorisation_request_serialize(
            pre_authorisation_request=pre_authorisation_request,
            raw=raw,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPreAuthorisationResponse",
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
    async def create_pre_authorisation_request_with_http_info(
        self,
        pre_authorisation_request: PreAuthorisationRequest,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
            ),
        ] = None,
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
    ) -> ApiResponse[ApiResponseOfPreAuthorisationResponse]:
        _param = self._create_pre_authorisation_request_serialize(
            pre_authorisation_request=pre_authorisation_request,
            raw=raw,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPreAuthorisationResponse",
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
    async def create_pre_authorisation_request_without_preload_content(
        self,
        pre_authorisation_request: PreAuthorisationRequest,
        raw: Annotated[
            Optional[StrictBool],
            Field(
                description="__Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>."
            ),
        ] = None,
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
        _param = self._create_pre_authorisation_request_serialize(
            pre_authorisation_request=pre_authorisation_request,
            raw=raw,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfPreAuthorisationResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_pre_authorisation_request_serialize(
        self,
        pre_authorisation_request,
        raw,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
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
        if raw is not None:
            _query_params.append(("raw", raw))
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if pre_authorisation_request is not None:
            _body_params = pre_authorisation_request
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
            resource_path="/pre-auth-requests",
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
    async def initiate_account_request(
        self,
        account_authorisation_request: AccountAuthorisationRequest,
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
    ) -> ApiResponseOfAccountAuthorisationResponse:
        _param = self._initiate_account_request_serialize(
            account_authorisation_request=account_authorisation_request,
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
            "201": "ApiResponseOfAccountAuthorisationResponse",
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
    async def initiate_account_request_with_http_info(
        self,
        account_authorisation_request: AccountAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfAccountAuthorisationResponse]:
        _param = self._initiate_account_request_serialize(
            account_authorisation_request=account_authorisation_request,
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
            "201": "ApiResponseOfAccountAuthorisationResponse",
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
    async def initiate_account_request_without_preload_content(
        self,
        account_authorisation_request: AccountAuthorisationRequest,
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
        _param = self._initiate_account_request_serialize(
            account_authorisation_request=account_authorisation_request,
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
            "201": "ApiResponseOfAccountAuthorisationResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _initiate_account_request_serialize(
        self,
        account_authorisation_request,
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
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if account_authorisation_request is not None:
            _body_params = account_authorisation_request
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
            resource_path="/account-auth-requests",
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
    async def initiate_embedded_account_request(
        self,
        embedded_account_authorisation_request: EmbeddedAccountAuthorisationRequest,
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
    ) -> ApiResponseOfEmbeddedAccountAuthorisationResponse:
        _param = self._initiate_embedded_account_request_serialize(
            embedded_account_authorisation_request=embedded_account_authorisation_request,
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
            "201": "ApiResponseOfEmbeddedAccountAuthorisationResponse",
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
    async def initiate_embedded_account_request_with_http_info(
        self,
        embedded_account_authorisation_request: EmbeddedAccountAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfEmbeddedAccountAuthorisationResponse]:
        _param = self._initiate_embedded_account_request_serialize(
            embedded_account_authorisation_request=embedded_account_authorisation_request,
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
            "201": "ApiResponseOfEmbeddedAccountAuthorisationResponse",
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
    async def initiate_embedded_account_request_without_preload_content(
        self,
        embedded_account_authorisation_request: EmbeddedAccountAuthorisationRequest,
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
        _param = self._initiate_embedded_account_request_serialize(
            embedded_account_authorisation_request=embedded_account_authorisation_request,
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
            "201": "ApiResponseOfEmbeddedAccountAuthorisationResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _initiate_embedded_account_request_serialize(
        self,
        embedded_account_authorisation_request,
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
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if embedded_account_authorisation_request is not None:
            _body_params = embedded_account_authorisation_request
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
            resource_path="/embedded-account-auth-requests",
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
    async def re_authorise_account(
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
    ) -> ApiResponseOfAccountAuthorisationResponse:
        _param = self._re_authorise_account_serialize(
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
            "201": "ApiResponseOfAccountAuthorisationResponse",
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
    async def re_authorise_account_with_http_info(
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
    ) -> ApiResponse[ApiResponseOfAccountAuthorisationResponse]:
        _param = self._re_authorise_account_serialize(
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
            "201": "ApiResponseOfAccountAuthorisationResponse",
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
    async def re_authorise_account_without_preload_content(
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
        _param = self._re_authorise_account_serialize(
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
            "201": "ApiResponseOfAccountAuthorisationResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _re_authorise_account_serialize(
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
            method="PATCH",
            resource_path="/account-auth-requests",
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
    async def update_embedded_account_request(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        embedded_account_authorisation_request: EmbeddedAccountAuthorisationRequest,
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
    ) -> ApiResponseOfEmbeddedAccountAuthorisationResponse:
        _param = self._update_embedded_account_request_serialize(
            consent_id=consent_id,
            embedded_account_authorisation_request=embedded_account_authorisation_request,
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
            "201": "ApiResponseOfEmbeddedAccountAuthorisationResponse",
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
    async def update_embedded_account_request_with_http_info(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        embedded_account_authorisation_request: EmbeddedAccountAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfEmbeddedAccountAuthorisationResponse]:
        _param = self._update_embedded_account_request_serialize(
            consent_id=consent_id,
            embedded_account_authorisation_request=embedded_account_authorisation_request,
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
            "201": "ApiResponseOfEmbeddedAccountAuthorisationResponse",
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
    async def update_embedded_account_request_without_preload_content(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        embedded_account_authorisation_request: EmbeddedAccountAuthorisationRequest,
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
        _param = self._update_embedded_account_request_serialize(
            consent_id=consent_id,
            embedded_account_authorisation_request=embedded_account_authorisation_request,
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
            "201": "ApiResponseOfEmbeddedAccountAuthorisationResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _update_embedded_account_request_serialize(
        self,
        consent_id,
        embedded_account_authorisation_request,
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
        if consent_id is not None:
            _path_params["consentId"] = consent_id
        if raw is not None:
            _query_params.append(("raw", raw))
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if embedded_account_authorisation_request is not None:
            _body_params = embedded_account_authorisation_request
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
            method="PUT",
            resource_path="/embedded-account-auth-requests/{consentId}",
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
    async def update_embedded_bulk_payment_authorisation(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        bulk_payment_embedded_authorisation_request: BulkPaymentEmbeddedAuthorisationRequest,
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
    ) -> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse:
        _param = self._update_embedded_bulk_payment_authorisation_serialize(
            consent_id=consent_id,
            bulk_payment_embedded_authorisation_request=bulk_payment_embedded_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
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
    async def update_embedded_bulk_payment_authorisation_with_http_info(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        bulk_payment_embedded_authorisation_request: BulkPaymentEmbeddedAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]:
        _param = self._update_embedded_bulk_payment_authorisation_serialize(
            consent_id=consent_id,
            bulk_payment_embedded_authorisation_request=bulk_payment_embedded_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
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
    async def update_embedded_bulk_payment_authorisation_without_preload_content(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        bulk_payment_embedded_authorisation_request: BulkPaymentEmbeddedAuthorisationRequest,
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
        _param = self._update_embedded_bulk_payment_authorisation_serialize(
            consent_id=consent_id,
            bulk_payment_embedded_authorisation_request=bulk_payment_embedded_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _update_embedded_bulk_payment_authorisation_serialize(
        self,
        consent_id,
        bulk_payment_embedded_authorisation_request,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
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
        if consent_id is not None:
            _path_params["consentId"] = consent_id
        if raw is not None:
            _query_params.append(("raw", raw))
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if bulk_payment_embedded_authorisation_request is not None:
            _body_params = bulk_payment_embedded_authorisation_request
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
            method="PUT",
            resource_path="/embedded-bulk-payment-auth-requests/{consentId}",
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
    async def update_embedded_payment_authorisation(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        payment_embedded_authorisation_request: PaymentEmbeddedAuthorisationRequest,
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
    ) -> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse:
        _param = self._update_embedded_payment_authorisation_serialize(
            consent_id=consent_id,
            payment_embedded_authorisation_request=payment_embedded_authorisation_request,
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
            "200": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
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
    async def update_embedded_payment_authorisation_with_http_info(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        payment_embedded_authorisation_request: PaymentEmbeddedAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse]:
        _param = self._update_embedded_payment_authorisation_serialize(
            consent_id=consent_id,
            payment_embedded_authorisation_request=payment_embedded_authorisation_request,
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
            "200": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
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
    async def update_embedded_payment_authorisation_without_preload_content(
        self,
        consent_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The consent Id of the `Consent` to update."
            ),
        ],
        payment_embedded_authorisation_request: PaymentEmbeddedAuthorisationRequest,
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
        _param = self._update_embedded_payment_authorisation_serialize(
            consent_id=consent_id,
            payment_embedded_authorisation_request=payment_embedded_authorisation_request,
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
            "200": "ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _update_embedded_payment_authorisation_serialize(
        self,
        consent_id,
        payment_embedded_authorisation_request,
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
        if consent_id is not None:
            _path_params["consentId"] = consent_id
        if raw is not None:
            _query_params.append(("raw", raw))
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if payment_embedded_authorisation_request is not None:
            _body_params = payment_embedded_authorisation_request
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
            method="PUT",
            resource_path="/embedded-payment-auth-requests/{consentId}",
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
    async def update_payment_authorisation(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        payment_authorisation_request: PaymentAuthorisationRequest,
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
    ) -> ApiResponseOfPaymentAuthorisationRequestResponse:
        _param = self._update_payment_authorisation_serialize(
            consent=consent,
            payment_authorisation_request=payment_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfPaymentAuthorisationRequestResponse",
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
    async def update_payment_authorisation_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        payment_authorisation_request: PaymentAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentAuthorisationRequestResponse]:
        _param = self._update_payment_authorisation_serialize(
            consent=consent,
            payment_authorisation_request=payment_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfPaymentAuthorisationRequestResponse",
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
    async def update_payment_authorisation_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        payment_authorisation_request: PaymentAuthorisationRequest,
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
        _param = self._update_payment_authorisation_serialize(
            consent=consent,
            payment_authorisation_request=payment_authorisation_request,
            psu_id=psu_id,
            psu_corporate_id=psu_corporate_id,
            psu_ip_address=psu_ip_address,
            raw=raw,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfPaymentAuthorisationRequestResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _update_payment_authorisation_serialize(
        self,
        consent,
        payment_authorisation_request,
        psu_id,
        psu_corporate_id,
        psu_ip_address,
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
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if consent is not None:
            _header_params["consent"] = consent
        if payment_authorisation_request is not None:
            _body_params = payment_authorisation_request
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
            method="PUT",
            resource_path="/payment-auth-requests",
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
    async def update_pre_authorise_account_consent(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_authorisation_request: AccountAuthorisationRequest,
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
    ) -> ApiResponseOfAccountAuthorisationResponse:
        _param = self._update_pre_authorise_account_consent_serialize(
            consent=consent,
            account_authorisation_request=account_authorisation_request,
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
            "200": "ApiResponseOfAccountAuthorisationResponse",
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
    async def update_pre_authorise_account_consent_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_authorisation_request: AccountAuthorisationRequest,
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
    ) -> ApiResponse[ApiResponseOfAccountAuthorisationResponse]:
        _param = self._update_pre_authorise_account_consent_serialize(
            consent=consent,
            account_authorisation_request=account_authorisation_request,
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
            "200": "ApiResponseOfAccountAuthorisationResponse",
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
    async def update_pre_authorise_account_consent_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        account_authorisation_request: AccountAuthorisationRequest,
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
        _param = self._update_pre_authorise_account_consent_serialize(
            consent=consent,
            account_authorisation_request=account_authorisation_request,
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
            "200": "ApiResponseOfAccountAuthorisationResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _update_pre_authorise_account_consent_serialize(
        self,
        consent,
        account_authorisation_request,
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
        if account_authorisation_request is not None:
            _body_params = account_authorisation_request
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
            method="PUT",
            resource_path="/account-auth-requests",
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
