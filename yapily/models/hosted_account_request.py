from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from yapily.models.feature_enum import FeatureEnum
from typing import Set
from typing_extensions import Self


class HostedAccountRequest(BaseModel):
    transaction_from: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Specifies the earliest date of the transaction records to be returned.<br><br> You must supply this field to retrieve transactions older than 90 days for banks accessed via the the [CBI Globe Gateway](https://docs.yapily.com/pages/data/financial-data-resources/data-restrictions/#cbi-globe-gateway).",
        alias="transactionFrom",
    )
    transaction_to: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Specifies the latest date of the transaction records to be returned.",
        alias="transactionTo",
    )
    expires_at: Optional[datetime] = Field(
        default=None,
        description="__Optional__. Used to set a hard date for when the user's associated `Consent` will expire.<br><br>**Note**: If this supported by the bank, specifying this is property is opting out of having a long-lived consent that can be perpetually re-authorised by the user. This will add an `expiresAt` field on the `Consent` object which will render it unusable after this date.<br><br>**Note**: This is not supported by every `Institution`. In such case, the request will not fail but the property will be ignored and the created `Consent` will not have an expiry date.",
        alias="expiresAt",
    )
    feature_scope: Optional[List[FeatureEnum]] = Field(
        default=None,
        description="__Optional__. Used to granularly specify the set of features that the user will give their consent for when requesting access to their account information. Depending on the `Institution`, this may also populate a consent screen which list these scopes before the user authorises.<br><br>This endpoint accepts allow all [Financial Data Features](/guides/financial-data/features/#feature-list) that the `Institution` supports.To find out which scopes an `Institution` supports, check [GET Institution](./#get-institution).",
        alias="featureScope",
    )
    __properties: ClassVar[List[str]] = [
        "transactionFrom",
        "transactionTo",
        "expiresAt",
        "featureScope",
    ]
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "transactionFrom": obj.get("transactionFrom"),
                "transactionTo": obj.get("transactionTo"),
                "expiresAt": obj.get("expiresAt"),
                "featureScope": obj.get("featureScope"),
            }
        )
        return _obj
