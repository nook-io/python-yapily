from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AccountType(str, Enum):
    """
    allowed enum values
    """

    CASH_TRADING = "CASH_TRADING"
    CASH_INCOME = "CASH_INCOME"
    CASH_PAYMENT = "CASH_PAYMENT"
    CHARGE_CARD = "CHARGE_CARD"
    CHARGES = "CHARGES"
    COMMISSION = "COMMISSION"
    CREDIT_CARD = "CREDIT_CARD"
    CURRENT = "CURRENT"
    E_MONEY = "E_MONEY"
    LIMITED_LIQUIDITY_SAVINGS_ACCOUNT = "LIMITED_LIQUIDITY_SAVINGS_ACCOUNT"
    LOAN = "LOAN"
    MARGINAL_LENDING = "MARGINAL_LENDING"
    MONEY_MARKET = "MONEY_MARKET"
    MORTGAGE = "MORTGAGE"
    NON_RESIDENT_EXTERNAL = "NON_RESIDENT_EXTERNAL"
    OTHER = "OTHER"
    OVERDRAFT = "OVERDRAFT"
    OVERNIGHT_DEPOSIT = "OVERNIGHT_DEPOSIT"
    PREPAID_CARD = "PREPAID_CARD"
    SALARY = "SALARY"
    SAVINGS = "SAVINGS"
    SETTLEMENT = "SETTLEMENT"
    TAX = "TAX"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(json.loads(json_str))
