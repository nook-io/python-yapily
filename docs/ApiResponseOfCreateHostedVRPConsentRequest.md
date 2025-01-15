# ApiResponseOfCreateHostedVRPConsentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**HostedVRPConsentRequestResponse**](HostedVRPConsentRequestResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_of_create_hosted_vrp_consent_request import ApiResponseOfCreateHostedVRPConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfCreateHostedVRPConsentRequest from a JSON string
api_response_of_create_hosted_vrp_consent_request_instance = ApiResponseOfCreateHostedVRPConsentRequest.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfCreateHostedVRPConsentRequest.to_json()

# convert the object into a dict
api_response_of_create_hosted_vrp_consent_request_dict = api_response_of_create_hosted_vrp_consent_request_instance.to_dict()
# create an instance of ApiResponseOfCreateHostedVRPConsentRequest from a dict
api_response_of_create_hosted_vrp_consent_request_from_dict = ApiResponseOfCreateHostedVRPConsentRequest.from_dict(api_response_of_create_hosted_vrp_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


