# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 7.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from yapily.models.api_error_response_v2_error import ApiErrorResponseV2Error

class TestApiErrorResponseV2Error(unittest.TestCase):
    """ApiErrorResponseV2Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiErrorResponseV2Error:
        """Test ApiErrorResponseV2Error
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiErrorResponseV2Error`
        """
        model = ApiErrorResponseV2Error()
        if include_optional:
            return ApiErrorResponseV2Error(
                tracing_id = '',
                code = 56,
                status = '',
                support_url = '',
                source = '',
                issues = [
                    yapily.models.api_error_response_v2_error_issues_inner.ApiErrorResponseV2_error_issues_inner(
                        type = '', 
                        code = '', 
                        message = '', )
                    ]
            )
        else:
            return ApiErrorResponseV2Error(
                tracing_id = '',
                code = 56,
                status = '',
                issues = [
                    yapily.models.api_error_response_v2_error_issues_inner.ApiErrorResponseV2_error_issues_inner(
                        type = '', 
                        code = '', 
                        message = '', )
                    ],
        )
        """

    def testApiErrorResponseV2Error(self):
        """Test ApiErrorResponseV2Error"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
