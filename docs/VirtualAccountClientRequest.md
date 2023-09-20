# VirtualAccountClientRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**VirtualAccountClientType**](VirtualAccountClientType.md) |  | 
**individual** | [**VirtualAccountIndividualClient**](VirtualAccountIndividualClient.md) |  | [optional] 
**business** | [**VirtualAccountBusinessClient**](VirtualAccountBusinessClient.md) |  | [optional] 

## Example

```python
from yapily.models.virtual_account_client_request import VirtualAccountClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountClientRequest from a JSON string
virtual_account_client_request_instance = VirtualAccountClientRequest.from_json(json)
# print the JSON string representation of the object
print VirtualAccountClientRequest.to_json()

# convert the object into a dict
virtual_account_client_request_dict = virtual_account_client_request_instance.to_dict()
# create an instance of VirtualAccountClientRequest from a dict
virtual_account_client_request_form_dict = virtual_account_client_request.from_dict(virtual_account_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


