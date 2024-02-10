# IdentityAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **List[str]** |  | [optional] 
**city** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**street_name** | **str** |  | [optional] 
**building_number** | **str** |  | [optional] 
**type** | [**AddressTypeEnum**](AddressTypeEnum.md) |  | [optional] 
**county** | **str** |  | [optional] 

## Example

```python
from yapily.models.identity_address import IdentityAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAddress from a JSON string
identity_address_instance = IdentityAddress.from_json(json)
# print the JSON string representation of the object
print IdentityAddress.to_json()

# convert the object into a dict
identity_address_dict = identity_address_instance.to_dict()
# create an instance of IdentityAddress from a dict
identity_address_form_dict = identity_address.from_dict(identity_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


