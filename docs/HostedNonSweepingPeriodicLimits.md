# HostedNonSweepingPeriodicLimits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_amount** | [**Amount**](Amount.md) |  | 
**frequency** | **str** | __Mandatory__. Frequency for which the payment limits are enforced. Allowed values are [MONTHLY]. | 
**alignment** | **str** | __Mandatory__. Period alignment for which the payment limits are enforced. Allowed values are [CONSENT, CALENDAR]. If CONSENT, then period starts on consent creation date. If CALENDAR, then period lines up with the frequency e.g. WEEKLY period will begin at start of the week in question. | 

## Example

```python
from yapily.models.hosted_non_sweeping_periodic_limits import HostedNonSweepingPeriodicLimits

# TODO update the JSON string below
json = "{}"
# create an instance of HostedNonSweepingPeriodicLimits from a JSON string
hosted_non_sweeping_periodic_limits_instance = HostedNonSweepingPeriodicLimits.from_json(json)
# print the JSON string representation of the object
print HostedNonSweepingPeriodicLimits.to_json()

# convert the object into a dict
hosted_non_sweeping_periodic_limits_dict = hosted_non_sweeping_periodic_limits_instance.to_dict()
# create an instance of HostedNonSweepingPeriodicLimits from a dict
hosted_non_sweeping_periodic_limits_form_dict = hosted_non_sweeping_periodic_limits.from_dict(hosted_non_sweeping_periodic_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


