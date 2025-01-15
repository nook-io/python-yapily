# HostedVRPLimitsRequest

The restrictions and limits for payments executed under the VRP consent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodic_limits** | [**List[HostedNonSweepingPeriodicLimits]**](HostedNonSweepingPeriodicLimits.md) |  | [optional] 
**max_amount_per_payment** | [**Amount**](Amount.md) | __Optional__. Max amount that can be submitted per payment. | [optional] 
**max_cumulative_amount** | [**Amount**](Amount.md) | __Optional__. Max cumulative amount that can be submitted under this consent. | [optional] 
**max_cumulative_number_of_payments** | **int** | __Optional__. Max number of payments that can be submitted under this consent. | [optional] 

## Example

```python
from yapily.models.hosted_vrp_limits_request import HostedVRPLimitsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostedVRPLimitsRequest from a JSON string
hosted_vrp_limits_request_instance = HostedVRPLimitsRequest.from_json(json)
# print the JSON string representation of the object
print(HostedVRPLimitsRequest.to_json())

# convert the object into a dict
hosted_vrp_limits_request_dict = hosted_vrp_limits_request_instance.to_dict()
# create an instance of HostedVRPLimitsRequest from a dict
hosted_vrp_limits_request_from_dict = HostedVRPLimitsRequest.from_dict(hosted_vrp_limits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


