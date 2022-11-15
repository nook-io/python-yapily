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
from yapily.models.virtual_account_pay_in_details import VirtualAccountPayInDetails  # noqa: E501
from yapily.rest import ApiException

class TestVirtualAccountPayInDetails(unittest.TestCase):
    """VirtualAccountPayInDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VirtualAccountPayInDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.virtual_account_pay_in_details.VirtualAccountPayInDetails()  # noqa: E501
        if include_optional :
            return VirtualAccountPayInDetails(
                id = 'za2ad0234-a333-5435-8787-a3a3cef4031c', 
                payment_scheme = 'FASTER_PAYMENTS', 
                amount = null, 
                reference = 'Invoice 1267765', 
                source = yapily.models.virtual_account_payment_source.VirtualAccountPaymentSource(
                    type = 'EXTERNAL', 
                    account_id = 'eb2ad083-a111-4143-8756-a3a3cef4031c', 
                    account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], ), 
                name = 'Sam Sender', 
                address = '123 Baker Street'
            )
        else :
            return VirtualAccountPayInDetails(
        )

    def testVirtualAccountPayInDetails(self):
        """Test VirtualAccountPayInDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
