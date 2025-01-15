# ComplianceDataIndividual

__Conditional__. Mandatory if the type is INDIVIDUAL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the first and last name of your end user. | 
**birth_date** | **date** | This is the date of birth of your end user. | 

## Example

```python
from yapily.models.compliance_data_individual import ComplianceDataIndividual

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceDataIndividual from a JSON string
compliance_data_individual_instance = ComplianceDataIndividual.from_json(json)
# print the JSON string representation of the object
print ComplianceDataIndividual.to_json()

# convert the object into a dict
compliance_data_individual_dict = compliance_data_individual_instance.to_dict()
# create an instance of ComplianceDataIndividual from a dict
compliance_data_individual_from_dict = ComplianceDataIndividual.from_dict(compliance_data_individual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


