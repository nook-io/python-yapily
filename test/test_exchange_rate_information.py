# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/#getting-started) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/guides/applications/institutions/sandbox/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.exchange_rate_information import ExchangeRateInformation  # noqa: E501
from openapi_client.rest import ApiException

class TestExchangeRateInformation(unittest.TestCase):
    """ExchangeRateInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExchangeRateInformation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.exchange_rate_information.ExchangeRateInformation()  # noqa: E501
        if include_optional :
            return ExchangeRateInformation(
                unit_currency = '0', 
                rate = 1.337, 
                rate_type = 'ACTUAL', 
                foreign_exchange_contract_reference = '0'
            )
        else :
            return ExchangeRateInformation(
                unit_currency = '0',
                rate_type = 'ACTUAL',
        )

    def testExchangeRateInformation(self):
        """Test ExchangeRateInformation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
