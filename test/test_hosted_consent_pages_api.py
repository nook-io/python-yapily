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

from yapily.api.hosted_consent_pages_api import HostedConsentPagesApi


class TestHostedConsentPagesApi(unittest.IsolatedAsyncioTestCase):
    """HostedConsentPagesApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = HostedConsentPagesApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_create_hosted_consent_request(self) -> None:
        """Test case for create_hosted_consent_request

        Create Hosted Consent Request
        """
        pass

    async def test_get_hosted_consent_request(self) -> None:
        """Test case for get_hosted_consent_request

        Get Hosted Consent Request
        """
        pass


if __name__ == "__main__":
    unittest.main()
