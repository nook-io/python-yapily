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

import openapi_client
from openapi_client.models.terminated_transaction_stream import TerminatedTransactionStream  # noqa: E501
from openapi_client.rest import ApiException

class TestTerminatedTransactionStream(unittest.TestCase):
    """TerminatedTransactionStream unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TerminatedTransactionStream
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.terminated_transaction_stream.TerminatedTransactionStream()  # noqa: E501
        if include_optional :
            return TerminatedTransactionStream(
                name = 'Amazon Marketplace', 
                transactions = [
                    openapi_client.models.enriched_transaction.EnrichedTransaction(
                        transaction_id = 'c51e3bee-36fb-4c0a-8441-d6ba2056fe87', 
                        transaction_information = 'Amazon Marketplace', 
                        amount = 21.99, 
                        institution = 'starling', 
                        booking_date_time = '2020-04-24T00:30:19.951Z', )
                    ], 
                transaction_schedule = openapi_client.models.transaction_schedule.TransactionSchedule(
                    frequency = 'Daily', 
                    detailed_frequency = 'Daily', 
                    detailed_frequency_parameter = 1, ), 
                schedule_consistency_score = 0.44, 
                next_expected_transaction_date = 'Fri Oct 04 01:00:00 BST 2019', 
                earliest_transaction_date = 'Fri Apr 24 01:00:00 BST 2020', 
                most_recent_transaction_date = 'Thu Oct 03 01:00:00 BST 2019', 
                amount_consistency_score = 0.74, 
                average_amount = 19.708, 
                missed_transactions = 3
            )
        else :
            return TerminatedTransactionStream(
        )

    def testTerminatedTransactionStream(self):
        """Test TerminatedTransactionStream"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
