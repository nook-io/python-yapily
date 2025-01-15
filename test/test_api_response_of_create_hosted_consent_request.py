# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 7.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from yapily.models.api_response_of_create_hosted_consent_request import ApiResponseOfCreateHostedConsentRequest

class TestApiResponseOfCreateHostedConsentRequest(unittest.TestCase):
    """ApiResponseOfCreateHostedConsentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResponseOfCreateHostedConsentRequest:
        """Test ApiResponseOfCreateHostedConsentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResponseOfCreateHostedConsentRequest`
        """
        model = ApiResponseOfCreateHostedConsentRequest()
        if include_optional:
            return ApiResponseOfCreateHostedConsentRequest(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '', ),
                data = yapily.models.hosted_consent_request_response.HostedConsentRequestResponse(
                    consent_request_id = '', 
                    user_id = '', 
                    application_user_id = '', 
                    application_id = '', 
                    institution_identifiers = yapily.models.institution_identifiers_response.InstitutionIdentifiersResponse(
                        institution_id = '', 
                        institution_country_code = 'GB', ), 
                    user_settings = yapily.models.user_settings.UserSettings(
                        language = 'en', 
                        location = 'GB', ), 
                    redirect_url = 'https://tpp-application.com', 
                    account_request_details = yapily.models.hosted_account_request_details_response.HostedAccountRequestDetailsResponse(
                        transaction_from = '2020-01-01T00:00Z', 
                        transaction_to = '2021-01-01T00:00Z', 
                        expires_at = '2025-01-01T00:00Z', 
                        feature_scope = [
                            'INITIATE_PRE_AUTHORISATION'
                            ], ), 
                    hosted_url = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    authorisation_expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return ApiResponseOfCreateHostedConsentRequest(
        )
        """

    def testApiResponseOfCreateHostedConsentRequest(self):
        """Test ApiResponseOfCreateHostedConsentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
