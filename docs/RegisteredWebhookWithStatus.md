# RegisteredWebhookWithStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the UUID of the registered webhook, used to update or remove the webhook | [optional] 
**application_id** | **str** | user applicaiton id | [optional] 
**categories** | **List[str]** |  | [optional] 
**callback_url** | [**RegisteredWebhookCallbackUrl**](RegisteredWebhookCallbackUrl.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**status** | [**WebhookStatusType**](WebhookStatusType.md) |  | [optional] 

## Example

```python
from yapily.models.registered_webhook_with_status import RegisteredWebhookWithStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredWebhookWithStatus from a JSON string
registered_webhook_with_status_instance = RegisteredWebhookWithStatus.from_json(json)
# print the JSON string representation of the object
print RegisteredWebhookWithStatus.to_json()

# convert the object into a dict
registered_webhook_with_status_dict = registered_webhook_with_status_instance.to_dict()
# create an instance of RegisteredWebhookWithStatus from a dict
registered_webhook_with_status_from_dict = RegisteredWebhookWithStatus.from_dict(registered_webhook_with_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


