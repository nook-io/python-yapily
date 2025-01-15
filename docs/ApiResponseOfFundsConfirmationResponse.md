# ApiResponseOfFundsConfirmationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**FundsConfirmationResponse**](FundsConfirmationResponse.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_of_funds_confirmation_response import ApiResponseOfFundsConfirmationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfFundsConfirmationResponse from a JSON string
api_response_of_funds_confirmation_response_instance = ApiResponseOfFundsConfirmationResponse.from_json(json)
# print the JSON string representation of the object
print(ApiResponseOfFundsConfirmationResponse.to_json())

# convert the object into a dict
api_response_of_funds_confirmation_response_dict = api_response_of_funds_confirmation_response_instance.to_dict()
# create an instance of ApiResponseOfFundsConfirmationResponse from a dict
api_response_of_funds_confirmation_response_from_dict = ApiResponseOfFundsConfirmationResponse.from_dict(api_response_of_funds_confirmation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


