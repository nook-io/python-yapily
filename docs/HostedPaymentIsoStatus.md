# HostedPaymentIsoStatus

The ISO status of the payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The ISO 20022 &#x60;PaymentStatusCode&#x60;. One of : &lt;br&gt; ACSC &lt;br&gt; ACCC &lt;br&gt; ACCP  &lt;br&gt; ACSP &lt;br&gt; ACTC &lt;br&gt; ACWC &lt;br&gt; ACWP &lt;br&gt; ACFC &lt;br&gt; RCVD &lt;br&gt; PART &lt;br&gt; PATC &lt;br&gt; PDNG &lt;br&gt; RJCT &lt;br&gt; CANC | [optional] 
**name** | **str** | The full name of the ISO 20022 &#x60;PaymentStatusCode&#x60;. | [optional] 

## Example

```python
from yapily.models.hosted_payment_iso_status import HostedPaymentIsoStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPaymentIsoStatus from a JSON string
hosted_payment_iso_status_instance = HostedPaymentIsoStatus.from_json(json)
# print the JSON string representation of the object
print(HostedPaymentIsoStatus.to_json())

# convert the object into a dict
hosted_payment_iso_status_dict = hosted_payment_iso_status_instance.to_dict()
# create an instance of HostedPaymentIsoStatus from a dict
hosted_payment_iso_status_from_dict = HostedPaymentIsoStatus.from_dict(hosted_payment_iso_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


