# Beneficiary

Account information belonging to the target beneficiary (person/ business).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the &#x60;beneficiary&#x60;. | [optional] 
**reference** | **str** | A creditor reference that is requested to be used for all payment instructions to this beneficiary. | [optional] 
**payee** | [**BeneficiaryPayee**](BeneficiaryPayee.md) |  | [optional] 
**trusted** | **bool** | Indicates whether the account owner has stated that this beneficiary should be trusted. This often results in reduced authentication and authorisation requirements on payments to the beneficiary. | [optional] 

## Example

```python
from yapily.models.beneficiary import Beneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of Beneficiary from a JSON string
beneficiary_instance = Beneficiary.from_json(json)
# print the JSON string representation of the object
print Beneficiary.to_json()

# convert the object into a dict
beneficiary_dict = beneficiary_instance.to_dict()
# create an instance of Beneficiary from a dict
beneficiary_form_dict = beneficiary.from_dict(beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


