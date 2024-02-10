# InstitutionError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**http_status_code** | **int** |  | [optional] 

## Example

```python
from yapily.models.institution_error import InstitutionError

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionError from a JSON string
institution_error_instance = InstitutionError.from_json(json)
# print the JSON string representation of the object
print InstitutionError.to_json()

# convert the object into a dict
institution_error_dict = institution_error_instance.to_dict()
# create an instance of InstitutionError from a dict
institution_error_form_dict = institution_error.from_dict(institution_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


