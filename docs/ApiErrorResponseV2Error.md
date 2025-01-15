# ApiErrorResponseV2Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** | Unique identifier of the request, used by Yapily for support purposes | 
**code** | **int** | Numeric HTTP status code associated with the error | 
**status** | **str** | Textual description of the HTTP status | 
**support_url** | **str** | Link to where further information regarding the error can be found | [optional] 
**source** | **str** | Source of the error. This may be YAPILY, the INSTITUTION, or the USER | [optional] 
**issues** | [**List[ApiErrorResponseV2ErrorIssuesInner]**](ApiErrorResponseV2ErrorIssuesInner.md) | List of issues relating to the error | 

## Example

```python
from yapily.models.api_error_response_v2_error import ApiErrorResponseV2Error

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorResponseV2Error from a JSON string
api_error_response_v2_error_instance = ApiErrorResponseV2Error.from_json(json)
# print the JSON string representation of the object
print(ApiErrorResponseV2Error.to_json())

# convert the object into a dict
api_error_response_v2_error_dict = api_error_response_v2_error_instance.to_dict()
# create an instance of ApiErrorResponseV2Error from a dict
api_error_response_v2_error_from_dict = ApiErrorResponseV2Error.from_dict(api_error_response_v2_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


