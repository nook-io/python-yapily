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

from yapily.models.one_time_token_request import OneTimeTokenRequest

class TestOneTimeTokenRequest(unittest.TestCase):
    """OneTimeTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OneTimeTokenRequest:
        """Test OneTimeTokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OneTimeTokenRequest`
        """
        model = OneTimeTokenRequest()
        if include_optional:
            return OneTimeTokenRequest(
                one_time_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJJTlNUSVRVVElPTiI6ImJidmEtc2FuZGJveCIsIlVVSUQiOiJmMzNmNGU4ZC1jMDQ0LTQ2YTktOTlkMC0wYmRlMzIyYTJjOTIifQ.4Qv3NJI6av2nKi1U3aNmm71cIwJ3TvRsIlYDafQUVv_Khy_e-8oEpV_BoP4V1CII12oT-Yq4cPveHILz8BOwjg'
            )
        else:
            return OneTimeTokenRequest(
                one_time_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJJTlNUSVRVVElPTiI6ImJidmEtc2FuZGJveCIsIlVVSUQiOiJmMzNmNGU4ZC1jMDQ0LTQ2YTktOTlkMC0wYmRlMzIyYTJjOTIifQ.4Qv3NJI6av2nKi1U3aNmm71cIwJ3TvRsIlYDafQUVv_Khy_e-8oEpV_BoP4V1CII12oT-Yq4cPveHILz8BOwjg',
        )
        """

    def testOneTimeTokenRequest(self):
        """Test OneTimeTokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
