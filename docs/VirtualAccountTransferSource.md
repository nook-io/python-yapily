# VirtualAccountTransferSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Identifies the Virtual Account from which the transfer was made | 

## Example

```python
from yapily.models.virtual_account_transfer_source import VirtualAccountTransferSource

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountTransferSource from a JSON string
virtual_account_transfer_source_instance = VirtualAccountTransferSource.from_json(json)
# print the JSON string representation of the object
print VirtualAccountTransferSource.to_json()

# convert the object into a dict
virtual_account_transfer_source_dict = virtual_account_transfer_source_instance.to_dict()
# create an instance of VirtualAccountTransferSource from a dict
virtual_account_transfer_source_form_dict = virtual_account_transfer_source.from_dict(virtual_account_transfer_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


