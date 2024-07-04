# ComplianceDataAddress

This is the registered company or trading address of your end user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | __Mandatory__. AddressLine1 of the business. | 
**address_line2** | **str** | __Optional__. AddressLine2 of the business. | [optional] 
**town_name** | **str** | __Mandatory__. Town name of the business. | 
**post_code** | **str** | __Mandatory__. Post code of the business. | 
**country** | **str** | __Mandatory__. Country of the business. | 

## Example

```python
from yapily.models.compliance_data_address import ComplianceDataAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceDataAddress from a JSON string
compliance_data_address_instance = ComplianceDataAddress.from_json(json)
# print the JSON string representation of the object
print ComplianceDataAddress.to_json()

# convert the object into a dict
compliance_data_address_dict = compliance_data_address_instance.to_dict()
# create an instance of ComplianceDataAddress from a dict
compliance_data_address_form_dict = compliance_data_address.from_dict(compliance_data_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


