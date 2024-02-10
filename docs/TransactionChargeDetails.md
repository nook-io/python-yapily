# TransactionChargeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_amount** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from yapily.models.transaction_charge_details import TransactionChargeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionChargeDetails from a JSON string
transaction_charge_details_instance = TransactionChargeDetails.from_json(json)
# print the JSON string representation of the object
print TransactionChargeDetails.to_json()

# convert the object into a dict
transaction_charge_details_dict = transaction_charge_details_instance.to_dict()
# create an instance of TransactionChargeDetails from a dict
transaction_charge_details_form_dict = transaction_charge_details.from_dict(transaction_charge_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


