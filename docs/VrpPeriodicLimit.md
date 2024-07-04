# VrpPeriodicLimit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_amount** | [**Amount**](Amount.md) |  | 
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
vrp_periodic_limit_form_dict = vrp_periodic_limit.from_dict(vrp_periodic_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


