# CreateHostedPaymentRequestLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | __Conditional__. Yapily Identifier for the &#x60;User&#x60; returned by the create user step POST /users. You must either provide &#x60;userId&#x60; or &#x60;applicationUserId&#x60;. | [optional] 
**application_user_id** | **str** | __Conditional__. Your own &#x60;User&#x60; reference. If you want to work with their own unique references for individual PSUs then you can use the &#x60;applicationUserId&#x60; property to provide that value. Where Yapily does not already have a Yapily userId that matches the supplied &#x60;applicationUserId&#x60;, then a new Yapily userId is created automatically and linked to the &#x60;applicationUserId&#x60; value. You must either provide userId or &#x60;applicationUserId&#x60;. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiers**](InstitutionIdentifiers.md) |  | 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of your server to redirect the user after completion of the payment flow. | 
**authorisation_expires_at** | **datetime** | The date and time that the authorisation expires. Must be between 10 minutes and 30 days in the future. If not specified, the authorisation URL will expire 10 minutes after creation. | [optional] 
**payment_request_details** | [**HostedPaymentRequestDetailsLink**](HostedPaymentRequestDetailsLink.md) |  | 

## Example

```python
from yapily.models.create_hosted_payment_request_link import CreateHostedPaymentRequestLink

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostedPaymentRequestLink from a JSON string
create_hosted_payment_request_link_instance = CreateHostedPaymentRequestLink.from_json(json)
# print the JSON string representation of the object
print CreateHostedPaymentRequestLink.to_json()

# convert the object into a dict
create_hosted_payment_request_link_dict = create_hosted_payment_request_link_instance.to_dict()
# create an instance of CreateHostedPaymentRequestLink from a dict
create_hosted_payment_request_link_from_dict = CreateHostedPaymentRequestLink.from_dict(create_hosted_payment_request_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


