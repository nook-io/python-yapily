# GetHostedVRPConsentsResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Represents the Unique Id of the VRP consent request | 
**application_id** | **str** | Represents the Unique Id of the &#x60;Application&#x60; the user is associated with. | 
**institution_identifiers** | [**InstitutionIdentifiers**](InstitutionIdentifiers.md) |  | [optional] 
**vrp_setup** | [**VRPSetupRequest**](VRPSetupRequest.md) |  | [optional] 
**updated_at** | **datetime** | Represents the date and time at which the Consent was updated. | [optional] 
**consent_status** | **str** | Current status of the authorisation. Can be one of [AWAITING_AUTHORIZATION, AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED] | [optional] 

## Example

```python
from yapily.models.get_hosted_vrp_consents_response_inner import GetHostedVRPConsentsResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHostedVRPConsentsResponseInner from a JSON string
get_hosted_vrp_consents_response_inner_instance = GetHostedVRPConsentsResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetHostedVRPConsentsResponseInner.to_json())

# convert the object into a dict
get_hosted_vrp_consents_response_inner_dict = get_hosted_vrp_consents_response_inner_instance.to_dict()
# create an instance of GetHostedVRPConsentsResponseInner from a dict
get_hosted_vrp_consents_response_inner_from_dict = GetHostedVRPConsentsResponseInner.from_dict(get_hosted_vrp_consents_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


