# RegisteredWebhookCallbackUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main** | [**RegisteredWebhookCallbackUrlMain**](RegisteredWebhookCallbackUrlMain.md) |  | [optional] 
**backup** | [**RegisterWebhookRequestCallbackUrlBackup**](RegisterWebhookRequestCallbackUrlBackup.md) |  | [optional] 

## Example

```python
from yapily.models.registered_webhook_callback_url import RegisteredWebhookCallbackUrl

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredWebhookCallbackUrl from a JSON string
registered_webhook_callback_url_instance = RegisteredWebhookCallbackUrl.from_json(json)
# print the JSON string representation of the object
print(RegisteredWebhookCallbackUrl.to_json())

# convert the object into a dict
registered_webhook_callback_url_dict = registered_webhook_callback_url_instance.to_dict()
# create an instance of RegisteredWebhookCallbackUrl from a dict
registered_webhook_callback_url_from_dict = RegisteredWebhookCallbackUrl.from_dict(registered_webhook_callback_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


