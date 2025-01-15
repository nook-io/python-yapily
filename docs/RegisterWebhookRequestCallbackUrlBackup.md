# RegisterWebhookRequestCallbackUrlBackup

backup webhook url used to send events to in case the main one is not responding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from yapily.models.register_webhook_request_callback_url_backup import RegisterWebhookRequestCallbackUrlBackup

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterWebhookRequestCallbackUrlBackup from a JSON string
register_webhook_request_callback_url_backup_instance = RegisterWebhookRequestCallbackUrlBackup.from_json(json)
# print the JSON string representation of the object
print(RegisterWebhookRequestCallbackUrlBackup.to_json())

# convert the object into a dict
register_webhook_request_callback_url_backup_dict = register_webhook_request_callback_url_backup_instance.to_dict()
# create an instance of RegisterWebhookRequestCallbackUrlBackup from a dict
register_webhook_request_callback_url_backup_from_dict = RegisterWebhookRequestCallbackUrlBackup.from_dict(register_webhook_request_callback_url_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


