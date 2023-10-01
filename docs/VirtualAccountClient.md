# VirtualAccountClient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id generated in the on-boarding process, it will be used as client-id for virtual accounts request | [optional] 
**type** | [**VirtualAccountClientType**](VirtualAccountClientType.md) |  | [optional] 
**kyc_status** | [**VirtualAccountKycStatus**](VirtualAccountKycStatus.md) |  | [optional] 
**status** | [**VirtualAccountClientStatus**](VirtualAccountClientStatus.md) |  | [optional] 
**created_date_time** | **datetime** |  | [optional] 
**individual** | [**VirtualAccountIndividualClient**](VirtualAccountIndividualClient.md) |  | [optional] 
**business** | [**VirtualAccountBusinessClient**](VirtualAccountBusinessClient.md) |  | [optional] 

## Example

```python
from yapily.models.virtual_account_client import VirtualAccountClient

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountClient from a JSON string
virtual_account_client_instance = VirtualAccountClient.from_json(json)
# print the JSON string representation of the object
print VirtualAccountClient.to_json()

# convert the object into a dict
virtual_account_client_dict = virtual_account_client_instance.to_dict()
# create an instance of VirtualAccountClient from a dict
virtual_account_client_form_dict = virtual_account_client.from_dict(virtual_account_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


