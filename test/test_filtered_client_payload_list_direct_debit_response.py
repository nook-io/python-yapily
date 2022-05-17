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
from yapily.models.filtered_client_payload_list_direct_debit_response import FilteredClientPayloadListDirectDebitResponse  # noqa: E501
from yapily.rest import ApiException

class TestFilteredClientPayloadListDirectDebitResponse(unittest.TestCase):
    """FilteredClientPayloadListDirectDebitResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FilteredClientPayloadListDirectDebitResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.filtered_client_payload_list_direct_debit_response.FilteredClientPayloadListDirectDebitResponse()  # noqa: E501
        if include_optional :
            return FilteredClientPayloadListDirectDebitResponse(
                api_call = yapily.models.api_call.ApiCall(), 
                data = [
                    yapily.models.direct_debit_response.DirectDebitResponse(
                        id = '0', 
                        status_details = yapily.models.payment_status_details.PaymentStatusDetails(
                            status = 'PENDING', 
                            status_reason = '0', 
                            status_reason_description = '0', 
                            status_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            multi_authorisation_status = yapily.models.multi_authorisation.MultiAuthorisation(
                                number_of_authorisation_required = 56, 
                                number_of_authorisation_received = 56, 
                                last_updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiration_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            iso_status = yapily.models.payment_iso_status.PaymentIsoStatus(
                                code = 'ACCC', 
                                name = 'AcceptedCreditSettlementCompleted', ), ), 
                        payee_details = yapily.models.direct_debit_payee.DirectDebitPayee(
                            name = 'Tempus Risus Company', ), 
                        reference = '0', 
                        previous_payment_amount = yapily.models.amount.Amount(
                            amount = 10, 
                            currency = 'GBP', ), 
                        previous_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
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
                total_count = 56
            )
        else :
            return FilteredClientPayloadListDirectDebitResponse(
        )

    def testFilteredClientPayloadListDirectDebitResponse(self):
        """Test FilteredClientPayloadListDirectDebitResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
