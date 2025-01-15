# ApiListOfApplicationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ApplicationResponseListMeta**](ApplicationResponseListMeta.md) |  | [optional] 
**data** | [**List[ApplicationResponse]**](ApplicationResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_list_of_application_response import ApiListOfApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListOfApplicationResponse from a JSON string
api_list_of_application_response_instance = ApiListOfApplicationResponse.from_json(json)
# print the JSON string representation of the object
print ApiListOfApplicationResponse.to_json()

# convert the object into a dict
api_list_of_application_response_dict = api_list_of_application_response_instance.to_dict()
# create an instance of ApiListOfApplicationResponse from a dict
api_list_of_application_response_from_dict = ApiListOfApplicationResponse.from_dict(api_list_of_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


