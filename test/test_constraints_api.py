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

from yapily.api.constraints_api import ConstraintsApi  # noqa: E501


class TestConstraintsApi(unittest.TestCase):
    """ConstraintsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConstraintsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_account_constraints_rules_by_institution(self) -> None:
        """Test case for get_account_constraints_rules_by_institution

        Get Data Constraints Rules  # noqa: E501
        """
        pass

    def test_get_payment_constraints_rules_by_institution(self) -> None:
        """Test case for get_payment_constraints_rules_by_institution

        Get Payment Constraints Rules  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
