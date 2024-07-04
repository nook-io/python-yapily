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

from yapily.models.hosted_vrp_payment_response import HostedVRPPaymentResponse  # noqa: E501

class TestHostedVRPPaymentResponse(unittest.TestCase):
    """HostedVRPPaymentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HostedVRPPaymentResponse:
        """Test HostedVRPPaymentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HostedVRPPaymentResponse`
        """
        model = HostedVRPPaymentResponse()  # noqa: E501
        if include_optional:
            return HostedVRPPaymentResponse(
                id = '',
                payment_idempotency_id = '',
                amount = yapily.models.amount_details.Amount Details(
                    amount = 10, 
                    currency = 'GBP', ),
                reference = 'Own Account Sweeping',
                payee = yapily.models.payee_details.Payee Details(
                    name = 'Jane Doe', 
                    account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                    account_type = '', 
                    address = {"country":"GB"}, 
                    merchant_id = '24589303', 
                    merchant_category_code = '5551', ),
                payer = yapily.models.payer_details.Payer Details(
                    name = 'John Doe', 
                    account_identifications = [
                        yapily.models.account_identifications.Account Identifications(
                            type = 'SORT_CODE', 
                            identification = '401016', )
                        ], 
                    address = {"country":"GB"}, ),
                refund_account = yapily.models.hosted_vrp_refund_account.HostedVrpRefundAccount(
                    name = '', 
                    account_identifications = [
                        yapily.models.account_identifications.Account Identifications(
                            type = 'SORT_CODE', 
                            identification = '401016', )
                        ], ),
                risk = yapily.models.payment_risk.PaymentRisk(
                    context_type = '', ),
                payment_lifecycle_id = '',
                expected_execution_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expected_settlement_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                institution_payment_id = '',
                status_details = yapily.models.hosted_payment_status_details.HostedPaymentStatusDetails(
                    status = 'PENDING', 
                    status_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    iso_status = yapily.models.hosted_payment_iso_status.HostedPaymentIsoStatus(
                        code = 'ACSC', 
                        name = 'AcceptedCreditSettlementCompleted', ), )
            )
        else:
            return HostedVRPPaymentResponse(
        )
        """

    def testHostedVRPPaymentResponse(self):
        """Test HostedVRPPaymentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
