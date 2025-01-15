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

from yapily.models.submission_request import SubmissionRequest  # noqa: E501


class TestSubmissionRequest(unittest.TestCase):
    """SubmissionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubmissionRequest:
        """Test SubmissionRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SubmissionRequest`
        """
        model = SubmissionRequest()  # noqa: E501
        if include_optional:
            return SubmissionRequest(
                payment_idempotency_id = '04ab4536gaerfc0e1f93c4f4',
                psu_authentication_method = '',
                context_type = 'OTHER',
                payment_amount = yapily.models.amount_details.Amount Details(
                    amount = 10, 
                    currency = 'GBP', )
            )
        else:
            return SubmissionRequest(
                payment_idempotency_id = '04ab4536gaerfc0e1f93c4f4',
                psu_authentication_method = '',
                payment_amount = yapily.models.amount_details.Amount Details(
                    amount = 10, 
                    currency = 'GBP', ),
        )
        """

    def testSubmissionRequest(self):
        """Test SubmissionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
