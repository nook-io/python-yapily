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

from yapily.models.real_time_transaction import RealTimeTransaction  # noqa: E501


class TestRealTimeTransaction(unittest.TestCase):
    """RealTimeTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RealTimeTransaction:
        """Test RealTimeTransaction
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RealTimeTransaction`
        """
        model = RealTimeTransaction()  # noqa: E501
        if include_optional:
            return RealTimeTransaction(
                id = '',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                booking_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                value_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'BOOKED',
                transaction_amount = yapily.models.amount_details.Amount Details(
                    amount = 10, 
                    currency = 'GBP', ),
                gross_amount = yapily.models.amount_details.Amount Details(
                    amount = 10, 
                    currency = 'GBP', ),
                currency_exchange = yapily.models.currency_exchange.CurrencyExchange(
                    source_currency = '', 
                    target_currency = '', 
                    unit_currency = '', 
                    exchange_rate = 1.337, ),
                charge_details = yapily.models.transaction_charge_details.TransactionChargeDetails(
                    charge_amount = yapily.models.amount_details.Amount Details(
                        amount = 10, 
                        currency = 'GBP', ), ),
                reference = '',
                statement_references = [
                    yapily.models.statement_reference.StatementReference(
                        value = '', )
                    ],
                description = '',
                transaction_information = [
                    ''
                    ],
                address_details = yapily.models.address_details.AddressDetails(
                    address_line = '', ),
                iso_bank_transaction_code = yapily.models.iso_bank_transaction_code.IsoBankTransactionCode(
                    domain_code = yapily.models.iso_code_details.IsoCodeDetails(
                        code = 'UNKNOWN', 
                        name = 'UNKNOWN', ), 
                    family_code = yapily.models.iso_code_details.IsoCodeDetails(
                        code = 'UNKNOWN', 
                        name = 'UNKNOWN', ), 
                    sub_family_code = , ),
                proprietary_bank_transaction_code = yapily.models.proprietary_bank_transaction_code.ProprietaryBankTransactionCode(
                    code = '', 
                    issuer = '', ),
                balance = yapily.models.transaction_balance.TransactionBalance(
                    type = 'CLOSING_AVAILABLE', 
                    balance_amount = yapily.models.amount_details.Amount Details(
                        amount = 10, 
                        currency = 'GBP', ), ),
                payee_details = yapily.models.payee_details.Payee Details(
                    name = 'Jane Doe', 
                    account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                    account_type = '', 
                    address = {"country":"GB"}, 
                    merchant_id = '24589303', 
                    merchant_category_code = '5551', ),
                payer_details = yapily.models.payer_details.Payer Details(
                    name = 'John Doe', 
                    account_identifications = [
                        yapily.models.account_identifications.Account Identifications(
                            type = 'SORT_CODE', 
                            identification = '401016', )
                        ], 
                    address = {"country":"GB"}, ),
                merchant = yapily.models.merchant.Merchant(
                    merchant_name = '', 
                    merchant_category_code = '', ),
                supplementary_data = yapily.models.supplementary_data.supplementaryData()
            )
        else:
            return RealTimeTransaction(
        )
        """

    def testRealTimeTransaction(self):
        """Test RealTimeTransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
