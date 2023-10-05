# ProprietaryBankTransactionCode

Transaction code that is proprietary to the `Institution`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | __Mandatory__. Properietary code used to identify the underlying transaction. | [optional] 
**issuer** | **str** | __Mandatory__. Issuer of the properitary code. | [optional] 

## Example

```python
from yapily.models.proprietary_bank_transaction_code import ProprietaryBankTransactionCode

# TODO update the JSON string below
json = "{}"
# create an instance of ProprietaryBankTransactionCode from a JSON string
proprietary_bank_transaction_code_instance = ProprietaryBankTransactionCode.from_json(json)
# print the JSON string representation of the object
print ProprietaryBankTransactionCode.to_json()

# convert the object into a dict
proprietary_bank_transaction_code_dict = proprietary_bank_transaction_code_instance.to_dict()
# create an instance of ProprietaryBankTransactionCode from a dict
proprietary_bank_transaction_code_form_dict = proprietary_bank_transaction_code.from_dict(proprietary_bank_transaction_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


