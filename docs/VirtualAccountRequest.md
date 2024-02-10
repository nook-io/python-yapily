# VirtualAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** | Reference that can be provided in order to help with identification of the account | 
**currency** | **str** | Three-letter ISO 4217 currency code | 

## Example

```python
from yapily.models.virtual_account_request import VirtualAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountRequest from a JSON string
virtual_account_request_instance = VirtualAccountRequest.from_json(json)
# print the JSON string representation of the object
print VirtualAccountRequest.to_json()

# convert the object into a dict
virtual_account_request_dict = virtual_account_request_instance.to_dict()
# create an instance of VirtualAccountRequest from a dict
virtual_account_request_form_dict = virtual_account_request.from_dict(virtual_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


