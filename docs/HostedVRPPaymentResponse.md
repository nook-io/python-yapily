# HostedVRPPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payment_idempotency_id** | **str** |  | [optional] 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**reference** | **str** | __Optional__. The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**payee** | [**Payee**](Payee.md) |  | [optional] 
**payer** | [**HostedVrpPayerResponse**](HostedVrpPayerResponse.md) |  | [optional] 
**refund_account** | [**HostedVrpRefundAccount**](HostedVrpRefundAccount.md) |  | [optional] 
**risk** | [**PaymentRisk**](PaymentRisk.md) |  | [optional] 
**payment_lifecycle_id** | **str** | The Unique Identifier provided by TPP in the Payment request to identify the payment. | [optional] 
**expected_execution_time** | **datetime** |  | [optional] 
**expected_settlement_time** | **datetime** |  | [optional] 
**institution_payment_id** | **str** |  | [optional] 
**status_details** | [**HostedPaymentStatusDetails**](HostedPaymentStatusDetails.md) |  | [optional] 

## Example

```python
from yapily.models.hosted_vrp_payment_response import HostedVRPPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostedVRPPaymentResponse from a JSON string
hosted_vrp_payment_response_instance = HostedVRPPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(HostedVRPPaymentResponse.to_json())

# convert the object into a dict
hosted_vrp_payment_response_dict = hosted_vrp_payment_response_instance.to_dict()
# create an instance of HostedVRPPaymentResponse from a dict
hosted_vrp_payment_response_from_dict = HostedVRPPaymentResponse.from_dict(hosted_vrp_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


