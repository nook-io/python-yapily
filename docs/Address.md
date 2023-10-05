# Address

__Conditional__. The address of the `Payee` or `Payer`.<ul><li>`payee.address` is mandatory when the `paymentType` is an `INTERNATIONAL` payment</li><li>An `Institution` may require you to specify the `country` when used in the context of the `Payee` to be able to make a payment.</li></ul>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **List[str]** | __Optional__. The address line of the address | [optional] 
**street_name** | **str** | __Optional__. The street name of the address | [optional] 
**building_number** | **str** | __Optional__. The building number of the address | [optional] 
**post_code** | **str** | __Optional__. The post code of the address | [optional] 
**town_name** | **str** | __Optional__. The town name of the address | [optional] 
**county** | **List[str]** | __Optional__. The list of counties for the address | [optional] 
**country** | **str** | __Conditional__. The 2-letter country code for the address. &lt;br&gt;&lt;br&gt;An &#x60;Institution&#x60; may require you to specify the &#x60;country&#x60; when used in the context of the &#x60;Payee&#x60; to be able to make a payment | [optional] 
**department** | **str** | __Optional__. The department for the address | [optional] 
**sub_department** | **str** | __Optional__. The sub-department for the address | [optional] 
**address_type** | [**AddressTypeEnum**](AddressTypeEnum.md) |  | [optional] 

## Example

```python
from yapily.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print Address.to_json()

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_form_dict = address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


