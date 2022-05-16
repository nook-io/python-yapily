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
from openapi_client.models.api_list_response_of_direct_debit_response import ApiListResponseOfDirectDebitResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestApiListResponseOfDirectDebitResponse(unittest.TestCase):
    """ApiListResponseOfDirectDebitResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiListResponseOfDirectDebitResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.api_list_response_of_direct_debit_response.ApiListResponseOfDirectDebitResponse()  # noqa: E501
        if include_optional :
            return ApiListResponseOfDirectDebitResponse(
                meta = openapi_client.models.response_list_meta.ResponseListMeta(
                    tracing_id = '0', 
                    count = 56, 
                    pagination = openapi_client.models.pagination.Pagination(
                        total_count = 56, 
                        self = openapi_client.models.filter_and_sort.FilterAndSort(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            sort = 'date', 
                            offset = 56, 
                            cursor = '0', ), 
                        next = openapi_client.models.next.Next(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            cursor = '0', ), ), ), 
                data = [
                    openapi_client.models.direct_debit_response.DirectDebitResponse(
                        id = '0', 
                        status_details = openapi_client.models.payment_status_details.PaymentStatusDetails(
                            status = 'PENDING', 
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
                        payee_details = openapi_client.models.direct_debit_payee.DirectDebitPayee(
                            name = 'Tempus Risus Company', ), 
                        reference = '0', 
                        previous_payment_amount = openapi_client.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        previous_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
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
                paging = openapi_client.models.filtered_client_payload_list_direct_debit_response.FilteredClientPayloadListDirectDebitResponse(
                    api_call = openapi_client.models.api_call.ApiCall(), 
                    data = [
                        openapi_client.models.direct_debit_response.DirectDebitResponse(
                            id = '0', 
                            status_details = openapi_client.models.payment_status_details.PaymentStatusDetails(
                                status = 'PENDING', 
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
                            payee_details = openapi_client.models.direct_debit_payee.DirectDebitPayee(
                                name = 'Tempus Risus Company', ), 
                            reference = '0', 
                            previous_payment_amount = openapi_client.models.amount.Amount(
                                amount = 10, 
                                currency = 'GBP', ), 
                            previous_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    next_cursor_hash = '0', 
                    next_link = '0', 
                    paging_map = {
                        'key' : openapi_client.models.filter_and_sort.FilterAndSort(
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
            return ApiListResponseOfDirectDebitResponse(
        )

    def testApiListResponseOfDirectDebitResponse(self):
        """Test ApiListResponseOfDirectDebitResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
