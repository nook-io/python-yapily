# SweepingControlParameters

Define the restrictions and limits for payment orders as part of Sweeping VRP consent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psu_authentication_methods** | **List[str]** | __Mandatory__. Defines the authentication method(s) allowed in payment submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED]. | 
**periodic_limits** | [**List[SweepingPeriodicLimits]**](SweepingPeriodicLimits.md) |  | 
**max_amount_per_payment** | [**Amount**](Amount.md) |  | 
**valid_from** | **datetime** | __Optional__. Start date when the consent becomes valid. | [optional] 
**valid_to** | **datetime** | __Optional__. End date when the consent expires and becomes invalid. | [optional] 

## Example

```python
from yapily.models.sweeping_control_parameters import SweepingControlParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SweepingControlParameters from a JSON string
sweeping_control_parameters_instance = SweepingControlParameters.from_json(json)
# print the JSON string representation of the object
print SweepingControlParameters.to_json()

# convert the object into a dict
sweeping_control_parameters_dict = sweeping_control_parameters_instance.to_dict()
# create an instance of SweepingControlParameters from a dict
sweeping_control_parameters_form_dict = sweeping_control_parameters.from_dict(sweeping_control_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


