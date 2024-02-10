# UpdateVirtualAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** | New reference that can be provided in order to help with identification of the account | [optional] 
**status** | **str** | New state of the Account: CLOSED - The account has been permanently closed and cannot be used | [optional] 

## Example

```python
from yapily.models.update_virtual_account_request import UpdateVirtualAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVirtualAccountRequest from a JSON string
update_virtual_account_request_instance = UpdateVirtualAccountRequest.from_json(json)
# print the JSON string representation of the object
print UpdateVirtualAccountRequest.to_json()

# convert the object into a dict
update_virtual_account_request_dict = update_virtual_account_request_instance.to_dict()
# create an instance of UpdateVirtualAccountRequest from a dict
update_virtual_account_request_form_dict = update_virtual_account_request.from_dict(update_virtual_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


