# ApiResponseOfApplicationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**ApplicationResponse**](ApplicationResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_of_application_response import ApiResponseOfApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfApplicationResponse from a JSON string
api_response_of_application_response_instance = ApiResponseOfApplicationResponse.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfApplicationResponse.to_json()

# convert the object into a dict
api_response_of_application_response_dict = api_response_of_application_response_instance.to_dict()
# create an instance of ApiResponseOfApplicationResponse from a dict
api_response_of_application_response_from_dict = ApiResponseOfApplicationResponse.from_dict(api_response_of_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


