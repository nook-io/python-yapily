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


class MonitoringEndpointStatus(object):
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
        'last_tested': 'datetime',
        'resource_endpoint': 'str',
        'span': 'str',
        'status': 'MonitoringStatusEnum'
    }

    attribute_map = {
        'last_tested': 'lastTested',
        'resource_endpoint': 'resourceEndpoint',
        'span': 'span',
        'status': 'status'
    }

    def __init__(self, last_tested=None, resource_endpoint=None, span=None, status=None, local_vars_configuration=None):  # noqa: E501
        """MonitoringEndpointStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_tested = None
        self._resource_endpoint = None
        self._span = None
        self._status = None
        self.discriminator = None

        if last_tested is not None:
            self.last_tested = last_tested
        if resource_endpoint is not None:
            self.resource_endpoint = resource_endpoint
        if span is not None:
            self.span = span
        if status is not None:
            self.status = status

    @property
    def last_tested(self):
        """Gets the last_tested of this MonitoringEndpointStatus.  # noqa: E501


        :return: The last_tested of this MonitoringEndpointStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_tested

    @last_tested.setter
    def last_tested(self, last_tested):
        """Sets the last_tested of this MonitoringEndpointStatus.


        :param last_tested: The last_tested of this MonitoringEndpointStatus.  # noqa: E501
        :type: datetime
        """

        self._last_tested = last_tested

    @property
    def resource_endpoint(self):
        """Gets the resource_endpoint of this MonitoringEndpointStatus.  # noqa: E501


        :return: The resource_endpoint of this MonitoringEndpointStatus.  # noqa: E501
        :rtype: str
        """
        return self._resource_endpoint

    @resource_endpoint.setter
    def resource_endpoint(self, resource_endpoint):
        """Sets the resource_endpoint of this MonitoringEndpointStatus.


        :param resource_endpoint: The resource_endpoint of this MonitoringEndpointStatus.  # noqa: E501
        :type: str
        """

        self._resource_endpoint = resource_endpoint

    @property
    def span(self):
        """Gets the span of this MonitoringEndpointStatus.  # noqa: E501


        :return: The span of this MonitoringEndpointStatus.  # noqa: E501
        :rtype: str
        """
        return self._span

    @span.setter
    def span(self, span):
        """Sets the span of this MonitoringEndpointStatus.


        :param span: The span of this MonitoringEndpointStatus.  # noqa: E501
        :type: str
        """

        self._span = span

    @property
    def status(self):
        """Gets the status of this MonitoringEndpointStatus.  # noqa: E501


        :return: The status of this MonitoringEndpointStatus.  # noqa: E501
        :rtype: MonitoringStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MonitoringEndpointStatus.


        :param status: The status of this MonitoringEndpointStatus.  # noqa: E501
        :type: MonitoringStatusEnum
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
        if not isinstance(other, MonitoringEndpointStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MonitoringEndpointStatus):
            return True

        return self.to_dict() != other.to_dict()
