# ApiErrorResponseV2

API Error Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ApiErrorResponseV2Error**](ApiErrorResponseV2Error.md) |  | [optional] 

## Example

```python
from yapily.models.api_error_response_v2 import ApiErrorResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorResponseV2 from a JSON string
api_error_response_v2_instance = ApiErrorResponseV2.from_json(json)
# print the JSON string representation of the object
print(ApiErrorResponseV2.to_json())

# convert the object into a dict
api_error_response_v2_dict = api_error_response_v2_instance.to_dict()
# create an instance of ApiErrorResponseV2 from a dict
api_error_response_v2_from_dict = ApiErrorResponseV2.from_dict(api_error_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


