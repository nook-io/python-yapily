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


class ApiListResponseOfConsent(object):
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
        'meta': 'ResponseListMeta',
        'data': 'list[Consent]',
        'links': 'dict(str, str)',
        'forwarded_data': 'list[ResponseForwardedData]',
        'raw': 'list[RawResponse]',
        'paging': 'FilteredClientPayloadListConsent',
        'tracing_id': 'str'
    }

    attribute_map = {
        'meta': 'meta',
        'data': 'data',
        'links': 'links',
        'forwarded_data': 'forwardedData',
        'raw': 'raw',
        'paging': 'paging',
        'tracing_id': 'tracingId'
    }

    def __init__(self, meta=None, data=None, links=None, forwarded_data=None, raw=None, paging=None, tracing_id=None, local_vars_configuration=None):  # noqa: E501
        """ApiListResponseOfConsent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._meta = None
        self._data = None
        self._links = None
        self._forwarded_data = None
        self._raw = None
        self._paging = None
        self._tracing_id = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if data is not None:
            self.data = data
        if links is not None:
            self.links = links
        if forwarded_data is not None:
            self.forwarded_data = forwarded_data
        if raw is not None:
            self.raw = raw
        if paging is not None:
            self.paging = paging
        if tracing_id is not None:
            self.tracing_id = tracing_id

    @property
    def meta(self):
        """Gets the meta of this ApiListResponseOfConsent.  # noqa: E501


        :return: The meta of this ApiListResponseOfConsent.  # noqa: E501
        :rtype: ResponseListMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ApiListResponseOfConsent.


        :param meta: The meta of this ApiListResponseOfConsent.  # noqa: E501
        :type: ResponseListMeta
        """

        self._meta = meta

    @property
    def data(self):
        """Gets the data of this ApiListResponseOfConsent.  # noqa: E501


        :return: The data of this ApiListResponseOfConsent.  # noqa: E501
        :rtype: list[Consent]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiListResponseOfConsent.


        :param data: The data of this ApiListResponseOfConsent.  # noqa: E501
        :type: list[Consent]
        """

        self._data = data

    @property
    def links(self):
        """Gets the links of this ApiListResponseOfConsent.  # noqa: E501


        :return: The links of this ApiListResponseOfConsent.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ApiListResponseOfConsent.


        :param links: The links of this ApiListResponseOfConsent.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

    @property
    def forwarded_data(self):
        """Gets the forwarded_data of this ApiListResponseOfConsent.  # noqa: E501


        :return: The forwarded_data of this ApiListResponseOfConsent.  # noqa: E501
        :rtype: list[ResponseForwardedData]
        """
        return self._forwarded_data

    @forwarded_data.setter
    def forwarded_data(self, forwarded_data):
        """Sets the forwarded_data of this ApiListResponseOfConsent.


        :param forwarded_data: The forwarded_data of this ApiListResponseOfConsent.  # noqa: E501
        :type: list[ResponseForwardedData]
        """

        self._forwarded_data = forwarded_data

    @property
    def raw(self):
        """Gets the raw of this ApiListResponseOfConsent.  # noqa: E501


        :return: The raw of this ApiListResponseOfConsent.  # noqa: E501
        :rtype: list[RawResponse]
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this ApiListResponseOfConsent.


        :param raw: The raw of this ApiListResponseOfConsent.  # noqa: E501
        :type: list[RawResponse]
        """

        self._raw = raw

    @property
    def paging(self):
        """Gets the paging of this ApiListResponseOfConsent.  # noqa: E501


        :return: The paging of this ApiListResponseOfConsent.  # noqa: E501
        :rtype: FilteredClientPayloadListConsent
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this ApiListResponseOfConsent.


        :param paging: The paging of this ApiListResponseOfConsent.  # noqa: E501
        :type: FilteredClientPayloadListConsent
        """

        self._paging = paging

    @property
    def tracing_id(self):
        """Gets the tracing_id of this ApiListResponseOfConsent.  # noqa: E501


        :return: The tracing_id of this ApiListResponseOfConsent.  # noqa: E501
        :rtype: str
        """
        return self._tracing_id

    @tracing_id.setter
    def tracing_id(self, tracing_id):
        """Sets the tracing_id of this ApiListResponseOfConsent.


        :param tracing_id: The tracing_id of this ApiListResponseOfConsent.  # noqa: E501
        :type: str
        """

        self._tracing_id = tracing_id

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
        if not isinstance(other, ApiListResponseOfConsent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiListResponseOfConsent):
            return True

        return self.to_dict() != other.to_dict()
