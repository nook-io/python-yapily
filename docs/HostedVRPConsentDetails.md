# HostedVRPConsentDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the consent request. | 
**user_id** | **str** | Represents the Unique Identifier for the &#x60;User&#x60; assigned by Yapily. | [optional] 
**application_user_id** | **str** | Represents the User-friendly reference to the &#x60;User&#x60;. | [optional] 
**application_id** | **str** | Represens the Unique Identifier of the &#x60;Application&#x60; the user is associated with. | 
**institution_identifiers** | [**InstitutionIdentifiers**](InstitutionIdentifiers.md) |  | [optional] 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of client&#39;s server to redirect the PSU after completion of the consent authorisation. | [optional] 
**vrp_setup** | [**VRPSetup**](VRPSetup.md) |  | 
**created_at** | **datetime** |  | [optional] 
**authorisation_expires_at** | **datetime** | Represents the date and time at which the auth Token will expire. | [optional] 
**consent_token** | **str** | Represents the authorisation to make VRP payments | [optional] 
**consent_status** | **str** | Current status of the authorisation. Can be one of [AWAITING_AUTHORIZATION, AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED] | 
**phases** | [**List[HostedVRPPhase]**](HostedVRPPhase.md) |  | [optional] 

## Example

```python
from yapily.models.hosted_vrp_consent_details import HostedVRPConsentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostedVRPConsentDetails from a JSON string
hosted_vrp_consent_details_instance = HostedVRPConsentDetails.from_json(json)
# print the JSON string representation of the object
print HostedVRPConsentDetails.to_json()

# convert the object into a dict
hosted_vrp_consent_details_dict = hosted_vrp_consent_details_instance.to_dict()
# create an instance of HostedVRPConsentDetails from a dict
hosted_vrp_consent_details_from_dict = HostedVRPConsentDetails.from_dict(hosted_vrp_consent_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


