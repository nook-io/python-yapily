# Merchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** |  | [optional] 
**merchant_category_code** | **str** |  | [optional] 

## Example

```python
from yapily.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print Merchant.to_json()

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_form_dict = merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


