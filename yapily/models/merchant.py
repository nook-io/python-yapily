import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class Merchant(BaseModel):
    """
    Details of the merchant involved in the transaction.  # noqa: E501
    """

    merchant_name: Annotated[
        StrictStr | None,
        Field(alias="merchantName", description="The name of the merchant involved in the transaction."),
    ] = None
    merchant_category_code: Annotated[
        StrictStr | None,
        Field(
            alias="merchantCategoryCode",
            description="Defines the underlying services and goods that the merchant provides. Specified as a 3-letter ISO 18245 code ",
        ),
    ] = None
    __properties = ["merchantName", "merchantCategoryCode"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Merchant":
        """Create an instance of Merchant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "Merchant":
        """Create an instance of Merchant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Merchant.model_validate(obj)

        return Merchant.model_validate(
            {"merchant_name": obj.get("merchantName"), "merchant_category_code": obj.get("merchantCategoryCode")}
        )
