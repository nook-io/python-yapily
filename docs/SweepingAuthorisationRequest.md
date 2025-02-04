# SweepingAuthorisationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | This is the Yapily user identifier for the user returned by the create user step POST ../users | [optional] 
**application_user_id** | **str** | A client&#39;s own user reference. If the client wants to work with their own unique references for individual PSUs then they can use the applicationUserId property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied applicationUserId, then a new Yapily userId is created automatically and linked to the applicationUserId value.  Clients can then use either their own applicationUserId or the Yapily userId to reference the same user in future calls. | [optional] 
**forward_parameters** | **List[str]** | Extra parameters the TPP may want to get forwarded in the callback request after the PSU redirect. | [optional] 
**context_type** | [**PaymentContextType**](PaymentContextType.md) |  | [optional] 
**institution_id** | **str** | __Mandatory__. The reference to the &#x60;Institution&#x60; which identifies which institution the authorisation request is sent to. | 
**callback** | **str** | __Optional__. The server to redirect the user to after the user complete the authorisation at the &#x60;Institution&#x60;. &lt;br&gt;&lt;br&gt;See [Using a callback (Optional)](https://docs.yapily.com/knowledge/callback_url/#using-a-callback-optional) for more information. | [optional] 
**redirect** | [**RedirectRequest**](RedirectRequest.md) |  | [optional] 
**one_time_token** | **bool** | __Conditional__. Used to receive a &#x60;oneTimeToken&#x60; rather than a &#x60;consentToken&#x60; at the &#x60;callback&#x60; for additional security. This can only be used when the &#x60;callback&#x60; is set. &lt;br&gt;&lt;br&gt;See [Using a callback with an OTT (Optional)](https://docs.yapily.com/knowledge/callback_url/#using-a-callback-with-an-ott-optional) for more information. | [optional] 
**control_parameters** | [**SweepingControlParameters**](SweepingControlParameters.md) |  | 
**initiation_details** | [**InitiationDetails**](InitiationDetails.md) |  | 
**compliance_data** | [**ComplianceData**](ComplianceData.md) |  | [optional] 

## Example

```python
from yapily.models.sweeping_authorisation_request import SweepingAuthorisationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SweepingAuthorisationRequest from a JSON string
sweeping_authorisation_request_instance = SweepingAuthorisationRequest.from_json(json)
# print the JSON string representation of the object
print SweepingAuthorisationRequest.to_json()

# convert the object into a dict
sweeping_authorisation_request_dict = sweeping_authorisation_request_instance.to_dict()
# create an instance of SweepingAuthorisationRequest from a dict
sweeping_authorisation_request_from_dict = SweepingAuthorisationRequest.from_dict(sweeping_authorisation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


