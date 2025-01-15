# HostedPaymentDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_request_id** | **str** | The unique ID of the payment request. | [optional] 
**user_id** | **str** | The Unique Identifier for the &#x60;User&#x60; assigned by Yapily. | [optional] 
**application_user_id** | **str** | Your reference to the &#x60;User&#x60;. | [optional] 
**application_id** | **str** | The Unique Identifier of the &#x60;Application&#x60; the user is associated with. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiersResponse**](InstitutionIdentifiersResponse.md) |  | [optional] 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of your server to redirect the user after completion of the payment flow. | [optional] 
**payment_request_details** | [**HostedPaymentRequestDetailsLink**](HostedPaymentRequestDetailsLink.md) |  | [optional] 
**created_at** | **datetime** | The date and time at which the payment request was created. | [optional] 
**authorisation_expires_at** | **datetime** | The date and time at which the auth Token will expire. | [optional] 
**status** | **str** | Current status of the payment request. &lt;br&gt; Possible values: &lt;br&gt; ACTIVE &lt;br&gt; INACTIVE | [optional] 
**payments** | [**List[HostedPayment]**](HostedPayment.md) | Payments that have been initiated as part of this request | [optional] 

## Example

```python
from yapily.models.hosted_payment_details import HostedPaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPaymentDetails from a JSON string
hosted_payment_details_instance = HostedPaymentDetails.from_json(json)
# print the JSON string representation of the object
print HostedPaymentDetails.to_json()

# convert the object into a dict
hosted_payment_details_dict = hosted_payment_details_instance.to_dict()
# create an instance of HostedPaymentDetails from a dict
hosted_payment_details_from_dict = HostedPaymentDetails.from_dict(hosted_payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


