# VirtualAccountPayOutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Unique id of the source / payer account | 
**amount** | [**VirtualAccountPaymentAmount**](VirtualAccountPaymentAmount.md) |  | 
**reference** | **str** | Reference to be associated with the payment. This will be appear on the beneficiary&#39;s bank statement | 
**beneficiary_id** | **str** | Unique id of the beneficiary to whom the payment will be made | 
**payment_scheme** | **str** | Method of settlement to complete the payment. One of: &lt;br&gt; FASTER_PAYMENTS &lt;br&gt; SEPA_CREDIT &lt;br&gt; SEPA_INSTANT &lt;br&gt; SWIFT &lt;br&gt; SWIFT_EXPRESS &lt;br&gt; CHAPS &lt;br&gt; IAT &lt;br&gt; WIRE | 
**payment_date** | **date** | Date on which a payment instruction will be executed, that must be in the future | [optional] 

## Example

```python
from yapily.models.virtual_account_pay_out_request import VirtualAccountPayOutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountPayOutRequest from a JSON string
virtual_account_pay_out_request_instance = VirtualAccountPayOutRequest.from_json(json)
# print the JSON string representation of the object
print VirtualAccountPayOutRequest.to_json()

# convert the object into a dict
virtual_account_pay_out_request_dict = virtual_account_pay_out_request_instance.to_dict()
# create an instance of VirtualAccountPayOutRequest from a dict
virtual_account_pay_out_request_form_dict = virtual_account_pay_out_request.from_dict(virtual_account_pay_out_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


