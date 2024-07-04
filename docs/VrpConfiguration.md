# VrpConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_individual_amount** | [**Amount**](Amount.md) |  | [optional] 
**maximum_cumulative_amount** | [**Amount**](Amount.md) |  | [optional] 
**maximum_cumulative_number_of_payments** | **int** | Maximum cumulative number of payments | [optional] 
**periodic_limits** | [**List[VrpPeriodicLimit]**](VrpPeriodicLimit.md) |  | [optional] 
**recurring_payment_category** | **str** | Payment Category with allowed values: ONGOING, SUBSCRIPTION | [optional] 

## Example

```python
from yapily.models.vrp_configuration import VrpConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of VrpConfiguration from a JSON string
vrp_configuration_instance = VrpConfiguration.from_json(json)
# print the JSON string representation of the object
print VrpConfiguration.to_json()

# convert the object into a dict
vrp_configuration_dict = vrp_configuration_instance.to_dict()
# create an instance of VrpConfiguration from a dict
vrp_configuration_form_dict = vrp_configuration.from_dict(vrp_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


