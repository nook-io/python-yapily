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

from yapily.models.hosted_account_request_details_response import (
    HostedAccountRequestDetailsResponse,
)


class TestHostedAccountRequestDetailsResponse(unittest.TestCase):
    """HostedAccountRequestDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HostedAccountRequestDetailsResponse:
        """Test HostedAccountRequestDetailsResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `HostedAccountRequestDetailsResponse`
        """
        model = HostedAccountRequestDetailsResponse()
        if include_optional:
            return HostedAccountRequestDetailsResponse(
                transaction_from = '2020-01-01T00:00Z',
                transaction_to = '2021-01-01T00:00Z',
                expires_at = '2025-01-01T00:00Z',
                feature_scope = [
                    'INITIATE_PRE_AUTHORISATION'
                    ]
            )
        else:
            return HostedAccountRequestDetailsResponse(
        )
        """

    def testHostedAccountRequestDetailsResponse(self):
        """Test HostedAccountRequestDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
