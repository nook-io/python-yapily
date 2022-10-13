# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.feature_details import FeatureDetails  # noqa: E501
from yapily.rest import ApiException

class TestFeatureDetails(unittest.TestCase):
    """FeatureDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FeatureDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.feature_details.FeatureDetails()  # noqa: E501
        if include_optional :
            return FeatureDetails(
                feature = 'INITIATE_PRE_AUTHORISATION', 
                endpoint = '0', 
                documentation_url = '0'
            )
        else :
            return FeatureDetails(
        )

    def testFeatureDetails(self):
        """Test FeatureDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
