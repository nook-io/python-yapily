# TransactionPayeeDetailsAccountIdentificationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccountIdentificationType**](AccountIdentificationType.md) | Describes the format of the account. | [optional] 
**identification** | **str** | The value associated with the account identification type. | [optional] 

## Example

```python
from yapily.models.transaction_payee_details_account_identifications_inner import TransactionPayeeDetailsAccountIdentificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPayeeDetailsAccountIdentificationsInner from a JSON string
transaction_payee_details_account_identifications_inner_instance = TransactionPayeeDetailsAccountIdentificationsInner.from_json(json)
# print the JSON string representation of the object
print(TransactionPayeeDetailsAccountIdentificationsInner.to_json())

# convert the object into a dict
transaction_payee_details_account_identifications_inner_dict = transaction_payee_details_account_identifications_inner_instance.to_dict()
# create an instance of TransactionPayeeDetailsAccountIdentificationsInner from a dict
transaction_payee_details_account_identifications_inner_from_dict = TransactionPayeeDetailsAccountIdentificationsInner.from_dict(transaction_payee_details_account_identifications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


