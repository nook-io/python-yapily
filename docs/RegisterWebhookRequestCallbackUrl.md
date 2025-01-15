# RegisterWebhookRequestCallbackUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main** | [**RegisterWebhookRequestCallbackUrlMain**](RegisterWebhookRequestCallbackUrlMain.md) |  | 
**backup** | [**RegisterWebhookRequestCallbackUrlBackup**](RegisterWebhookRequestCallbackUrlBackup.md) |  | [optional] 

## Example

```python
from yapily.models.register_webhook_request_callback_url import RegisterWebhookRequestCallbackUrl

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterWebhookRequestCallbackUrl from a JSON string
register_webhook_request_callback_url_instance = RegisterWebhookRequestCallbackUrl.from_json(json)
# print the JSON string representation of the object
print(RegisterWebhookRequestCallbackUrl.to_json())

# convert the object into a dict
register_webhook_request_callback_url_dict = register_webhook_request_callback_url_instance.to_dict()
# create an instance of RegisterWebhookRequestCallbackUrl from a dict
register_webhook_request_callback_url_from_dict = RegisterWebhookRequestCallbackUrl.from_dict(register_webhook_request_callback_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


