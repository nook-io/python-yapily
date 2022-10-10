# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.virtual_account_client import VirtualAccountClient  # noqa: E501
from yapily.rest import ApiException

class TestVirtualAccountClient(unittest.TestCase):
    """VirtualAccountClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VirtualAccountClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.virtual_account_client.VirtualAccountClient()  # noqa: E501
        if include_optional :
            return VirtualAccountClient(
                id = 'cf996ecc-8720-4bb3-8dbb-fe9018e0db12', 
                type = 'INDIVIDUAL', 
                kyc_status = 'UNVERIFIED', 
                status = 'PENDING', 
                created_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                individual = yapily.models.virtual_account_individual_client.VirtualAccountIndividualClient(
                    first_name = '0', 
                    middle_name = '0', 
                    last_name = '0', 
                    address = yapily.models.virtual_account_address.VirtualAccountAddress(
                        address_line1 = '12 New Street', 
                        address_line2 = 'Barcelona CA 08005', 
                        town_name = 'Barcelona ', 
                        post_code = '08005', 
                        country = 'ES', ), 
                    birth_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    email = '0', 
                    phone = '0', ), 
                business = yapily.models.virtual_account_business_client.VirtualAccountBusinessClient(
                    name = '0', 
                    type = 'SOLE_TRADER', 
                    registration_number = '0', 
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
                    contact_name = '0', 
                    email = '0', 
                    phone = '0', )
            )
        else :
            return VirtualAccountClient(
        )

    def testVirtualAccountClient(self):
        """Test VirtualAccountClient"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
