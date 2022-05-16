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
from openapi_client.models.api_response_of_payment_embedded_authorisation_request_response import ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestApiResponseOfPaymentEmbeddedAuthorisationRequestResponse(unittest.TestCase):
    """ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.api_response_of_payment_embedded_authorisation_request_response.ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse()  # noqa: E501
        if include_optional :
            return ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse(
                meta = openapi_client.models.response_meta.ResponseMeta(
                    tracing_id = '0', ), 
                data = openapi_client.models.payment_embedded_authorisation_request_response.PaymentEmbeddedAuthorisationRequestResponse(
                    id = '0', 
                    user_uuid = '0', 
                    application_user_id = '0', 
                    reference_id = '0', 
                    institution_id = '0', 
                    status = 'AWAITING_AUTHORIZATION', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    transaction_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    transaction_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_to_expire_in_millis = 56, 
                    time_to_expire = '0', 
                    feature_scope = [
                        'INITIATE_PRE_AUTHORISATION'
                        ], 
                    consent_token = '0', 
                    state = '0', 
                    authorized_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    institution_consent_id = '0', 
                    charges = [
                        openapi_client.models.payment_charge_details.PaymentChargeDetails(
                            charge_amount = openapi_client.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), 
                            charge_type = '0', 
                            charge_to = '0', )
                        ], 
                    exchange_rate_information = openapi_client.models.exchange_rate_information_response.ExchangeRateInformationResponse(
                        unit_currency = '0', 
                        rate = 1.337, 
                        rate_type = 'ACTUAL', 
                        foreign_exchange_contract_reference = '0', 
                        exchange_rate_expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    authorisation_url = '0', 
                    qr_code_url = '0', 
                    explanation = '0', 
                    sca_methods = [
                        {"id":"944","type":"PUSH_OTP","description":"SecureSIGN"}
                        ], 
                    selected_sca_method = {"id":"944","type":"PUSH_OTP","description":"SecureSIGN"}, ), 
                links = {
                    'key' : '0'
                    }, 
                forwarded_data = [
                    openapi_client.models.response_forwarded_data.ResponseForwardedData(
                        headers = {
                            'key' : '0'
                            }, 
                        url = '0', )
                    ], 
                raw = [
                    openapi_client.models.raw_response.RawResponse(
                        request = openapi_client.models.raw_request.RawRequest(
                            method = '0', 
                            url = '0', 
                            request_instant = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            headers = {
                                'key' : '0'
                                }, 
                            body = openapi_client.models.body.body(), 
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
                        result = openapi_client.models.result.result(), )
                    ], 
                tracing_id = '0'
            )
        else :
            return ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse(
        )

    def testApiResponseOfPaymentEmbeddedAuthorisationRequestResponse(self):
        """Test ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
