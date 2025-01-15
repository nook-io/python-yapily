# ApiResponseOfSweepingAuthorisationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**SweepingAuthorisationResponse**](SweepingAuthorisationResponse.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_of_sweeping_authorisation_response import ApiResponseOfSweepingAuthorisationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfSweepingAuthorisationResponse from a JSON string
api_response_of_sweeping_authorisation_response_instance = ApiResponseOfSweepingAuthorisationResponse.from_json(json)
# print the JSON string representation of the object
print(ApiResponseOfSweepingAuthorisationResponse.to_json())

# convert the object into a dict
api_response_of_sweeping_authorisation_response_dict = api_response_of_sweeping_authorisation_response_instance.to_dict()
# create an instance of ApiResponseOfSweepingAuthorisationResponse from a dict
api_response_of_sweeping_authorisation_response_from_dict = ApiResponseOfSweepingAuthorisationResponse.from_dict(api_response_of_sweeping_authorisation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


