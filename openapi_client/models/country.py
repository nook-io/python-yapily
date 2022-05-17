# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/#getting-started) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/guides/applications/institutions/sandbox/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Country(object):
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
        'display_name': 'str',
        'country_code2': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'country_code2': 'countryCode2'
    }

    def __init__(self, display_name=None, country_code2=None, local_vars_configuration=None):  # noqa: E501
        """Country - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._country_code2 = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if country_code2 is not None:
            self.country_code2 = country_code2

    @property
    def display_name(self):
        """Gets the display_name of this Country.  # noqa: E501


        :return: The display_name of this Country.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Country.


        :param display_name: The display_name of this Country.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def country_code2(self):
        """Gets the country_code2 of this Country.  # noqa: E501


        :return: The country_code2 of this Country.  # noqa: E501
        :rtype: str
        """
        return self._country_code2

    @country_code2.setter
    def country_code2(self, country_code2):
        """Sets the country_code2 of this Country.


        :param country_code2: The country_code2 of this Country.  # noqa: E501
        :type: str
        """

        self._country_code2 = country_code2

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
        if not isinstance(other, Country):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Country):
            return True

        return self.to_dict() != other.to_dict()