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


class UpdateVirtualAccountRequest(object):
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
        'nickname': 'str',
        'status': 'str'
    }

    attribute_map = {
        'nickname': 'nickname',
        'status': 'status'
    }

    def __init__(self, nickname=None, status=None, local_vars_configuration=None):  # noqa: E501
        """UpdateVirtualAccountRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nickname = None
        self._status = None
        self.discriminator = None

        if nickname is not None:
            self.nickname = nickname
        if status is not None:
            self.status = status

    @property
    def nickname(self):
        """Gets the nickname of this UpdateVirtualAccountRequest.  # noqa: E501

        New reference that can be provided in order to help with identification of the account  # noqa: E501

        :return: The nickname of this UpdateVirtualAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this UpdateVirtualAccountRequest.

        New reference that can be provided in order to help with identification of the account  # noqa: E501

        :param nickname: The nickname of this UpdateVirtualAccountRequest.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def status(self):
        """Gets the status of this UpdateVirtualAccountRequest.  # noqa: E501

        New state of the Account: CLOSED - The account has been permanently closed and cannot be used  # noqa: E501

        :return: The status of this UpdateVirtualAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateVirtualAccountRequest.

        New state of the Account: CLOSED - The account has been permanently closed and cannot be used  # noqa: E501

        :param status: The status of this UpdateVirtualAccountRequest.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, UpdateVirtualAccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateVirtualAccountRequest):
            return True

        return self.to_dict() != other.to_dict()
