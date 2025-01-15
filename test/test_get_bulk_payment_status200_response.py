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

from yapily.models.get_bulk_payment_status200_response import GetBulkPaymentStatus200Response

class TestGetBulkPaymentStatus200Response(unittest.TestCase):
    """GetBulkPaymentStatus200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetBulkPaymentStatus200Response:
        """Test GetBulkPaymentStatus200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBulkPaymentStatus200Response`
        """
        model = GetBulkPaymentStatus200Response()
        if include_optional:
            return GetBulkPaymentStatus200Response(
                meta = yapily.models.get_bulk_payment_status_200_response_meta.getBulkPaymentStatus_200_response_meta(
                    tracing_id = '', ),
                data = yapily.models.get_bulk_payment_status_200_response_data.getBulkPaymentStatus_200_response_data(
                    id = '', 
                    consent_id = '', 
                    status_details = yapily.models.get_bulk_payment_status_200_response_data_status_details.getBulkPaymentStatus_200_response_data_statusDetails(
                        status = '', 
                        updated_at = '', ), 
                    created_at = '', )
            )
        else:
            return GetBulkPaymentStatus200Response(
        )
        """

    def testGetBulkPaymentStatus200Response(self):
        """Test GetBulkPaymentStatus200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
