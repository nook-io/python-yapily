# AccountRequest

__Conditional__. Used to further specify details of the `Consent` to request <br><br>Conditions:<ol><li>Mandatory to specify the individual scopes to request from the user at the `Institution` for an account authorisation</li><li>Mandatory to specify an expiry time on the created `Consent` at which time will render it unusable</li><li>Mandatory to specify the date range that the created `Consent` will be able to access transactions for (given the range is support for the `Institution`)</li></ol>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_from** | **datetime** | __Optional__. Specifies the earliest date of the transaction records to be returned.&lt;br&gt;&lt;br&gt; You must supply this field to retrieve transactions older than 90 days for banks accessed via the the [CBI Globe Gateway](https://docs.yapily.com/pages/data/financial-data-resources/data-restrictions/#cbi-globe-gateway). | [optional] 
**transaction_to** | **datetime** | __Optional__. Specifies the latest date of the transaction records to be returned. | [optional] 
**expires_at** | **datetime** | __Optional__. Used to set a hard date for when the user&#39;s associated &#x60;Consent&#x60; will expire.&lt;br&gt;&lt;br&gt;**Note**: If this supported by the bank, specifying this is property is opting out of having a long-lived consent that can be perpetually re-authorised by the user. This will add an &#x60;expiresAt&#x60; field on the &#x60;Consent&#x60; object which will render it unusable after this date.&lt;br&gt;&lt;br&gt;**Note**: This is not supported by every &#x60;Institution&#x60;. In such case, the request will not fail but the property will be ignored and the created &#x60;Consent&#x60; will not have an expiry date. | [optional] 
**account_identifiers** | [**AccountInfo**](AccountInfo.md) |  | [optional] 
**account_identifiers_for_transaction** | [**List[AccountInfo]**](AccountInfo.md) | __Conditional__. Used to create a request for the transactions of the account specified. Once the user authorises the request, only the transactions can be obtained by executing [GET Account Transactions](./#get-account-transactions). &lt;br&gt;&lt;br&gt;This can be specified in conjunction with &#x60;accountIdentifiersForBalance&#x60; to generate a &#x60;Consent&#x60; that can both access the accounts balance and transactions. | [optional] 
**account_identifiers_for_balance** | [**List[AccountInfo]**](AccountInfo.md) | __Conditional__. Used to create a request for the balance of the account specified. Once the user authorises the request, only the balance can be obtained by executing [GET Account Balances](./#get-account-balances).&lt;br&gt;&lt;br&gt; This can be specified in conjunction with &#x60;accountIdentifiersForTransaction&#x60; to generate a &#x60;Consent&#x60; that can both access the accounts balance and transactions. | [optional] 
**feature_scope** | [**List[FeatureEnum]**](FeatureEnum.md) | __Optional__. Used to granularly specify the set of features that the user will give their consent for when requesting access to their account information. Depending on the &#x60;Institution&#x60;, this may also populate a consent screen which list these scopes before the user authorises.&lt;br&gt;&lt;br&gt;This endpoint accepts allow all [Financial Data Features](/guides/financial-data/features/#feature-list) that the &#x60;Institution&#x60; supports.To find out which scopes an &#x60;Institution&#x60; supports, check [GET Institution](./#get-institution). | [optional] 

## Example

```python
from yapily.models.account_request import AccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRequest from a JSON string
account_request_instance = AccountRequest.from_json(json)
# print the JSON string representation of the object
print AccountRequest.to_json()

# convert the object into a dict
account_request_dict = account_request_instance.to_dict()
# create an instance of AccountRequest from a dict
account_request_from_dict = AccountRequest.from_dict(account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


