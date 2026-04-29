import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class EnrichmentMerchant(BaseModel):
    """
    Details of the merchant, identified by Yapily data services.  # noqa: E501
    """

    merchant_name: Annotated[
        StrictStr | None,
        Field(
            alias="merchantName",
            description="The name of the indivdual merchant involved in the transaction e.g. (TESCO Petrol).",
        ),
    ] = None
    parent_group: Annotated[
        StrictStr | None,
        Field(alias="parentGroup", description="The parent organisation that the merchant belongs to e.g. (TESCO)."),
    ] = None
    __properties = ["merchantName", "parentGroup"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "EnrichmentMerchant":
        """Create an instance of EnrichmentMerchant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "EnrichmentMerchant":
        """Create an instance of EnrichmentMerchant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnrichmentMerchant.model_validate(obj)

        return EnrichmentMerchant.model_validate(
            {"merchant_name": obj.get("merchantName"), "parent_group": obj.get("parentGroup")}
        )
