# BeneficiaryPayee

__Mandatory__. Account details belonging to the `Beneficiary Payee` (person/ business). You must define this in your payment request along with all of the nested mandatory properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account holder name of the beneficiary. | [optional] 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;BeneficiaryPayee&#x60; bank account. | 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from yapily.models.beneficiary_payee import BeneficiaryPayee

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiaryPayee from a JSON string
beneficiary_payee_instance = BeneficiaryPayee.from_json(json)
# print the JSON string representation of the object
print BeneficiaryPayee.to_json()

# convert the object into a dict
beneficiary_payee_dict = beneficiary_payee_instance.to_dict()
# create an instance of BeneficiaryPayee from a dict
beneficiary_payee_from_dict = BeneficiaryPayee.from_dict(beneficiary_payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


