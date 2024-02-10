# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from yapily.models.api_response_of_financial_profile_authorisation_response import ApiResponseOfFinancialProfileAuthorisationResponse

class TestApiResponseOfFinancialProfileAuthorisationResponse(unittest.TestCase):
    """ApiResponseOfFinancialProfileAuthorisationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResponseOfFinancialProfileAuthorisationResponse:
        """Test ApiResponseOfFinancialProfileAuthorisationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResponseOfFinancialProfileAuthorisationResponse`
        """
        model = ApiResponseOfFinancialProfileAuthorisationResponse()
        if include_optional:
            return ApiResponseOfFinancialProfileAuthorisationResponse(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '', ),
                data = [
                    yapily.models.profile_consent.ProfileConsent(
                        id = 'eb2ad083-a111-4143-8756-a3a3cef4031c', 
                        status = 'PENDING', 
                        user_id = '3ddf5dd0-aa48-4d0f-baa7-fa057e9e911d', 
                        reference_consent_id = '1e2e5167-8519-4c19-b016-8f2f0c6e38b6', 
                        institution_id = 'mock-sandbox', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        data_inserted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                links = {
                    'key' : ''
                    }
            )
        else:
            return ApiResponseOfFinancialProfileAuthorisationResponse(
        )
        """

    def testApiResponseOfFinancialProfileAuthorisationResponse(self):
        """Test ApiResponseOfFinancialProfileAuthorisationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
