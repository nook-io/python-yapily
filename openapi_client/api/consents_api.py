# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/#getting-started) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/guides/applications/institutions/sandbox/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ConsentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_consent_with_code(self, consent_auth_code_request, **kwargs):  # noqa: E501
        """Exchange OAuth2 Code  # noqa: E501

        Used to obtain a Yapily Consent object containing the `consentToken` once the user has authenticated and you have an OAuth2 authorisation code `auth-code` and state `auth-state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_consent_with_code(consent_auth_code_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ConsentAuthCodeRequest consent_auth_code_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Consent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_consent_with_code_with_http_info(consent_auth_code_request, **kwargs)  # noqa: E501

    def create_consent_with_code_with_http_info(self, consent_auth_code_request, **kwargs):  # noqa: E501
        """Exchange OAuth2 Code  # noqa: E501

        Used to obtain a Yapily Consent object containing the `consentToken` once the user has authenticated and you have an OAuth2 authorisation code `auth-code` and state `auth-state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_consent_with_code_with_http_info(consent_auth_code_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ConsentAuthCodeRequest consent_auth_code_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Consent, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'consent_auth_code_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_consent_with_code" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consent_auth_code_request' is set
        if self.api_client.client_side_validation and ('consent_auth_code_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['consent_auth_code_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consent_auth_code_request` when calling `create_consent_with_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'consent_auth_code_request' in local_var_params:
            body_params = local_var_params['consent_auth_code_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consent-auth-code', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Consent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete(self, consent_id, **kwargs):  # noqa: E501
        """Delete Consent  # noqa: E501

        Delete a consent using the consent Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete(consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent_id: __Mandatory__. The consent Id of the `Consent` to update. (required)
        :param bool force_delete: __Optional__. Whether to force the deletion.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponseOfConsentDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_with_http_info(consent_id, **kwargs)  # noqa: E501

    def delete_with_http_info(self, consent_id, **kwargs):  # noqa: E501
        """Delete Consent  # noqa: E501

        Delete a consent using the consent Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_with_http_info(consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent_id: __Mandatory__. The consent Id of the `Consent` to update. (required)
        :param bool force_delete: __Optional__. Whether to force the deletion.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponseOfConsentDeleteResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'consent_id',
            'force_delete'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consent_id' is set
        if self.api_client.client_side_validation and ('consent_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['consent_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consent_id` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in local_var_params:
            path_params['consentId'] = local_var_params['consent_id']  # noqa: E501

        query_params = []
        if 'force_delete' in local_var_params and local_var_params['force_delete'] is not None:  # noqa: E501
            query_params.append(('forceDelete', local_var_params['force_delete']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consents/{consentId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfConsentDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_consent_by_id(self, consent_id, **kwargs):  # noqa: E501
        """Get Consent  # noqa: E501

        Get consent using the consent Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consent_by_id(consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent_id: __Mandatory__. The consent Id of the `Consent` to update. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponseOfConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_consent_by_id_with_http_info(consent_id, **kwargs)  # noqa: E501

    def get_consent_by_id_with_http_info(self, consent_id, **kwargs):  # noqa: E501
        """Get Consent  # noqa: E501

        Get consent using the consent Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consent_by_id_with_http_info(consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent_id: __Mandatory__. The consent Id of the `Consent` to update. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponseOfConsent, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'consent_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consent_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consent_id' is set
        if self.api_client.client_side_validation and ('consent_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['consent_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consent_id` when calling `get_consent_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in local_var_params:
            path_params['consentId'] = local_var_params['consent_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consents/{consentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfConsent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_consent_by_single_access_consent(self, one_time_token_request, **kwargs):  # noqa: E501
        """Exchange One Time Token  # noqa: E501

        Exchange a One-time-token for the consent token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consent_by_single_access_consent(one_time_token_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param OneTimeTokenRequest one_time_token_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Consent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_consent_by_single_access_consent_with_http_info(one_time_token_request, **kwargs)  # noqa: E501

    def get_consent_by_single_access_consent_with_http_info(self, one_time_token_request, **kwargs):  # noqa: E501
        """Exchange One Time Token  # noqa: E501

        Exchange a One-time-token for the consent token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consent_by_single_access_consent_with_http_info(one_time_token_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param OneTimeTokenRequest one_time_token_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Consent, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'one_time_token_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consent_by_single_access_consent" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'one_time_token_request' is set
        if self.api_client.client_side_validation and ('one_time_token_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['one_time_token_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `one_time_token_request` when calling `get_consent_by_single_access_consent`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'one_time_token_request' in local_var_params:
            body_params = local_var_params['one_time_token_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consent-one-time-token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Consent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_consents(self, **kwargs):  # noqa: E501
        """Get Consents  # noqa: E501

        Used to retrieve all the consents created for each user within an application  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consents(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] filter_application_user_id: __Optional__. Filter records based on the list of `applicationUserId` users provided.
        :param list[str] filter_user_uuid: __Optional__. Filter records based on the list of `userUuid` users provided.
        :param list[str] filter_institution: __Optional__. Filter records based on the list of `Institution` provided.
        :param list[str] filter_status: __Optional__. Filter records based on the list of `Consent` [statuses](https://docs.yapily.com/api/#tocS_AuthorisationStatus).
        :param str _from: __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). 
        :param str before: __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).
        :param int limit: __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000.
        :param int offset: __Optional__. The number of transaction records to be skipped. Used primarily with paginated results.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiListResponseOfConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_consents_with_http_info(**kwargs)  # noqa: E501

    def get_consents_with_http_info(self, **kwargs):  # noqa: E501
        """Get Consents  # noqa: E501

        Used to retrieve all the consents created for each user within an application  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consents_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] filter_application_user_id: __Optional__. Filter records based on the list of `applicationUserId` users provided.
        :param list[str] filter_user_uuid: __Optional__. Filter records based on the list of `userUuid` users provided.
        :param list[str] filter_institution: __Optional__. Filter records based on the list of `Institution` provided.
        :param list[str] filter_status: __Optional__. Filter records based on the list of `Consent` [statuses](https://docs.yapily.com/api/#tocS_AuthorisationStatus).
        :param str _from: __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). 
        :param str before: __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).
        :param int limit: __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000.
        :param int offset: __Optional__. The number of transaction records to be skipped. Used primarily with paginated results.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiListResponseOfConsent, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'filter_application_user_id',
            'filter_user_uuid',
            'filter_institution',
            'filter_status',
            '_from',
            'before',
            'limit',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consents" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_application_user_id' in local_var_params and local_var_params['filter_application_user_id'] is not None:  # noqa: E501
            query_params.append(('filter[applicationUserId]', local_var_params['filter_application_user_id']))  # noqa: E501
            collection_formats['filter[applicationUserId]'] = 'multi'  # noqa: E501
        if 'filter_user_uuid' in local_var_params and local_var_params['filter_user_uuid'] is not None:  # noqa: E501
            query_params.append(('filter[userUuid]', local_var_params['filter_user_uuid']))  # noqa: E501
            collection_formats['filter[userUuid]'] = 'multi'  # noqa: E501
        if 'filter_institution' in local_var_params and local_var_params['filter_institution'] is not None:  # noqa: E501
            query_params.append(('filter[institution]', local_var_params['filter_institution']))  # noqa: E501
            collection_formats['filter[institution]'] = 'multi'  # noqa: E501
        if 'filter_status' in local_var_params and local_var_params['filter_status'] is not None:  # noqa: E501
            query_params.append(('filter[status]', local_var_params['filter_status']))  # noqa: E501
            collection_formats['filter[status]'] = 'multi'  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'before' in local_var_params and local_var_params['before'] is not None:  # noqa: E501
            query_params.append(('before', local_var_params['before']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfConsent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)