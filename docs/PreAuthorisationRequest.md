# PreAuthorisationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** |  | [optional] 
**application_user_id** | **str** | __Conditional__. The user-friendly reference to the &#x60;User&#x60; that will authorise the authorisation request. If a &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; exists, it will be used otherwise, a new &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; will be created and used. Either the &#x60;userUuid&#x60; or &#x60;applicationUserId&#x60; must be provided. | [optional] 
**forward_parameters** | **List[str]** | Extra parameters to be forwarded in the redirect back to the client after the user authorisation flow has been completed. | [optional] 
**institution_id** | **str** | __Mandatory__. The reference to the &#x60;Institution&#x60; which identifies which institution the authorisation request is sent to. | 
**callback** | **str** | __Optional__. The server to redirect the user to after the user complete the authorisation at the &#x60;Institution&#x60;. &lt;br&gt;&lt;br&gt;See [Using a callback (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-optional) for more information. | [optional] 
**redirect** | [**RedirectRequest**](RedirectRequest.md) |  | [optional] 
**one_time_token** | **bool** | __Conditional__. Used to receive a &#x60;oneTimeToken&#x60; rather than a &#x60;consentToken&#x60; at the &#x60;callback&#x60; for additional security. This can only be used when the &#x60;callback&#x60; is set. &lt;br&gt;&lt;br&gt;See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information. | [optional] 
**scope** | **str** | __Mandatory__. Defines the scope of the pre-authorisation request. | 

## Example

```python
from yapily.models.pre_authorisation_request import PreAuthorisationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreAuthorisationRequest from a JSON string
pre_authorisation_request_instance = PreAuthorisationRequest.from_json(json)
# print the JSON string representation of the object
print(PreAuthorisationRequest.to_json())

# convert the object into a dict
pre_authorisation_request_dict = pre_authorisation_request_instance.to_dict()
# create an instance of PreAuthorisationRequest from a dict
pre_authorisation_request_from_dict = PreAuthorisationRequest.from_dict(pre_authorisation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


