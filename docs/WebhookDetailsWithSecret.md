# WebhookDetailsWithSecret


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**data** | [**RegisterWebhook201ResponseData**](RegisterWebhook201ResponseData.md) |  | [optional] 

## Example

```python
from yapily.models.webhook_details_with_secret import WebhookDetailsWithSecret

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDetailsWithSecret from a JSON string
webhook_details_with_secret_instance = WebhookDetailsWithSecret.from_json(json)
# print the JSON string representation of the object
print WebhookDetailsWithSecret.to_json()

# convert the object into a dict
webhook_details_with_secret_dict = webhook_details_with_secret_instance.to_dict()
# create an instance of WebhookDetailsWithSecret from a dict
webhook_details_with_secret_from_dict = WebhookDetailsWithSecret.from_dict(webhook_details_with_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


