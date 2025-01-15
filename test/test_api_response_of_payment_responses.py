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

from yapily.models.api_response_of_payment_responses import (
    ApiResponseOfPaymentResponses,
)  # noqa: E501


class TestApiResponseOfPaymentResponses(unittest.TestCase):
    """ApiResponseOfPaymentResponses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResponseOfPaymentResponses:
        """Test ApiResponseOfPaymentResponses
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ApiResponseOfPaymentResponses`
        """
        model = ApiResponseOfPaymentResponses()  # noqa: E501
        if include_optional:
            return ApiResponseOfPaymentResponses(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '', ),
                data = yapily.models.payment_responses.PaymentResponses(
                    payments = [
                        yapily.models.payment_response.PaymentResponse(
                            id = '', 
                            institution_consent_id = '', 
                            payment_idempotency_id = '', 
                            payment_lifecycle_id = '', 
                            status = 'PENDING', 
                            status_details = yapily.models.payment_status_details.PaymentStatusDetails(
                                status_reason = '', 
                                status_reason_description = '', 
                                status_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                multi_authorisation_status = yapily.models.multi_authorisation.MultiAuthorisation(
                                    number_of_authorisation_required = 56, 
                                    number_of_authorisation_received = 56, 
                                    last_updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    expiration_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                iso_status = yapily.models.payment_iso_status.PaymentIsoStatus(
                                    code = 'ACCC', 
                                    name = 'AcceptedCreditSettlementCompleted', ), ), 
                            payer = yapily.models.payer_details.Payer Details(
                                name = 'John Doe', 
                                account_identifications = [
                                    yapily.models.account_identifications.Account Identifications(
                                        type = 'SORT_CODE', 
                                        identification = '401016', )
                                    ], 
                                address = {"country":"GB"}, ), 
                            payee_details = yapily.models.payee_details.Payee Details(
                                name = 'Jane Doe', 
                                account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                                account_type = '', 
                                merchant_id = '24589303', 
                                merchant_category_code = '5551', ), 
                            reference = '', 
                            amount = 1.337, 
                            currency = '', 
                            amount_details = yapily.models.amount_details.Amount Details(
                                amount = 10, 
                                currency = 'GBP', ), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            first_payment_amount = yapily.models.amount_details.Amount Details(
                                amount = 10, 
                                currency = 'GBP', ), 
                            first_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            next_payment_amount = , 
                            next_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            final_payment_amount = , 
                            final_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            number_of_payments = 56, 
                            previous_payment_amount = , 
                            previous_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            charge_details = [
                                yapily.models.payment_charge_details.PaymentChargeDetails(
                                    charge_amount = , 
                                    charge_type = '', 
                                    charge_to = '', )
                                ], 
                            scheduled_payment_type = '', 
                            scheduled_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            frequency = yapily.models.frequency_response.FrequencyResponse(
                                frequency_type = 'DAILY', 
                                interval_week = 56, 
                                interval_month = 56, 
                                execution_day = 56, ), 
                            currency_of_transfer = '', 
                            purpose = '', 
                            priority = 'NORMAL', 
                            exchange_rate = yapily.models.exchange_rate_information_response.ExchangeRateInformationResponse(
                                unit_currency = '', 
                                rate = 1.337, 
                                rate_type = 'ACTUAL', 
                                foreign_exchange_contract_reference = '', 
                                exchange_rate_expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            refund_account = yapily.models.refund_account.RefundAccount(
                                name = '', ), 
                            bulk_amount_sum = 1.337, )
                        ], ),
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
                tracing_id = ''
            )
        else:
            return ApiResponseOfPaymentResponses(
        )
        """

    def testApiResponseOfPaymentResponses(self):
        """Test ApiResponseOfPaymentResponses"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
