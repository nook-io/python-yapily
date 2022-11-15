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


class AccountRequest(object):
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
        'transaction_from': 'datetime',
        'transaction_to': 'datetime',
        'expires_at': 'datetime',
        'account_identifiers': 'AccountInfo',
        'account_identifiers_for_transaction': 'list[AccountInfo]',
        'account_identifiers_for_balance': 'list[AccountInfo]',
        'feature_scope': 'list[FeatureEnum]'
    }

    attribute_map = {
        'transaction_from': 'transactionFrom',
        'transaction_to': 'transactionTo',
        'expires_at': 'expiresAt',
        'account_identifiers': 'accountIdentifiers',
        'account_identifiers_for_transaction': 'accountIdentifiersForTransaction',
        'account_identifiers_for_balance': 'accountIdentifiersForBalance',
        'feature_scope': 'featureScope'
    }

    def __init__(self, transaction_from=None, transaction_to=None, expires_at=None, account_identifiers=None, account_identifiers_for_transaction=None, account_identifiers_for_balance=None, feature_scope=None, local_vars_configuration=None):  # noqa: E501
        """AccountRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_from = None
        self._transaction_to = None
        self._expires_at = None
        self._account_identifiers = None
        self._account_identifiers_for_transaction = None
        self._account_identifiers_for_balance = None
        self._feature_scope = None
        self.discriminator = None

        if transaction_from is not None:
            self.transaction_from = transaction_from
        if transaction_to is not None:
            self.transaction_to = transaction_to
        if expires_at is not None:
            self.expires_at = expires_at
        if account_identifiers is not None:
            self.account_identifiers = account_identifiers
        if account_identifiers_for_transaction is not None:
            self.account_identifiers_for_transaction = account_identifiers_for_transaction
        if account_identifiers_for_balance is not None:
            self.account_identifiers_for_balance = account_identifiers_for_balance
        if feature_scope is not None:
            self.feature_scope = feature_scope

    @property
    def transaction_from(self):
        """Gets the transaction_from of this AccountRequest.  # noqa: E501

        __Optional__. Used to specify the lower bound on when to pull transaction. This should be declared when accessing transaction older than 90 days for banks in the [CBI Globe](https://docs.yapily.com/pages/knowledge/open-banking/cbi_globe/).  # noqa: E501

        :return: The transaction_from of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_from

    @transaction_from.setter
    def transaction_from(self, transaction_from):
        """Sets the transaction_from of this AccountRequest.

        __Optional__. Used to specify the lower bound on when to pull transaction. This should be declared when accessing transaction older than 90 days for banks in the [CBI Globe](https://docs.yapily.com/pages/knowledge/open-banking/cbi_globe/).  # noqa: E501

        :param transaction_from: The transaction_from of this AccountRequest.  # noqa: E501
        :type: datetime
        """

        self._transaction_from = transaction_from

    @property
    def transaction_to(self):
        """Gets the transaction_to of this AccountRequest.  # noqa: E501

        __Optional__. When performing a request using the consent, this is the latest date of transaction records that can be retrieved.  # noqa: E501

        :return: The transaction_to of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_to

    @transaction_to.setter
    def transaction_to(self, transaction_to):
        """Sets the transaction_to of this AccountRequest.

        __Optional__. When performing a request using the consent, this is the latest date of transaction records that can be retrieved.  # noqa: E501

        :param transaction_to: The transaction_to of this AccountRequest.  # noqa: E501
        :type: datetime
        """

        self._transaction_to = transaction_to

    @property
    def expires_at(self):
        """Gets the expires_at of this AccountRequest.  # noqa: E501

        __Optional__. Used to set a hard date for when the user's associated `Consent` will expire.<br><br>**Note**: If this supported by the bank, specifying this is property is opting out of having a long-lived consent that can be perpetually re-authorised by the user. This will add an `expiresAt` field on the `Consent` object which will render it unusable after this date.<br><br>**Note**: This is not supported by every `Institution`. In such case, the request will not fail but the property will be ignored and the created `Consent` will not have an expiry date.  # noqa: E501

        :return: The expires_at of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this AccountRequest.

        __Optional__. Used to set a hard date for when the user's associated `Consent` will expire.<br><br>**Note**: If this supported by the bank, specifying this is property is opting out of having a long-lived consent that can be perpetually re-authorised by the user. This will add an `expiresAt` field on the `Consent` object which will render it unusable after this date.<br><br>**Note**: This is not supported by every `Institution`. In such case, the request will not fail but the property will be ignored and the created `Consent` will not have an expiry date.  # noqa: E501

        :param expires_at: The expires_at of this AccountRequest.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def account_identifiers(self):
        """Gets the account_identifiers of this AccountRequest.  # noqa: E501


        :return: The account_identifiers of this AccountRequest.  # noqa: E501
        :rtype: AccountInfo
        """
        return self._account_identifiers

    @account_identifiers.setter
    def account_identifiers(self, account_identifiers):
        """Sets the account_identifiers of this AccountRequest.


        :param account_identifiers: The account_identifiers of this AccountRequest.  # noqa: E501
        :type: AccountInfo
        """

        self._account_identifiers = account_identifiers

    @property
    def account_identifiers_for_transaction(self):
        """Gets the account_identifiers_for_transaction of this AccountRequest.  # noqa: E501

        __Conditional__. Used to create a request for the transactions of the account specified. Once the user authorises the request, only the transactions can be obtained by executing [GET Account Transactions](./#get-account-transactions). <br><br>This can be specified in conjunction with `accountIdentifiersForBalance` to generate a `Consent` that can both access the accounts balance and transactions.  # noqa: E501

        :return: The account_identifiers_for_transaction of this AccountRequest.  # noqa: E501
        :rtype: list[AccountInfo]
        """
        return self._account_identifiers_for_transaction

    @account_identifiers_for_transaction.setter
    def account_identifiers_for_transaction(self, account_identifiers_for_transaction):
        """Sets the account_identifiers_for_transaction of this AccountRequest.

        __Conditional__. Used to create a request for the transactions of the account specified. Once the user authorises the request, only the transactions can be obtained by executing [GET Account Transactions](./#get-account-transactions). <br><br>This can be specified in conjunction with `accountIdentifiersForBalance` to generate a `Consent` that can both access the accounts balance and transactions.  # noqa: E501

        :param account_identifiers_for_transaction: The account_identifiers_for_transaction of this AccountRequest.  # noqa: E501
        :type: list[AccountInfo]
        """

        self._account_identifiers_for_transaction = account_identifiers_for_transaction

    @property
    def account_identifiers_for_balance(self):
        """Gets the account_identifiers_for_balance of this AccountRequest.  # noqa: E501

        __Conditional__. Used to create a request for the balance of the account specified. Once the user authorises the request, only the balance can be obtained by executing [GET Account Balances](./#get-account-balances).<br><br> This can be specified in conjunction with `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and transactions.  # noqa: E501

        :return: The account_identifiers_for_balance of this AccountRequest.  # noqa: E501
        :rtype: list[AccountInfo]
        """
        return self._account_identifiers_for_balance

    @account_identifiers_for_balance.setter
    def account_identifiers_for_balance(self, account_identifiers_for_balance):
        """Sets the account_identifiers_for_balance of this AccountRequest.

        __Conditional__. Used to create a request for the balance of the account specified. Once the user authorises the request, only the balance can be obtained by executing [GET Account Balances](./#get-account-balances).<br><br> This can be specified in conjunction with `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and transactions.  # noqa: E501

        :param account_identifiers_for_balance: The account_identifiers_for_balance of this AccountRequest.  # noqa: E501
        :type: list[AccountInfo]
        """

        self._account_identifiers_for_balance = account_identifiers_for_balance

    @property
    def feature_scope(self):
        """Gets the feature_scope of this AccountRequest.  # noqa: E501

        __Optional__. Used to granularly specify the set of features that the user will give their consent for when requesting access to their account information. Depending on the `Institution`, this may also populate a consent screen which list these scopes before the user authorises.<br><br>This endpoint accepts allow all [Financial Data Features](/guides/financial-data/features/#feature-list) that the `Institution` supports.To find out which scopes an `Institution` supports, check [GET Institution](./#get-institution).  # noqa: E501

        :return: The feature_scope of this AccountRequest.  # noqa: E501
        :rtype: list[FeatureEnum]
        """
        return self._feature_scope

    @feature_scope.setter
    def feature_scope(self, feature_scope):
        """Sets the feature_scope of this AccountRequest.

        __Optional__. Used to granularly specify the set of features that the user will give their consent for when requesting access to their account information. Depending on the `Institution`, this may also populate a consent screen which list these scopes before the user authorises.<br><br>This endpoint accepts allow all [Financial Data Features](/guides/financial-data/features/#feature-list) that the `Institution` supports.To find out which scopes an `Institution` supports, check [GET Institution](./#get-institution).  # noqa: E501

        :param feature_scope: The feature_scope of this AccountRequest.  # noqa: E501
        :type: list[FeatureEnum]
        """

        self._feature_scope = feature_scope

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
        if not isinstance(other, AccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountRequest):
            return True

        return self.to_dict() != other.to_dict()
