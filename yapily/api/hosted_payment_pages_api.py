from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from yapily.models.api_response_of_create_hosted_payment_request import (
    ApiResponseOfCreateHostedPaymentRequest,
)
from yapily.models.api_response_of_create_hosted_payment_request_link import (
    ApiResponseOfCreateHostedPaymentRequestLink,
)
from yapily.models.api_response_of_create_hosted_vrp_consent_request import (
    ApiResponseOfCreateHostedVRPConsentRequest,
)
from yapily.models.api_response_of_create_hosted_vrp_payment_request import (
    ApiResponseOfCreateHostedVRPPaymentRequest,
)
from yapily.models.api_response_of_funds_confirmation_response import (
    ApiResponseOfFundsConfirmationResponse,
)
from yapily.models.api_response_of_get_hosted_payment_request import (
    ApiResponseOfGetHostedPaymentRequest,
)
from yapily.models.api_response_of_get_hosted_vrp_consent_request import (
    ApiResponseOfGetHostedVRPConsentRequest,
)
from yapily.models.api_response_of_get_hosted_vrp_consents_request import (
    ApiResponseOfGetHostedVRPConsentsRequest,
)
from yapily.models.api_response_of_get_hosted_vrp_payment_request import (
    ApiResponseOfGetHostedVRPPaymentRequest,
)
from yapily.models.api_response_of_revoke_hosted_vrp_consent_request import (
    ApiResponseOfRevokeHostedVRPConsentRequest,
)
from yapily.models.create_hosted_payment_request import CreateHostedPaymentRequest
from yapily.models.create_hosted_payment_request_link import (
    CreateHostedPaymentRequestLink,
)
from yapily.models.create_hosted_vrp_consent_request import (
    CreateHostedVRPConsentRequest,
)
from yapily.models.create_hosted_vrp_payment_request import (
    CreateHostedVRPPaymentRequest,
)
from yapily.models.funds_confirmation_request import FundsConfirmationRequest
from yapily.api_client import ApiClient, RequestSerialized
from yapily.api_response import ApiResponse
from yapily.rest import RESTResponseType


class HostedPaymentPagesApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def create_hosted_payment_request(
        self,
        create_hosted_payment_request: CreateHostedPaymentRequest,
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
    ) -> ApiResponseOfCreateHostedPaymentRequest:
        _param = self._create_hosted_payment_request_serialize(
            create_hosted_payment_request=create_hosted_payment_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedPaymentRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def create_hosted_payment_request_with_http_info(
        self,
        create_hosted_payment_request: CreateHostedPaymentRequest,
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
    ) -> ApiResponse[ApiResponseOfCreateHostedPaymentRequest]:
        _param = self._create_hosted_payment_request_serialize(
            create_hosted_payment_request=create_hosted_payment_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedPaymentRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def create_hosted_payment_request_without_preload_content(
        self,
        create_hosted_payment_request: CreateHostedPaymentRequest,
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
        _param = self._create_hosted_payment_request_serialize(
            create_hosted_payment_request=create_hosted_payment_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedPaymentRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_hosted_payment_request_serialize(
        self,
        create_hosted_payment_request,
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
        if create_hosted_payment_request is not None:
            _body_params = create_hosted_payment_request
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
            resource_path="/hosted/payment-requests",
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
    async def create_hosted_payment_request_link(
        self,
        create_hosted_payment_request_link: CreateHostedPaymentRequestLink,
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
    ) -> ApiResponseOfCreateHostedPaymentRequestLink:
        _param = self._create_hosted_payment_request_link_serialize(
            create_hosted_payment_request_link=create_hosted_payment_request_link,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedPaymentRequestLink",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def create_hosted_payment_request_link_with_http_info(
        self,
        create_hosted_payment_request_link: CreateHostedPaymentRequestLink,
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
    ) -> ApiResponse[ApiResponseOfCreateHostedPaymentRequestLink]:
        _param = self._create_hosted_payment_request_link_serialize(
            create_hosted_payment_request_link=create_hosted_payment_request_link,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedPaymentRequestLink",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def create_hosted_payment_request_link_without_preload_content(
        self,
        create_hosted_payment_request_link: CreateHostedPaymentRequestLink,
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
        _param = self._create_hosted_payment_request_link_serialize(
            create_hosted_payment_request_link=create_hosted_payment_request_link,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedPaymentRequestLink",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_hosted_payment_request_link_serialize(
        self,
        create_hosted_payment_request_link,
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
        if create_hosted_payment_request_link is not None:
            _body_params = create_hosted_payment_request_link
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
            resource_path="/hosted/payment-requests/links",
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
    async def create_hosted_vrp_consent_request(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ],
        create_hosted_vrp_consent_request: CreateHostedVRPConsentRequest,
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
    ) -> ApiResponseOfCreateHostedVRPConsentRequest:
        _param = self._create_hosted_vrp_consent_request_serialize(
            sub_application=sub_application,
            create_hosted_vrp_consent_request=create_hosted_vrp_consent_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedVRPConsentRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def create_hosted_vrp_consent_request_with_http_info(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ],
        create_hosted_vrp_consent_request: CreateHostedVRPConsentRequest,
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
    ) -> ApiResponse[ApiResponseOfCreateHostedVRPConsentRequest]:
        _param = self._create_hosted_vrp_consent_request_serialize(
            sub_application=sub_application,
            create_hosted_vrp_consent_request=create_hosted_vrp_consent_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedVRPConsentRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def create_hosted_vrp_consent_request_without_preload_content(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ],
        create_hosted_vrp_consent_request: CreateHostedVRPConsentRequest,
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
        _param = self._create_hosted_vrp_consent_request_serialize(
            sub_application=sub_application,
            create_hosted_vrp_consent_request=create_hosted_vrp_consent_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedVRPConsentRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_hosted_vrp_consent_request_serialize(
        self,
        sub_application,
        create_hosted_vrp_consent_request,
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
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if create_hosted_vrp_consent_request is not None:
            _body_params = create_hosted_vrp_consent_request
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
            resource_path="/hosted/vrp/consent-requests",
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
    async def create_hosted_vrp_funds_confirmation(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        funds_confirmation_request: FundsConfirmationRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponseOfFundsConfirmationResponse:
        _param = self._create_hosted_vrp_funds_confirmation_serialize(
            consent_request_id=consent_request_id,
            consent_token=consent_token,
            funds_confirmation_request=funds_confirmation_request,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfFundsConfirmationResponse",
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
    async def create_hosted_vrp_funds_confirmation_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        funds_confirmation_request: FundsConfirmationRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponse[ApiResponseOfFundsConfirmationResponse]:
        _param = self._create_hosted_vrp_funds_confirmation_serialize(
            consent_request_id=consent_request_id,
            consent_token=consent_token,
            funds_confirmation_request=funds_confirmation_request,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfFundsConfirmationResponse",
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
    async def create_hosted_vrp_funds_confirmation_without_preload_content(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        funds_confirmation_request: FundsConfirmationRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
        _param = self._create_hosted_vrp_funds_confirmation_serialize(
            consent_request_id=consent_request_id,
            consent_token=consent_token,
            funds_confirmation_request=funds_confirmation_request,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfFundsConfirmationResponse",
            "401": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_hosted_vrp_funds_confirmation_serialize(
        self,
        consent_request_id,
        consent_token,
        funds_confirmation_request,
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
        if consent_request_id is not None:
            _path_params["consentRequestId"] = consent_request_id
        if consent_token is not None:
            _header_params["consent-token"] = consent_token
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if funds_confirmation_request is not None:
            _body_params = funds_confirmation_request
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
            resource_path="/hosted/vrp/consent-requests/{consentRequestId}/funds-confirmation",
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
    async def create_hosted_vrp_payment(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        create_hosted_vrp_payment_request: CreateHostedVRPPaymentRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponseOfCreateHostedVRPPaymentRequest:
        _param = self._create_hosted_vrp_payment_serialize(
            consent_request_id=consent_request_id,
            consent_token=consent_token,
            create_hosted_vrp_payment_request=create_hosted_vrp_payment_request,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedVRPPaymentRequest",
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
    async def create_hosted_vrp_payment_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        create_hosted_vrp_payment_request: CreateHostedVRPPaymentRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponse[ApiResponseOfCreateHostedVRPPaymentRequest]:
        _param = self._create_hosted_vrp_payment_serialize(
            consent_request_id=consent_request_id,
            consent_token=consent_token,
            create_hosted_vrp_payment_request=create_hosted_vrp_payment_request,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedVRPPaymentRequest",
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
    async def create_hosted_vrp_payment_without_preload_content(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request."
            ),
        ],
        create_hosted_vrp_payment_request: CreateHostedVRPPaymentRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
        _param = self._create_hosted_vrp_payment_serialize(
            consent_request_id=consent_request_id,
            consent_token=consent_token,
            create_hosted_vrp_payment_request=create_hosted_vrp_payment_request,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "201": "ApiResponseOfCreateHostedVRPPaymentRequest",
            "401": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _create_hosted_vrp_payment_serialize(
        self,
        consent_request_id,
        consent_token,
        create_hosted_vrp_payment_request,
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
        if consent_request_id is not None:
            _path_params["consentRequestId"] = consent_request_id
        if consent_token is not None:
            _header_params["consent-token"] = consent_token
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if create_hosted_vrp_payment_request is not None:
            _body_params = create_hosted_vrp_payment_request
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
            resource_path="/hosted/vrp/consent-requests/{consentRequestId}/payments",
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
    async def get_hosted_payment_request(
        self,
        payment_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the payment request")
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
    ) -> ApiResponseOfGetHostedPaymentRequest:
        _param = self._get_hosted_payment_request_serialize(
            payment_request_id=payment_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedPaymentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def get_hosted_payment_request_with_http_info(
        self,
        payment_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the payment request")
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
    ) -> ApiResponse[ApiResponseOfGetHostedPaymentRequest]:
        _param = self._get_hosted_payment_request_serialize(
            payment_request_id=payment_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedPaymentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def get_hosted_payment_request_without_preload_content(
        self,
        payment_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the payment request")
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
        _param = self._get_hosted_payment_request_serialize(
            payment_request_id=payment_request_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedPaymentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_hosted_payment_request_serialize(
        self,
        payment_request_id,
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
        if payment_request_id is not None:
            _path_params["paymentRequestId"] = payment_request_id
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/hosted/payment-requests/{paymentRequestId}",
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
    async def get_hosted_vrp_consent_request(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponseOfGetHostedVRPConsentRequest:
        _param = self._get_hosted_vrp_consent_request_serialize(
            consent_request_id=consent_request_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPConsentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def get_hosted_vrp_consent_request_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponse[ApiResponseOfGetHostedVRPConsentRequest]:
        _param = self._get_hosted_vrp_consent_request_serialize(
            consent_request_id=consent_request_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPConsentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def get_hosted_vrp_consent_request_without_preload_content(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
        _param = self._get_hosted_vrp_consent_request_serialize(
            consent_request_id=consent_request_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPConsentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_hosted_vrp_consent_request_serialize(
        self,
        consent_request_id,
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
        if consent_request_id is not None:
            _path_params["consentRequestId"] = consent_request_id
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/hosted/vrp/consent-requests/{consentRequestId}",
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
    async def get_hosted_vrp_consent_requests(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponseOfGetHostedVRPConsentsRequest:
        _param = self._get_hosted_vrp_consent_requests_serialize(
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPConsentsRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def get_hosted_vrp_consent_requests_with_http_info(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponse[ApiResponseOfGetHostedVRPConsentsRequest]:
        _param = self._get_hosted_vrp_consent_requests_serialize(
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPConsentsRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def get_hosted_vrp_consent_requests_without_preload_content(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
        _param = self._get_hosted_vrp_consent_requests_serialize(
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPConsentsRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_hosted_vrp_consent_requests_serialize(
        self,
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
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/hosted/vrp/consent-requests",
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
    async def get_hosted_vrp_payment_request(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        payment_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponseOfGetHostedVRPPaymentRequest:
        _param = self._get_hosted_vrp_payment_request_serialize(
            consent_request_id=consent_request_id,
            payment_id=payment_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPPaymentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def get_hosted_vrp_payment_request_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        payment_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponse[ApiResponseOfGetHostedVRPPaymentRequest]:
        _param = self._get_hosted_vrp_payment_request_serialize(
            consent_request_id=consent_request_id,
            payment_id=payment_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPPaymentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def get_hosted_vrp_payment_request_without_preload_content(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        payment_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
        _param = self._get_hosted_vrp_payment_request_serialize(
            consent_request_id=consent_request_id,
            payment_id=payment_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfGetHostedVRPPaymentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_hosted_vrp_payment_request_serialize(
        self,
        consent_request_id,
        payment_id,
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
        if consent_request_id is not None:
            _path_params["consentRequestId"] = consent_request_id
        if payment_id is not None:
            _path_params["paymentId"] = payment_id
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="GET",
            resource_path="/hosted/vrp/consent-requests/{consentRequestId}/payments/{paymentId}",
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
    async def revoke_hosted_consent_request(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponseOfRevokeHostedVRPConsentRequest:
        _param = self._revoke_hosted_consent_request_serialize(
            consent_request_id=consent_request_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfRevokeHostedVRPConsentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def revoke_hosted_consent_request_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
    ) -> ApiResponse[ApiResponseOfRevokeHostedVRPConsentRequest]:
        _param = self._revoke_hosted_consent_request_serialize(
            consent_request_id=consent_request_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfRevokeHostedVRPConsentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
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
    async def revoke_hosted_consent_request_without_preload_content(
        self,
        consent_request_id: Annotated[
            StrictStr, Field(description="Unique Identifier of the Consent Request")
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
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
        _param = self._revoke_hosted_consent_request_serialize(
            consent_request_id=consent_request_id,
            sub_application=sub_application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )
        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ApiResponseOfRevokeHostedVRPConsentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _revoke_hosted_consent_request_serialize(
        self,
        consent_request_id,
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
        if consent_request_id is not None:
            _path_params["consentRequestId"] = consent_request_id
        if sub_application is not None:
            _header_params["sub-application"] = sub_application
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json;charset=UTF-8"]
            )
        _auth_settings: List[str] = ["basicAuth"]
        return self.api_client.param_serialize(
            method="POST",
            resource_path="/hosted/vrp/consent-requests/{consentRequestId}/revoke",
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
