# VirtualAccountAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | __Mandatory__. AddressLine1 of the sub-client | 
**address_line2** | **str** | __Optional__. AddressLine2 of the sub-client | [optional] 
**town_name** | **str** | __Mandatory__. Town name of the sub-client | 
**post_code** | **str** | __Optional__. Address postcode of the sub-client | [optional] 
**country** | **str** | __Optional__. Country of the sub-client | 

## Example

```python
from yapily.models.virtual_account_address import VirtualAccountAddress

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountAddress from a JSON string
virtual_account_address_instance = VirtualAccountAddress.from_json(json)
# print the JSON string representation of the object
print VirtualAccountAddress.to_json()

# convert the object into a dict
virtual_account_address_dict = virtual_account_address_instance.to_dict()
# create an instance of VirtualAccountAddress from a dict
virtual_account_address_form_dict = virtual_account_address.from_dict(virtual_account_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


