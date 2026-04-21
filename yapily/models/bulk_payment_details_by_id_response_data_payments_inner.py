import json
import pprint

from pydantic import BaseModel, ConfigDict, StrictStr


class BulkPaymentDetailsByIdResponseDataPaymentsInner(BaseModel):
    """
    BulkPaymentDetailsByIdResponseDataPaymentsInner
    """

    reference: StrictStr | None = None
    status: StrictStr | None = None
    __properties = ["reference", "status"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "BulkPaymentDetailsByIdResponseDataPaymentsInner":
        """Create an instance of BulkPaymentDetailsByIdResponseDataPaymentsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "BulkPaymentDetailsByIdResponseDataPaymentsInner":
        """Create an instance of BulkPaymentDetailsByIdResponseDataPaymentsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BulkPaymentDetailsByIdResponseDataPaymentsInner.parse_obj(obj)

        return BulkPaymentDetailsByIdResponseDataPaymentsInner.parse_obj(
            {"reference": obj.get("reference"), "status": obj.get("status")}
        )
