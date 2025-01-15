# OneTimeTokenRequest

The request body containing the `OneTimeTokenRequest` json payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_time_token** | **str** | __Mandatory__. The one time token to exchange for a consent token. | 

## Example

```python
from yapily.models.one_time_token_request import OneTimeTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OneTimeTokenRequest from a JSON string
one_time_token_request_instance = OneTimeTokenRequest.from_json(json)
# print the JSON string representation of the object
print(OneTimeTokenRequest.to_json())

# convert the object into a dict
one_time_token_request_dict = one_time_token_request_instance.to_dict()
# create an instance of OneTimeTokenRequest from a dict
one_time_token_request_from_dict = OneTimeTokenRequest.from_dict(one_time_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


