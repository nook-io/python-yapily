# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 7.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from yapily.models.api_list_response_of_data_constraints import ApiListResponseOfDataConstraints
from yapily.models.api_list_response_of_payment_constraints import ApiListResponseOfPaymentConstraints

from yapily.api_client import ApiClient, RequestSerialized
from yapily.api_response import ApiResponse
from yapily.rest import RESTResponseType


class ConstraintsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def get_account_constraints_rules_by_institution(
        self,
        institution_ids: Annotated[List[StrictStr], Field(description="Unique Id(s) of the `Institution`(s) to retrieve the Data Constraints for. Multiple institutionIds need to be separated by `,`")],
        institution_country_code: Annotated[StrictStr, Field(description="Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response.")],
        endpoint_path: Annotated[Optional[StrictStr], Field(description="The path on the API that is associated with the operation for which constraints are to be retrieved")] = None,
        endpoint_method: Annotated[Optional[StrictStr], Field(description="The HTTP method that is associated with the operation for which constraints are to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiListResponseOfDataConstraints:
        """Get Data Constraints Rules

        Get Data Constraints Rules against an Institution for Account Authorisation requests

        :param institution_ids: Unique Id(s) of the `Institution`(s) to retrieve the Data Constraints for. Multiple institutionIds need to be separated by `,` (required)
        :type institution_ids: List[str]
        :param institution_country_code: Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response. (required)
        :type institution_country_code: str
        :param endpoint_path: The path on the API that is associated with the operation for which constraints are to be retrieved
        :type endpoint_path: str
        :param endpoint_method: The HTTP method that is associated with the operation for which constraints are to be retrieved
        :type endpoint_method: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_account_constraints_rules_by_institution_serialize(
            institution_ids=institution_ids,
            institution_country_code=institution_country_code,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiListResponseOfDataConstraints",
            '400': "ApiResponseError",
            '401': "ApiResponseError",
            '404': "ApiResponseError",
            '500': "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def get_account_constraints_rules_by_institution_with_http_info(
        self,
        institution_ids: Annotated[List[StrictStr], Field(description="Unique Id(s) of the `Institution`(s) to retrieve the Data Constraints for. Multiple institutionIds need to be separated by `,`")],
        institution_country_code: Annotated[StrictStr, Field(description="Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response.")],
        endpoint_path: Annotated[Optional[StrictStr], Field(description="The path on the API that is associated with the operation for which constraints are to be retrieved")] = None,
        endpoint_method: Annotated[Optional[StrictStr], Field(description="The HTTP method that is associated with the operation for which constraints are to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiListResponseOfDataConstraints]:
        """Get Data Constraints Rules

        Get Data Constraints Rules against an Institution for Account Authorisation requests

        :param institution_ids: Unique Id(s) of the `Institution`(s) to retrieve the Data Constraints for. Multiple institutionIds need to be separated by `,` (required)
        :type institution_ids: List[str]
        :param institution_country_code: Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response. (required)
        :type institution_country_code: str
        :param endpoint_path: The path on the API that is associated with the operation for which constraints are to be retrieved
        :type endpoint_path: str
        :param endpoint_method: The HTTP method that is associated with the operation for which constraints are to be retrieved
        :type endpoint_method: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_account_constraints_rules_by_institution_serialize(
            institution_ids=institution_ids,
            institution_country_code=institution_country_code,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiListResponseOfDataConstraints",
            '400': "ApiResponseError",
            '401': "ApiResponseError",
            '404': "ApiResponseError",
            '500': "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def get_account_constraints_rules_by_institution_without_preload_content(
        self,
        institution_ids: Annotated[List[StrictStr], Field(description="Unique Id(s) of the `Institution`(s) to retrieve the Data Constraints for. Multiple institutionIds need to be separated by `,`")],
        institution_country_code: Annotated[StrictStr, Field(description="Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response.")],
        endpoint_path: Annotated[Optional[StrictStr], Field(description="The path on the API that is associated with the operation for which constraints are to be retrieved")] = None,
        endpoint_method: Annotated[Optional[StrictStr], Field(description="The HTTP method that is associated with the operation for which constraints are to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Data Constraints Rules

        Get Data Constraints Rules against an Institution for Account Authorisation requests

        :param institution_ids: Unique Id(s) of the `Institution`(s) to retrieve the Data Constraints for. Multiple institutionIds need to be separated by `,` (required)
        :type institution_ids: List[str]
        :param institution_country_code: Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response. (required)
        :type institution_country_code: str
        :param endpoint_path: The path on the API that is associated with the operation for which constraints are to be retrieved
        :type endpoint_path: str
        :param endpoint_method: The HTTP method that is associated with the operation for which constraints are to be retrieved
        :type endpoint_method: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_account_constraints_rules_by_institution_serialize(
            institution_ids=institution_ids,
            institution_country_code=institution_country_code,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiListResponseOfDataConstraints",
            '400': "ApiResponseError",
            '401': "ApiResponseError",
            '404': "ApiResponseError",
            '500': "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_account_constraints_rules_by_institution_serialize(
        self,
        institution_ids,
        institution_country_code,
        endpoint_path,
        endpoint_method,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'institutionIds': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if institution_ids is not None:
            
            _query_params.append(('institutionIds', institution_ids))
            
        if institution_country_code is not None:
            
            _query_params.append(('institutionCountryCode', institution_country_code))
            
        if endpoint_path is not None:
            
            _query_params.append(('endpointPath', endpoint_path))
            
        if endpoint_method is not None:
            
            _query_params.append(('endpointMethod', endpoint_method))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json;charset=UTF-8'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'basicAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/institutions/constraints/data',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    async def get_payment_constraints_rules_by_institution(
        self,
        institution_ids: Annotated[List[StrictStr], Field(description="Unique Id(s) of the `Institution`(s) to retrieve the Payment Constraints for. Multiple institutionIds need to be separated by `,`")],
        institution_country_code: Annotated[StrictStr, Field(description="Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response.")],
        payment_type: Annotated[StrictStr, Field(description="Type of payment to retrieve payment constraints for")],
        endpoint_path: Annotated[Optional[StrictStr], Field(description="The path on the API that is associated with the operation for which constraints are to be retrieved")] = None,
        endpoint_method: Annotated[Optional[StrictStr], Field(description="The HTTP method that is associated with the operation for which constraints are to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiListResponseOfPaymentConstraints:
        """Get Payment Constraints Rules

        Retrieve institution specific constraints for payment authorisation and submission requests

        :param institution_ids: Unique Id(s) of the `Institution`(s) to retrieve the Payment Constraints for. Multiple institutionIds need to be separated by `,` (required)
        :type institution_ids: List[str]
        :param institution_country_code: Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response. (required)
        :type institution_country_code: str
        :param payment_type: Type of payment to retrieve payment constraints for (required)
        :type payment_type: str
        :param endpoint_path: The path on the API that is associated with the operation for which constraints are to be retrieved
        :type endpoint_path: str
        :param endpoint_method: The HTTP method that is associated with the operation for which constraints are to be retrieved
        :type endpoint_method: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_payment_constraints_rules_by_institution_serialize(
            institution_ids=institution_ids,
            institution_country_code=institution_country_code,
            payment_type=payment_type,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiListResponseOfPaymentConstraints",
            '400': "ApiResponseError",
            '401': "ApiResponseError",
            '404': "ApiResponseError",
            '500': "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def get_payment_constraints_rules_by_institution_with_http_info(
        self,
        institution_ids: Annotated[List[StrictStr], Field(description="Unique Id(s) of the `Institution`(s) to retrieve the Payment Constraints for. Multiple institutionIds need to be separated by `,`")],
        institution_country_code: Annotated[StrictStr, Field(description="Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response.")],
        payment_type: Annotated[StrictStr, Field(description="Type of payment to retrieve payment constraints for")],
        endpoint_path: Annotated[Optional[StrictStr], Field(description="The path on the API that is associated with the operation for which constraints are to be retrieved")] = None,
        endpoint_method: Annotated[Optional[StrictStr], Field(description="The HTTP method that is associated with the operation for which constraints are to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ApiListResponseOfPaymentConstraints]:
        """Get Payment Constraints Rules

        Retrieve institution specific constraints for payment authorisation and submission requests

        :param institution_ids: Unique Id(s) of the `Institution`(s) to retrieve the Payment Constraints for. Multiple institutionIds need to be separated by `,` (required)
        :type institution_ids: List[str]
        :param institution_country_code: Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response. (required)
        :type institution_country_code: str
        :param payment_type: Type of payment to retrieve payment constraints for (required)
        :type payment_type: str
        :param endpoint_path: The path on the API that is associated with the operation for which constraints are to be retrieved
        :type endpoint_path: str
        :param endpoint_method: The HTTP method that is associated with the operation for which constraints are to be retrieved
        :type endpoint_method: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_payment_constraints_rules_by_institution_serialize(
            institution_ids=institution_ids,
            institution_country_code=institution_country_code,
            payment_type=payment_type,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiListResponseOfPaymentConstraints",
            '400': "ApiResponseError",
            '401': "ApiResponseError",
            '404': "ApiResponseError",
            '500': "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def get_payment_constraints_rules_by_institution_without_preload_content(
        self,
        institution_ids: Annotated[List[StrictStr], Field(description="Unique Id(s) of the `Institution`(s) to retrieve the Payment Constraints for. Multiple institutionIds need to be separated by `,`")],
        institution_country_code: Annotated[StrictStr, Field(description="Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response.")],
        payment_type: Annotated[StrictStr, Field(description="Type of payment to retrieve payment constraints for")],
        endpoint_path: Annotated[Optional[StrictStr], Field(description="The path on the API that is associated with the operation for which constraints are to be retrieved")] = None,
        endpoint_method: Annotated[Optional[StrictStr], Field(description="The HTTP method that is associated with the operation for which constraints are to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Payment Constraints Rules

        Retrieve institution specific constraints for payment authorisation and submission requests

        :param institution_ids: Unique Id(s) of the `Institution`(s) to retrieve the Payment Constraints for. Multiple institutionIds need to be separated by `,` (required)
        :type institution_ids: List[str]
        :param institution_country_code: Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response. (required)
        :type institution_country_code: str
        :param payment_type: Type of payment to retrieve payment constraints for (required)
        :type payment_type: str
        :param endpoint_path: The path on the API that is associated with the operation for which constraints are to be retrieved
        :type endpoint_path: str
        :param endpoint_method: The HTTP method that is associated with the operation for which constraints are to be retrieved
        :type endpoint_method: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_payment_constraints_rules_by_institution_serialize(
            institution_ids=institution_ids,
            institution_country_code=institution_country_code,
            payment_type=payment_type,
            endpoint_path=endpoint_path,
            endpoint_method=endpoint_method,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiListResponseOfPaymentConstraints",
            '400': "ApiResponseError",
            '401': "ApiResponseError",
            '404': "ApiResponseError",
            '500': "ApiResponseError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_payment_constraints_rules_by_institution_serialize(
        self,
        institution_ids,
        institution_country_code,
        payment_type,
        endpoint_path,
        endpoint_method,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'institutionIds': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if institution_ids is not None:
            
            _query_params.append(('institutionIds', institution_ids))
            
        if institution_country_code is not None:
            
            _query_params.append(('institutionCountryCode', institution_country_code))
            
        if payment_type is not None:
            
            _query_params.append(('paymentType', payment_type))
            
        if endpoint_path is not None:
            
            _query_params.append(('endpointPath', endpoint_path))
            
        if endpoint_method is not None:
            
            _query_params.append(('endpointMethod', endpoint_method))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json;charset=UTF-8'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'basicAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/institutions/constraints/payments',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


