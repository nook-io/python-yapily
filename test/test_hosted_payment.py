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

from yapily.models.hosted_payment import HostedPayment  # noqa: E501

class TestHostedPayment(unittest.TestCase):
    """HostedPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HostedPayment:
        """Test HostedPayment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HostedPayment`
        """
        model = HostedPayment()  # noqa: E501
        if include_optional:
            return HostedPayment(
                payment_id = '',
                hosted_payment_id = '',
                consent_id = '',
                institution_identifiers = yapily.models.institution_identifiers_response.InstitutionIdentifiersResponse(
                    institution_id = '', 
                    institution_country_code = 'GB', ),
                phases = [
                    yapily.models.hosted_payment_phase.HostedPaymentPhase(
                        phase_name = '', 
                        phase_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                payment_status = '',
                status_details = [
                    yapily.models.hosted_payment_status_details.HostedPaymentStatusDetails(
                        status = 'PENDING', 
                        status_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        iso_status = yapily.models.hosted_payment_iso_status.HostedPaymentIsoStatus(
                            code = 'ACSC', 
                            name = 'AcceptedCreditSettlementCompleted', ), )
                    ],
                institution_payment_id = '',
                payment_lifecycle_id = '',
                payment_idempotency_id = '04ab4536gaerfc0e1f93c4f4',
                reference = 'Bill payment',
                context_type = 'BILL',
                type = 'DOMESTIC_PAYMENT',
                payee = yapily.models.payee_details.Payee Details(
                    name = 'Jane Doe', 
                    account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
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
                amount = yapily.models.amount_details.Amount Details(
                    currency = 'GBP', )
            )
        else:
            return HostedPayment(
        )
        """

    def testHostedPayment(self):
        """Test HostedPayment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
