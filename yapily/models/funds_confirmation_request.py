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


class FundsConfirmationRequest(object):
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
        'reference': 'str',
        'payment_amount': 'Amount'
    }

    attribute_map = {
        'reference': 'reference',
        'payment_amount': 'paymentAmount'
    }

    def __init__(self, reference=None, payment_amount=None, local_vars_configuration=None):  # noqa: E501
        """FundsConfirmationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reference = None
        self._payment_amount = None
        self.discriminator = None

        if reference is not None:
            self.reference = reference
        self.payment_amount = payment_amount

    @property
    def reference(self):
        """Gets the reference of this FundsConfirmationRequest.  # noqa: E501

        __Optional__. The payment reference or description. Limited to a maximum of 18 characters long.  # noqa: E501

        :return: The reference of this FundsConfirmationRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this FundsConfirmationRequest.

        __Optional__. The payment reference or description. Limited to a maximum of 18 characters long.  # noqa: E501

        :param reference: The reference of this FundsConfirmationRequest.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def payment_amount(self):
        """Gets the payment_amount of this FundsConfirmationRequest.  # noqa: E501


        :return: The payment_amount of this FundsConfirmationRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this FundsConfirmationRequest.


        :param payment_amount: The payment_amount of this FundsConfirmationRequest.  # noqa: E501
        :type: Amount
        """
        if self.local_vars_configuration.client_side_validation and payment_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_amount`, must not be `None`")  # noqa: E501

        self._payment_amount = payment_amount

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
        if not isinstance(other, FundsConfirmationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FundsConfirmationRequest):
            return True

        return self.to_dict() != other.to_dict()
