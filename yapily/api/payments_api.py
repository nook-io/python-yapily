from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from pydantic import StrictBool
from yapily.models.api_response_of_payment_response import ApiResponseOfPaymentResponse
from yapily.models.api_response_of_payment_responses import (
    ApiResponseOfPaymentResponses,
)
from yapily.models.get_bulk_payment_status200_response import (
    GetBulkPaymentStatus200Response,
)
from yapily.models.payment_request import PaymentRequest
from yapily.models.submit_bulk_payment_request import SubmitBulkPaymentRequest
from yapily.api_client import ApiClient, RequestSerialized
from yapily.api_response import ApiResponse
from yapily.rest import RESTResponseType


class PaymentsApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def create_bulk_payment(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        submit_bulk_payment_request: SubmitBulkPaymentRequest,
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
    ) -> ApiResponseOfPaymentResponse:
        _param = self._create_bulk_payment_serialize(
            consent=consent,
            submit_bulk_payment_request=submit_bulk_payment_request,
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
            "201": "ApiResponseOfPaymentResponse",
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
    async def create_bulk_payment_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        submit_bulk_payment_request: SubmitBulkPaymentRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentResponse]:
        _param = self._create_bulk_payment_serialize(
            consent=consent,
            submit_bulk_payment_request=submit_bulk_payment_request,
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
            "201": "ApiResponseOfPaymentResponse",
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
    async def create_bulk_payment_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        submit_bulk_payment_request: SubmitBulkPaymentRequest,
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
        _param = self._create_bulk_payment_serialize(
            consent=consent,
            submit_bulk_payment_request=submit_bulk_payment_request,
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
            "201": "ApiResponseOfPaymentResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_bulk_payment_serialize(
        self,
        consent,
        submit_bulk_payment_request,
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
        if consent is not None:
            _header_params["consent"] = consent
        if psu_id is not None:
            _header_params["psu-id"] = psu_id
        if psu_corporate_id is not None:
            _header_params["psu-corporate-id"] = psu_corporate_id
        if psu_ip_address is not None:
            _header_params["psu-ip-address"] = psu_ip_address
        if submit_bulk_payment_request is not None:
            _body_params = submit_bulk_payment_request
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
            resource_path="/bulk-payments",
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
    async def create_payment(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        payment_request: PaymentRequest,
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
    ) -> ApiResponseOfPaymentResponse:
        _param = self._create_payment_serialize(
            consent=consent,
            payment_request=payment_request,
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
            "201": "ApiResponseOfPaymentResponse",
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
    async def create_payment_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        payment_request: PaymentRequest,
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
    ) -> ApiResponse[ApiResponseOfPaymentResponse]:
        _param = self._create_payment_serialize(
            consent=consent,
            payment_request=payment_request,
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
            "201": "ApiResponseOfPaymentResponse",
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
    async def create_payment_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        payment_request: PaymentRequest,
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
        _param = self._create_payment_serialize(
            consent=consent,
            payment_request=payment_request,
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
            "201": "ApiResponseOfPaymentResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_payment_serialize(
        self,
        consent,
        payment_request,
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
        if payment_request is not None:
            _body_params = payment_request
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
            resource_path="/payments",
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
    async def get_bulk_payment_status(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent token` containing the user's authorisation to make the request."
            ),
        ],
        bulk_payment_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. Bulk payment id returned when bulk payment request was submitted."
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
    ) -> GetBulkPaymentStatus200Response:
        _param = self._get_bulk_payment_status_serialize(
            consent=consent,
            bulk_payment_id=bulk_payment_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetBulkPaymentStatus200Response",
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
    async def get_bulk_payment_status_with_http_info(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent token` containing the user's authorisation to make the request."
            ),
        ],
        bulk_payment_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. Bulk payment id returned when bulk payment request was submitted."
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
    ) -> ApiResponse[GetBulkPaymentStatus200Response]:
        _param = self._get_bulk_payment_status_serialize(
            consent=consent,
            bulk_payment_id=bulk_payment_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetBulkPaymentStatus200Response",
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
    async def get_bulk_payment_status_without_preload_content(
        self,
        consent: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent token` containing the user's authorisation to make the request."
            ),
        ],
        bulk_payment_id: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. Bulk payment id returned when bulk payment request was submitted."
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
        _param = self._get_bulk_payment_status_serialize(
            consent=consent,
            bulk_payment_id=bulk_payment_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetBulkPaymentStatus200Response",
            "400": "ApiErrorResponseV2",
            "401": "ApiErrorResponseV2",
            "404": "ApiErrorResponseV2",
            "500": "ApiErrorResponseV2",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_bulk_payment_status_serialize(
        self,
        consent,
        bulk_payment_id,
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
        if bulk_payment_id is not None:
            _path_params["bulkPaymentId"] = bulk_payment_id
        if consent is not None:
            _header_params["consent"] = consent
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json", "application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/bulk-payments/{bulkPaymentId}",
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
    async def get_payments(
        self,
        payment_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The payment Id of the payment."),
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
    ) -> ApiResponseOfPaymentResponses:
        _param = self._get_payments_serialize(
            payment_id=payment_id,
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
            "200": "ApiResponseOfPaymentResponses",
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
    async def get_payments_with_http_info(
        self,
        payment_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The payment Id of the payment."),
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
    ) -> ApiResponse[ApiResponseOfPaymentResponses]:
        _param = self._get_payments_serialize(
            payment_id=payment_id,
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
            "200": "ApiResponseOfPaymentResponses",
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
    async def get_payments_without_preload_content(
        self,
        payment_id: Annotated[
            StrictStr,
            Field(description="__Mandatory__. The payment Id of the payment."),
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
        _param = self._get_payments_serialize(
            payment_id=payment_id,
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
            "200": "ApiResponseOfPaymentResponses",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_payments_serialize(
        self,
        payment_id,
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
        if payment_id is not None:
            _path_params["paymentId"] = payment_id
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
            resource_path="/payments/{paymentId}/details",
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
