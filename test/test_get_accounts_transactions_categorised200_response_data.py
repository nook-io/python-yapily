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
import datetime

from yapily.models.get_accounts_transactions_categorised200_response_data import GetAccountsTransactionsCategorised200ResponseData  # noqa: E501

class TestGetAccountsTransactionsCategorised200ResponseData(unittest.TestCase):
    """GetAccountsTransactionsCategorised200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountsTransactionsCategorised200ResponseData:
        """Test GetAccountsTransactionsCategorised200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountsTransactionsCategorised200ResponseData`
        """
        model = GetAccountsTransactionsCategorised200ResponseData()  # noqa: E501
        if include_optional:
            return GetAccountsTransactionsCategorised200ResponseData(
                transactions = [
                    yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner.get_accounts_transactions_categorised_200_response_data_transactions_inner(
                        id = '', 
                        date = '', 
                        booking_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = '', 
                        amount = 56, 
                        currency = '', 
                        transaction_amount = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_transaction_amount.get_accounts_transactions_categorised_200_response_data_transactions_inner_transactionAmount(
                            amount = 56, 
                            currency = '', ), 
                        reference = '', 
                        description = '', 
                        transaction_information = [
                            ''
                            ], 
                        proprietary_bank_transaction_code = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_proprietary_bank_transaction_code.get_accounts_transactions_categorised_200_response_data_transactions_inner_proprietaryBankTransactionCode(
                            code = '', 
                            issuer = '', ), 
                        iso_bank_transaction_code = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_iso_bank_transaction_code.get_accounts_transactions_categorised_200_response_data_transactions_inner_isoBankTransactionCode(
                            domain_code = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_iso_bank_transaction_code_domain_code.get_accounts_transactions_categorised_200_response_data_transactions_inner_isoBankTransactionCode_domainCode(
                                code = '', 
                                name = '', ), 
                            family_code = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_iso_bank_transaction_code_domain_code.get_accounts_transactions_categorised_200_response_data_transactions_inner_isoBankTransactionCode_domainCode(
                                code = '', 
                                name = '', ), 
                            sub_family_code = , ), 
                        balance = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_balance.get_accounts_transactions_categorised_200_response_data_transactions_inner_balance(
                            type = '', 
                            balance_amount = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_transaction_amount.get_accounts_transactions_categorised_200_response_data_transactions_inner_transactionAmount(
                                amount = 56, 
                                currency = '', ), ), 
                        enrichment = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_enrichment.get_accounts_transactions_categorised_200_response_data_transactions_inner_enrichment(
                            categorisation = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_enrichment_categorisation.get_accounts_transactions_categorised_200_response_data_transactions_inner_enrichment_categorisation(
                                categories = [
                                    ''
                                    ], ), 
                            recurrence = '', 
                            transaction_hash = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_enrichment_transaction_hash.get_accounts_transactions_categorised_200_response_data_transactions_inner_enrichment_transactionHash(
                                hash = '', ), 
                            merchant = yapily.models.get_accounts_transactions_categorised_200_response_data_transactions_inner_enrichment_merchant.get_accounts_transactions_categorised_200_response_data_transactions_inner_enrichment_merchant(
                                id = '', 
                                name = '', ), 
                            payment_processor = '', ), 
                        hash = '', )
                    ]
            )
        else:
            return GetAccountsTransactionsCategorised200ResponseData(
        )
        """

    def testGetAccountsTransactionsCategorised200ResponseData(self):
        """Test GetAccountsTransactionsCategorised200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()