# AccountInfo

__Conditional__. Used to create a request for the balance of the account specified. Once the user authorises the request, only the balance can be obtained by executing [GET Account Balances](./#get-account-balances).<br><br> This can be specified in conjunction with `accountIdentifiersForTransaction` to generate a `Consent` that can both access the accounts balance and transactions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | __Mandatory__. Unique identifier of the account. | 
**account_identification** | [**AccountIdentification**](AccountIdentification.md) |  | 

## Example

```python
from yapily.models.account_info import AccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfo from a JSON string
account_info_instance = AccountInfo.from_json(json)
# print the JSON string representation of the object
print AccountInfo.to_json()

# convert the object into a dict
account_info_dict = account_info_instance.to_dict()
# create an instance of AccountInfo from a dict
account_info_form_dict = account_info.from_dict(account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


