# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 7.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AccountType(str, Enum):
    """
    The type of account e.g. (Credit Card, Savings).
    """

    """
    allowed enum values
    """
    CASH_TRADING = 'CASH_TRADING'
    CASH_INCOME = 'CASH_INCOME'
    CASH_PAYMENT = 'CASH_PAYMENT'
    CHARGE_CARD = 'CHARGE_CARD'
    CHARGES = 'CHARGES'
    COMMISSION = 'COMMISSION'
    CREDIT_CARD = 'CREDIT_CARD'
    CURRENT = 'CURRENT'
    E_MONEY = 'E_MONEY'
    LIMITED_LIQUIDITY_SAVINGS_ACCOUNT = 'LIMITED_LIQUIDITY_SAVINGS_ACCOUNT'
    LOAN = 'LOAN'
    MARGINAL_LENDING = 'MARGINAL_LENDING'
    MONEY_MARKET = 'MONEY_MARKET'
    MORTGAGE = 'MORTGAGE'
    NON_RESIDENT_EXTERNAL = 'NON_RESIDENT_EXTERNAL'
    OTHER = 'OTHER'
    OVERDRAFT = 'OVERDRAFT'
    OVERNIGHT_DEPOSIT = 'OVERNIGHT_DEPOSIT'
    PREPAID_CARD = 'PREPAID_CARD'
    SALARY = 'SALARY'
    SAVINGS = 'SAVINGS'
    SETTLEMENT = 'SETTLEMENT'
    TAX = 'TAX'
    UNKNOWN = 'UNKNOWN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccountType from a JSON string"""
        return cls(json.loads(json_str))


