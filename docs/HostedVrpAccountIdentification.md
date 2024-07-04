# HostedVrpAccountIdentification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Used to describe the format of the account.&lt;br&gt;&lt;br&gt; Allowed values: &lt;br&gt;MASKED_ACCOUNT_NUMBER&lt;br&gt;SORT_CODE&lt;br&gt;ACCOUNT_NUMBER  | 
**identification** | **str** | __Mandatory__. The value associated with the account identification type.&lt;br&gt;&lt;br&gt; See [Account Identification Combinations](https://docs.yapily.com/pages/key-concepts/payments/payment-execution/intro-to-payment-execution/#account-identifications-combinations) for more information on the format of the values. | 

## Example

```python
from yapily.models.hosted_vrp_account_identification import HostedVrpAccountIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of HostedVrpAccountIdentification from a JSON string
hosted_vrp_account_identification_instance = HostedVrpAccountIdentification.from_json(json)
# print the JSON string representation of the object
print HostedVrpAccountIdentification.to_json()

# convert the object into a dict
hosted_vrp_account_identification_dict = hosted_vrp_account_identification_instance.to_dict()
# create an instance of HostedVrpAccountIdentification from a dict
hosted_vrp_account_identification_form_dict = hosted_vrp_account_identification.from_dict(hosted_vrp_account_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


