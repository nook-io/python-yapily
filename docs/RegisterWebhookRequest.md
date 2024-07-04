# RegisterWebhookRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | user application id | 
**categories** | **List[str]** |  | 
**callback_url** | [**RegisterWebhookRequestCallbackUrl**](RegisterWebhookRequestCallbackUrl.md) |  | 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from yapily.models.register_webhook_request import RegisterWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterWebhookRequest from a JSON string
register_webhook_request_instance = RegisterWebhookRequest.from_json(json)
# print the JSON string representation of the object
print RegisterWebhookRequest.to_json()

# convert the object into a dict
register_webhook_request_dict = register_webhook_request_instance.to_dict()
# create an instance of RegisterWebhookRequest from a dict
register_webhook_request_form_dict = register_webhook_request.from_dict(register_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


