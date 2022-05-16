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
from openapi_client.models.payment_responses import PaymentResponses  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentResponses(unittest.TestCase):
    """PaymentResponses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentResponses
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.payment_responses.PaymentResponses()  # noqa: E501
        if include_optional :
            return PaymentResponses(
                payments = [
                    openapi_client.models.payment_response.PaymentResponse(
                        id = '0', 
                        institution_consent_id = '0', 
                        payment_idempotency_id = '0', 
                        payment_lifecycle_id = '0', 
                        status = 'PENDING', 
                        status_details = openapi_client.models.payment_status_details.PaymentStatusDetails(
                            status_reason = '0', 
                            status_reason_description = '0', 
                            status_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            multi_authorisation_status = openapi_client.models.multi_authorisation.MultiAuthorisation(
                                number_of_authorisation_required = 56, 
                                number_of_authorisation_received = 56, 
                                last_updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiration_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            iso_status = openapi_client.models.payment_iso_status.PaymentIsoStatus(
                                code = 'ACCC', 
                                name = 'AcceptedCreditSettlementCompleted', ), ), 
                        payer = openapi_client.models.payer.Payer(
                            name = 'John Doe', 
                            account_identifications = [
                                openapi_client.models.account_identification.AccountIdentification(
                                    type = 'SORT_CODE', 
                                    identification = '401016', )
                                ], 
                            address = {"country":"GB"}, ), 
                        payee_details = openapi_client.models.payee.Payee(
                            name = 'Jane Doe', 
                            account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                            merchant_id = '24589303', 
                            merchant_category_code = '5551', ), 
                        reference = '0', 
                        amount = 1.337, 
                        currency = '0', 
                        amount_details = openapi_client.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        first_payment_amount = openapi_client.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        first_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        next_payment_amount = openapi_client.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        next_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        final_payment_amount = openapi_client.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        final_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        number_of_payments = 56, 
                        previous_payment_amount = openapi_client.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        previous_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        charge_details = [
                            openapi_client.models.payment_charge_details.PaymentChargeDetails(
                                charge_amount = openapi_client.models.amount.Amount(
                                    amount = 10, 
                                    currency = 'GBP', ), 
                                charge_type = '0', 
                                charge_to = '0', )
                            ], 
                        scheduled_payment_type = '0', 
                        scheduled_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        frequency = openapi_client.models.frequency_response.FrequencyResponse(
                            frequency_type = 'DAILY', 
                            interval_week = 56, 
                            interval_month = 56, 
                            execution_day = 56, ), 
                        currency_of_transfer = '0', 
                        purpose = '0', 
                        priority = 'NORMAL', 
                        exchange_rate = openapi_client.models.exchange_rate_information_response.ExchangeRateInformationResponse(
                            unit_currency = '0', 
                            rate = 1.337, 
                            rate_type = 'ACTUAL', 
                            foreign_exchange_contract_reference = '0', 
                            exchange_rate_expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        refund_account = openapi_client.models.refund_account.RefundAccount(
                            name = '0', ), 
                        bulk_amount_sum = 1.337, )
                    ]
            )
        else :
            return PaymentResponses(
        )

    def testPaymentResponses(self):
        """Test PaymentResponses"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
