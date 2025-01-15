# Merchant

Details of the merchant involved in the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** | The name of the merchant involved in the transaction. | [optional] 
**merchant_category_code** | **str** | Defines the underlying services and goods that the merchant provides. Specified as a 3-letter ISO 18245 code  | [optional] 

## Example

```python
from yapily.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print(Merchant.to_json())

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_from_dict = Merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


