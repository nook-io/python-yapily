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

from yapily.models.payer_details_response import PayerDetailsResponse  # noqa: E501


class TestPayerDetailsResponse(unittest.TestCase):
    """PayerDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayerDetailsResponse:
        """Test PayerDetailsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PayerDetailsResponse`
        """
        model = PayerDetailsResponse()  # noqa: E501
        if include_optional:
            return PayerDetailsResponse(
                name = 'John Doe',
                account_identifications = [
                    yapily.models.account_identifications.Account Identifications(
                        type = 'SORT_CODE', 
                        identification = '401016', )
                    ],
                address = {"country":"GB"}
            )
        else:
            return PayerDetailsResponse(
        )
        """

    def testPayerDetailsResponse(self):
        """Test PayerDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
