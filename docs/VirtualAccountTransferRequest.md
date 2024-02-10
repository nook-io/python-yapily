# VirtualAccountTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**VirtualAccountPaymentAmount**](VirtualAccountPaymentAmount.md) |  | 
**reference** | **str** | Reference to be associated with the transfer. This will be appear on the destination&#39;s bank statement | 
**source** | [**VirtualAccountTransferSource**](VirtualAccountTransferSource.md) |  | 
**destination** | [**VirtualAccountTransferDestination**](VirtualAccountTransferDestination.md) |  | 

## Example

```python
from yapily.models.virtual_account_transfer_request import VirtualAccountTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountTransferRequest from a JSON string
virtual_account_transfer_request_instance = VirtualAccountTransferRequest.from_json(json)
# print the JSON string representation of the object
print VirtualAccountTransferRequest.to_json()

# convert the object into a dict
virtual_account_transfer_request_dict = virtual_account_transfer_request_instance.to_dict()
# create an instance of VirtualAccountTransferRequest from a dict
virtual_account_transfer_request_form_dict = virtual_account_transfer_request.from_dict(virtual_account_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


