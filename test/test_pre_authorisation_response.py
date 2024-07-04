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

from yapily.models.pre_authorisation_response import PreAuthorisationResponse  # noqa: E501

class TestPreAuthorisationResponse(unittest.TestCase):
    """PreAuthorisationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PreAuthorisationResponse:
        """Test PreAuthorisationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PreAuthorisationResponse`
        """
        model = PreAuthorisationResponse()  # noqa: E501
        if include_optional:
            return PreAuthorisationResponse(
                id = '',
                user_uuid = '',
                application_user_id = '',
                reference_id = '',
                institution_id = '',
                status = 'AWAITING_AUTHORIZATION',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                transaction_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                transaction_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_to_expire_in_millis = 56,
                time_to_expire = '',
                feature_scope = [
                    'INITIATE_PRE_AUTHORISATION'
                    ],
                consent_token = '',
                state = '',
                authorized_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                institution_consent_id = '',
                authorisation_url = '',
                qr_code_url = ''
            )
        else:
            return PreAuthorisationResponse(
        )
        """

    def testPreAuthorisationResponse(self):
        """Test PreAuthorisationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
