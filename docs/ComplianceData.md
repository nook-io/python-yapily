# ComplianceData

__Conditional__. Information needed to complete compliance checks. Mandatory for Yapily Connect customers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer** | [**ComplianceDataPayer**](ComplianceDataPayer.md) |  | [optional] 

## Example

```python
from yapily.models.compliance_data import ComplianceData

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceData from a JSON string
compliance_data_instance = ComplianceData.from_json(json)
# print the JSON string representation of the object
print ComplianceData.to_json()

# convert the object into a dict
compliance_data_dict = compliance_data_instance.to_dict()
# create an instance of ComplianceData from a dict
compliance_data_from_dict = ComplianceData.from_dict(compliance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


