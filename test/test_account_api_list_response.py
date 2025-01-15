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

from yapily.models.account_api_list_response import AccountApiListResponse  # noqa: E501


class TestAccountApiListResponse(unittest.TestCase):
    """AccountApiListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountApiListResponse:
        """Test AccountApiListResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AccountApiListResponse`
        """
        model = AccountApiListResponse()  # noqa: E501
        if include_optional:
            return AccountApiListResponse(
                meta = yapily.models.response_list_meta.ResponseListMeta(
                    tracing_id = '', 
                    count = 56, 
                    pagination = yapily.models.pagination.Pagination(
                        total_count = 56, 
                        self = yapily.models.filter_and_sort.FilterAndSort(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            sort = 'date', 
                            offset = 56, 
                            cursor = '', ), 
                        next = yapily.models.next.Next(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            cursor = '', ), ), ),
                data = [
                    yapily.models.account.Account(
                        id = '', 
                        type = '', 
                        description = '', 
                        balance = 1.337, 
                        currency = '', 
                        usage_type = 'PERSONAL', 
                        account_type = 'CASH_TRADING', 
                        nickname = '', 
                        details = '', 
                        account_names = [
                            yapily.models.account_name.AccountName(
                                name = '', )
                            ], 
                        account_identifications = [
                            yapily.models.account_identifications.Account Identifications(
                                type = 'SORT_CODE', 
                                identification = '401016', )
                            ], 
                        account_balances = [
                            yapily.models.account_balance.AccountBalance(
                                date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                balance_amount = yapily.models.amount_details.Amount Details(
                                    amount = 10, 
                                    currency = 'GBP', ), 
                                credit_line_included = True, 
                                credit_lines = [
                                    yapily.models.credit_line.CreditLine(
                                        credit_line_amount = yapily.models.amount_details.Amount Details(
                                            amount = 10, 
                                            currency = 'GBP', ), )
                                    ], )
                            ], 
                        consolidated_account_information = yapily.models.consolidated_account_information.ConsolidatedAccountInformation(
                            id = '', ), )
                    ],
                links = {
                    'key' : ''
                    },
                forwarded_data = [
                    yapily.models.response_forwarded_data.ResponseForwardedData(
                        headers = {
                            'key' : ''
                            }, 
                        url = '', )
                    ],
                raw = [
                    yapily.models.raw_response.RawResponse(
                        request = yapily.models.raw_request.RawRequest(
                            method = '', 
                            url = '', 
                            request_instant = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            headers = {
                                'key' : ''
                                }, 
                            body = yapily.models.body.body(), 
                            body_parameters = {
                                'key' : ''
                                }, 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        duration = '', 
                        headers = {
                            'key' : ''
                            }, 
                        result_code = 56, 
                        result = yapily.models.result.result(), )
                    ],
                paging = yapily.models.filtered_client_payload_list_account.FilteredClientPayloadListAccount(
                    api_call = yapily.models.api_call.ApiCall(), 
                    data = [
                        yapily.models.account.Account(
                            id = '', 
                            type = '', 
                            description = '', 
                            balance = 1.337, 
                            currency = '', 
                            usage_type = 'PERSONAL', 
                            account_type = 'CASH_TRADING', 
                            nickname = '', 
                            details = '', 
                            account_names = [
                                yapily.models.account_name.AccountName(
                                    name = '', )
                                ], 
                            account_identifications = [
                                yapily.models.account_identifications.Account Identifications(
                                    type = 'SORT_CODE', 
                                    identification = '401016', )
                                ], 
                            account_balances = [
                                yapily.models.account_balance.AccountBalance(
                                    date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    balance_amount = yapily.models.amount_details.Amount Details(
                                        amount = 10, 
                                        currency = 'GBP', ), 
                                    credit_line_included = True, 
                                    credit_lines = [
                                        yapily.models.credit_line.CreditLine(
                                            credit_line_amount = yapily.models.amount_details.Amount Details(
                                                amount = 10, 
                                                currency = 'GBP', ), )
                                        ], )
                                ], 
                            consolidated_account_information = yapily.models.consolidated_account_information.ConsolidatedAccountInformation(
                                id = '', ), )
                        ], 
                    next_cursor_hash = '', 
                    next_link = '', 
                    paging_map = {
                        'key' : yapily.models.filter_and_sort.FilterAndSort(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            sort = 'date', 
                            offset = 56, 
                            cursor = '', )
                        }, 
                    total_count = 56, ),
                tracing_id = ''
            )
        else:
            return AccountApiListResponse(
        )
        """

    def testAccountApiListResponse(self):
        """Test AccountApiListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
