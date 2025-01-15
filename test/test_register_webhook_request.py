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

from yapily.models.register_webhook_request import RegisterWebhookRequest  # noqa: E501


class TestRegisterWebhookRequest(unittest.TestCase):
    """RegisterWebhookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RegisterWebhookRequest:
        """Test RegisterWebhookRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RegisterWebhookRequest`
        """
        model = RegisterWebhookRequest()  # noqa: E501
        if include_optional:
            return RegisterWebhookRequest(
                application_id = '',
                categories = [
                    ''
                    ],
                callback_url = yapily.models.register_webhook_request_callback_url.registerWebhook_request_callbackUrl(
                    main = yapily.models.register_webhook_request_callback_url_main.registerWebhook_request_callbackUrl_main(
                        url = '', ), 
                    backup = yapily.models.register_webhook_request_callback_url_backup.registerWebhook_request_callbackUrl_backup(
                        url = '', ), ),
                metadata = {
                    'key' : ''
                    }
            )
        else:
            return RegisterWebhookRequest(
                application_id = '',
                categories = [
                    ''
                    ],
                callback_url = yapily.models.register_webhook_request_callback_url.registerWebhook_request_callbackUrl(
                    main = yapily.models.register_webhook_request_callback_url_main.registerWebhook_request_callbackUrl_main(
                        url = '', ), 
                    backup = yapily.models.register_webhook_request_callback_url_backup.registerWebhook_request_callbackUrl_backup(
                        url = '', ), ),
        )
        """

    def testRegisterWebhookRequest(self):
        """Test RegisterWebhookRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
