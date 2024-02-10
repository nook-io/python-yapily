# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from yapily.models.filtered_client_payload_list_feature_details import FilteredClientPayloadListFeatureDetails

class TestFilteredClientPayloadListFeatureDetails(unittest.TestCase):
    """FilteredClientPayloadListFeatureDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FilteredClientPayloadListFeatureDetails:
        """Test FilteredClientPayloadListFeatureDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FilteredClientPayloadListFeatureDetails`
        """
        model = FilteredClientPayloadListFeatureDetails()
        if include_optional:
            return FilteredClientPayloadListFeatureDetails(
                api_call = yapily.models.api_call.ApiCall(),
                data = [
                    yapily.models.feature_details.FeatureDetails(
                        feature = 'INITIATE_PRE_AUTHORISATION', 
                        endpoint = '', 
                        documentation_url = '', )
                    ],
                next_cursor_hash = '',
                next_link = '',
                paging_map = {
                    'key' : yapily.models.filter_and_sort.FilterAndSort(
                        from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        limit = 56, 
                        sort = 'date', 
                        offset = 56, 
                        cursor = '', )
                    },
                total_count = 56
            )
        else:
            return FilteredClientPayloadListFeatureDetails(
        )
        """

    def testFilteredClientPayloadListFeatureDetails(self):
        """Test FilteredClientPayloadListFeatureDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
