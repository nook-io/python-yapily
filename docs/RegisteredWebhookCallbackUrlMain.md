# RegisteredWebhookCallbackUrlMain

primary webhook url used to send events to

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from yapily.models.registered_webhook_callback_url_main import RegisteredWebhookCallbackUrlMain

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredWebhookCallbackUrlMain from a JSON string
registered_webhook_callback_url_main_instance = RegisteredWebhookCallbackUrlMain.from_json(json)
# print the JSON string representation of the object
print RegisteredWebhookCallbackUrlMain.to_json()

# convert the object into a dict
registered_webhook_callback_url_main_dict = registered_webhook_callback_url_main_instance.to_dict()
# create an instance of RegisteredWebhookCallbackUrlMain from a dict
registered_webhook_callback_url_main_from_dict = RegisteredWebhookCallbackUrlMain.from_dict(registered_webhook_callback_url_main_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


