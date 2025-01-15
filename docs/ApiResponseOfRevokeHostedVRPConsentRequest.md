# ApiResponseOfRevokeHostedVRPConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**HostedVRPConsentDetails**](HostedVRPConsentDetails.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_of_revoke_hosted_vrp_consent_request import ApiResponseOfRevokeHostedVRPConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfRevokeHostedVRPConsentRequest from a JSON string
api_response_of_revoke_hosted_vrp_consent_request_instance = ApiResponseOfRevokeHostedVRPConsentRequest.from_json(json)
# print the JSON string representation of the object
print(ApiResponseOfRevokeHostedVRPConsentRequest.to_json())

# convert the object into a dict
api_response_of_revoke_hosted_vrp_consent_request_dict = api_response_of_revoke_hosted_vrp_consent_request_instance.to_dict()
# create an instance of ApiResponseOfRevokeHostedVRPConsentRequest from a dict
api_response_of_revoke_hosted_vrp_consent_request_from_dict = ApiResponseOfRevokeHostedVRPConsentRequest.from_dict(api_response_of_revoke_hosted_vrp_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


