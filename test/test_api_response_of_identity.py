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

from yapily.models.api_response_of_identity import ApiResponseOfIdentity  # noqa: E501


class TestApiResponseOfIdentity(unittest.TestCase):
    """ApiResponseOfIdentity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResponseOfIdentity:
        """Test ApiResponseOfIdentity
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ApiResponseOfIdentity`
        """
        model = ApiResponseOfIdentity()  # noqa: E501
        if include_optional:
            return ApiResponseOfIdentity(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '', ),
                data = yapily.models.identity.Identity(
                    id = '', 
                    first_name = '', 
                    last_name = '', 
                    full_name = '', 
                    gender = '', 
                    birthdate = '', 
                    email = '', 
                    phone = '', 
                    addresses = [
                        yapily.models.identity_address.IdentityAddress(
                            address_lines = [
                                ''
                                ], 
                            city = '', 
                            postal_code = '', 
                            country = '', 
                            street_name = '', 
                            building_number = '', 
                            type = 'BUSINESS', 
                            county = '', )
                        ], ),
                links = {
                    'key' : ''
                    },
                forwarded_data = [
                    yapily.models.response_forwarded_data.ResponseForwardedData(
                        headers = {
                            'key' : ''
                            }, 
                        url = '', )
                    ],
                raw = [
                    yapily.models.raw_response.RawResponse(
                        request = yapily.models.raw_request.RawRequest(
                            method = '', 
                            url = '', 
                            request_instant = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            headers = {
                                'key' : ''
                                }, 
                            body = yapily.models.body.body(), 
                            body_parameters = {
                                'key' : ''
                                }, 
                            start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        duration = '', 
                        headers = {
                            'key' : ''
                            }, 
                        result_code = 56, 
                        result = yapily.models.result.result(), )
                    ],
                tracing_id = ''
            )
        else:
            return ApiResponseOfIdentity(
        )
        """

    def testApiResponseOfIdentity(self):
        """Test ApiResponseOfIdentity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
