# ModelSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**maximum** | **float** |  | [optional] 
**exclusive_maximum** | **float** |  | [optional] 
**minimum** | **float** |  | [optional] 
**exclusive_minimum** | **float** |  | [optional] 
**pattern** | **str** |  | [optional] 
**max_items** | **int** |  | [optional] 
**min_items** | **int** |  | [optional] 
**unique_items** | **bool** |  | [optional] 
**required** | **List[str]** |  | [optional] 
**enum** | **List[object]** |  | [optional] 
**type** | [**SchemaType**](SchemaType.md) |  | [optional] 
**contains** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**var_not** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**var_if** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**then** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**var_else** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**all_of** | [**List[ModelSchema]**](ModelSchema.md) |  | [optional] 
**one_of** | [**List[ModelSchema]**](ModelSchema.md) |  | [optional] 
**any_of** | [**List[ModelSchema]**](ModelSchema.md) |  | [optional] 
**items** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**properties** | [**Dict[str, ModelSchema]**](ModelSchema.md) |  | [optional] 
**description** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**default** | **object** |  | [optional] 
**example** | **object** |  | [optional] 
**dependent_required** | **Dict[str, List[str]]** | dependentRequired keyword is used to satisfy dependency between fields | [optional] 
**defs** | [**Dict[str, ModelSchema]**](ModelSchema.md) |  | [optional] 
**ref** | **str** |  | [optional] 
**x_yapily_annotations** | [**SchemaXYapilyAnnotations**](SchemaXYapilyAnnotations.md) |  | [optional] 
**x_yapily_validations** | [**SchemaXYapilyValidations**](SchemaXYapilyValidations.md) |  | [optional] 

## Example

```python
from yapily.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print ModelSchema.to_json()

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_form_dict = model_schema.from_dict(model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


