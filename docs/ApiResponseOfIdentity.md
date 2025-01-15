# ApiResponseOfIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**Identity**](Identity.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_identity import ApiResponseOfIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfIdentity from a JSON string
api_response_of_identity_instance = ApiResponseOfIdentity.from_json(json)
# print the JSON string representation of the object
print(ApiResponseOfIdentity.to_json())

# convert the object into a dict
api_response_of_identity_dict = api_response_of_identity_instance.to_dict()
# create an instance of ApiResponseOfIdentity from a dict
api_response_of_identity_from_dict = ApiResponseOfIdentity.from_dict(api_response_of_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


