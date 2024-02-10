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

from yapily.models.virtual_account_payment import VirtualAccountPayment

class TestVirtualAccountPayment(unittest.TestCase):
    """VirtualAccountPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualAccountPayment:
        """Test VirtualAccountPayment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualAccountPayment`
        """
        model = VirtualAccountPayment()
        if include_optional:
            return VirtualAccountPayment(
                id = 'za2ad0234-a333-5435-8787-a3a3cef4031c',
                created_date_time = '2022-04-24T00:30:19.951Z',
                payment_date = 'Tue Oct 04 01:00:00 BST 2022',
                type = 'PAY_IN',
                payment_scheme = 'FASTER_PAYMENTS',
                amount = None,
                reference = 'Invoice 1267765',
                status = 'INITIATED',
                source = yapily.models.virtual_account_payment_source.VirtualAccountPaymentSource(
                    type = 'EXTERNAL', 
                    account_id = 'eb2ad083-a111-4143-8756-a3a3cef4031c', 
                    account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], ),
                destination = yapily.models.virtual_account_payment_destination.VirtualAccountPaymentDestination(
                    type = 'EXTERNAL', 
                    account_id = 'eb2ad083-a111-4143-8756-a3a3cef4031c', 
                    account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                    beneficiary_id = 'sd6ad034-a111-4143-8756-a3a3cef4045v', ),
                original_payment_id = 'za2ad0234-a333-5435-8787-a3a3cef4031c'
            )
        else:
            return VirtualAccountPayment(
        )
        """

    def testVirtualAccountPayment(self):
        """Test VirtualAccountPayment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
