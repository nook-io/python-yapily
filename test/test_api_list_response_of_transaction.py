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

import yapily
from yapily.models.api_list_response_of_transaction import ApiListResponseOfTransaction  # noqa: E501
from yapily.rest import ApiException

class TestApiListResponseOfTransaction(unittest.TestCase):
    """ApiListResponseOfTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiListResponseOfTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_list_response_of_transaction.ApiListResponseOfTransaction()  # noqa: E501
        if include_optional :
            return ApiListResponseOfTransaction(
                meta = yapily.models.response_list_meta.ResponseListMeta(
                    tracing_id = '0', 
                    count = 56, 
                    pagination = yapily.models.pagination.Pagination(
                        total_count = 56, 
                        self = yapily.models.filter_and_sort.FilterAndSort(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            sort = 'date', 
                            offset = 56, 
                            cursor = '0', ), 
                        next = yapily.models.next.Next(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            cursor = '0', ), ), ), 
                data = [
                    yapily.models.transaction.Transaction(
                        id = '0', 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        booking_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'BOOKED', 
                        amount = 1.337, 
                        currency = '0', 
                        transaction_amount = yapily.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        gross_amount = yapily.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        currency_exchange = yapily.models.currency_exchange.CurrencyExchange(
                            source_currency = '0', 
                            target_currency = '0', 
                            unit_currency = '0', 
                            exchange_rate = 1.337, ), 
                        charge_details = yapily.models.transaction_charge_details.TransactionChargeDetails(
                            charge_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), ), 
                        reference = '0', 
                        statement_references = [
                            yapily.models.statement_reference.StatementReference(
                                value = '0', )
                            ], 
                        description = '0', 
                        transaction_information = [
                            '0'
                            ], 
                        address_details = yapily.models.address_details.AddressDetails(
                            address_line = '0', ), 
                        iso_bank_transaction_code = yapily.models.iso_bank_transaction_code.IsoBankTransactionCode(
                            domain_code = yapily.models.iso_code_details.IsoCodeDetails(
                                code = 'UNKNOWN', 
                                name = 'UNKNOWN', ), 
                            family_code = yapily.models.iso_code_details.IsoCodeDetails(
                                code = 'UNKNOWN', 
                                name = 'UNKNOWN', ), 
                            sub_family_code = yapily.models.iso_code_details.IsoCodeDetails(
                                code = 'UNKNOWN', 
                                name = 'UNKNOWN', ), ), 
                        proprietary_bank_transaction_code = yapily.models.proprietary_bank_transaction_code.ProprietaryBankTransactionCode(
                            code = '0', 
                            issuer = '0', ), 
                        balance = yapily.models.transaction_balance.TransactionBalance(
                            type = 'CLOSING_AVAILABLE', 
                            balance_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), ), 
                        payee_details = yapily.models.payee.Payee(
                            name = 'Jane Doe', 
                            account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                            address = {"country":"GB"}, 
                            merchant_id = '24589303', 
                            merchant_category_code = '5551', ), 
                        payer_details = yapily.models.payer.Payer(
                            name = 'John Doe', 
                            account_identifications = [
                                yapily.models.account_identification.AccountIdentification(
                                    type = 'SORT_CODE', 
                                    identification = '401016', )
                                ], ), 
                        merchant = yapily.models.merchant.Merchant(
                            merchant_name = '0', 
                            merchant_category_code = '0', ), 
                        enrichment = yapily.models.enrichment.Enrichment(
                            categorisation = yapily.models.categorisation.Categorisation(
                                categories = [
                                    '0'
                                    ], 
                                source = '0', ), 
                            transaction_hash = yapily.models.transaction_hash.TransactionHash(
                                hash = '0', ), 
                            cleansed_description = '0', 
                            location = '0', 
                            payment_processor = '0', 
                            corrected_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        supplementary_data = yapily.models.supplementary_data.supplementaryData(), )
                    ], 
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
                paging = yapily.models.filtered_client_payload_list_transaction.FilteredClientPayloadListTransaction(
                    api_call = yapily.models.api_call.ApiCall(), 
                    data = [
                        yapily.models.transaction.Transaction(
                            id = '0', 
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            booking_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            value_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            status = 'BOOKED', 
                            amount = 1.337, 
                            currency = '0', 
                            transaction_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), 
                            gross_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), 
                            currency_exchange = yapily.models.currency_exchange.CurrencyExchange(
                                source_currency = '0', 
                                target_currency = '0', 
                                unit_currency = '0', 
                                exchange_rate = 1.337, ), 
                            charge_details = yapily.models.transaction_charge_details.TransactionChargeDetails(
                                charge_amount = yapily.models.amount.Amount(
                                    amount = 10, 
                                    currency = 'GBP', ), ), 
                            reference = '0', 
                            statement_references = [
                                yapily.models.statement_reference.StatementReference(
                                    value = '0', )
                                ], 
                            description = '0', 
                            transaction_information = [
                                '0'
                                ], 
                            address_details = yapily.models.address_details.AddressDetails(
                                address_line = '0', ), 
                            iso_bank_transaction_code = yapily.models.iso_bank_transaction_code.IsoBankTransactionCode(
                                domain_code = yapily.models.iso_code_details.IsoCodeDetails(
                                    code = 'UNKNOWN', 
                                    name = 'UNKNOWN', ), 
                                family_code = yapily.models.iso_code_details.IsoCodeDetails(
                                    code = 'UNKNOWN', 
                                    name = 'UNKNOWN', ), 
                                sub_family_code = yapily.models.iso_code_details.IsoCodeDetails(
                                    code = 'UNKNOWN', 
                                    name = 'UNKNOWN', ), ), 
                            proprietary_bank_transaction_code = yapily.models.proprietary_bank_transaction_code.ProprietaryBankTransactionCode(
                                code = '0', 
                                issuer = '0', ), 
                            balance = yapily.models.transaction_balance.TransactionBalance(
                                type = 'CLOSING_AVAILABLE', 
                                balance_amount = yapily.models.amount.Amount(
                                    amount = 10, 
                                    currency = 'GBP', ), ), 
                            payee_details = yapily.models.payee.Payee(
                                name = 'Jane Doe', 
                                account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                                address = {"country":"GB"}, 
                                merchant_id = '24589303', 
                                merchant_category_code = '5551', ), 
                            payer_details = yapily.models.payer.Payer(
                                name = 'John Doe', 
                                account_identifications = [
                                    yapily.models.account_identification.AccountIdentification(
                                        type = 'SORT_CODE', 
                                        identification = '401016', )
                                    ], ), 
                            merchant = yapily.models.merchant.Merchant(
                                merchant_name = '0', 
                                merchant_category_code = '0', ), 
                            enrichment = yapily.models.enrichment.Enrichment(
                                categorisation = yapily.models.categorisation.Categorisation(
                                    categories = [
                                        '0'
                                        ], 
                                    source = '0', ), 
                                transaction_hash = yapily.models.transaction_hash.TransactionHash(
                                    hash = '0', ), 
                                cleansed_description = '0', 
                                location = '0', 
                                payment_processor = '0', 
                                corrected_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            supplementary_data = yapily.models.supplementary_data.supplementaryData(), )
                        ], 
                    next_cursor_hash = '0', 
                    next_link = '0', 
                    paging_map = {
                        'key' : yapily.models.filter_and_sort.FilterAndSort(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            sort = 'date', 
                            offset = 56, 
                            cursor = '0', )
                        }, 
                    total_count = 56, ), 
                tracing_id = '0'
            )
        else :
            return ApiListResponseOfTransaction(
        )

    def testApiListResponseOfTransaction(self):
        """Test ApiListResponseOfTransaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
