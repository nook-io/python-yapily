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

from yapily.models.post_accounts_account_id_transactions_categorisation201_response_meta import (
    PostAccountsAccountIdTransactionsCategorisation201ResponseMeta,
)  # noqa: E501


class TestPostAccountsAccountIdTransactionsCategorisation201ResponseMeta(
    unittest.TestCase
):
    """PostAccountsAccountIdTransactionsCategorisation201ResponseMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PostAccountsAccountIdTransactionsCategorisation201ResponseMeta:
        """Test PostAccountsAccountIdTransactionsCategorisation201ResponseMeta
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PostAccountsAccountIdTransactionsCategorisation201ResponseMeta`
        """
        model = PostAccountsAccountIdTransactionsCategorisation201ResponseMeta()  # noqa: E501
        if include_optional:
            return PostAccountsAccountIdTransactionsCategorisation201ResponseMeta(
                tracing_id = ''
            )
        else:
            return PostAccountsAccountIdTransactionsCategorisation201ResponseMeta(
        )
        """

    def testPostAccountsAccountIdTransactionsCategorisation201ResponseMeta(self):
        """Test PostAccountsAccountIdTransactionsCategorisation201ResponseMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
