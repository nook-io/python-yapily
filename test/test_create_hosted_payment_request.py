# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.25.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from yapily.models.create_hosted_payment_request import CreateHostedPaymentRequest  # noqa: E501

class TestCreateHostedPaymentRequest(unittest.TestCase):
    """CreateHostedPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateHostedPaymentRequest:
        """Test CreateHostedPaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateHostedPaymentRequest`
        """
        model = CreateHostedPaymentRequest()  # noqa: E501
        if include_optional:
            return CreateHostedPaymentRequest(
                user_id = '',
                application_user_id = '',
                institution_identifiers = yapily.models.institution_identifiers.InstitutionIdentifiers(
                    institution_id = '', 
                    institution_country_code = 'GB', ),
                user_settings = yapily.models.user_settings.UserSettings(
                    language = 'en', 
                    location = 'GB', ),
                redirect_url = 'https://tpp-application.com',
                payment_request_details = yapily.models.hosted_payment_request_details.HostedPaymentRequestDetails(
                    payment_idempotency_id = '04ab4536gaerfc0e1f93c4f4', 
                    reference = 'Bill payment', 
                    context_type = 'OTHER', 
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
                            ], ), 
                    amount_details = yapily.models.hosted_amount_details.HostedAmountDetails(
                        amount_to_pay = 10.5, 
                        currency = 'GBP', ), 
                    payment_due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
            )
        else:
            return CreateHostedPaymentRequest(
                institution_identifiers = yapily.models.institution_identifiers.InstitutionIdentifiers(
                    institution_id = '', 
                    institution_country_code = 'GB', ),
                redirect_url = 'https://tpp-application.com',
                payment_request_details = yapily.models.hosted_payment_request_details.HostedPaymentRequestDetails(
                    payment_idempotency_id = '04ab4536gaerfc0e1f93c4f4', 
                    reference = 'Bill payment', 
                    context_type = 'OTHER', 
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
                            ], ), 
                    amount_details = yapily.models.hosted_amount_details.HostedAmountDetails(
                        amount_to_pay = 10.5, 
                        currency = 'GBP', ), 
                    payment_due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ),
        )
        """

    def testCreateHostedPaymentRequest(self):
        """Test CreateHostedPaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
