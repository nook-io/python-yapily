# AccountIdentificationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccountIdentificationTypeResponse**](AccountIdentificationTypeResponse.md) |  | [optional] 
**identification** | **str** | The value associated with the account identification type.&lt;br&gt;&lt;br&gt; See [Account Identification Combinations](https://docs.yapily.com/pages/payments/payments-resources/intro-to-payment-execution/#account-identifications-combinations) for more information on the format of the values. | [optional] 

## Example

```python
from yapily.models.account_identification_response import AccountIdentificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountIdentificationResponse from a JSON string
account_identification_response_instance = AccountIdentificationResponse.from_json(json)
# print the JSON string representation of the object
print AccountIdentificationResponse.to_json()

# convert the object into a dict
account_identification_response_dict = account_identification_response_instance.to_dict()
# create an instance of AccountIdentificationResponse from a dict
account_identification_response_from_dict = AccountIdentificationResponse.from_dict(account_identification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


