# ApiResponseOfSubmissionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**SubmissionResponse**](SubmissionResponse.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_of_submission_response import ApiResponseOfSubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfSubmissionResponse from a JSON string
api_response_of_submission_response_instance = ApiResponseOfSubmissionResponse.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfSubmissionResponse.to_json()

# convert the object into a dict
api_response_of_submission_response_dict = api_response_of_submission_response_instance.to_dict()
# create an instance of ApiResponseOfSubmissionResponse from a dict
api_response_of_submission_response_from_dict = ApiResponseOfSubmissionResponse.from_dict(api_response_of_submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


