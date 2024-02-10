# ConsentDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**delete_status** | [**DeleteStatusEnum**](DeleteStatusEnum.md) |  | [optional] 
**institution_id** | **str** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 

## Example

```python
from yapily.models.consent_delete_response import ConsentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentDeleteResponse from a JSON string
consent_delete_response_instance = ConsentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print ConsentDeleteResponse.to_json()

# convert the object into a dict
consent_delete_response_dict = consent_delete_response_instance.to_dict()
# create an instance of ConsentDeleteResponse from a dict
consent_delete_response_form_dict = consent_delete_response.from_dict(consent_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


