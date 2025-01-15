# CreateHostedConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | __Conditional__. Yapily Identifier for the &#x60;User&#x60; returned by the create user step POST /users. You must provide either a &#x60;userId&#x60; or &#x60;applicationUserId&#x60;. | [optional] 
**application_user_id** | **str** | __Conditional__. Your own &#x60;User&#x60; reference. This field allows you to use your own unique references for individual users. Where the &#x60;User&#x60; reference doesn&#39;t have an associated Yapily &#x60;userId&#x60;, a new &#x60;userId&#x60; is created and linked to it. You must provide either a &#x60;userId&#x60; or &#x60;applicationUserId&#x60;. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiers**](InstitutionIdentifiers.md) |  | 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of your server to redirect the user after completion of the consent flow. | 
**one_time_token** | **bool** | Used to receive a oneTimeToken rather than a consentToken at the redirectUrl for additional security. | [optional] 
**account_request** | [**HostedAccountRequest**](HostedAccountRequest.md) |  | [optional] 

## Example

```python
from yapily.models.create_hosted_consent_request import CreateHostedConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostedConsentRequest from a JSON string
create_hosted_consent_request_instance = CreateHostedConsentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHostedConsentRequest.to_json())

# convert the object into a dict
create_hosted_consent_request_dict = create_hosted_consent_request_instance.to_dict()
# create an instance of CreateHostedConsentRequest from a dict
create_hosted_consent_request_from_dict = CreateHostedConsentRequest.from_dict(create_hosted_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


