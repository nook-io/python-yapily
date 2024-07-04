# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401

from pydantic import validate_arguments

from typing_extensions import Annotated
from pydantic import Field, StrictStr

from typing import Optional

from yapily.models.api_list_response_of_event_subscription_response import ApiListResponseOfEventSubscriptionResponse
from yapily.models.api_response_of_event_subscription_delete_response import ApiResponseOfEventSubscriptionDeleteResponse
from yapily.models.api_response_of_event_subscription_response import ApiResponseOfEventSubscriptionResponse
from yapily.models.event_subscription_request import EventSubscriptionRequest

from yapily.api_client import ApiClient
from yapily.api_response import ApiResponse
from yapily.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NotificationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_event_subscription(self, event_subscription_request : EventSubscriptionRequest, sub_application : Annotated[Optional[StrictStr], Field(description="The sub-application ID to which event type is being subscribed to")] = None, **kwargs) -> ApiResponseOfEventSubscriptionResponse:  # noqa: E501
        """Create Event Subscription  # noqa: E501

        Used to subscribe to notifications relating to a specified event type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_event_subscription(event_subscription_request, sub_application, async_req=True)
        >>> result = thread.get()

        :param event_subscription_request: (required)
        :type event_subscription_request: EventSubscriptionRequest
        :param sub_application: The sub-application ID to which event type is being subscribed to
        :type sub_application: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiResponseOfEventSubscriptionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_event_subscription_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_event_subscription_with_http_info(event_subscription_request, sub_application, **kwargs)  # noqa: E501

    @validate_arguments
    def create_event_subscription_with_http_info(self, event_subscription_request : EventSubscriptionRequest, sub_application : Annotated[Optional[StrictStr], Field(description="The sub-application ID to which event type is being subscribed to")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Event Subscription  # noqa: E501

        Used to subscribe to notifications relating to a specified event type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_event_subscription_with_http_info(event_subscription_request, sub_application, async_req=True)
        >>> result = thread.get()

        :param event_subscription_request: (required)
        :type event_subscription_request: EventSubscriptionRequest
        :param sub_application: The sub-application ID to which event type is being subscribed to
        :type sub_application: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiResponseOfEventSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'event_subscription_request',
            'sub_application'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_event_subscription" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['sub_application'] is not None:
            _header_params['sub-application'] = _params['sub_application']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['event_subscription_request'] is not None:
            _body_params = _params['event_subscription_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['basicAuth']  # noqa: E501

        _response_types_map = {
            '201': "ApiResponseOfEventSubscriptionResponse",
            '400': None,
            '401': None,
            '409': None,
        }

        return self.api_client.call_api(
            '/notifications/event-subscriptions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_event_subscription_by_id(self, event_type_id : Annotated[StrictStr, Field(..., description="Unique identifier of the event type (for which notifications will be sent). ")], sub_application : Annotated[Optional[StrictStr], Field(description="The sub-application ID for which event type will be deleted")] = None, **kwargs) -> ApiResponseOfEventSubscriptionDeleteResponse:  # noqa: E501
        """Delete Event Subscription  # noqa: E501

        Used to unsubscribe to notifications relating to a specified event type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_event_subscription_by_id(event_type_id, sub_application, async_req=True)
        >>> result = thread.get()

        :param event_type_id: Unique identifier of the event type (for which notifications will be sent).  (required)
        :type event_type_id: str
        :param sub_application: The sub-application ID for which event type will be deleted
        :type sub_application: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiResponseOfEventSubscriptionDeleteResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_event_subscription_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.delete_event_subscription_by_id_with_http_info(event_type_id, sub_application, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_event_subscription_by_id_with_http_info(self, event_type_id : Annotated[StrictStr, Field(..., description="Unique identifier of the event type (for which notifications will be sent). ")], sub_application : Annotated[Optional[StrictStr], Field(description="The sub-application ID for which event type will be deleted")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Delete Event Subscription  # noqa: E501

        Used to unsubscribe to notifications relating to a specified event type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_event_subscription_by_id_with_http_info(event_type_id, sub_application, async_req=True)
        >>> result = thread.get()

        :param event_type_id: Unique identifier of the event type (for which notifications will be sent).  (required)
        :type event_type_id: str
        :param sub_application: The sub-application ID for which event type will be deleted
        :type sub_application: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiResponseOfEventSubscriptionDeleteResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'event_type_id',
            'sub_application'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_event_subscription_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['event_type_id'] is not None:
            _path_params['eventTypeId'] = _params['event_type_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['sub_application'] is not None:
            _header_params['sub-application'] = _params['sub_application']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth']  # noqa: E501

        _response_types_map = {
            '200': "ApiResponseOfEventSubscriptionDeleteResponse",
            '401': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/notifications/event-subscriptions/{eventTypeId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_event_subscription_by_id(self, event_type_id : Annotated[StrictStr, Field(..., description="Unique identifier of the event type (for which notifications will be sent). ")], sub_application : Annotated[Optional[StrictStr], Field(description="The sub-application ID for which details of specific event type will be returned")] = None, **kwargs) -> ApiResponseOfEventSubscriptionResponse:  # noqa: E501
        """Get Event Subscription  # noqa: E501

        Used to get details of your subscription to a specified event type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_subscription_by_id(event_type_id, sub_application, async_req=True)
        >>> result = thread.get()

        :param event_type_id: Unique identifier of the event type (for which notifications will be sent).  (required)
        :type event_type_id: str
        :param sub_application: The sub-application ID for which details of specific event type will be returned
        :type sub_application: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiResponseOfEventSubscriptionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_event_subscription_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_event_subscription_by_id_with_http_info(event_type_id, sub_application, **kwargs)  # noqa: E501

    @validate_arguments
    def get_event_subscription_by_id_with_http_info(self, event_type_id : Annotated[StrictStr, Field(..., description="Unique identifier of the event type (for which notifications will be sent). ")], sub_application : Annotated[Optional[StrictStr], Field(description="The sub-application ID for which details of specific event type will be returned")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Event Subscription  # noqa: E501

        Used to get details of your subscription to a specified event type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_subscription_by_id_with_http_info(event_type_id, sub_application, async_req=True)
        >>> result = thread.get()

        :param event_type_id: Unique identifier of the event type (for which notifications will be sent).  (required)
        :type event_type_id: str
        :param sub_application: The sub-application ID for which details of specific event type will be returned
        :type sub_application: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiResponseOfEventSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'event_type_id',
            'sub_application'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_subscription_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['event_type_id'] is not None:
            _path_params['eventTypeId'] = _params['event_type_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['sub_application'] is not None:
            _header_params['sub-application'] = _params['sub_application']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth']  # noqa: E501

        _response_types_map = {
            '200': "ApiResponseOfEventSubscriptionResponse",
            '401': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/notifications/event-subscriptions/{eventTypeId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_event_subscriptions(self, sub_application : Annotated[Optional[StrictStr], Field(description="The sub-application ID for which all event subscriptions will be returned")] = None, **kwargs) -> ApiListResponseOfEventSubscriptionResponse:  # noqa: E501
        """Get Event Subscriptions  # noqa: E501

        Get all event subscriptions that your application is subscribed to  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_subscriptions(sub_application, async_req=True)
        >>> result = thread.get()

        :param sub_application: The sub-application ID for which all event subscriptions will be returned
        :type sub_application: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiListResponseOfEventSubscriptionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_event_subscriptions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_event_subscriptions_with_http_info(sub_application, **kwargs)  # noqa: E501

    @validate_arguments
    def get_event_subscriptions_with_http_info(self, sub_application : Annotated[Optional[StrictStr], Field(description="The sub-application ID for which all event subscriptions will be returned")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Event Subscriptions  # noqa: E501

        Get all event subscriptions that your application is subscribed to  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_subscriptions_with_http_info(sub_application, async_req=True)
        >>> result = thread.get()

        :param sub_application: The sub-application ID for which all event subscriptions will be returned
        :type sub_application: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiListResponseOfEventSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'sub_application'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_subscriptions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['sub_application'] is not None:
            _header_params['sub-application'] = _params['sub_application']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth']  # noqa: E501

        _response_types_map = {
            '200': "ApiListResponseOfEventSubscriptionResponse",
            '401': None,
        }

        return self.api_client.call_api(
            '/notifications/event-subscriptions', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
