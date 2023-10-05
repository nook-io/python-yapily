# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.25.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from yapily.models.compliance_data import ComplianceData  # noqa: E501

class TestComplianceData(unittest.TestCase):
    """ComplianceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComplianceData:
        """Test ComplianceData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComplianceData`
        """
        model = ComplianceData()  # noqa: E501
        if include_optional:
            return ComplianceData(
                payer = yapily.models.compliance_data_payer.ComplianceDataPayer(
                    type = 'INDIVIDUAL', 
                    individual = yapily.models.compliance_data_individual.ComplianceDataIndividual(
                        name = 'John Doe', 
                        birth_date = 'Sat Aug 12 01:00:00 BST 2000', ), 
                    business = yapily.models.compliance_data_business.ComplianceDataBusiness(
                        name = 'Company LTD', 
                        registration_number = 'COM123NO', 
                        registered_address = yapily.models.compliance_data_address.ComplianceDataAddress(
                            address_line1 = '123 Queens Street', 
                            address_line2 = 'Unit 13', 
                            town_name = 'York', 
                            post_code = '12345', 
                            country = 'GB', ), 
                        trading_address = yapily.models.compliance_data_address.ComplianceDataAddress(
                            address_line1 = '123 Queens Street', 
                            address_line2 = 'Unit 13', 
                            town_name = 'York', 
                            post_code = '12345', 
                            country = 'GB', ), ), )
            )
        else:
            return ComplianceData(
        )
        """

    def testComplianceData(self):
        """Test ComplianceData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
