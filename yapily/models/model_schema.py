from __future__ import annotations
import pprint
import json
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from yapily.models.schema_type import SchemaType
from yapily.models.schema_x_yapily_annotations import SchemaXYapilyAnnotations
from yapily.models.schema_x_yapily_validations import SchemaXYapilyValidations
from typing import Set
from typing_extensions import Self


class ModelSchema(BaseModel):
    title: Optional[StrictStr] = None
    maximum: Optional[Union[StrictFloat, StrictInt]] = None
    exclusive_maximum: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="exclusiveMaximum"
    )
    minimum: Optional[Union[StrictFloat, StrictInt]] = None
    exclusive_minimum: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="exclusiveMinimum"
    )
    pattern: Optional[StrictStr] = None
    max_items: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, alias="maxItems"
    )
    min_items: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, alias="minItems"
    )
    unique_items: Optional[StrictBool] = Field(default=None, alias="uniqueItems")
    required: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = None
    enum: Optional[Annotated[List[Any], Field(min_length=1)]] = None
    type: Optional[SchemaType] = None
    contains: Optional[ModelSchema] = None
    var_not: Optional[ModelSchema] = Field(default=None, alias="not")
    var_if: Optional[ModelSchema] = Field(default=None, alias="if")
    then: Optional[ModelSchema] = None
    var_else: Optional[ModelSchema] = Field(default=None, alias="else")
    all_of: Optional[List[ModelSchema]] = Field(default=None, alias="allOf")
    one_of: Optional[List[ModelSchema]] = Field(default=None, alias="oneOf")
    any_of: Optional[List[ModelSchema]] = Field(default=None, alias="anyOf")
    items: Optional[ModelSchema] = None
    properties: Optional[Dict[str, ModelSchema]] = None
    description: Optional[StrictStr] = None
    format: Optional[StrictStr] = None
    default: Optional[Any] = None
    example: Optional[Any] = None
    dependent_required: Optional[Dict[str, List[StrictStr]]] = Field(
        default=None,
        description="dependentRequired keyword is used to satisfy dependency between fields",
        alias="dependentRequired",
    )
    defs: Optional[Dict[str, ModelSchema]] = Field(default=None, alias="$defs")
    ref: Optional[StrictStr] = Field(default=None, alias="$ref")
    x_yapily_annotations: Optional[SchemaXYapilyAnnotations] = Field(
        default=None, alias="x-yapily-annotations"
    )
    x_yapily_validations: Optional[SchemaXYapilyValidations] = Field(
        default=None, alias="x-yapily-validations"
    )
    __properties: ClassVar[List[str]] = [
        "title",
        "maximum",
        "exclusiveMaximum",
        "minimum",
        "exclusiveMinimum",
        "pattern",
        "maxItems",
        "minItems",
        "uniqueItems",
        "required",
        "enum",
        "type",
        "contains",
        "not",
        "if",
        "then",
        "else",
        "allOf",
        "oneOf",
        "anyOf",
        "items",
        "properties",
        "description",
        "format",
        "default",
        "example",
        "dependentRequired",
        "$defs",
        "$ref",
        "x-yapily-annotations",
        "x-yapily-validations",
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
        if self.contains:
            _dict["contains"] = self.contains.to_dict()
        if self.var_not:
            _dict["not"] = self.var_not.to_dict()
        if self.var_if:
            _dict["if"] = self.var_if.to_dict()
        if self.then:
            _dict["then"] = self.then.to_dict()
        if self.var_else:
            _dict["else"] = self.var_else.to_dict()
        _items = []
        if self.all_of:
            for _item_all_of in self.all_of:
                if _item_all_of:
                    _items.append(_item_all_of.to_dict())
            _dict["allOf"] = _items
        _items = []
        if self.one_of:
            for _item_one_of in self.one_of:
                if _item_one_of:
                    _items.append(_item_one_of.to_dict())
            _dict["oneOf"] = _items
        _items = []
        if self.any_of:
            for _item_any_of in self.any_of:
                if _item_any_of:
                    _items.append(_item_any_of.to_dict())
            _dict["anyOf"] = _items
        if self.items:
            _dict["items"] = self.items.to_dict()
        _field_dict = {}
        if self.properties:
            for _key_properties in self.properties:
                if self.properties[_key_properties]:
                    _field_dict[_key_properties] = self.properties[
                        _key_properties
                    ].to_dict()
            _dict["properties"] = _field_dict
        _field_dict = {}
        if self.defs:
            for _key_defs in self.defs:
                if self.defs[_key_defs]:
                    _field_dict[_key_defs] = self.defs[_key_defs].to_dict()
            _dict["$defs"] = _field_dict
        if self.x_yapily_annotations:
            _dict["x-yapily-annotations"] = self.x_yapily_annotations.to_dict()
        if self.x_yapily_validations:
            _dict["x-yapily-validations"] = self.x_yapily_validations.to_dict()
        if self.default is None and "default" in self.model_fields_set:
            _dict["default"] = None
        if self.example is None and "example" in self.model_fields_set:
            _dict["example"] = None
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "title": obj.get("title"),
                "maximum": obj.get("maximum"),
                "exclusiveMaximum": obj.get("exclusiveMaximum"),
                "minimum": obj.get("minimum"),
                "exclusiveMinimum": obj.get("exclusiveMinimum"),
                "pattern": obj.get("pattern"),
                "maxItems": obj.get("maxItems"),
                "minItems": obj.get("minItems"),
                "uniqueItems": obj.get("uniqueItems"),
                "required": obj.get("required"),
                "enum": obj.get("enum"),
                "type": obj.get("type"),
                "contains": ModelSchema.from_dict(obj["contains"])
                if obj.get("contains") is not None
                else None,
                "not": ModelSchema.from_dict(obj["not"])
                if obj.get("not") is not None
                else None,
                "if": ModelSchema.from_dict(obj["if"])
                if obj.get("if") is not None
                else None,
                "then": ModelSchema.from_dict(obj["then"])
                if obj.get("then") is not None
                else None,
                "else": ModelSchema.from_dict(obj["else"])
                if obj.get("else") is not None
                else None,
                "allOf": [ModelSchema.from_dict(_item) for _item in obj["allOf"]]
                if obj.get("allOf") is not None
                else None,
                "oneOf": [ModelSchema.from_dict(_item) for _item in obj["oneOf"]]
                if obj.get("oneOf") is not None
                else None,
                "anyOf": [ModelSchema.from_dict(_item) for _item in obj["anyOf"]]
                if obj.get("anyOf") is not None
                else None,
                "items": ModelSchema.from_dict(obj["items"])
                if obj.get("items") is not None
                else None,
                "properties": dict(
                    (_k, ModelSchema.from_dict(_v))
                    for _k, _v in obj["properties"].items()
                )
                if obj.get("properties") is not None
                else None,
                "description": obj.get("description"),
                "format": obj.get("format"),
                "default": obj.get("default"),
                "example": obj.get("example"),
                "dependentRequired": obj.get("dependentRequired"),
                "$defs": dict(
                    (_k, ModelSchema.from_dict(_v)) for _k, _v in obj["$defs"].items()
                )
                if obj.get("$defs") is not None
                else None,
                "$ref": obj.get("$ref"),
                "x-yapily-annotations": SchemaXYapilyAnnotations.from_dict(
                    obj["x-yapily-annotations"]
                )
                if obj.get("x-yapily-annotations") is not None
                else None,
                "x-yapily-validations": SchemaXYapilyValidations.from_dict(
                    obj["x-yapily-validations"]
                )
                if obj.get("x-yapily-validations") is not None
                else None,
            }
        )
        return _obj


ModelSchema.model_rebuild(raise_errors=False)
