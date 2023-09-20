# VirtualAccountTransferDestination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Identifies the Virtual Account to which the transfer was made | 

## Example

```python
from yapily.models.virtual_account_transfer_destination import VirtualAccountTransferDestination

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountTransferDestination from a JSON string
virtual_account_transfer_destination_instance = VirtualAccountTransferDestination.from_json(json)
# print the JSON string representation of the object
print VirtualAccountTransferDestination.to_json()

# convert the object into a dict
virtual_account_transfer_destination_dict = virtual_account_transfer_destination_instance.to_dict()
# create an instance of VirtualAccountTransferDestination from a dict
virtual_account_transfer_destination_form_dict = virtual_account_transfer_destination.from_dict(virtual_account_transfer_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


