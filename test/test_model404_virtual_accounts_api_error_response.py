# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from yapily.models.model404_virtual_accounts_api_error_response import Model404VirtualAccountsApiErrorResponse  # noqa: E501

class TestModel404VirtualAccountsApiErrorResponse(unittest.TestCase):
    """Model404VirtualAccountsApiErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Model404VirtualAccountsApiErrorResponse:
        """Test Model404VirtualAccountsApiErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Model404VirtualAccountsApiErrorResponse`
        """
        model = Model404VirtualAccountsApiErrorResponse()  # noqa: E501
        if include_optional:
            return Model404VirtualAccountsApiErrorResponse(
                error = yapily.models.error_details.ErrorDetails(
                    tracing_id = '', 
                    code = 56, 
                    status = '', 
                    support_url = '', 
                    source = '', 
                    issues = [
                        yapily.models.error_issue.ErrorIssue(
                            type = '', 
                            code = '', 
                            parameter = '', 
                            message = '', 
                            institution_error = yapily.models.institution_error.InstitutionError(
                                error_message = '', 
                                http_status_code = 56, ), )
                        ], ),
                monitoring = [
                    yapily.models.monitoring_endpoint_status.MonitoringEndpointStatus(
                        last_tested = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        resource_endpoint = '', 
                        span = '', 
                        status = 'Up', )
                    ]
            )
        else:
            return Model404VirtualAccountsApiErrorResponse(
        )
        """

    def testModel404VirtualAccountsApiErrorResponse(self):
        """Test Model404VirtualAccountsApiErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
