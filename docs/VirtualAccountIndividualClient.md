# VirtualAccountIndividualClient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | 
**address** | [**VirtualAccountAddress**](VirtualAccountAddress.md) |  | [optional] 
**birth_date** | **date** |  | 
**email** | **str** |  | 
**phone** | **str** |  | [optional] 

## Example

```python
from yapily.models.virtual_account_individual_client import VirtualAccountIndividualClient

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountIndividualClient from a JSON string
virtual_account_individual_client_instance = VirtualAccountIndividualClient.from_json(json)
# print the JSON string representation of the object
print VirtualAccountIndividualClient.to_json()

# convert the object into a dict
virtual_account_individual_client_dict = virtual_account_individual_client_instance.to_dict()
# create an instance of VirtualAccountIndividualClient from a dict
virtual_account_individual_client_form_dict = virtual_account_individual_client.from_dict(virtual_account_individual_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


