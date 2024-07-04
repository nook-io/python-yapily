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

from yapily.models.initiation_details import InitiationDetails  # noqa: E501

class TestInitiationDetails(unittest.TestCase):
    """InitiationDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InitiationDetails:
        """Test InitiationDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InitiationDetails`
        """
        model = InitiationDetails()  # noqa: E501
        if include_optional:
            return InitiationDetails(
                reference = 'Own Account Sweeping',
                payer = yapily.models.payer_details.Payer Details(
                    name = 'John Doe', 
                    account_identifications = [
                        yapily.models.account_identifications.Account Identifications(
                            type = 'SORT_CODE', 
                            identification = '401016', )
                        ], 
                    address = {"country":"GB"}, ),
                payee = yapily.models.payee_details.Payee Details(
                    name = 'Jane Doe', 
                    account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                    account_type = '', 
                    address = {"country":"GB"}, 
                    merchant_id = '24589303', 
                    merchant_category_code = '5551', )
            )
        else:
            return InitiationDetails(
        )
        """

    def testInitiationDetails(self):
        """Test InitiationDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
