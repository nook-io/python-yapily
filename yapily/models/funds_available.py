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


class FundsAvailable(object):
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
        'funds_available': 'bool',
        'funds_available_at': 'datetime'
    }

    attribute_map = {
        'funds_available': 'fundsAvailable',
        'funds_available_at': 'fundsAvailableAt'
    }

    def __init__(self, funds_available=None, funds_available_at=None, local_vars_configuration=None):  # noqa: E501
        """FundsAvailable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._funds_available = None
        self._funds_available_at = None
        self.discriminator = None

        self.funds_available = funds_available
        self.funds_available_at = funds_available_at

    @property
    def funds_available(self):
        """Gets the funds_available of this FundsAvailable.  # noqa: E501

        __Mandatory__. Indicates whether funds are available or not.  # noqa: E501

        :return: The funds_available of this FundsAvailable.  # noqa: E501
        :rtype: bool
        """
        return self._funds_available

    @funds_available.setter
    def funds_available(self, funds_available):
        """Sets the funds_available of this FundsAvailable.

        __Mandatory__. Indicates whether funds are available or not.  # noqa: E501

        :param funds_available: The funds_available of this FundsAvailable.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and funds_available is None:  # noqa: E501
            raise ValueError("Invalid value for `funds_available`, must not be `None`")  # noqa: E501

        self._funds_available = funds_available

    @property
    def funds_available_at(self):
        """Gets the funds_available_at of this FundsAvailable.  # noqa: E501

        __Mandatory__. Date and Time when the funds availability is checked.  # noqa: E501

        :return: The funds_available_at of this FundsAvailable.  # noqa: E501
        :rtype: datetime
        """
        return self._funds_available_at

    @funds_available_at.setter
    def funds_available_at(self, funds_available_at):
        """Sets the funds_available_at of this FundsAvailable.

        __Mandatory__. Date and Time when the funds availability is checked.  # noqa: E501

        :param funds_available_at: The funds_available_at of this FundsAvailable.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and funds_available_at is None:  # noqa: E501
            raise ValueError("Invalid value for `funds_available_at`, must not be `None`")  # noqa: E501

        self._funds_available_at = funds_available_at

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
        if not isinstance(other, FundsAvailable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FundsAvailable):
            return True

        return self.to_dict() != other.to_dict()