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

from yapily.models.api_response_of_financial_profile import (
    ApiResponseOfFinancialProfile,
)  # noqa: E501


class TestApiResponseOfFinancialProfile(unittest.TestCase):
    """ApiResponseOfFinancialProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResponseOfFinancialProfile:
        """Test ApiResponseOfFinancialProfile
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ApiResponseOfFinancialProfile`
        """
        model = ApiResponseOfFinancialProfile()  # noqa: E501
        if include_optional:
            return ApiResponseOfFinancialProfile(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '', ),
                data = yapily.models.financial_profile.FinancialProfile(
                    status = 'COMPLETED', 
                    profile_consents = [
                        yapily.models.profile_consent.ProfileConsent(
                            id = 'eb2ad083-a111-4143-8756-a3a3cef4031c', 
                            status = 'PENDING', 
                            user_id = '3ddf5dd0-aa48-4d0f-baa7-fa057e9e911d', 
                            reference_consent_id = '1e2e5167-8519-4c19-b016-8f2f0c6e38b6', 
                            institution_id = 'mock-sandbox', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            data_inserted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    enrichment = yapily.models.enriched_wrapper.EnrichedWrapper(
                        income_streams = [
                            yapily.models.transaction_stream.TransactionStream(
                                name = 'Amazon Marketplace', 
                                transactions = [
                                    yapily.models.enriched_transaction.EnrichedTransaction(
                                        transaction_id = 'c51e3bee-36fb-4c0a-8441-d6ba2056fe87', 
                                        transaction_information = 'Amazon Marketplace', 
                                        amount = 21.99, 
                                        institution = 'starling', 
                                        booking_date_time = '2020-04-24T00:30:19.951Z', )
                                    ], 
                                transaction_schedule = yapily.models.transaction_schedule.TransactionSchedule(
                                    frequency = 'Daily', 
                                    detailed_frequency = 'Daily', 
                                    detailed_frequency_parameter = 1, ), 
                                schedule_consistency_score = 0.44, 
                                next_expected_transaction_date = 'Fri Oct 04 01:00:00 BST 2019', 
                                earliest_transaction_date = 'Fri Apr 24 01:00:00 BST 2020', 
                                most_recent_transaction_date = 'Thu Oct 03 01:00:00 BST 2019', 
                                amount_consistency_score = 0.74, 
                                average_amount = 19.708, )
                            ], 
                        expenditure_streams = [
                            yapily.models.transaction_stream.TransactionStream(
                                name = 'Amazon Marketplace', 
                                schedule_consistency_score = 0.44, 
                                next_expected_transaction_date = 'Fri Oct 04 01:00:00 BST 2019', 
                                earliest_transaction_date = 'Fri Apr 24 01:00:00 BST 2020', 
                                most_recent_transaction_date = 'Thu Oct 03 01:00:00 BST 2019', 
                                amount_consistency_score = 0.74, 
                                average_amount = 19.708, )
                            ], 
                        recently_terminated_income_streams = [
                            yapily.models.terminated_transaction_stream.TerminatedTransactionStream(
                                name = 'Amazon Marketplace', 
                                schedule_consistency_score = 0.44, 
                                next_expected_transaction_date = 'Fri Oct 04 01:00:00 BST 2019', 
                                earliest_transaction_date = 'Fri Apr 24 01:00:00 BST 2020', 
                                most_recent_transaction_date = 'Thu Oct 03 01:00:00 BST 2019', 
                                amount_consistency_score = 0.74, 
                                average_amount = 19.708, 
                                missed_transactions = 3, )
                            ], 
                        recently_terminated_expenditure_streams = [
                            yapily.models.terminated_transaction_stream.TerminatedTransactionStream(
                                name = 'Amazon Marketplace', 
                                schedule_consistency_score = 0.44, 
                                next_expected_transaction_date = 'Fri Oct 04 01:00:00 BST 2019', 
                                earliest_transaction_date = 'Fri Apr 24 01:00:00 BST 2020', 
                                most_recent_transaction_date = 'Thu Oct 03 01:00:00 BST 2019', 
                                amount_consistency_score = 0.74, 
                                average_amount = 19.708, 
                                missed_transactions = 3, )
                            ], ), ),
                links = {
                    'key' : ''
                    }
            )
        else:
            return ApiResponseOfFinancialProfile(
        )
        """

    def testApiResponseOfFinancialProfile(self):
        """Test ApiResponseOfFinancialProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
