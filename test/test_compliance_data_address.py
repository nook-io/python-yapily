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

from yapily.models.compliance_data_address import ComplianceDataAddress  # noqa: E501

class TestComplianceDataAddress(unittest.TestCase):
    """ComplianceDataAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComplianceDataAddress:
        """Test ComplianceDataAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComplianceDataAddress`
        """
        model = ComplianceDataAddress()  # noqa: E501
        if include_optional:
            return ComplianceDataAddress(
                address_line1 = '123 Queens Street',
                address_line2 = 'Unit 13',
                town_name = 'York',
                post_code = '12345',
                country = 'GB'
            )
        else:
            return ComplianceDataAddress(
                address_line1 = '123 Queens Street',
                town_name = 'York',
                post_code = '12345',
                country = 'GB',
        )
        """

    def testComplianceDataAddress(self):
        """Test ComplianceDataAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()