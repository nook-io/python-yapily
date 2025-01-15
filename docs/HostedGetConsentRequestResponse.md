# HostedGetConsentRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_request_id** | **str** | Unique Id of the consent request. | [optional] 
**consent_id** | **str** | Identification of the consent. | [optional] 
**user_id** | **str** | Unique Id for the &#x60;User&#x60; assigned by Yapily. | [optional] 
**application_user_id** | **str** | Your reference to the &#x60;User&#x60;. | [optional] 
**application_id** | **str** | Unique Id of the &#x60;Application&#x60; the user is associated with. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiersResponse**](InstitutionIdentifiersResponse.md) |  | [optional] 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of consent server to redirect the user after completion of the consent flow. | [optional] 
**created_at** | **datetime** | The date and time at which the payment was created. | [optional] 
**authorisation_expires_at** | **datetime** | The date and time at which the auth Token will expire. | [optional] 
**status** | **str** | Current status of the consent request. Allowed values are [AWAITING_AUTHORIZATION, AUTHORIZED, REJECTED, REVOKED, FAILED, EXPIRED, AWAITING_DECOUPLED_AUTHORIZATION] | [optional] 
**phases** | [**List[HostedConsentPhase]**](HostedConsentPhase.md) | The phase reached by the consent and its timestamp. | [optional] 
**consent_token** | **str** | Represents the authorisation to gain access to the requested features. Required to access account information. | [optional] 

## Example

```python
from yapily.models.hosted_get_consent_request_response import HostedGetConsentRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostedGetConsentRequestResponse from a JSON string
hosted_get_consent_request_response_instance = HostedGetConsentRequestResponse.from_json(json)
# print the JSON string representation of the object
print HostedGetConsentRequestResponse.to_json()

# convert the object into a dict
hosted_get_consent_request_response_dict = hosted_get_consent_request_response_instance.to_dict()
# create an instance of HostedGetConsentRequestResponse from a dict
hosted_get_consent_request_response_from_dict = HostedGetConsentRequestResponse.from_dict(hosted_get_consent_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


