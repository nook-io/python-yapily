# CategoryStructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | webhook event category name | [optional] 
**description** | **str** | description of the webhook event category | [optional] 

## Example

```python
from yapily.models.category_structure import CategoryStructure

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryStructure from a JSON string
category_structure_instance = CategoryStructure.from_json(json)
# print the JSON string representation of the object
print(CategoryStructure.to_json())

# convert the object into a dict
category_structure_dict = category_structure_instance.to_dict()
# create an instance of CategoryStructure from a dict
category_structure_from_dict = CategoryStructure.from_dict(category_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


