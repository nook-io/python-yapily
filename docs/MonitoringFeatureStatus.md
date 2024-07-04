# MonitoringFeatureStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_tested** | **datetime** |  | [optional] 
**span** | **str** |  | [optional] 
**status** | [**MonitoringStatusEnum**](MonitoringStatusEnum.md) |  | [optional] 

## Example

```python
from yapily.models.monitoring_feature_status import MonitoringFeatureStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoringFeatureStatus from a JSON string
monitoring_feature_status_instance = MonitoringFeatureStatus.from_json(json)
# print the JSON string representation of the object
print MonitoringFeatureStatus.to_json()

# convert the object into a dict
monitoring_feature_status_dict = monitoring_feature_status_instance.to_dict()
# create an instance of MonitoringFeatureStatus from a dict
monitoring_feature_status_form_dict = monitoring_feature_status.from_dict(monitoring_feature_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


