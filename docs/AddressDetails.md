# AddressDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line** | **str** | Information, in free format text, that identifies a specific address. | [optional] 

## Example

```python
from yapily.models.address_details import AddressDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AddressDetails from a JSON string
address_details_instance = AddressDetails.from_json(json)
# print the JSON string representation of the object
print AddressDetails.to_json()

# convert the object into a dict
address_details_dict = address_details_instance.to_dict()
# create an instance of AddressDetails from a dict
address_details_from_dict = AddressDetails.from_dict(address_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


