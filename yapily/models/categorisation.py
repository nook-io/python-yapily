import json
import pprint
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StrictStr


class Categorisation(BaseModel):
    """
    Income and Expense categorisation that the Yapily categorisation engine has determined for the transaction.  # noqa: E501
    """

    categories: Annotated[list[StrictStr], Field()] | None = None
    source: StrictStr | None = None
    __properties = ["categories", "source"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "Categorisation":
        """Create an instance of Categorisation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> "Categorisation":
        """Create an instance of Categorisation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Categorisation.parse_obj(obj)

        return Categorisation.parse_obj({"categories": obj.get("categories"), "source": obj.get("source")})
