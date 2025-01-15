# HostedVrpRefundAccount

The account to which funds should be returned if the payment is to be later refunded.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**account_identifications** | [**List[HostedVrpAccountIdentification]**](HostedVrpAccountIdentification.md) |  | [optional] 

## Example

```python
from yapily.models.hosted_vrp_refund_account import HostedVrpRefundAccount

# TODO update the JSON string below
json = "{}"
# create an instance of HostedVrpRefundAccount from a JSON string
hosted_vrp_refund_account_instance = HostedVrpRefundAccount.from_json(json)
# print the JSON string representation of the object
print HostedVrpRefundAccount.to_json()

# convert the object into a dict
hosted_vrp_refund_account_dict = hosted_vrp_refund_account_instance.to_dict()
# create an instance of HostedVrpRefundAccount from a dict
hosted_vrp_refund_account_from_dict = HostedVrpRefundAccount.from_dict(hosted_vrp_refund_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


