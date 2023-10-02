# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the account. | [optional] 
**type** | **str** | Specifies the type of account e.g. (BUSINESS_CURRENT). | [optional] 
**description** | **str** | Product name as defined by the financial institution for this account | [optional] 
**balance** | **float** | Main / headline balance for the account. &lt;br&gt;&lt;br&gt; Use of this field is recommended as fallback only. Instead, use of the typed balances (accountBalances) is recommended. | [optional] 
**currency** | **str** | Currency the bank account balance is denoted in. &lt;br&gt;&lt;br&gt; Specified as a 3-letter ISO 4217 currency code | [optional] 
**usage_type** | [**UsageType**](UsageType.md) |  | [optional] 
**account_type** | [**AccountType**](AccountType.md) |  | [optional] 
**nickname** | **str** | Nickname of the account that was provided by the account owner. &lt;br&gt;&lt;br&gt; May be used to aid identification of the account. | [optional] 
**details** | **str** | Supplementary specifications that might be provided by the Bank. These provide further characteristics about the account. | [optional] 
**account_names** | [**List[AccountName]**](AccountName.md) |  | [optional] 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) |  | [optional] 
**account_balances** | [**List[AccountBalance]**](AccountBalance.md) |  | [optional] 
**consolidated_account_information** | [**ConsolidatedAccountInformation**](ConsolidatedAccountInformation.md) |  | [optional] 

## Example

```python
from yapily.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print Account.to_json()

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_form_dict = account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


