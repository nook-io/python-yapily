import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr

from yapily.models.bulk_payment_details_by_id_response_data_payments_inner import (
    BulkPaymentDetailsByIdResponseDataPaymentsInner,
)


class BulkPaymentDetailsByIdResponseData(BaseModel):
    """
    BulkPaymentDetailsByIdResponseData
    """

    id: StrictStr | None = None
    consent_id: Annotated[StrictStr | None, Field(alias="consentId")] = None
    created_at: Annotated[StrictStr | None, Field(alias="createdAt")] = None
    payments: Annotated[list[BulkPaymentDetailsByIdResponseDataPaymentsInner], Field()] | None = None
    __properties = ["id", "consentId", "createdAt", "payments"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "BulkPaymentDetailsByIdResponseData":
        """Create an instance of BulkPaymentDetailsByIdResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item in self.payments:
                if _item:
                    _items.append(_item.to_dict())
            _dict["payments"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> "BulkPaymentDetailsByIdResponseData":
        """Create an instance of BulkPaymentDetailsByIdResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BulkPaymentDetailsByIdResponseData.model_validate(obj)

        return BulkPaymentDetailsByIdResponseData.model_validate(
            {
                "id": obj.get("id"),
                "consent_id": obj.get("consentId"),
                "created_at": obj.get("createdAt"),
                "payments": [
                    BulkPaymentDetailsByIdResponseDataPaymentsInner.from_dict(_item) for _item in obj.get("payments")
                ]
                if obj.get("payments") is not None
                else None,
            }
        )
