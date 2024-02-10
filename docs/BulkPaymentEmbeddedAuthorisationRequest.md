# BulkPaymentEmbeddedAuthorisationRequest

The request body containing a `BulkPaymentEmbeddedAuthorisationRequest` json payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** | __Conditional__. The reference to the &#x60;User&#x60; that will authorise the authorisation request using the Yapily generated UUID. Either the &#x60;userUuid&#x60; or &#x60;applicationUserId&#x60; must be provided. | [optional] 
**application_user_id** | **str** | __Conditional__. The user-friendly reference to the &#x60;User&#x60; that will authorise the authorisation request. If a &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; exists, it will be used otherwise, a new &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; will be created and used. Either the &#x60;userUuid&#x60; or &#x60;applicationUserId&#x60; must be provided. | [optional] 
**institution_id** | **str** | __Mandatory__. The reference to the &#x60;Institution&#x60; which identifies which institution the authorisation request is sent to. | 
**callback** | **str** | __Optional__. The server to redirect the user to after the user complete the authorisation at the &#x60;Institution&#x60;. &lt;br&gt;&lt;br&gt;See [Using a callback (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-optional) for more information. | [optional] 
**redirect** | [**RedirectRequest**](RedirectRequest.md) |  | [optional] 
**one_time_token** | **bool** | __Conditional__. Used to receive a &#x60;oneTimeToken&#x60; rather than a &#x60;consentToken&#x60; at the &#x60;callback&#x60; for additional security. This can only be used when the &#x60;callback&#x60; is set. &lt;br&gt;&lt;br&gt;See [Using a callback with an OTT (Optional)](https://docs.yapily.com/pages/knowledge/yapily-concepts/callback_url/#using-a-callback-with-an-ott-optional) for more information. | [optional] 
**payment_request** | [**BulkPaymentRequest**](BulkPaymentRequest.md) |  | [optional] 
**user_credentials** | [**UserCredentials**](UserCredentials.md) |  | [optional] 
**selected_sca_method** | [**ScaMethod**](ScaMethod.md) |  | [optional] 
**sca_code** | **str** | __Conditional__. Used to update the authorisation with the sca code received by the user from the &#x60;Institution&#x60; using the embedded payment authorisation flow.&lt;br&gt;&lt;br&gt;This is the penultimate step required in the embedded payment authorisation flow to authorise the &#x60;Consent&#x60;. After sending the sca code, to obtain an authorised consent, the last step is to poll [Get Consent](https://docs.yapily.com/api/reference/#operation/getConsentById) until the &#x60;Institution&#x60; authorises the request and the &#x60;Consent&#x60; &#x60;status&#x60; transitions to &#x60;AUTHORIZED&#x60;. | [optional] 

## Example

```python
from yapily.models.bulk_payment_embedded_authorisation_request import BulkPaymentEmbeddedAuthorisationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPaymentEmbeddedAuthorisationRequest from a JSON string
bulk_payment_embedded_authorisation_request_instance = BulkPaymentEmbeddedAuthorisationRequest.from_json(json)
# print the JSON string representation of the object
print BulkPaymentEmbeddedAuthorisationRequest.to_json()

# convert the object into a dict
bulk_payment_embedded_authorisation_request_dict = bulk_payment_embedded_authorisation_request_instance.to_dict()
# create an instance of BulkPaymentEmbeddedAuthorisationRequest from a dict
bulk_payment_embedded_authorisation_request_form_dict = bulk_payment_embedded_authorisation_request.from_dict(bulk_payment_embedded_authorisation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


