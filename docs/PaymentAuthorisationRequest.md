# PaymentAuthorisationRequest

The request body containing an `PaymentAuthorisationRequest` json payload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** |  | [optional] 
**application_user_id** | **str** | __Conditional__. The user-friendly reference to the &#x60;User&#x60; that will authorise the authorisation request. If a &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; exists, it will be used otherwise, a new &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; will be created and used. Either the &#x60;userUuid&#x60; or &#x60;applicationUserId&#x60; must be provided. | [optional] 
**forward_parameters** | **List[str]** | Extra parameters the TPP may want to get forwarded in the callback request after the PSU redirect. | [optional] 
**institution_id** | **str** | __Mandatory__. The reference to the &#x60;Institution&#x60; which identifies which institution the authorisation request is sent to. | 
**callback** | **str** | __Optional__. The server to redirect the user to after the user complete the authorisation at the &#x60;Institution&#x60;. &lt;br&gt;&lt;br&gt;See [Using a callback (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-optional) for more information. | [optional] 
**redirect** | [**RedirectRequest**](RedirectRequest.md) |  | [optional] 
**one_time_token** | **bool** | __Conditional__. Used to receive a &#x60;oneTimeToken&#x60; rather than a &#x60;consentToken&#x60; at the &#x60;callback&#x60; for additional security. This can only be used when the &#x60;callback&#x60; is set. &lt;br&gt;&lt;br&gt;See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information. | [optional] 
**payment_request** | [**PaymentRequest**](PaymentRequest.md) |  | 

## Example

```python
from yapily.models.payment_authorisation_request import PaymentAuthorisationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAuthorisationRequest from a JSON string
payment_authorisation_request_instance = PaymentAuthorisationRequest.from_json(json)
# print the JSON string representation of the object
print PaymentAuthorisationRequest.to_json()

# convert the object into a dict
payment_authorisation_request_dict = payment_authorisation_request_instance.to_dict()
# create an instance of PaymentAuthorisationRequest from a dict
payment_authorisation_request_form_dict = payment_authorisation_request.from_dict(payment_authorisation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


