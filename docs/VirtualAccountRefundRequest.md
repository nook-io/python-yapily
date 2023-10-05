# VirtualAccountRefundRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_payment** | [**VirtualAccountOriginalPayment**](VirtualAccountOriginalPayment.md) |  | 
**amount** | [**VirtualAccountRefundRequestAmount**](VirtualAccountRefundRequestAmount.md) |  | [optional] 
**reason** | **str** | Reason for the refund. Allowed values [REQUESTED_BY_CUSTOMER, DUPLICATE_PAYMENT, OTHER] | [optional] 
**payment_date** | **date** | The date that the refund instruction will be executed. Must be in the present or future | [optional] 
**reference** | **str** | Reference to be associated with the refund. This will appear on the beneficiary&#39;s bank statement | [optional] 
**refund_to** | **str** | Indicates which account will be used for refund. Allowed value: SOURCE | 
**refund_to_original_payer** | **bool** | __Conditional__. This field is required when refundTo is BENEFICIARY. Indicates if the refund is back to the original payer. Allowed value: true | [optional] 
**beneficiary_type** | **str** | __Conditional__. This field is required when refundTo is SOURCE. Indicates the type of Beneficiary as either an INDIVIDUAL or BUSINESS. | [optional] 
**beneficiary** | [**VirtualAccountRefundRequestBeneficiary**](VirtualAccountRefundRequestBeneficiary.md) |  | [optional] 

## Example

```python
from yapily.models.virtual_account_refund_request import VirtualAccountRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountRefundRequest from a JSON string
virtual_account_refund_request_instance = VirtualAccountRefundRequest.from_json(json)
# print the JSON string representation of the object
print VirtualAccountRefundRequest.to_json()

# convert the object into a dict
virtual_account_refund_request_dict = virtual_account_refund_request_instance.to_dict()
# create an instance of VirtualAccountRefundRequest from a dict
virtual_account_refund_request_form_dict = virtual_account_refund_request.from_dict(virtual_account_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


