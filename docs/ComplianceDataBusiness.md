# ComplianceDataBusiness

__Conditional__. Mandatory if the type is BUSINESS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the registered company name of your end user. | 
**registration_number** | **str** | This is the registered company number of the business. | 
**registered_address** | [**ComplianceDataAddress**](ComplianceDataAddress.md) |  | 
**trading_address** | [**ComplianceDataAddress**](ComplianceDataAddress.md) |  | [optional] 

## Example

```python
from yapily.models.compliance_data_business import ComplianceDataBusiness

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceDataBusiness from a JSON string
compliance_data_business_instance = ComplianceDataBusiness.from_json(json)
# print the JSON string representation of the object
print ComplianceDataBusiness.to_json()

# convert the object into a dict
compliance_data_business_dict = compliance_data_business_instance.to_dict()
# create an instance of ComplianceDataBusiness from a dict
compliance_data_business_from_dict = ComplianceDataBusiness.from_dict(compliance_data_business_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


