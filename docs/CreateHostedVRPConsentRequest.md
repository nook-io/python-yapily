# CreateHostedVRPConsentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | __Conditional__. Yapily Identifier for the &#x60;User&#x60; returned by the create user step POST /users. Clients must either provide userId or applicationUserId. | [optional] 
**application_user_id** | **str** | __Conditional__. Client&#39;s own &#x60;User&#x60; reference. If the client wants to work with their own unique references for individual PSUs then they can use the applicationUserId property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a new Yapily userId is created automatically and linked to the applicationUserId value. Clients must either provide userId or applicationUserId. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiers**](InstitutionIdentifiers.md) |  | 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of client&#39;s server to redirect the PSU after completion of the consent authorisation. | 
**one_time_token** | **bool** | Used to receive a oneTimeToken rather than a consentToken at the redirectUrl for additional security. This can only be used when the redirectUrl is set. | [optional] 
**vrp_setup** | [**VRPSetupRequest**](VRPSetupRequest.md) |  | 

## Example

```python
from yapily.models.create_hosted_vrp_consent_request import CreateHostedVRPConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostedVRPConsentRequest from a JSON string
create_hosted_vrp_consent_request_instance = CreateHostedVRPConsentRequest.from_json(json)
# print the JSON string representation of the object
print CreateHostedVRPConsentRequest.to_json()

# convert the object into a dict
create_hosted_vrp_consent_request_dict = create_hosted_vrp_consent_request_instance.to_dict()
# create an instance of CreateHostedVRPConsentRequest from a dict
create_hosted_vrp_consent_request_from_dict = CreateHostedVRPConsentRequest.from_dict(create_hosted_vrp_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


