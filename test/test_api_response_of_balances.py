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
from yapily.models.api_response_of_balances import ApiResponseOfBalances  # noqa: E501
from yapily.rest import ApiException

class TestApiResponseOfBalances(unittest.TestCase):
    """ApiResponseOfBalances unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseOfBalances
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_response_of_balances.ApiResponseOfBalances()  # noqa: E501
        if include_optional :
            return ApiResponseOfBalances(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '0', ), 
                data = yapily.models.balances.Balances(
                    main_balance_amount = yapily.models.amount.Amount(
                        amount = 10, 
                        currency = 'GBP', ), 
                    balances = [
                        yapily.models.account_balance.AccountBalance(
                            type = 'CLOSING_AVAILABLE', 
                            date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            balance_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), 
                            credit_line_included = True, 
                            credit_lines = [
                                yapily.models.credit_line.CreditLine(
                                    credit_line_amount = yapily.models.amount.Amount(
                                        amount = 10, 
                                        currency = 'GBP', ), )
                                ], )
                        ], ), 
                links = {
                    'key' : '0'
                    }, 
                forwarded_data = [
                    yapily.models.response_forwarded_data.ResponseForwardedData(
                        headers = {
                            'key' : '0'
                            }, 
                        url = '0', )
                    ], 
                raw = [
                    yapily.models.raw_response.RawResponse(
                        request = yapily.models.raw_request.RawRequest(
                            method = '0', 
                            url = '0', 
                            request_instant = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            headers = {
                                'key' : '0'
                                }, 
                            body = yapily.models.body.body(), 
                            body_parameters = {
                                'key' : '0'
                                }, 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        duration = '0', 
                        headers = {
                            'key' : '0'
                            }, 
                        result_code = 56, 
                        result = yapily.models.result.result(), )
                    ], 
                tracing_id = '0'
            )
        else :
            return ApiResponseOfBalances(
        )

    def testApiResponseOfBalances(self):
        """Test ApiResponseOfBalances"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
