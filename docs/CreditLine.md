# CreditLine

__Mandatory__. Details whether the account has access to a credit line from an `Institution`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CreditLineType**](CreditLineType.md) |  | [optional] 
**credit_line_amount** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from yapily.models.credit_line import CreditLine

# TODO update the JSON string below
json = "{}"
# create an instance of CreditLine from a JSON string
credit_line_instance = CreditLine.from_json(json)
# print the JSON string representation of the object
print(CreditLine.to_json())

# convert the object into a dict
credit_line_dict = credit_line_instance.to_dict()
# create an instance of CreditLine from a dict
credit_line_from_dict = CreditLine.from_dict(credit_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


