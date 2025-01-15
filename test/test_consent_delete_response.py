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

from yapily.models.consent_delete_response import ConsentDeleteResponse  # noqa: E501


class TestConsentDeleteResponse(unittest.TestCase):
    """ConsentDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConsentDeleteResponse:
        """Test ConsentDeleteResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ConsentDeleteResponse`
        """
        model = ConsentDeleteResponse()  # noqa: E501
        if include_optional:
            return ConsentDeleteResponse(
                id = '',
                delete_status = 'SUCCESS',
                institution_id = '',
                institution_consent_id = '',
                creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ConsentDeleteResponse(
        )
        """

    def testConsentDeleteResponse(self):
        """Test ConsentDeleteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
