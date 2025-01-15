# HostedPaymentRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_request_id** | **str** | Unique Id of the payment request. | [optional] 
**user_id** | **str** | Unique Id for the &#x60;User&#x60; assigned by Yapily. | [optional] 
**application_user_id** | **str** | Your reference to the &#x60;User&#x60;. | [optional] 
**application_id** | **str** | Unique Id of the &#x60;Application&#x60; the user is associated with. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiersResponse**](InstitutionIdentifiersResponse.md) |  | [optional] 
**user_settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**redirect_url** | **str** | URL of payment server to redirect the user after completion of the payment flow. | [optional] 
**payment_request_details** | [**HostedPaymentResponseDetails**](HostedPaymentResponseDetails.md) |  | [optional] 
**hosted_url** | **str** | The URL of Hosted UI page for the applicationId which initiates the user journey for the payment. &lt;br&gt; URL would be appended with authToken, applicationId and userSettings. | [optional] 
**created_at** | **datetime** | The date and time at which the payment was created. | [optional] 
**authorisation_expires_at** | **datetime** | The date and time at which the auth Token will expire. | [optional] 
**status** | **str** | Current status of the payment request. | [optional] 

## Example

```python
from yapily.models.hosted_payment_request_response import HostedPaymentRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPaymentRequestResponse from a JSON string
hosted_payment_request_response_instance = HostedPaymentRequestResponse.from_json(json)
# print the JSON string representation of the object
print(HostedPaymentRequestResponse.to_json())

# convert the object into a dict
hosted_payment_request_response_dict = hosted_payment_request_response_instance.to_dict()
# create an instance of HostedPaymentRequestResponse from a dict
hosted_payment_request_response_from_dict = HostedPaymentRequestResponse.from_dict(hosted_payment_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


