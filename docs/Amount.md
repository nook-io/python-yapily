# Amount

__Mandatory__. Monetary Amount.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | __Mandatory__. The monetary value | 
**currency** | **str** | __Mandatory__. The [ISO 4217](https://www.xe.com/iso4217.php) currency code | 

## Example

```python
from yapily.models.amount import Amount

# TODO update the JSON string below
json = "{}"
# create an instance of Amount from a JSON string
amount_instance = Amount.from_json(json)
# print the JSON string representation of the object
print Amount.to_json()

# convert the object into a dict
amount_dict = amount_instance.to_dict()
# create an instance of Amount from a dict
amount_form_dict = amount.from_dict(amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


