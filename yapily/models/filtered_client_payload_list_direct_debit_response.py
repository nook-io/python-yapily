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


class FilteredClientPayloadListDirectDebitResponse(object):
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
        'api_call': 'object',
        'data': 'list[DirectDebitResponse]',
        'next_cursor_hash': 'str',
        'next_link': 'str',
        'paging_map': 'dict(str, FilterAndSort)',
        'total_count': 'int'
    }

    attribute_map = {
        'api_call': 'apiCall',
        'data': 'data',
        'next_cursor_hash': 'nextCursorHash',
        'next_link': 'nextLink',
        'paging_map': 'pagingMap',
        'total_count': 'totalCount'
    }

    def __init__(self, api_call=None, data=None, next_cursor_hash=None, next_link=None, paging_map=None, total_count=None, local_vars_configuration=None):  # noqa: E501
        """FilteredClientPayloadListDirectDebitResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_call = None
        self._data = None
        self._next_cursor_hash = None
        self._next_link = None
        self._paging_map = None
        self._total_count = None
        self.discriminator = None

        if api_call is not None:
            self.api_call = api_call
        if data is not None:
            self.data = data
        if next_cursor_hash is not None:
            self.next_cursor_hash = next_cursor_hash
        if next_link is not None:
            self.next_link = next_link
        if paging_map is not None:
            self.paging_map = paging_map
        if total_count is not None:
            self.total_count = total_count

    @property
    def api_call(self):
        """Gets the api_call of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501


        :return: The api_call of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :rtype: object
        """
        return self._api_call

    @api_call.setter
    def api_call(self, api_call):
        """Sets the api_call of this FilteredClientPayloadListDirectDebitResponse.


        :param api_call: The api_call of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :type: object
        """

        self._api_call = api_call

    @property
    def data(self):
        """Gets the data of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501


        :return: The data of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :rtype: list[DirectDebitResponse]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FilteredClientPayloadListDirectDebitResponse.


        :param data: The data of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :type: list[DirectDebitResponse]
        """

        self._data = data

    @property
    def next_cursor_hash(self):
        """Gets the next_cursor_hash of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501


        :return: The next_cursor_hash of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_cursor_hash

    @next_cursor_hash.setter
    def next_cursor_hash(self, next_cursor_hash):
        """Sets the next_cursor_hash of this FilteredClientPayloadListDirectDebitResponse.


        :param next_cursor_hash: The next_cursor_hash of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :type: str
        """

        self._next_cursor_hash = next_cursor_hash

    @property
    def next_link(self):
        """Gets the next_link of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501


        :return: The next_link of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this FilteredClientPayloadListDirectDebitResponse.


        :param next_link: The next_link of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

    @property
    def paging_map(self):
        """Gets the paging_map of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501


        :return: The paging_map of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :rtype: dict(str, FilterAndSort)
        """
        return self._paging_map

    @paging_map.setter
    def paging_map(self, paging_map):
        """Sets the paging_map of this FilteredClientPayloadListDirectDebitResponse.


        :param paging_map: The paging_map of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :type: dict(str, FilterAndSort)
        """

        self._paging_map = paging_map

    @property
    def total_count(self):
        """Gets the total_count of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501


        :return: The total_count of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this FilteredClientPayloadListDirectDebitResponse.


        :param total_count: The total_count of this FilteredClientPayloadListDirectDebitResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, FilteredClientPayloadListDirectDebitResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilteredClientPayloadListDirectDebitResponse):
            return True

        return self.to_dict() != other.to_dict()
