# HostedVRPConsentRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Represents the Unique Id of the VRP consent request | 
**user_id** | **str** | Represents the Unique Id for the &#x60;User&#x60; assigned by Yapily. | [optional] 
**application_user_id** | **str** | Represents the user-friendly reference to the &#x60;User&#x60;. | [optional] 
**application_id** | **str** | Represents the Unique Id of the &#x60;Application&#x60; the user is associated with. | 
**institution_identifiers** | [**InstitutionIdentifiers**](InstitutionIdentifiers.md) |  | [optional] 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of client&#39;s server to redirect the PSU after completion of the consent authorisation. | [optional] 
**vrp_setup** | [**VRPSetupRequest**](VRPSetupRequest.md) |  | [optional] 
**hosted_url** | **str** | Represents the URL of Hosted UI page for the applicationId which initiates the user journey for the Consent. &lt;br&gt; URL would be appended with authToken, applicationId and userSettings. | 
**auth_token** | **str** | Represents the JWT Token signed by the certificate-vault using Yapily&#39;s keys. | 
**created_at** | **datetime** | Represents the date and time at which the Consent was created. | 
**authorisation_expires_at** | **datetime** | Represents the date and time at which the auth Token will expire. | [optional] 

## Example

```python
from yapily.models.hosted_vrp_consent_request_response import HostedVRPConsentRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostedVRPConsentRequestResponse from a JSON string
hosted_vrp_consent_request_response_instance = HostedVRPConsentRequestResponse.from_json(json)
# print the JSON string representation of the object
print HostedVRPConsentRequestResponse.to_json()

# convert the object into a dict
hosted_vrp_consent_request_response_dict = hosted_vrp_consent_request_response_instance.to_dict()
# create an instance of HostedVRPConsentRequestResponse from a dict
hosted_vrp_consent_request_response_form_dict = hosted_vrp_consent_request_response.from_dict(hosted_vrp_consent_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


