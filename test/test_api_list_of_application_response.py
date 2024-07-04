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

from yapily.models.api_list_of_application_response import ApiListOfApplicationResponse  # noqa: E501

class TestApiListOfApplicationResponse(unittest.TestCase):
    """ApiListOfApplicationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiListOfApplicationResponse:
        """Test ApiListOfApplicationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiListOfApplicationResponse`
        """
        model = ApiListOfApplicationResponse()  # noqa: E501
        if include_optional:
            return ApiListOfApplicationResponse(
                meta = yapily.models.application_response_list_meta.ApplicationResponseListMeta(
                    tracing_id = '', 
                    count = 0, 
                    pagination = yapily.models.application_response_list_meta_pagination.ApplicationResponseListMeta_pagination(
                        self = yapily.models.application_response_list_meta_pagination_self.ApplicationResponseListMeta_pagination_self(
                            offset = 0, 
                            limit = 0, 
                            sort = '', ), 
                        total_count = 0, ), ),
                data = [
                    yapily.models.application_response.ApplicationResponse(
                        id = '2698db90-6635-4f76-b673-5ce8e2aeda0e', 
                        root_application_id = 'eb25e1ee-f6af-4131-92fe-748e177bf950', 
                        name = '', 
                        merchant_category_code = '0742', 
                        ppc_user_group = 'WHOLESALE_FI_FI', 
                        callback_urls = [
                            ''
                            ], 
                        is_contract_present = True, )
                    ]
            )
        else:
            return ApiListOfApplicationResponse(
        )
        """

    def testApiListOfApplicationResponse(self):
        """Test ApiListOfApplicationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
