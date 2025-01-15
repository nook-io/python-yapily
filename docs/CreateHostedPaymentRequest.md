# CreateHostedPaymentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | __Conditional__. Yapily Identifier for the &#x60;User&#x60; returned by the create user step POST /users. You must provide either a &#x60;userId&#x60; or &#x60;applicationUserId&#x60;. | [optional] 
**application_user_id** | **str** | __Conditional__. Your own &#x60;User&#x60; reference. This field allows you to use your own unique references for individual users. Where the &#x60;User&#x60; reference doesn&#39;t have an associated Yapily &#x60;userId&#x60;, a new &#x60;userId&#x60; is created and linked to it. You must provide either a &#x60;userId&#x60; or &#x60;applicationUserId&#x60;. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiers**](InstitutionIdentifiers.md) |  | 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of your server to redirect the user after completion of the payment flow. | 
**payment_request_details** | [**HostedPaymentRequestDetails**](HostedPaymentRequestDetails.md) |  | 

## Example

```python
from yapily.models.create_hosted_payment_request import CreateHostedPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostedPaymentRequest from a JSON string
create_hosted_payment_request_instance = CreateHostedPaymentRequest.from_json(json)
# print the JSON string representation of the object
print CreateHostedPaymentRequest.to_json()

# convert the object into a dict
create_hosted_payment_request_dict = create_hosted_payment_request_instance.to_dict()
# create an instance of CreateHostedPaymentRequest from a dict
create_hosted_payment_request_from_dict = CreateHostedPaymentRequest.from_dict(create_hosted_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


