# Categorisation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from yapily.models.categorisation import Categorisation

# TODO update the JSON string below
json = "{}"
# create an instance of Categorisation from a JSON string
categorisation_instance = Categorisation.from_json(json)
# print the JSON string representation of the object
print Categorisation.to_json()

# convert the object into a dict
categorisation_dict = categorisation_instance.to_dict()
# create an instance of Categorisation from a dict
categorisation_form_dict = categorisation.from_dict(categorisation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


