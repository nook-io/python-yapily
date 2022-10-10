# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.13.1
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class EventSubscriptionDeleteResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'event_type_id': 'str',
        'application_id': 'str',
        'created': 'datetime',
        'delete_status': 'DeleteStatusEnum'
    }

    attribute_map = {
        'event_type_id': 'eventTypeId',
        'application_id': 'applicationId',
        'created': 'created',
        'delete_status': 'deleteStatus'
    }

    def __init__(self, event_type_id=None, application_id=None, created=None, delete_status=None, local_vars_configuration=None):  # noqa: E501
        """EventSubscriptionDeleteResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_type_id = None
        self._application_id = None
        self._created = None
        self._delete_status = None
        self.discriminator = None

        self.event_type_id = event_type_id
        self.application_id = application_id
        self.created = created
        self.delete_status = delete_status

    @property
    def event_type_id(self):
        """Gets the event_type_id of this EventSubscriptionDeleteResponse.  # noqa: E501

        Unique identifier of the event type (for which notifications will be sent)  # noqa: E501

        :return: The event_type_id of this EventSubscriptionDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._event_type_id

    @event_type_id.setter
    def event_type_id(self, event_type_id):
        """Sets the event_type_id of this EventSubscriptionDeleteResponse.

        Unique identifier of the event type (for which notifications will be sent)  # noqa: E501

        :param event_type_id: The event_type_id of this EventSubscriptionDeleteResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type_id`, must not be `None`")  # noqa: E501

        self._event_type_id = event_type_id

    @property
    def application_id(self):
        """Gets the application_id of this EventSubscriptionDeleteResponse.  # noqa: E501

        Application related to event subscription.  # noqa: E501

        :return: The application_id of this EventSubscriptionDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this EventSubscriptionDeleteResponse.

        Application related to event subscription.  # noqa: E501

        :param application_id: The application_id of this EventSubscriptionDeleteResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def created(self):
        """Gets the created of this EventSubscriptionDeleteResponse.  # noqa: E501

        Creation datetime of event subscription.  # noqa: E501

        :return: The created of this EventSubscriptionDeleteResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EventSubscriptionDeleteResponse.

        Creation datetime of event subscription.  # noqa: E501

        :param created: The created of this EventSubscriptionDeleteResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def delete_status(self):
        """Gets the delete_status of this EventSubscriptionDeleteResponse.  # noqa: E501


        :return: The delete_status of this EventSubscriptionDeleteResponse.  # noqa: E501
        :rtype: DeleteStatusEnum
        """
        return self._delete_status

    @delete_status.setter
    def delete_status(self, delete_status):
        """Sets the delete_status of this EventSubscriptionDeleteResponse.


        :param delete_status: The delete_status of this EventSubscriptionDeleteResponse.  # noqa: E501
        :type: DeleteStatusEnum
        """
        if self.local_vars_configuration.client_side_validation and delete_status is None:  # noqa: E501
            raise ValueError("Invalid value for `delete_status`, must not be `None`")  # noqa: E501

        self._delete_status = delete_status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventSubscriptionDeleteResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventSubscriptionDeleteResponse):
            return True

        return self.to_dict() != other.to_dict()
