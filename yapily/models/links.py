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


class Links(object):
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
        '_self': 'str',
        'first': 'str',
        'last': 'str',
        'next': 'str',
        'previous': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'first': 'first',
        'last': 'last',
        'next': 'next',
        'previous': 'previous'
    }

    def __init__(self, _self=None, first=None, last=None, next=None, previous=None, local_vars_configuration=None):  # noqa: E501
        """Links - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__self = None
        self._first = None
        self._last = None
        self._next = None
        self._previous = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if first is not None:
            self.first = first
        if last is not None:
            self.last = last
        if next is not None:
            self.next = next
        if previous is not None:
            self.previous = previous

    @property
    def _self(self):
        """Gets the _self of this Links.  # noqa: E501


        :return: The _self of this Links.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Links.


        :param _self: The _self of this Links.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def first(self):
        """Gets the first of this Links.  # noqa: E501


        :return: The first of this Links.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this Links.


        :param first: The first of this Links.  # noqa: E501
        :type: str
        """

        self._first = first

    @property
    def last(self):
        """Gets the last of this Links.  # noqa: E501


        :return: The last of this Links.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this Links.


        :param last: The last of this Links.  # noqa: E501
        :type: str
        """

        self._last = last

    @property
    def next(self):
        """Gets the next of this Links.  # noqa: E501


        :return: The next of this Links.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Links.


        :param next: The next of this Links.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this Links.  # noqa: E501


        :return: The previous of this Links.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this Links.


        :param previous: The previous of this Links.  # noqa: E501
        :type: str
        """

        self._previous = previous

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
        if not isinstance(other, Links):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Links):
            return True

        return self.to_dict() != other.to_dict()