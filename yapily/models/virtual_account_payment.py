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


class VirtualAccountPayment(object):
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
        'created_date_time': 'datetime',
        'payment_date': 'date',
        'type': 'str',
        'payment_scheme': 'str',
        'amount': 'Amount',
        'reference': 'str',
        'status': 'str',
        'source': 'VirtualAccountPaymentSource',
        'destination': 'VirtualAccountPaymentDestination',
        'original_payment_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_date_time': 'createdDateTime',
        'payment_date': 'paymentDate',
        'type': 'type',
        'payment_scheme': 'paymentScheme',
        'amount': 'amount',
        'reference': 'reference',
        'status': 'status',
        'source': 'source',
        'destination': 'destination',
        'original_payment_id': 'originalPaymentId'
    }

    def __init__(self, id=None, created_date_time=None, payment_date=None, type=None, payment_scheme=None, amount=None, reference=None, status=None, source=None, destination=None, original_payment_id=None, local_vars_configuration=None):  # noqa: E501
        """VirtualAccountPayment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_date_time = None
        self._payment_date = None
        self._type = None
        self._payment_scheme = None
        self._amount = None
        self._reference = None
        self._status = None
        self._source = None
        self._destination = None
        self._original_payment_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if payment_date is not None:
            self.payment_date = payment_date
        if type is not None:
            self.type = type
        if payment_scheme is not None:
            self.payment_scheme = payment_scheme
        if amount is not None:
            self.amount = amount
        if reference is not None:
            self.reference = reference
        if status is not None:
            self.status = status
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination
        if original_payment_id is not None:
            self.original_payment_id = original_payment_id

    @property
    def id(self):
        """Gets the id of this VirtualAccountPayment.  # noqa: E501

        Unique id of the payment  # noqa: E501

        :return: The id of this VirtualAccountPayment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualAccountPayment.

        Unique id of the payment  # noqa: E501

        :param id: The id of this VirtualAccountPayment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_date_time(self):
        """Gets the created_date_time of this VirtualAccountPayment.  # noqa: E501

        Date and time that the payment was created  # noqa: E501

        :return: The created_date_time of this VirtualAccountPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this VirtualAccountPayment.

        Date and time that the payment was created  # noqa: E501

        :param created_date_time: The created_date_time of this VirtualAccountPayment.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

    @property
    def payment_date(self):
        """Gets the payment_date of this VirtualAccountPayment.  # noqa: E501

        Date on which the payment instruction will be executed, that may be in the future  # noqa: E501

        :return: The payment_date of this VirtualAccountPayment.  # noqa: E501
        :rtype: date
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this VirtualAccountPayment.

        Date on which the payment instruction will be executed, that may be in the future  # noqa: E501

        :param payment_date: The payment_date of this VirtualAccountPayment.  # noqa: E501
        :type: date
        """

        self._payment_date = payment_date

    @property
    def type(self):
        """Gets the type of this VirtualAccountPayment.  # noqa: E501

        Type of payment. One of PAY_IN, PAY_OUT, RETURN_IN or RETURN_OUT  # noqa: E501

        :return: The type of this VirtualAccountPayment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VirtualAccountPayment.

        Type of payment. One of PAY_IN, PAY_OUT, RETURN_IN or RETURN_OUT  # noqa: E501

        :param type: The type of this VirtualAccountPayment.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def payment_scheme(self):
        """Gets the payment_scheme of this VirtualAccountPayment.  # noqa: E501

        Method of settlement to complete the payment. One of: <br> FASTER_PAYMENTS <br> SEPA_CREDIT <br> SEPA_INSTANT <br> SWIFT <br> SWIFT_EXPRESS <br> CHAPS <br> IAT <br> WIRE  # noqa: E501

        :return: The payment_scheme of this VirtualAccountPayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_scheme

    @payment_scheme.setter
    def payment_scheme(self, payment_scheme):
        """Sets the payment_scheme of this VirtualAccountPayment.

        Method of settlement to complete the payment. One of: <br> FASTER_PAYMENTS <br> SEPA_CREDIT <br> SEPA_INSTANT <br> SWIFT <br> SWIFT_EXPRESS <br> CHAPS <br> IAT <br> WIRE  # noqa: E501

        :param payment_scheme: The payment_scheme of this VirtualAccountPayment.  # noqa: E501
        :type: str
        """

        self._payment_scheme = payment_scheme

    @property
    def amount(self):
        """Gets the amount of this VirtualAccountPayment.  # noqa: E501


        :return: The amount of this VirtualAccountPayment.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this VirtualAccountPayment.


        :param amount: The amount of this VirtualAccountPayment.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def reference(self):
        """Gets the reference of this VirtualAccountPayment.  # noqa: E501

        Reference to be associated with the payment. This will be appear on the beneficiary's bank statement  # noqa: E501

        :return: The reference of this VirtualAccountPayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this VirtualAccountPayment.

        Reference to be associated with the payment. This will be appear on the beneficiary's bank statement  # noqa: E501

        :param reference: The reference of this VirtualAccountPayment.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def status(self):
        """Gets the status of this VirtualAccountPayment.  # noqa: E501

        The current state of the transaction <br> INITIATED - The transaction request is acknowledged and will not undergo validation checks <br> PROCESSING - Initial checks succeeded and the transaction request is now being processed <br> COMPLETED - The transaction has been successfully processed (terminal status) <br> FAILED - An failure occured during transaction processing (terminal status)  # noqa: E501

        :return: The status of this VirtualAccountPayment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VirtualAccountPayment.

        The current state of the transaction <br> INITIATED - The transaction request is acknowledged and will not undergo validation checks <br> PROCESSING - Initial checks succeeded and the transaction request is now being processed <br> COMPLETED - The transaction has been successfully processed (terminal status) <br> FAILED - An failure occured during transaction processing (terminal status)  # noqa: E501

        :param status: The status of this VirtualAccountPayment.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def source(self):
        """Gets the source of this VirtualAccountPayment.  # noqa: E501


        :return: The source of this VirtualAccountPayment.  # noqa: E501
        :rtype: VirtualAccountPaymentSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this VirtualAccountPayment.


        :param source: The source of this VirtualAccountPayment.  # noqa: E501
        :type: VirtualAccountPaymentSource
        """

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this VirtualAccountPayment.  # noqa: E501


        :return: The destination of this VirtualAccountPayment.  # noqa: E501
        :rtype: VirtualAccountPaymentDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this VirtualAccountPayment.


        :param destination: The destination of this VirtualAccountPayment.  # noqa: E501
        :type: VirtualAccountPaymentDestination
        """

        self._destination = destination

    @property
    def original_payment_id(self):
        """Gets the original_payment_id of this VirtualAccountPayment.  # noqa: E501

        Unique id of the original payment that was refunded  # noqa: E501

        :return: The original_payment_id of this VirtualAccountPayment.  # noqa: E501
        :rtype: str
        """
        return self._original_payment_id

    @original_payment_id.setter
    def original_payment_id(self, original_payment_id):
        """Sets the original_payment_id of this VirtualAccountPayment.

        Unique id of the original payment that was refunded  # noqa: E501

        :param original_payment_id: The original_payment_id of this VirtualAccountPayment.  # noqa: E501
        :type: str
        """

        self._original_payment_id = original_payment_id

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
        if not isinstance(other, VirtualAccountPayment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualAccountPayment):
            return True

        return self.to_dict() != other.to_dict()
