# HostedConsentRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_request_id** | **str** | Unique Id of the consent request. | [optional] 
**user_id** | **str** | Unique Id for the &#x60;User&#x60; assigned by Yapily. | [optional] 
**application_user_id** | **str** | Your reference to the &#x60;User&#x60;. | [optional] 
**application_id** | **str** | Unique Id of the &#x60;Application&#x60; the user is associated with. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiersResponse**](InstitutionIdentifiersResponse.md) |  | [optional] 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of consent server to redirect the user after completion of the consent flow. | [optional] 
**account_request_details** | [**HostedAccountRequestDetailsResponse**](HostedAccountRequestDetailsResponse.md) |  | [optional] 
**hosted_url** | **str** | The URL of Hosted UI page for the applicationId which initiates the user journey for the consent. &lt;br&gt; URL would be appended with authToken, applicationId and userSettings. | [optional] 
**created_at** | **datetime** | The date and time at which the consent was created. | [optional] 
**authorisation_expires_at** | **datetime** | The date and time at which the auth Token will expire. | [optional] 

## Example

```python
from yapily.models.hosted_consent_request_response import HostedConsentRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostedConsentRequestResponse from a JSON string
hosted_consent_request_response_instance = HostedConsentRequestResponse.from_json(json)
# print the JSON string representation of the object
print HostedConsentRequestResponse.to_json()

# convert the object into a dict
hosted_consent_request_response_dict = hosted_consent_request_response_instance.to_dict()
# create an instance of HostedConsentRequestResponse from a dict
hosted_consent_request_response_from_dict = HostedConsentRequestResponse.from_dict(hosted_consent_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


