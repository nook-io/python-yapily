# VirtualAccountPayInDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the payment | [optional] 
**payment_scheme** | **str** | Method of settlement to complete the payment. One of: &lt;br&gt; FASTER_PAYMENTS &lt;br&gt; SEPA_CREDIT &lt;br&gt; SEPA_INSTANT &lt;br&gt; SWIFT &lt;br&gt; SWIFT_EXPRESS &lt;br&gt; CHAPS &lt;br&gt; IAT &lt;br&gt; WIRE | [optional] 
**amount** | [**VirtualAccountPaymentAmount**](VirtualAccountPaymentAmount.md) |  | [optional] 
**reference** | **str** | Reference associated with the payment and which appears on the beneficiary&#39;s bank statement | [optional] 
**source** | [**VirtualAccountPaymentSource**](VirtualAccountPaymentSource.md) |  | [optional] 
**name** | **str** | Account source name | [optional] 
**address** | **str** | The address of the source bank account | [optional] 

## Example

```python
from yapily.models.virtual_account_pay_in_details import VirtualAccountPayInDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountPayInDetails from a JSON string
virtual_account_pay_in_details_instance = VirtualAccountPayInDetails.from_json(json)
# print the JSON string representation of the object
print VirtualAccountPayInDetails.to_json()

# convert the object into a dict
virtual_account_pay_in_details_dict = virtual_account_pay_in_details_instance.to_dict()
# create an instance of VirtualAccountPayInDetails from a dict
virtual_account_pay_in_details_form_dict = virtual_account_pay_in_details.from_dict(virtual_account_pay_in_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


