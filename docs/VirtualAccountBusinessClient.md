# VirtualAccountBusinessClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**VirtualAccountClientBusinessType**](VirtualAccountClientBusinessType.md) |  | 
**registration_number** | **str** |  | 
**registered_address** | [**VirtualAccountAddress**](VirtualAccountAddress.md) |  | 
**trading_address** | [**VirtualAccountAddress**](VirtualAccountAddress.md) |  | [optional] 
**contact_name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from yapily.models.virtual_account_business_client import VirtualAccountBusinessClient

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountBusinessClient from a JSON string
virtual_account_business_client_instance = VirtualAccountBusinessClient.from_json(json)
# print the JSON string representation of the object
print VirtualAccountBusinessClient.to_json()

# convert the object into a dict
virtual_account_business_client_dict = virtual_account_business_client_instance.to_dict()
# create an instance of VirtualAccountBusinessClient from a dict
virtual_account_business_client_form_dict = virtual_account_business_client.from_dict(virtual_account_business_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


