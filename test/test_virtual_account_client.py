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

from yapily.models.virtual_account_client import VirtualAccountClient

class TestVirtualAccountClient(unittest.TestCase):
    """VirtualAccountClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualAccountClient:
        """Test VirtualAccountClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualAccountClient`
        """
        model = VirtualAccountClient()
        if include_optional:
            return VirtualAccountClient(
                id = 'cf996ecc-8720-4bb3-8dbb-fe9018e0db12',
                type = 'INDIVIDUAL',
                kyc_status = 'UNVERIFIED',
                status = 'PENDING',
                created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                individual = yapily.models.virtual_account_individual_client.VirtualAccountIndividualClient(
                    first_name = '', 
                    middle_name = '', 
                    last_name = '', 
                    address = yapily.models.virtual_account_address.VirtualAccountAddress(
                        address_line1 = '12 New Street', 
                        address_line2 = 'Barcelona CA 08005', 
                        town_name = 'Barcelona ', 
                        post_code = '08005', 
                        country = 'ES', ), 
                    birth_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    email = '', 
                    phone = '', ),
                business = yapily.models.virtual_account_business_client.VirtualAccountBusinessClient(
                    name = '', 
                    type = 'SOLE_TRADER', 
                    registration_number = '', 
                    registered_address = yapily.models.virtual_account_address.VirtualAccountAddress(
                        address_line1 = '12 New Street', 
                        address_line2 = 'Barcelona CA 08005', 
                        town_name = 'Barcelona ', 
                        post_code = '08005', 
                        country = 'ES', ), 
                    trading_address = yapily.models.virtual_account_address.VirtualAccountAddress(
                        address_line1 = '12 New Street', 
                        address_line2 = 'Barcelona CA 08005', 
                        town_name = 'Barcelona ', 
                        post_code = '08005', 
                        country = 'ES', ), 
                    contact_name = '', 
                    email = '', 
                    phone = '', )
            )
        else:
            return VirtualAccountClient(
        )
        """

    def testVirtualAccountClient(self):
        """Test VirtualAccountClient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
