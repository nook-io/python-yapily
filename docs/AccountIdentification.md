# AccountIdentification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccountIdentificationType**](AccountIdentificationType.md) |  | 
**identification** | **str** | __Mandatory__. The value associated with the account identification type.&lt;br&gt;&lt;br&gt; See [Account Identification Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#account-identifications-combinations) for more information on the format of the values. | 

## Example

```python
from yapily.models.account_identification import AccountIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of AccountIdentification from a JSON string
account_identification_instance = AccountIdentification.from_json(json)
# print the JSON string representation of the object
print(AccountIdentification.to_json())

# convert the object into a dict
account_identification_dict = account_identification_instance.to_dict()
# create an instance of AccountIdentification from a dict
account_identification_from_dict = AccountIdentification.from_dict(account_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


