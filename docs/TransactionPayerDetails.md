# TransactionPayerDetails

Details of the benefactor [person or business].

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account holder name of the Payer. | [optional] 
**account_identifications** | [**List[TransactionPayeeDetailsAccountIdentificationsInner]**](TransactionPayeeDetailsAccountIdentificationsInner.md) | The account identifications that identify the Payer&#39;s bank account. | [optional] 

## Example

```python
from yapily.models.transaction_payer_details import TransactionPayerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPayerDetails from a JSON string
transaction_payer_details_instance = TransactionPayerDetails.from_json(json)
# print the JSON string representation of the object
print TransactionPayerDetails.to_json()

# convert the object into a dict
transaction_payer_details_dict = transaction_payer_details_instance.to_dict()
# create an instance of TransactionPayerDetails from a dict
transaction_payer_details_from_dict = TransactionPayerDetails.from_dict(transaction_payer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


