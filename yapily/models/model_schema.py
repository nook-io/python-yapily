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
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional, Union
from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
    conint,
    conlist,
)
from yapily.models.schema_type import SchemaType
from yapily.models.schema_x_yapily_annotations import SchemaXYapilyAnnotations
from yapily.models.schema_x_yapily_validations import SchemaXYapilyValidations


class ModelSchema(BaseModel):
    """
    ModelSchema
    """

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
    max_items: Optional[conint(strict=True, ge=0)] = Field(
        default=None, alias="maxItems"
    )
    min_items: Optional[conint(strict=True, ge=0)] = Field(
        default=None, alias="minItems"
    )
    unique_items: Optional[StrictBool] = Field(default=None, alias="uniqueItems")
    required: Optional[conlist(StrictStr, min_items=1, unique_items=True)] = None
    enum: Optional[conlist(Any, min_items=1)] = None
    type: Optional[SchemaType] = None
    contains: Optional[ModelSchema] = None
    var_not: Optional[ModelSchema] = Field(default=None, alias="not")
    var_if: Optional[ModelSchema] = Field(default=None, alias="if")
    then: Optional[ModelSchema] = None
    var_else: Optional[ModelSchema] = Field(default=None, alias="else")
    all_of: Optional[conlist(ModelSchema)] = Field(default=None, alias="allOf")
    one_of: Optional[conlist(ModelSchema)] = Field(default=None, alias="oneOf")
    any_of: Optional[conlist(ModelSchema)] = Field(default=None, alias="anyOf")
    items: Optional[ModelSchema] = None
    properties: Optional[Dict[str, ModelSchema]] = None
    description: Optional[StrictStr] = None
    format: Optional[StrictStr] = None
    default: Optional[Any] = None
    example: Optional[Any] = None
    dependent_required: Optional[Dict[str, conlist(StrictStr, unique_items=True)]] = (
        Field(
            default=None,
            alias="dependentRequired",
            description="dependentRequired keyword is used to satisfy dependency between fields",
        )
    )
    defs: Optional[Dict[str, ModelSchema]] = Field(default=None, alias="$defs")
    ref: Optional[StrictStr] = Field(default=None, alias="$ref")
    x_yapily_annotations: Optional[SchemaXYapilyAnnotations] = Field(
        default=None, alias="x-yapily-annotations"
    )
    x_yapily_validations: Optional[SchemaXYapilyValidations] = Field(
        default=None, alias="x-yapily-validations"
    )
    __properties = [
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

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ModelSchema:
        """Create an instance of ModelSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of contains
        if self.contains:
            _dict["contains"] = self.contains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_not
        if self.var_not:
            _dict["not"] = self.var_not.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_if
        if self.var_if:
            _dict["if"] = self.var_if.to_dict()
        # override the default output from pydantic by calling `to_dict()` of then
        if self.then:
            _dict["then"] = self.then.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_else
        if self.var_else:
            _dict["else"] = self.var_else.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in all_of (list)
        _items = []
        if self.all_of:
            for _item in self.all_of:
                if _item:
                    _items.append(_item.to_dict())
            _dict["allOf"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in one_of (list)
        _items = []
        if self.one_of:
            for _item in self.one_of:
                if _item:
                    _items.append(_item.to_dict())
            _dict["oneOf"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in any_of (list)
        _items = []
        if self.any_of:
            for _item in self.any_of:
                if _item:
                    _items.append(_item.to_dict())
            _dict["anyOf"] = _items
        # override the default output from pydantic by calling `to_dict()` of items
        if self.items:
            _dict["items"] = self.items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict["properties"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in defs (dict)
        _field_dict = {}
        if self.defs:
            for _key in self.defs:
                if self.defs[_key]:
                    _field_dict[_key] = self.defs[_key].to_dict()
            _dict["$defs"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of x_yapily_annotations
        if self.x_yapily_annotations:
            _dict["x-yapily-annotations"] = self.x_yapily_annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of x_yapily_validations
        if self.x_yapily_validations:
            _dict["x-yapily-validations"] = self.x_yapily_validations.to_dict()
        # set to None if default (nullable) is None
        # and __fields_set__ contains the field
        if self.default is None and "default" in self.__fields_set__:
            _dict["default"] = None

        # set to None if example (nullable) is None
        # and __fields_set__ contains the field
        if self.example is None and "example" in self.__fields_set__:
            _dict["example"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelSchema:
        """Create an instance of ModelSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelSchema.parse_obj(obj)

        _obj = ModelSchema.parse_obj(
            {
                "title": obj.get("title"),
                "maximum": obj.get("maximum"),
                "exclusive_maximum": obj.get("exclusiveMaximum"),
                "minimum": obj.get("minimum"),
                "exclusive_minimum": obj.get("exclusiveMinimum"),
                "pattern": obj.get("pattern"),
                "max_items": obj.get("maxItems"),
                "min_items": obj.get("minItems"),
                "unique_items": obj.get("uniqueItems"),
                "required": obj.get("required"),
                "enum": obj.get("enum"),
                "type": obj.get("type"),
                "contains": ModelSchema.from_dict(obj.get("contains"))
                if obj.get("contains") is not None
                else None,
                "var_not": ModelSchema.from_dict(obj.get("not"))
                if obj.get("not") is not None
                else None,
                "var_if": ModelSchema.from_dict(obj.get("if"))
                if obj.get("if") is not None
                else None,
                "then": ModelSchema.from_dict(obj.get("then"))
                if obj.get("then") is not None
                else None,
                "var_else": ModelSchema.from_dict(obj.get("else"))
                if obj.get("else") is not None
                else None,
                "all_of": [ModelSchema.from_dict(_item) for _item in obj.get("allOf")]
                if obj.get("allOf") is not None
                else None,
                "one_of": [ModelSchema.from_dict(_item) for _item in obj.get("oneOf")]
                if obj.get("oneOf") is not None
                else None,
                "any_of": [ModelSchema.from_dict(_item) for _item in obj.get("anyOf")]
                if obj.get("anyOf") is not None
                else None,
                "items": ModelSchema.from_dict(obj.get("items"))
                if obj.get("items") is not None
                else None,
                "properties": dict(
                    (_k, ModelSchema.from_dict(_v))
                    for _k, _v in obj.get("properties").items()
                )
                if obj.get("properties") is not None
                else None,
                "description": obj.get("description"),
                "format": obj.get("format"),
                "default": obj.get("default"),
                "example": obj.get("example"),
                "dependent_required": obj.get("dependentRequired"),
                "defs": dict(
                    (_k, ModelSchema.from_dict(_v))
                    for _k, _v in obj.get("$defs").items()
                )
                if obj.get("$defs") is not None
                else None,
                "ref": obj.get("$ref"),
                "x_yapily_annotations": SchemaXYapilyAnnotations.from_dict(
                    obj.get("x-yapily-annotations")
                )
                if obj.get("x-yapily-annotations") is not None
                else None,
                "x_yapily_validations": SchemaXYapilyValidations.from_dict(
                    obj.get("x-yapily-validations")
                )
                if obj.get("x-yapily-validations") is not None
                else None,
            }
        )
        return _obj


ModelSchema.update_forward_refs()
