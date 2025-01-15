# IsoBankTransactionCode

Defines the underlying transaction type (e.g. Card or Debit Transactions, Loans or Mortages). <br><br> Conforms to `ISO` standards - ISO 20022.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_code** | [**IsoCodeDetails**](IsoCodeDetails.md) |  | [optional] 
**family_code** | [**IsoCodeDetails**](IsoCodeDetails.md) |  | [optional] 
**sub_family_code** | [**IsoCodeDetails**](IsoCodeDetails.md) |  | [optional] 

## Example

```python
from yapily.models.iso_bank_transaction_code import IsoBankTransactionCode

# TODO update the JSON string below
json = "{}"
# create an instance of IsoBankTransactionCode from a JSON string
iso_bank_transaction_code_instance = IsoBankTransactionCode.from_json(json)
# print the JSON string representation of the object
print(IsoBankTransactionCode.to_json())

# convert the object into a dict
iso_bank_transaction_code_dict = iso_bank_transaction_code_instance.to_dict()
# create an instance of IsoBankTransactionCode from a dict
iso_bank_transaction_code_from_dict = IsoBankTransactionCode.from_dict(iso_bank_transaction_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


