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


class VirtualAccountBeneficiaryAccount(object):
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
        'currency': 'str',
        'bank_name': 'str',
        'bank_address': 'str',
        'bank_country': 'str',
        'account_identifications': 'list[AccountIdentification]'
    }

    attribute_map = {
        'currency': 'currency',
        'bank_name': 'bankName',
        'bank_address': 'bankAddress',
        'bank_country': 'bankCountry',
        'account_identifications': 'accountIdentifications'
    }

    def __init__(self, currency=None, bank_name=None, bank_address=None, bank_country=None, account_identifications=None, local_vars_configuration=None):  # noqa: E501
        """VirtualAccountBeneficiaryAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._bank_name = None
        self._bank_address = None
        self._bank_country = None
        self._account_identifications = None
        self.discriminator = None

        self.currency = currency
        if bank_name is not None:
            self.bank_name = bank_name
        if bank_address is not None:
            self.bank_address = bank_address
        if bank_country is not None:
            self.bank_country = bank_country
        self.account_identifications = account_identifications

    @property
    def currency(self):
        """Gets the currency of this VirtualAccountBeneficiaryAccount.  # noqa: E501

        Three-letter ISO 4217 currency code  # noqa: E501

        :return: The currency of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this VirtualAccountBeneficiaryAccount.

        Three-letter ISO 4217 currency code  # noqa: E501

        :param currency: The currency of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def bank_name(self):
        """Gets the bank_name of this VirtualAccountBeneficiaryAccount.  # noqa: E501


        :return: The bank_name of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this VirtualAccountBeneficiaryAccount.


        :param bank_name: The bank_name of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def bank_address(self):
        """Gets the bank_address of this VirtualAccountBeneficiaryAccount.  # noqa: E501


        :return: The bank_address of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_address

    @bank_address.setter
    def bank_address(self, bank_address):
        """Sets the bank_address of this VirtualAccountBeneficiaryAccount.


        :param bank_address: The bank_address of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :type: str
        """

        self._bank_address = bank_address

    @property
    def bank_country(self):
        """Gets the bank_country of this VirtualAccountBeneficiaryAccount.  # noqa: E501

        Two-letter ISO 3166 country code  # noqa: E501

        :return: The bank_country of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_country

    @bank_country.setter
    def bank_country(self, bank_country):
        """Sets the bank_country of this VirtualAccountBeneficiaryAccount.

        Two-letter ISO 3166 country code  # noqa: E501

        :param bank_country: The bank_country of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :type: str
        """

        self._bank_country = bank_country

    @property
    def account_identifications(self):
        """Gets the account_identifications of this VirtualAccountBeneficiaryAccount.  # noqa: E501

        The account identifications that identify the Beneficiary bank account.  # noqa: E501

        :return: The account_identifications of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :rtype: list[AccountIdentification]
        """
        return self._account_identifications

    @account_identifications.setter
    def account_identifications(self, account_identifications):
        """Sets the account_identifications of this VirtualAccountBeneficiaryAccount.

        The account identifications that identify the Beneficiary bank account.  # noqa: E501

        :param account_identifications: The account_identifications of this VirtualAccountBeneficiaryAccount.  # noqa: E501
        :type: list[AccountIdentification]
        """
        if self.local_vars_configuration.client_side_validation and account_identifications is None:  # noqa: E501
            raise ValueError("Invalid value for `account_identifications`, must not be `None`")  # noqa: E501

        self._account_identifications = account_identifications

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
        if not isinstance(other, VirtualAccountBeneficiaryAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualAccountBeneficiaryAccount):
            return True

        return self.to_dict() != other.to_dict()