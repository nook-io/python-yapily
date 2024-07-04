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

from yapily.api.notifications_api import NotificationsApi  # noqa: E501


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotificationsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_event_subscription(self) -> None:
        """Test case for create_event_subscription

        Create Event Subscription  # noqa: E501
        """
        pass

    def test_delete_event_subscription_by_id(self) -> None:
        """Test case for delete_event_subscription_by_id

        Delete Event Subscription  # noqa: E501
        """
        pass

    def test_get_event_subscription_by_id(self) -> None:
        """Test case for get_event_subscription_by_id

        Get Event Subscription  # noqa: E501
        """
        pass

    def test_get_event_subscriptions(self) -> None:
        """Test case for get_event_subscriptions

        Get Event Subscriptions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
