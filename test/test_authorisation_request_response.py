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
from yapily.models.authorisation_request_response import AuthorisationRequestResponse  # noqa: E501
from yapily.rest import ApiException

class TestAuthorisationRequestResponse(unittest.TestCase):
    """AuthorisationRequestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthorisationRequestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.authorisation_request_response.AuthorisationRequestResponse()  # noqa: E501
        if include_optional :
            return AuthorisationRequestResponse(
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
                authorisation_url = '0', 
                qr_code_url = '0'
            )
        else :
            return AuthorisationRequestResponse(
        )

    def testAuthorisationRequestResponse(self):
        """Test AuthorisationRequestResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
