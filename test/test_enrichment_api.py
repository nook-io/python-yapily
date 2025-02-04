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

from yapily.api.enrichment_api import EnrichmentApi  # noqa: E501


class TestEnrichmentApi(unittest.TestCase):
    """EnrichmentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EnrichmentApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_accounts_transactions_categorised(self) -> None:
        """Test case for get_accounts_transactions_categorised

        Get Categorised Transactions  # noqa: E501
        """
        pass

    def test_get_categorisation_account_type(self) -> None:
        """Test case for get_categorisation_account_type

        Get the list of all categories for a specific account type  # noqa: E501
        """
        pass

    def test_post_accounts_account_id_transactions_categorisation(self) -> None:
        """Test case for post_accounts_account_id_transactions_categorisation

        Trigger transaction categorisation  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
