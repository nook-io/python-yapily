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

from yapily.models.bulk_payment_request import BulkPaymentRequest

class TestBulkPaymentRequest(unittest.TestCase):
    """BulkPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkPaymentRequest:
        """Test BulkPaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkPaymentRequest`
        """
        model = BulkPaymentRequest()
        if include_optional:
            return BulkPaymentRequest(
                payments = [
                    yapily.models.payment_request.PaymentRequest(
                        payment_idempotency_id = '04ab4536gaerfc0e1f93c4f4', 
                        payer = yapily.models.payer.Payer(
                            name = 'John Doe', 
                            account_identifications = [
                                yapily.models.account_identification.AccountIdentification(
                                    type = 'SORT_CODE', 
                                    identification = '401016', )
                                ], 
                            address = {"country":"GB"}, ), 
                        reference = 'Bill payment', 
                        context_type = 'OTHER', 
                        type = 'DOMESTIC_PAYMENT', 
                        payee = yapily.models.payee.Payee(
                            name = 'Jane Doe', 
                            account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                            merchant_id = '24589303', 
                            merchant_category_code = '5551', ), 
                        periodic_payment = yapily.models.periodic_payment_request.PeriodicPaymentRequest(
                            frequency = yapily.models.frequency_request.FrequencyRequest(
                                type = 'DAILY', 
                                interval_week = 1, 
                                interval_month = 1, 
                                execution_day = 1, ), 
                            number_of_payments = 5, 
                            next_payment_date_time = '2018-01-10T00:00Z', 
                            next_payment_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), 
                            final_payment_date_time = '2030-01-10T00:00Z', 
                            final_payment_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), ), 
                        international_payment = yapily.models.international_payment_request.InternationalPaymentRequest(
                            currency_of_transfer = '', 
                            exchange_rate_information = yapily.models.exchange_rate_information.ExchangeRateInformation(
                                unit_currency = '', 
                                rate = 1.337, 
                                rate_type = 'ACTUAL', 
                                foreign_exchange_contract_reference = '', ), 
                            purpose = '', 
                            priority = 'NORMAL', 
                            charge_bearer = 'DEBT', ), 
                        amount = , 
                        payment_date_time = '2021-07-21T17:32:28Z', 
                        read_refund_account = False, )
                    ],
                originator_identification_number = '',
                execution_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BulkPaymentRequest(
                payments = [
                    yapily.models.payment_request.PaymentRequest(
                        payment_idempotency_id = '04ab4536gaerfc0e1f93c4f4', 
                        payer = yapily.models.payer.Payer(
                            name = 'John Doe', 
                            account_identifications = [
                                yapily.models.account_identification.AccountIdentification(
                                    type = 'SORT_CODE', 
                                    identification = '401016', )
                                ], 
                            address = {"country":"GB"}, ), 
                        reference = 'Bill payment', 
                        context_type = 'OTHER', 
                        type = 'DOMESTIC_PAYMENT', 
                        payee = yapily.models.payee.Payee(
                            name = 'Jane Doe', 
                            account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                            merchant_id = '24589303', 
                            merchant_category_code = '5551', ), 
                        periodic_payment = yapily.models.periodic_payment_request.PeriodicPaymentRequest(
                            frequency = yapily.models.frequency_request.FrequencyRequest(
                                type = 'DAILY', 
                                interval_week = 1, 
                                interval_month = 1, 
                                execution_day = 1, ), 
                            number_of_payments = 5, 
                            next_payment_date_time = '2018-01-10T00:00Z', 
                            next_payment_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), 
                            final_payment_date_time = '2030-01-10T00:00Z', 
                            final_payment_amount = yapily.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), ), 
                        international_payment = yapily.models.international_payment_request.InternationalPaymentRequest(
                            currency_of_transfer = '', 
                            exchange_rate_information = yapily.models.exchange_rate_information.ExchangeRateInformation(
                                unit_currency = '', 
                                rate = 1.337, 
                                rate_type = 'ACTUAL', 
                                foreign_exchange_contract_reference = '', ), 
                            purpose = '', 
                            priority = 'NORMAL', 
                            charge_bearer = 'DEBT', ), 
                        amount = , 
                        payment_date_time = '2021-07-21T17:32:28Z', 
                        read_refund_account = False, )
                    ],
        )
        """

    def testBulkPaymentRequest(self):
        """Test BulkPaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
