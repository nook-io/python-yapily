# ComplianceDataPayer

__Conditional__. Payer details required for compliance checks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The payer type. Allowed values: INDIVIDUAL, BUSINESS. The corresponding object must be included. | 
**individual** | [**ComplianceDataIndividual**](ComplianceDataIndividual.md) |  | [optional] 
**business** | [**ComplianceDataBusiness**](ComplianceDataBusiness.md) |  | [optional] 

## Example

```python
from yapily.models.compliance_data_payer import ComplianceDataPayer

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceDataPayer from a JSON string
compliance_data_payer_instance = ComplianceDataPayer.from_json(json)
# print the JSON string representation of the object
print ComplianceDataPayer.to_json()

# convert the object into a dict
compliance_data_payer_dict = compliance_data_payer_instance.to_dict()
# create an instance of ComplianceDataPayer from a dict
compliance_data_payer_form_dict = compliance_data_payer.from_dict(compliance_data_payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


