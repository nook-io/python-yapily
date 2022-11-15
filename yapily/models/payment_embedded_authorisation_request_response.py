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


class PaymentEmbeddedAuthorisationRequestResponse(object):
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
        'id': 'str',
        'user_uuid': 'str',
        'application_user_id': 'str',
        'reference_id': 'str',
        'institution_id': 'str',
        'status': 'AuthorisationStatus',
        'created_at': 'datetime',
        'transaction_from': 'datetime',
        'transaction_to': 'datetime',
        'expires_at': 'datetime',
        'time_to_expire_in_millis': 'int',
        'time_to_expire': 'str',
        'feature_scope': 'list[FeatureEnum]',
        'consent_token': 'str',
        'state': 'str',
        'authorized_at': 'datetime',
        'institution_consent_id': 'str',
        'charges': 'list[PaymentChargeDetails]',
        'exchange_rate_information': 'ExchangeRateInformationResponse',
        'authorisation_url': 'str',
        'qr_code_url': 'str',
        'explanation': 'str',
        'sca_methods': 'list[ScaMethod]',
        'selected_sca_method': 'ScaMethod'
    }

    attribute_map = {
        'id': 'id',
        'user_uuid': 'userUuid',
        'application_user_id': 'applicationUserId',
        'reference_id': 'referenceId',
        'institution_id': 'institutionId',
        'status': 'status',
        'created_at': 'createdAt',
        'transaction_from': 'transactionFrom',
        'transaction_to': 'transactionTo',
        'expires_at': 'expiresAt',
        'time_to_expire_in_millis': 'timeToExpireInMillis',
        'time_to_expire': 'timeToExpire',
        'feature_scope': 'featureScope',
        'consent_token': 'consentToken',
        'state': 'state',
        'authorized_at': 'authorizedAt',
        'institution_consent_id': 'institutionConsentId',
        'charges': 'charges',
        'exchange_rate_information': 'exchangeRateInformation',
        'authorisation_url': 'authorisationUrl',
        'qr_code_url': 'qrCodeUrl',
        'explanation': 'explanation',
        'sca_methods': 'scaMethods',
        'selected_sca_method': 'selectedScaMethod'
    }

    def __init__(self, id=None, user_uuid=None, application_user_id=None, reference_id=None, institution_id=None, status=None, created_at=None, transaction_from=None, transaction_to=None, expires_at=None, time_to_expire_in_millis=None, time_to_expire=None, feature_scope=None, consent_token=None, state=None, authorized_at=None, institution_consent_id=None, charges=None, exchange_rate_information=None, authorisation_url=None, qr_code_url=None, explanation=None, sca_methods=None, selected_sca_method=None, local_vars_configuration=None):  # noqa: E501
        """PaymentEmbeddedAuthorisationRequestResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_uuid = None
        self._application_user_id = None
        self._reference_id = None
        self._institution_id = None
        self._status = None
        self._created_at = None
        self._transaction_from = None
        self._transaction_to = None
        self._expires_at = None
        self._time_to_expire_in_millis = None
        self._time_to_expire = None
        self._feature_scope = None
        self._consent_token = None
        self._state = None
        self._authorized_at = None
        self._institution_consent_id = None
        self._charges = None
        self._exchange_rate_information = None
        self._authorisation_url = None
        self._qr_code_url = None
        self._explanation = None
        self._sca_methods = None
        self._selected_sca_method = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if application_user_id is not None:
            self.application_user_id = application_user_id
        if reference_id is not None:
            self.reference_id = reference_id
        if institution_id is not None:
            self.institution_id = institution_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if transaction_from is not None:
            self.transaction_from = transaction_from
        if transaction_to is not None:
            self.transaction_to = transaction_to
        if expires_at is not None:
            self.expires_at = expires_at
        if time_to_expire_in_millis is not None:
            self.time_to_expire_in_millis = time_to_expire_in_millis
        if time_to_expire is not None:
            self.time_to_expire = time_to_expire
        if feature_scope is not None:
            self.feature_scope = feature_scope
        if consent_token is not None:
            self.consent_token = consent_token
        if state is not None:
            self.state = state
        if authorized_at is not None:
            self.authorized_at = authorized_at
        if institution_consent_id is not None:
            self.institution_consent_id = institution_consent_id
        if charges is not None:
            self.charges = charges
        if exchange_rate_information is not None:
            self.exchange_rate_information = exchange_rate_information
        if authorisation_url is not None:
            self.authorisation_url = authorisation_url
        if qr_code_url is not None:
            self.qr_code_url = qr_code_url
        if explanation is not None:
            self.explanation = explanation
        if sca_methods is not None:
            self.sca_methods = sca_methods
        if selected_sca_method is not None:
            self.selected_sca_method = selected_sca_method

    @property
    def id(self):
        """Gets the id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentEmbeddedAuthorisationRequestResponse.


        :param id: The id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The user_uuid of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this PaymentEmbeddedAuthorisationRequestResponse.


        :param user_uuid: The user_uuid of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def application_user_id(self):
        """Gets the application_user_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The application_user_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_user_id

    @application_user_id.setter
    def application_user_id(self, application_user_id):
        """Sets the application_user_id of this PaymentEmbeddedAuthorisationRequestResponse.


        :param application_user_id: The application_user_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._application_user_id = application_user_id

    @property
    def reference_id(self):
        """Gets the reference_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The reference_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this PaymentEmbeddedAuthorisationRequestResponse.


        :param reference_id: The reference_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def institution_id(self):
        """Gets the institution_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The institution_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this PaymentEmbeddedAuthorisationRequestResponse.


        :param institution_id: The institution_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def status(self):
        """Gets the status of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The status of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: AuthorisationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentEmbeddedAuthorisationRequestResponse.


        :param status: The status of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: AuthorisationStatus
        """

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The created_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PaymentEmbeddedAuthorisationRequestResponse.


        :param created_at: The created_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def transaction_from(self):
        """Gets the transaction_from of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The transaction_from of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_from

    @transaction_from.setter
    def transaction_from(self, transaction_from):
        """Sets the transaction_from of this PaymentEmbeddedAuthorisationRequestResponse.


        :param transaction_from: The transaction_from of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._transaction_from = transaction_from

    @property
    def transaction_to(self):
        """Gets the transaction_to of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The transaction_to of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_to

    @transaction_to.setter
    def transaction_to(self, transaction_to):
        """Sets the transaction_to of this PaymentEmbeddedAuthorisationRequestResponse.


        :param transaction_to: The transaction_to of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._transaction_to = transaction_to

    @property
    def expires_at(self):
        """Gets the expires_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The expires_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this PaymentEmbeddedAuthorisationRequestResponse.


        :param expires_at: The expires_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def time_to_expire_in_millis(self):
        """Gets the time_to_expire_in_millis of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The time_to_expire_in_millis of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: int
        """
        return self._time_to_expire_in_millis

    @time_to_expire_in_millis.setter
    def time_to_expire_in_millis(self, time_to_expire_in_millis):
        """Sets the time_to_expire_in_millis of this PaymentEmbeddedAuthorisationRequestResponse.


        :param time_to_expire_in_millis: The time_to_expire_in_millis of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: int
        """

        self._time_to_expire_in_millis = time_to_expire_in_millis

    @property
    def time_to_expire(self):
        """Gets the time_to_expire of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The time_to_expire of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._time_to_expire

    @time_to_expire.setter
    def time_to_expire(self, time_to_expire):
        """Sets the time_to_expire of this PaymentEmbeddedAuthorisationRequestResponse.


        :param time_to_expire: The time_to_expire of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._time_to_expire = time_to_expire

    @property
    def feature_scope(self):
        """Gets the feature_scope of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The feature_scope of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: list[FeatureEnum]
        """
        return self._feature_scope

    @feature_scope.setter
    def feature_scope(self, feature_scope):
        """Sets the feature_scope of this PaymentEmbeddedAuthorisationRequestResponse.


        :param feature_scope: The feature_scope of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: list[FeatureEnum]
        """

        self._feature_scope = feature_scope

    @property
    def consent_token(self):
        """Gets the consent_token of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The consent_token of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._consent_token

    @consent_token.setter
    def consent_token(self, consent_token):
        """Sets the consent_token of this PaymentEmbeddedAuthorisationRequestResponse.


        :param consent_token: The consent_token of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._consent_token = consent_token

    @property
    def state(self):
        """Gets the state of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The state of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentEmbeddedAuthorisationRequestResponse.


        :param state: The state of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def authorized_at(self):
        """Gets the authorized_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The authorized_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._authorized_at

    @authorized_at.setter
    def authorized_at(self, authorized_at):
        """Sets the authorized_at of this PaymentEmbeddedAuthorisationRequestResponse.


        :param authorized_at: The authorized_at of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._authorized_at = authorized_at

    @property
    def institution_consent_id(self):
        """Gets the institution_consent_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The institution_consent_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._institution_consent_id

    @institution_consent_id.setter
    def institution_consent_id(self, institution_consent_id):
        """Sets the institution_consent_id of this PaymentEmbeddedAuthorisationRequestResponse.


        :param institution_consent_id: The institution_consent_id of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._institution_consent_id = institution_consent_id

    @property
    def charges(self):
        """Gets the charges of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The charges of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: list[PaymentChargeDetails]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this PaymentEmbeddedAuthorisationRequestResponse.


        :param charges: The charges of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: list[PaymentChargeDetails]
        """

        self._charges = charges

    @property
    def exchange_rate_information(self):
        """Gets the exchange_rate_information of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The exchange_rate_information of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: ExchangeRateInformationResponse
        """
        return self._exchange_rate_information

    @exchange_rate_information.setter
    def exchange_rate_information(self, exchange_rate_information):
        """Sets the exchange_rate_information of this PaymentEmbeddedAuthorisationRequestResponse.


        :param exchange_rate_information: The exchange_rate_information of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: ExchangeRateInformationResponse
        """

        self._exchange_rate_information = exchange_rate_information

    @property
    def authorisation_url(self):
        """Gets the authorisation_url of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The authorisation_url of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_url

    @authorisation_url.setter
    def authorisation_url(self, authorisation_url):
        """Sets the authorisation_url of this PaymentEmbeddedAuthorisationRequestResponse.


        :param authorisation_url: The authorisation_url of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._authorisation_url = authorisation_url

    @property
    def qr_code_url(self):
        """Gets the qr_code_url of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The qr_code_url of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, qr_code_url):
        """Sets the qr_code_url of this PaymentEmbeddedAuthorisationRequestResponse.


        :param qr_code_url: The qr_code_url of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._qr_code_url = qr_code_url

    @property
    def explanation(self):
        """Gets the explanation of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The explanation of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this PaymentEmbeddedAuthorisationRequestResponse.


        :param explanation: The explanation of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._explanation = explanation

    @property
    def sca_methods(self):
        """Gets the sca_methods of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The sca_methods of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: list[ScaMethod]
        """
        return self._sca_methods

    @sca_methods.setter
    def sca_methods(self, sca_methods):
        """Sets the sca_methods of this PaymentEmbeddedAuthorisationRequestResponse.


        :param sca_methods: The sca_methods of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: list[ScaMethod]
        """

        self._sca_methods = sca_methods

    @property
    def selected_sca_method(self):
        """Gets the selected_sca_method of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501


        :return: The selected_sca_method of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :rtype: ScaMethod
        """
        return self._selected_sca_method

    @selected_sca_method.setter
    def selected_sca_method(self, selected_sca_method):
        """Sets the selected_sca_method of this PaymentEmbeddedAuthorisationRequestResponse.


        :param selected_sca_method: The selected_sca_method of this PaymentEmbeddedAuthorisationRequestResponse.  # noqa: E501
        :type: ScaMethod
        """

        self._selected_sca_method = selected_sca_method

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
        if not isinstance(other, PaymentEmbeddedAuthorisationRequestResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentEmbeddedAuthorisationRequestResponse):
            return True

        return self.to_dict() != other.to_dict()
