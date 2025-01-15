# VrpPeriodicLimit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_amount** | [**Amount**](Amount.md) | __Mandatory__. Maximum amount that can be specified in all payment instructions in a given period under this VRP consent. If the Alignment is Calendar, the limit is pro-rated in the first period to the remaining number of days. | 
**frequency** | [**FrequencyEnum**](FrequencyEnum.md) |  | 
**alignment** | [**AlignmentEnum**](AlignmentEnum.md) |  | 

## Example

```python
from yapily.models.vrp_periodic_limit import VrpPeriodicLimit

# TODO update the JSON string below
json = "{}"
# create an instance of VrpPeriodicLimit from a JSON string
vrp_periodic_limit_instance = VrpPeriodicLimit.from_json(json)
# print the JSON string representation of the object
print VrpPeriodicLimit.to_json()

# convert the object into a dict
vrp_periodic_limit_dict = vrp_periodic_limit_instance.to_dict()
# create an instance of VrpPeriodicLimit from a dict
vrp_periodic_limit_from_dict = VrpPeriodicLimit.from_dict(vrp_periodic_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


