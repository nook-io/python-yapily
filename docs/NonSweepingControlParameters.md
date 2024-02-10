# NonSweepingControlParameters

Define the restrictions and limits for payment orders as part of Non-Sweeping VRP consent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psu_authentication_methods** | **List[str]** | __Mandatory__. Defines the authentication method(s) allowed in payment submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED]. | 
**periodic_limits** | [**List[NonSweepingPeriodicLimits]**](NonSweepingPeriodicLimits.md) |  | 
**max_amount_per_payment** | [**Amount**](Amount.md) |  | 
**max_cumulative_amount** | [**Amount**](Amount.md) |  | [optional] 
**max_cumulative_number_of_payments** | **int** | __Optional__. Max number of payments that can be submitted under this consent. | [optional] 
**valid_from** | **datetime** | __Optional__. Start date when the consent becomes valid. | [optional] 
**valid_to** | **datetime** | __Optional__. End date when the consent expires and becomes invalid. | [optional] 

## Example

```python
from yapily.models.non_sweeping_control_parameters import NonSweepingControlParameters

# TODO update the JSON string below
json = "{}"
# create an instance of NonSweepingControlParameters from a JSON string
non_sweeping_control_parameters_instance = NonSweepingControlParameters.from_json(json)
# print the JSON string representation of the object
print NonSweepingControlParameters.to_json()

# convert the object into a dict
non_sweeping_control_parameters_dict = non_sweeping_control_parameters_instance.to_dict()
# create an instance of NonSweepingControlParameters from a dict
non_sweeping_control_parameters_form_dict = non_sweeping_control_parameters.from_dict(non_sweeping_control_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


