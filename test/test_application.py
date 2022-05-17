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

import yapily
from yapily.models.application import Application  # noqa: E501
from yapily.rest import ApiException

class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Application
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.application.Application()  # noqa: E501
        if include_optional :
            return Application(
                uuid = '0', 
                name = '0', 
                active = True, 
                auth_callbacks = [
                    '0'
                    ], 
                institutions = [
                    yapily.models.institution.Institution(
                        id = '0', 
                        name = '0', 
                        full_name = '0', 
                        countries = [
                            yapily.models.country.Country(
                                display_name = '0', 
                                country_code2 = '0', )
                            ], 
                        environment_type = 'SANDBOX', 
                        credentials_type = 'OAUTH1', 
                        media = [
                            yapily.models.media.Media(
                                source = '0', 
                                type = '0', )
                            ], 
                        features = [
                            'INITIATE_PRE_AUTHORISATION'
                            ], 
                        monitoring = {
                            'key' : yapily.models.monitoring_feature_status.MonitoringFeatureStatus(
                                last_tested = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                span = '0', 
                                status = 'Up', )
                            }, )
                    ], 
                media = [
                    yapily.models.media.Media(
                        source = '0', 
                        type = '0', )
                    ], 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Application(
        )

    def testApplication(self):
        """Test Application"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
