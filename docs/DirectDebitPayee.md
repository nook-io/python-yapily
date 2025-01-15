# DirectDebitPayee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | __Mandatory__. The account holder name. | [optional] 

## Example

```python
from yapily.models.direct_debit_payee import DirectDebitPayee

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDebitPayee from a JSON string
direct_debit_payee_instance = DirectDebitPayee.from_json(json)
# print the JSON string representation of the object
print DirectDebitPayee.to_json()

# convert the object into a dict
direct_debit_payee_dict = direct_debit_payee_instance.to_dict()
# create an instance of DirectDebitPayee from a dict
direct_debit_payee_from_dict = DirectDebitPayee.from_dict(direct_debit_payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


