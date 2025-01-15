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

from yapily.models.account import Account  # noqa: E501


class TestAccount(unittest.TestCase):
    """Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Account:
        """Test Account
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Account`
        """
        model = Account()  # noqa: E501
        if include_optional:
            return Account(
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
                        type = 'CLOSING_AVAILABLE', 
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
                    id = '', 
                    account_balances = [
                        yapily.models.account_balance.AccountBalance(
                            type = 'CLOSING_AVAILABLE', 
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
                        ], )
            )
        else:
            return Account(
        )
        """

    def testAccount(self):
        """Test Account"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
