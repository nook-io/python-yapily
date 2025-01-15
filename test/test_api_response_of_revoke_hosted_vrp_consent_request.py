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

from yapily.models.api_response_of_revoke_hosted_vrp_consent_request import (
    ApiResponseOfRevokeHostedVRPConsentRequest,
)  # noqa: E501


class TestApiResponseOfRevokeHostedVRPConsentRequest(unittest.TestCase):
    """ApiResponseOfRevokeHostedVRPConsentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> ApiResponseOfRevokeHostedVRPConsentRequest:
        """Test ApiResponseOfRevokeHostedVRPConsentRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ApiResponseOfRevokeHostedVRPConsentRequest`
        """
        model = ApiResponseOfRevokeHostedVRPConsentRequest()  # noqa: E501
        if include_optional:
            return ApiResponseOfRevokeHostedVRPConsentRequest(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '', ),
                data = yapily.models.hosted_vrp_consent_details.HostedVRPConsentDetails(
                    id = '', 
                    user_id = '', 
                    application_user_id = '', 
                    application_id = '', 
                    institution_identifiers = yapily.models.institution_identifiers.InstitutionIdentifiers(
                        institution_id = '', 
                        institution_country_code = 'GB', ), 
                    user_settings = yapily.models.user_settings.UserSettings(
                        language = 'en', 
                        location = 'GB', ), 
                    redirect_url = 'https://tpp-application.com', 
                    vrp_setup = yapily.models.vrp_setup.VRPSetup(
                        payer = yapily.models.payer_details.Payer Details(
                            name = 'John Doe', 
                            account_identifications = [
                                yapily.models.account_identifications.Account Identifications(
                                    type = 'SORT_CODE', 
                                    identification = '401016', )
                                ], 
                            address = {"country":"GB"}, ), 
                        payee = yapily.models.payee_details.Payee Details(
                            name = 'Jane Doe', 
                            account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                            account_type = '', 
                            merchant_id = '24589303', 
                            merchant_category_code = '5551', ), 
                        reference = 'Own Account Sweeping', 
                        limits = yapily.models.hosted_vrp_limits.HostedVRPLimits(
                            periodic_limits = [
                                yapily.models.hosted_non_sweeping_periodic_limits.HostedNonSweepingPeriodicLimits(
                                    max_amount = null, 
                                    frequency = '', 
                                    alignment = '', )
                                ], 
                            max_amount_per_payment = null, 
                            max_cumulative_amount = null, 
                            max_cumulative_number_of_payments = 56, 
                            edited_by_user = True, ), 
                        valid_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        valid_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        recurring_payment_category = '', 
                        initial_payment = null, 
                        risk = yapily.models.payment_risk.PaymentRisk(
                            context_type = '', ), ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    authorisation_expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    consent_token = '', 
                    consent_status = '', 
                    phases = [
                        yapily.models.hosted_vrp_phase.HostedVRPPhase(
                            phase_name = '', 
                            phase_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], )
            )
        else:
            return ApiResponseOfRevokeHostedVRPConsentRequest(
        )
        """

    def testApiResponseOfRevokeHostedVRPConsentRequest(self):
        """Test ApiResponseOfRevokeHostedVRPConsentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
