# ApiResponseOfGetHostedVRPConsentsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**List[GetHostedVRPConsentsResponseInner]**](GetHostedVRPConsentsResponseInner.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_of_get_hosted_vrp_consents_request import ApiResponseOfGetHostedVRPConsentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfGetHostedVRPConsentsRequest from a JSON string
api_response_of_get_hosted_vrp_consents_request_instance = ApiResponseOfGetHostedVRPConsentsRequest.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfGetHostedVRPConsentsRequest.to_json()

# convert the object into a dict
api_response_of_get_hosted_vrp_consents_request_dict = api_response_of_get_hosted_vrp_consents_request_instance.to_dict()
# create an instance of ApiResponseOfGetHostedVRPConsentsRequest from a dict
api_response_of_get_hosted_vrp_consents_request_from_dict = ApiResponseOfGetHostedVRPConsentsRequest.from_dict(api_response_of_get_hosted_vrp_consents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


