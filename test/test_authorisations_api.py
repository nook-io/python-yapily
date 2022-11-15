# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.authorisations_api import AuthorisationsApi  # noqa: E501
from yapily.rest import ApiException


class TestAuthorisationsApi(unittest.TestCase):
    """AuthorisationsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.authorisations_api.AuthorisationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bulk_payment_authorisation(self):
        """Test case for create_bulk_payment_authorisation

        Create Bulk Payment Authorisation  # noqa: E501
        """
        pass

    def test_create_embedded_bulk_payment_authorisation(self):
        """Test case for create_embedded_bulk_payment_authorisation

        Create Embedded Bulk Payment Authorisation  # noqa: E501
        """
        pass

    def test_create_embedded_payment_authorisation(self):
        """Test case for create_embedded_payment_authorisation

        Create Embedded Payment Authorisation  # noqa: E501
        """
        pass

    def test_create_payment_authorisation(self):
        """Test case for create_payment_authorisation

        Create Payment Authorisation  # noqa: E501
        """
        pass

    def test_create_payment_pre_authorisation_request(self):
        """Test case for create_payment_pre_authorisation_request

        Create Payment Pre-authorisation  # noqa: E501
        """
        pass

    def test_create_pre_authorisation_request(self):
        """Test case for create_pre_authorisation_request

        Create Pre-authorisation  # noqa: E501
        """
        pass

    def test_initiate_account_request(self):
        """Test case for initiate_account_request

        Create Account Authorisation  # noqa: E501
        """
        pass

    def test_initiate_embedded_account_request(self):
        """Test case for initiate_embedded_account_request

        Create Embedded Account Authorisation  # noqa: E501
        """
        pass

    def test_re_authorise_account(self):
        """Test case for re_authorise_account

        Re-authorise Account Consent  # noqa: E501
        """
        pass

    def test_update_embedded_account_request(self):
        """Test case for update_embedded_account_request

        Update Embedded Account Authorisation  # noqa: E501
        """
        pass

    def test_update_embedded_bulk_payment_authorisation(self):
        """Test case for update_embedded_bulk_payment_authorisation

        Update Embedded Bulk Payment Authorisation  # noqa: E501
        """
        pass

    def test_update_embedded_payment_authorisation(self):
        """Test case for update_embedded_payment_authorisation

        Update Embedded Payment Authorisation  # noqa: E501
        """
        pass

    def test_update_payment_authorisation(self):
        """Test case for update_payment_authorisation

        Update Payment Pre-authorisation  # noqa: E501
        """
        pass

    def test_update_pre_authorise_account_consent(self):
        """Test case for update_pre_authorise_account_consent

        Update Account Pre-authorisation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
