# AddressResponse

The address of the `Payee` or `Payer`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **List[str]** | The address line of the address | [optional] 
**street_name** | **str** | The street name of the address | [optional] 
**building_number** | **str** | The building number of the address | [optional] 
**post_code** | **str** | The post code of the address | [optional] 
**town_name** | **str** | The town name of the address | [optional] 
**county** | **List[str]** | The list of counties for the address | [optional] 
**country** | **str** | The 2-letter country code for the address. | [optional] 
**department** | **str** | The department for the address | [optional] 
**sub_department** | **str** | The sub-department for the address | [optional] 
**address_type** | [**AddressTypeEnumResponse**](AddressTypeEnumResponse.md) |  | [optional] 

## Example

```python
from yapily.models.address_response import AddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressResponse from a JSON string
address_response_instance = AddressResponse.from_json(json)
# print the JSON string representation of the object
print(AddressResponse.to_json())

# convert the object into a dict
address_response_dict = address_response_instance.to_dict()
# create an instance of AddressResponse from a dict
address_response_from_dict = AddressResponse.from_dict(address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


