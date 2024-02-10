# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from yapily.models.virtual_account_beneficiary_account import VirtualAccountBeneficiaryAccount

class TestVirtualAccountBeneficiaryAccount(unittest.TestCase):
    """VirtualAccountBeneficiaryAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualAccountBeneficiaryAccount:
        """Test VirtualAccountBeneficiaryAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualAccountBeneficiaryAccount`
        """
        model = VirtualAccountBeneficiaryAccount()
        if include_optional:
            return VirtualAccountBeneficiaryAccount(
                currency = 'GBP',
                bank_name = 'Lloyds Bank',
                bank_address = 'WE12 ABC',
                bank_country = 'GB',
                account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}]
            )
        else:
            return VirtualAccountBeneficiaryAccount(
                currency = 'GBP',
                account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}],
        )
        """

    def testVirtualAccountBeneficiaryAccount(self):
        """Test VirtualAccountBeneficiaryAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
