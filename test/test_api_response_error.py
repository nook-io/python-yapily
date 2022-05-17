# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/#getting-started) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/guides/applications/institutions/sandbox/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_response_error import ApiResponseError  # noqa: E501
from yapily.rest import ApiException

class TestApiResponseError(unittest.TestCase):
    """ApiResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_response_error.ApiResponseError()  # noqa: E501
        if include_optional :
            return ApiResponseError(
                error = yapily.models.api_error.ApiError(
                    code = 56, 
                    institution_error = yapily.models.institution_error.InstitutionError(
                        error_message = '0', 
                        http_status_code = 56, ), 
                    message = '0', 
                    source = '0', 
                    status = '0', 
                    tracing_id = '0', ), 
                monitoring = [
                    yapily.models.monitoring_endpoint_status.MonitoringEndpointStatus(
                        last_tested = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        resource_endpoint = '0', 
                        span = '0', 
                        status = 'Up', )
                    ], 
                raw = [
                    yapily.models.raw_response.RawResponse(
                        request = yapily.models.raw_request.RawRequest(
                            method = '0', 
                            url = '0', 
                            request_instant = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            headers = {
                                'key' : '0'
                                }, 
                            body = yapily.models.body.body(), 
                            body_parameters = {
                                'key' : '0'
                                }, 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        duration = '0', 
                        headers = {
                            'key' : '0'
                            }, 
                        result_code = 56, 
                        result = yapily.models.result.result(), )
                    ]
            )
        else :
            return ApiResponseError(
        )

    def testApiResponseError(self):
        """Test ApiResponseError"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
