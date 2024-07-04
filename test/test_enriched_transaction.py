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

from yapily.models.enriched_transaction import EnrichedTransaction  # noqa: E501

class TestEnrichedTransaction(unittest.TestCase):
    """EnrichedTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnrichedTransaction:
        """Test EnrichedTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnrichedTransaction`
        """
        model = EnrichedTransaction()  # noqa: E501
        if include_optional:
            return EnrichedTransaction(
                transaction_id = 'c51e3bee-36fb-4c0a-8441-d6ba2056fe87',
                transaction_information = 'Amazon Marketplace',
                amount = 21.99,
                institution = 'starling',
                booking_date_time = '2020-04-24T00:30:19.951Z'
            )
        else:
            return EnrichedTransaction(
        )
        """

    def testEnrichedTransaction(self):
        """Test EnrichedTransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
