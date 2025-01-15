# TransactionPayeeDetails

Details of the beneficiary [person or business].

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account holder name of the Payee. | [optional] 
**account_identifications** | [**List[TransactionPayeeDetailsAccountIdentificationsInner]**](TransactionPayeeDetailsAccountIdentificationsInner.md) | The account identifications that identify the Payee&#39;s bank account. | [optional] 

## Example

```python
from yapily.models.transaction_payee_details import TransactionPayeeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPayeeDetails from a JSON string
transaction_payee_details_instance = TransactionPayeeDetails.from_json(json)
# print the JSON string representation of the object
print(TransactionPayeeDetails.to_json())

# convert the object into a dict
transaction_payee_details_dict = transaction_payee_details_instance.to_dict()
# create an instance of TransactionPayeeDetails from a dict
transaction_payee_details_from_dict = TransactionPayeeDetails.from_dict(transaction_payee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


