# RegisterWebhook201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the UUID of the registered webhook, used to update or remove the webhook | [optional] 
**application_id** | **str** | user applicaiton id | [optional] 
**categories** | **List[str]** |  | [optional] 
**callback_url** | [**RegisteredWebhookCallbackUrl**](RegisteredWebhookCallbackUrl.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**status** | [**WebhookStatusType**](WebhookStatusType.md) |  | [optional] 
**webhook_secret** | **str** | HMAC secret needed to validate that the request payload is genuine | [optional] 

## Example

```python
from yapily.models.register_webhook201_response_data import RegisterWebhook201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterWebhook201ResponseData from a JSON string
register_webhook201_response_data_instance = RegisterWebhook201ResponseData.from_json(json)
# print the JSON string representation of the object
print(RegisterWebhook201ResponseData.to_json())

# convert the object into a dict
register_webhook201_response_data_dict = register_webhook201_response_data_instance.to_dict()
# create an instance of RegisterWebhook201ResponseData from a dict
register_webhook201_response_data_from_dict = RegisterWebhook201ResponseData.from_dict(register_webhook201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


