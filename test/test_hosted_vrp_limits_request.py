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

from yapily.models.hosted_vrp_limits_request import HostedVRPLimitsRequest  # noqa: E501


class TestHostedVRPLimitsRequest(unittest.TestCase):
    """HostedVRPLimitsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HostedVRPLimitsRequest:
        """Test HostedVRPLimitsRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `HostedVRPLimitsRequest`
        """
        model = HostedVRPLimitsRequest()  # noqa: E501
        if include_optional:
            return HostedVRPLimitsRequest(
                periodic_limits = [
                    yapily.models.hosted_non_sweeping_periodic_limits.HostedNonSweepingPeriodicLimits(
                        max_amount = null, 
                        frequency = '', 
                        alignment = '', )
                    ],
                max_amount_per_payment = yapily.models.amount_details.Amount Details(
                    amount = 10, 
                    currency = 'GBP', ),
                max_cumulative_amount = yapily.models.amount_details.Amount Details(
                    amount = 10, 
                    currency = 'GBP', ),
                max_cumulative_number_of_payments = 56
            )
        else:
            return HostedVRPLimitsRequest(
        )
        """

    def testHostedVRPLimitsRequest(self):
        """Test HostedVRPLimitsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
