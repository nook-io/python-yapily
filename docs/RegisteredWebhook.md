# RegisteredWebhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the UUID of the registered webhook, used to update or remove the webhook | [optional] 
**application_id** | **str** | user applicaiton id | [optional] 
**categories** | **List[str]** |  | [optional] 
**callback_url** | [**RegisteredWebhookCallbackUrl**](RegisteredWebhookCallbackUrl.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from yapily.models.registered_webhook import RegisteredWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredWebhook from a JSON string
registered_webhook_instance = RegisteredWebhook.from_json(json)
# print the JSON string representation of the object
print RegisteredWebhook.to_json()

# convert the object into a dict
registered_webhook_dict = registered_webhook_instance.to_dict()
# create an instance of RegisteredWebhook from a dict
registered_webhook_from_dict = RegisteredWebhook.from_dict(registered_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


