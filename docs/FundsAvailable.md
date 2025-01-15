# FundsAvailable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funds_available** | **bool** | __Mandatory__. Indicates whether funds are available or not. | 
**funds_available_at** | **datetime** | __Mandatory__. Date and Time when the funds availability is checked. | 

## Example

```python
from yapily.models.funds_available import FundsAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of FundsAvailable from a JSON string
funds_available_instance = FundsAvailable.from_json(json)
# print the JSON string representation of the object
print FundsAvailable.to_json()

# convert the object into a dict
funds_available_dict = funds_available_instance.to_dict()
# create an instance of FundsAvailable from a dict
funds_available_from_dict = FundsAvailable.from_dict(funds_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


