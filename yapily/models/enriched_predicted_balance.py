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


class EnrichedPredictedBalance(object):
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
        'date': 'date',
        'median_balance': 'float',
        '_90percentile_balance': 'float',
        '_10percentile_balance': 'float'
    }

    attribute_map = {
        'date': 'date',
        'median_balance': 'medianBalance',
        '_90percentile_balance': '90percentileBalance',
        '_10percentile_balance': '10percentileBalance'
    }

    def __init__(self, date=None, median_balance=None, _90percentile_balance=None, _10percentile_balance=None, local_vars_configuration=None):  # noqa: E501
        """EnrichedPredictedBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._median_balance = None
        self.__90percentile_balance = None
        self.__10percentile_balance = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if median_balance is not None:
            self.median_balance = median_balance
        if _90percentile_balance is not None:
            self._90percentile_balance = _90percentile_balance
        if _10percentile_balance is not None:
            self._10percentile_balance = _10percentile_balance

    @property
    def date(self):
        """Gets the date of this EnrichedPredictedBalance.  # noqa: E501

        The date for which Balance amount is predicted.  # noqa: E501

        :return: The date of this EnrichedPredictedBalance.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this EnrichedPredictedBalance.

        The date for which Balance amount is predicted.  # noqa: E501

        :param date: The date of this EnrichedPredictedBalance.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def median_balance(self):
        """Gets the median_balance of this EnrichedPredictedBalance.  # noqa: E501

        The median Balance amount for a future date.  # noqa: E501

        :return: The median_balance of this EnrichedPredictedBalance.  # noqa: E501
        :rtype: float
        """
        return self._median_balance

    @median_balance.setter
    def median_balance(self, median_balance):
        """Sets the median_balance of this EnrichedPredictedBalance.

        The median Balance amount for a future date.  # noqa: E501

        :param median_balance: The median_balance of this EnrichedPredictedBalance.  # noqa: E501
        :type: float
        """

        self._median_balance = median_balance

    @property
    def _90percentile_balance(self):
        """Gets the _90percentile_balance of this EnrichedPredictedBalance.  # noqa: E501

        The 90th percentile Balance amount for a future date.  # noqa: E501

        :return: The _90percentile_balance of this EnrichedPredictedBalance.  # noqa: E501
        :rtype: float
        """
        return self.__90percentile_balance

    @_90percentile_balance.setter
    def _90percentile_balance(self, _90percentile_balance):
        """Sets the _90percentile_balance of this EnrichedPredictedBalance.

        The 90th percentile Balance amount for a future date.  # noqa: E501

        :param _90percentile_balance: The _90percentile_balance of this EnrichedPredictedBalance.  # noqa: E501
        :type: float
        """

        self.__90percentile_balance = _90percentile_balance

    @property
    def _10percentile_balance(self):
        """Gets the _10percentile_balance of this EnrichedPredictedBalance.  # noqa: E501

        The 10th percentile Balance amount for a future date.  # noqa: E501

        :return: The _10percentile_balance of this EnrichedPredictedBalance.  # noqa: E501
        :rtype: float
        """
        return self.__10percentile_balance

    @_10percentile_balance.setter
    def _10percentile_balance(self, _10percentile_balance):
        """Sets the _10percentile_balance of this EnrichedPredictedBalance.

        The 10th percentile Balance amount for a future date.  # noqa: E501

        :param _10percentile_balance: The _10percentile_balance of this EnrichedPredictedBalance.  # noqa: E501
        :type: float
        """

        self.__10percentile_balance = _10percentile_balance

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
        if not isinstance(other, EnrichedPredictedBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnrichedPredictedBalance):
            return True

        return self.to_dict() != other.to_dict()