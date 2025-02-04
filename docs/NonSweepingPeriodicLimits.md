# NonSweepingPeriodicLimits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_max_amount** | [**Amount**](Amount.md) | __Mandatory__. Maximum amount that can be specified in all payment instructions in a given period under this VRP consent. If the Alignment is Calendar, the limit is pro-rated in the first period to the remaining number of days. | 
**frequency** | **str** | __Mandatory__. Frequency for which the payment limits are enforced. Allowed values are [DAILY, WEEKLY, EVERY_TWO_WEEKS, MONTHLY, YEARLY]. This field cannot be enforced when &#x60;recurringPaymentCategory&#x3D;ONGOING&#x60;. | [optional] 
**alignment** | **str** | __Mandatory__. Period alignment for which the payment limits are enforced. Allowed values are [CONSENT, CALENDAR]. If CONSENT, then period starts on consent creation date. If CALENDAR, then period lines up with the frequency e.g. WEEKLY period will begin at start of the week in question. This field cannot be enforced when &#x60;recurringPaymentCategory&#x3D;ONGOING&#x60;. | [optional] 
**max_number_of_payments** | **int** | __Optional__. Max number of payments that can be submitted under this period. | [optional] 

## Example

```python
from yapily.models.non_sweeping_periodic_limits import NonSweepingPeriodicLimits

# TODO update the JSON string below
json = "{}"
# create an instance of NonSweepingPeriodicLimits from a JSON string
non_sweeping_periodic_limits_instance = NonSweepingPeriodicLimits.from_json(json)
# print the JSON string representation of the object
print NonSweepingPeriodicLimits.to_json()

# convert the object into a dict
non_sweeping_periodic_limits_dict = non_sweeping_periodic_limits_instance.to_dict()
# create an instance of NonSweepingPeriodicLimits from a dict
non_sweeping_periodic_limits_from_dict = NonSweepingPeriodicLimits.from_dict(non_sweeping_periodic_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


