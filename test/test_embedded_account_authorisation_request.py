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

from yapily.models.embedded_account_authorisation_request import (
    EmbeddedAccountAuthorisationRequest,
)  # noqa: E501


class TestEmbeddedAccountAuthorisationRequest(unittest.TestCase):
    """EmbeddedAccountAuthorisationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmbeddedAccountAuthorisationRequest:
        """Test EmbeddedAccountAuthorisationRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EmbeddedAccountAuthorisationRequest`
        """
        model = EmbeddedAccountAuthorisationRequest()  # noqa: E501
        if include_optional:
            return EmbeddedAccountAuthorisationRequest(
                user_uuid = '',
                application_user_id = 'user-234562290',
                forward_parameters = [
                    ''
                    ],
                institution_id = 'yapily-mock',
                callback = 'https://display-parameters.com',
                redirect = yapily.models.redirect_request.RedirectRequest(
                    url = '', ),
                one_time_token = False,
                user_credentials = yapily.models.user_credentials.UserCredentials(
                    id = '6154057725', 
                    corporate_id = '6345898763', 
                    password = 'PISPWD12', ),
                selected_sca_method = {"id":"944","type":"PUSH_OTP","description":"SecureSIGN"},
                sca_code = '325614',
                account_request = yapily.models.account_request.AccountRequest(
                    transaction_from = '2020-01-01T00:00Z', 
                    transaction_to = '2021-01-01T00:00Z', 
                    expires_at = '2025-01-01T00:00Z', 
                    account_identifiers = yapily.models.account_info.AccountInfo(
                        account_id = '500000000000000000000001', 
                        account_identification = yapily.models.account_identifications.Account Identifications(
                            type = 'SORT_CODE', 
                            identification = '401016', ), ), 
                    account_identifiers_for_transaction = [
                        yapily.models.account_info.AccountInfo(
                            account_id = '500000000000000000000001', 
                            account_identification = yapily.models.account_identifications.Account Identifications(
                                type = 'SORT_CODE', 
                                identification = '401016', ), )
                        ], 
                    account_identifiers_for_balance = [
                        
                        ], 
                    feature_scope = [
                        'INITIATE_PRE_AUTHORISATION'
                        ], )
            )
        else:
            return EmbeddedAccountAuthorisationRequest(
                institution_id = 'yapily-mock',
        )
        """

    def testEmbeddedAccountAuthorisationRequest(self):
        """Test EmbeddedAccountAuthorisationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
