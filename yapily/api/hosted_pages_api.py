from pydantic import validate_arguments
from typing_extensions import Annotated
from pydantic import Field, StrictStr
from typing import Optional
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
from yapily.api_client import ApiClient
from yapily.api_response import ApiResponse
from yapily.exceptions import (
    ApiTypeError,
)


class HostedPagesApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_hosted_payment_request(
        self, create_hosted_payment_request: CreateHostedPaymentRequest, **kwargs
    ) -> ApiResponseOfCreateHostedPaymentRequest:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_hosted_payment_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.create_hosted_payment_request_with_http_info(
            create_hosted_payment_request, **kwargs
        )

    @validate_arguments
    def create_hosted_payment_request_with_http_info(
        self, create_hosted_payment_request: CreateHostedPaymentRequest, **kwargs
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["create_hosted_payment_request"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hosted_payment_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        _form_params = []
        _files = {}
        _body_params = None
        if _params["create_hosted_payment_request"] is not None:
            _body_params = _params["create_hosted_payment_request"]
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(
                ["application/json;charset=UTF-8"]
            ),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "201": "ApiResponseOfCreateHostedPaymentRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/payment-requests",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def create_hosted_payment_request_link(
        self,
        create_hosted_payment_request_link: CreateHostedPaymentRequestLink,
        **kwargs,
    ) -> ApiResponseOfCreateHostedPaymentRequestLink:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_hosted_payment_request_link_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.create_hosted_payment_request_link_with_http_info(
            create_hosted_payment_request_link, **kwargs
        )

    @validate_arguments
    def create_hosted_payment_request_link_with_http_info(
        self,
        create_hosted_payment_request_link: CreateHostedPaymentRequestLink,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["create_hosted_payment_request_link"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hosted_payment_request_link" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        _form_params = []
        _files = {}
        _body_params = None
        if _params["create_hosted_payment_request_link"] is not None:
            _body_params = _params["create_hosted_payment_request_link"]
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(
                ["application/json;charset=UTF-8"]
            ),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "201": "ApiResponseOfCreateHostedPaymentRequestLink",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/payment-requests/links",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def create_hosted_vrp_consent_request(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                ...,
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)",
            ),
        ],
        create_hosted_vrp_consent_request: CreateHostedVRPConsentRequest,
        **kwargs,
    ) -> ApiResponseOfCreateHostedVRPConsentRequest:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_hosted_vrp_consent_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.create_hosted_vrp_consent_request_with_http_info(
            sub_application, create_hosted_vrp_consent_request, **kwargs
        )

    @validate_arguments
    def create_hosted_vrp_consent_request_with_http_info(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                ...,
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)",
            ),
        ],
        create_hosted_vrp_consent_request: CreateHostedVRPConsentRequest,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["sub_application", "create_hosted_vrp_consent_request"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hosted_vrp_consent_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["sub_application"] is not None:
            _header_params["sub-application"] = _params["sub_application"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["create_hosted_vrp_consent_request"] is not None:
            _body_params = _params["create_hosted_vrp_consent_request"]
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(
                ["application/json;charset=UTF-8"]
            ),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "201": "ApiResponseOfCreateHostedVRPConsentRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/vrp/consent-requests",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def create_hosted_vrp_funds_confirmation(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                ...,
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request.",
            ),
        ],
        funds_confirmation_request: FundsConfirmationRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponseOfFundsConfirmationResponse:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_hosted_vrp_funds_confirmation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.create_hosted_vrp_funds_confirmation_with_http_info(
            consent_request_id,
            consent_token,
            funds_confirmation_request,
            sub_application,
            **kwargs,
        )

    @validate_arguments
    def create_hosted_vrp_funds_confirmation_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                ...,
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request.",
            ),
        ],
        funds_confirmation_request: FundsConfirmationRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "consent_request_id",
            "consent_token",
            "funds_confirmation_request",
            "sub_application",
        ]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hosted_vrp_funds_confirmation" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["consent_request_id"] is not None:
            _path_params["consentRequestId"] = _params["consent_request_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["consent_token"] is not None:
            _header_params["consent-token"] = _params["consent_token"]
        if _params["sub_application"] is not None:
            _header_params["sub-application"] = _params["sub_application"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["funds_confirmation_request"] is not None:
            _body_params = _params["funds_confirmation_request"]
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(
                ["application/json;charset=UTF-8"]
            ),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "201": "ApiResponseOfFundsConfirmationResponse",
            "401": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/vrp/consent-requests/{consentRequestId}/funds-confirmation",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def create_hosted_vrp_payment(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                ...,
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request.",
            ),
        ],
        create_hosted_vrp_payment_request: CreateHostedVRPPaymentRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponseOfCreateHostedVRPPaymentRequest:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_hosted_vrp_payment_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.create_hosted_vrp_payment_with_http_info(
            consent_request_id,
            consent_token,
            create_hosted_vrp_payment_request,
            sub_application,
            **kwargs,
        )

    @validate_arguments
    def create_hosted_vrp_payment_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        consent_token: Annotated[
            StrictStr,
            Field(
                ...,
                description="__Mandatory__. The `consent-token` containing the user's authorisation to make the request.",
            ),
        ],
        create_hosted_vrp_payment_request: CreateHostedVRPPaymentRequest,
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = [
            "consent_request_id",
            "consent_token",
            "create_hosted_vrp_payment_request",
            "sub_application",
        ]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hosted_vrp_payment" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["consent_request_id"] is not None:
            _path_params["consentRequestId"] = _params["consent_request_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["consent_token"] is not None:
            _header_params["consent-token"] = _params["consent_token"]
        if _params["sub_application"] is not None:
            _header_params["sub-application"] = _params["sub_application"]
        _form_params = []
        _files = {}
        _body_params = None
        if _params["create_hosted_vrp_payment_request"] is not None:
            _body_params = _params["create_hosted_vrp_payment_request"]
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(
                ["application/json;charset=UTF-8"]
            ),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "201": "ApiResponseOfCreateHostedVRPPaymentRequest",
            "401": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/vrp/consent-requests/{consentRequestId}/payments",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def get_hosted_consent_request(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponseOfGetHostedVRPConsentRequest:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_hosted_consent_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.get_hosted_consent_request_with_http_info(
            consent_request_id, sub_application, **kwargs
        )

    @validate_arguments
    def get_hosted_consent_request_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["consent_request_id", "sub_application"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hosted_consent_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["consent_request_id"] is not None:
            _path_params["consentRequestId"] = _params["consent_request_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["sub_application"] is not None:
            _header_params["sub-application"] = _params["sub_application"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "200": "ApiResponseOfGetHostedVRPConsentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/vrp/consent-requests/{consentRequestId}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def get_hosted_payment_request(
        self,
        payment_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the payment request"),
        ],
        **kwargs,
    ) -> ApiResponseOfGetHostedPaymentRequest:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_hosted_payment_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.get_hosted_payment_request_with_http_info(
            payment_request_id, **kwargs
        )

    @validate_arguments
    def get_hosted_payment_request_with_http_info(
        self,
        payment_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the payment request"),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["payment_request_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hosted_payment_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["payment_request_id"] is not None:
            _path_params["paymentRequestId"] = _params["payment_request_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "200": "ApiResponseOfGetHostedPaymentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/payment-requests/{paymentRequestId}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def get_hosted_vrp_consent_requests(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                ...,
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)",
            ),
        ],
        **kwargs,
    ) -> ApiResponseOfGetHostedVRPConsentsRequest:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_hosted_vrp_consent_requests_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.get_hosted_vrp_consent_requests_with_http_info(
            sub_application, **kwargs
        )

    @validate_arguments
    def get_hosted_vrp_consent_requests_with_http_info(
        self,
        sub_application: Annotated[
            StrictStr,
            Field(
                ...,
                description="__Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)",
            ),
        ],
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["sub_application"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hosted_vrp_consent_requests" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["sub_application"] is not None:
            _header_params["sub-application"] = _params["sub_application"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "200": "ApiResponseOfGetHostedVRPConsentsRequest",
            "400": "ApiResponseError",
            "401": "ApiResponseError",
            "500": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/vrp/consent-requests",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def get_hosted_vrp_payment_request(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        payment_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponseOfGetHostedVRPPaymentRequest:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_hosted_vrp_payment_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.get_hosted_vrp_payment_request_with_http_info(
            consent_request_id, payment_id, sub_application, **kwargs
        )

    @validate_arguments
    def get_hosted_vrp_payment_request_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        payment_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["consent_request_id", "payment_id", "sub_application"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hosted_vrp_payment_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["consent_request_id"] is not None:
            _path_params["consentRequestId"] = _params["consent_request_id"]
        if _params["payment_id"] is not None:
            _path_params["paymentId"] = _params["payment_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["sub_application"] is not None:
            _header_params["sub-application"] = _params["sub_application"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "200": "ApiResponseOfGetHostedVRPPaymentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/vrp/consent-requests/{consentRequestId}/payments/{paymentId}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def revoke_hosted_consent_request(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponseOfRevokeHostedVRPConsentRequest:
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the revoke_hosted_consent_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            raise ValueError(message)
        return self.revoke_hosted_consent_request_with_http_info(
            consent_request_id, sub_application, **kwargs
        )

    @validate_arguments
    def revoke_hosted_consent_request_with_http_info(
        self,
        consent_request_id: Annotated[
            StrictStr,
            Field(..., description="Unique Identifier of the Consent Request"),
        ],
        sub_application: Annotated[
            Optional[StrictStr],
            Field(
                description="The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)"
            ),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        _params = locals()
        _all_params = ["consent_request_id", "sub_application"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revoke_hosted_consent_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]
        _collection_formats = {}
        _path_params = {}
        if _params["consent_request_id"] is not None:
            _path_params["consentRequestId"] = _params["consent_request_id"]
        _query_params = []
        _header_params = dict(_params.get("_headers", {}))
        if _params["sub_application"] is not None:
            _header_params["sub-application"] = _params["sub_application"]
        _form_params = []
        _files = {}
        _body_params = None
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json;charset=UTF-8"]
        )
        _auth_settings = ["basicAuth"]
        _response_types_map = {
            "200": "ApiResponseOfRevokeHostedVRPConsentRequest",
            "401": "ApiResponseError",
            "404": "ApiResponseError",
            "500": "ApiResponseError",
        }
        return self.api_client.call_api(
            "/hosted/vrp/consent-requests/{consentRequestId}/revoke",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
