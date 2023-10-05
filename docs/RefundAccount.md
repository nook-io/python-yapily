# RefundAccount

The account to which funds should be returned if the payment is to be later refunded.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) |  | [optional] 

## Example

```python
from yapily.models.refund_account import RefundAccount

# TODO update the JSON string below
json = "{}"
# create an instance of RefundAccount from a JSON string
refund_account_instance = RefundAccount.from_json(json)
# print the JSON string representation of the object
print RefundAccount.to_json()

# convert the object into a dict
refund_account_dict = refund_account_instance.to_dict()
# create an instance of RefundAccount from a dict
refund_account_form_dict = refund_account.from_dict(refund_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


