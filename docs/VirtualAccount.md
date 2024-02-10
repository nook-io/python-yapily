# VirtualAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the account | [optional] 
**created_date_time** | **datetime** | Date and time that the account was created | [optional] 
**status** | **str** | The current state of the Account &lt;br&gt; PENDING - Creation of the account is in progress &lt;br&gt; ACTIVE - The account is active and in use &lt;br&gt; FAILED - An issue occured during account creation &lt;br&gt; SUSPENDED - The account has been temporarily suspended by the account provider. It cannot currently be used &lt;br&gt; CLOSED - The account has been permanently closed and cannot be used | [optional] 
**nickname** | **str** | Reference that can be provided in order to help with identification of the account | [optional] 
**currency** | **str** | Three-letter ISO 4217 currency code | [optional] 
**balances** | [**List[VirtualAccountBalance]**](VirtualAccountBalance.md) |  | [optional] 
**bank_account** | [**VirtualAccountBankAccount**](VirtualAccountBankAccount.md) |  | [optional] 

## Example

```python
from yapily.models.virtual_account import VirtualAccount

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccount from a JSON string
virtual_account_instance = VirtualAccount.from_json(json)
# print the JSON string representation of the object
print VirtualAccount.to_json()

# convert the object into a dict
virtual_account_dict = virtual_account_instance.to_dict()
# create an instance of VirtualAccount from a dict
virtual_account_form_dict = virtual_account.from_dict(virtual_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


