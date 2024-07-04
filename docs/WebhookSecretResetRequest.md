# WebhookSecretResetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay** | **float** | delay in seconds | 

## Example

```python
from yapily.models.webhook_secret_reset_request import WebhookSecretResetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretResetRequest from a JSON string
webhook_secret_reset_request_instance = WebhookSecretResetRequest.from_json(json)
# print the JSON string representation of the object
print WebhookSecretResetRequest.to_json()

# convert the object into a dict
webhook_secret_reset_request_dict = webhook_secret_reset_request_instance.to_dict()
# create an instance of WebhookSecretResetRequest from a dict
webhook_secret_reset_request_form_dict = webhook_secret_reset_request.from_dict(webhook_secret_reset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


