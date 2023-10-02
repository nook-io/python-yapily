# MonitoringEndpointStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_tested** | **datetime** |  | [optional] 
**resource_endpoint** | **str** |  | [optional] 
**span** | **str** |  | [optional] 
**status** | [**MonitoringStatusEnum**](MonitoringStatusEnum.md) |  | [optional] 

## Example

```python
from yapily.models.monitoring_endpoint_status import MonitoringEndpointStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoringEndpointStatus from a JSON string
monitoring_endpoint_status_instance = MonitoringEndpointStatus.from_json(json)
# print the JSON string representation of the object
print MonitoringEndpointStatus.to_json()

# convert the object into a dict
monitoring_endpoint_status_dict = monitoring_endpoint_status_instance.to_dict()
# create an instance of MonitoringEndpointStatus from a dict
monitoring_endpoint_status_form_dict = monitoring_endpoint_status.from_dict(monitoring_endpoint_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


