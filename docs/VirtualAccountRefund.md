# VirtualAccountRefund


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the refund | [optional] 
**original_payment** | [**VirtualAccountOriginalPayment**](VirtualAccountOriginalPayment.md) |  | [optional] 
**status** | **str** | The current state of the transaction &lt;br&gt; INITIATED - The transaction request is acknowledged and will not undergo validation checks &lt;br&gt; PENDING - Initial checks were successful and the payment is pending processing. This is primarily used for future dated payments that have not yet reached their payment date &lt;br&gt; PROCESSING - Initial checks succeeded and the transaction request is now being processed &lt;br&gt; COMPLETED - The transaction has been successfully processed (terminal status) &lt;br&gt; FAILED - An failure occured during transaction processing (terminal status) | [optional] 
**amount** | [**VirtualAccountPaymentAmount**](VirtualAccountPaymentAmount.md) |  | [optional] 
**issues** | [**List[ErrorIssue]**](ErrorIssue.md) | List of issues relating to a FAILED status | [optional] 
**reason** | **str** | The reason of the refund request | [optional] 
**payment_date** | **date** | Date on which the refund instruction will be executed, that may be in the future | [optional] 
**reference** | **str** | Reference to be associated with the refund. This will appear on the beneficiary&#39;s bank statement | [optional] 
**refund_to** | **str** | Indicates which account will be used for refund. | [optional] 
**refund_to_original_payer** | **bool** | Indicates if the refund is back to the original payer. | [optional] 
**beneficiary_type** | **str** | Indicates the type of Beneficiary as either an INDIVIDUAL or BUSINESS | [optional] 
**beneficiary_id** | **str** | Unique id of the beneficiary to whom the payment will be made | [optional] 
**created_date_time** | **datetime** | Date and time that the refund was created | [optional] 
**updated_date_time** | **datetime** | Date and time that the refund was updated | [optional] 

## Example

```python
from yapily.models.virtual_account_refund import VirtualAccountRefund

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountRefund from a JSON string
virtual_account_refund_instance = VirtualAccountRefund.from_json(json)
# print the JSON string representation of the object
print VirtualAccountRefund.to_json()

# convert the object into a dict
virtual_account_refund_dict = virtual_account_refund_instance.to_dict()
# create an instance of VirtualAccountRefund from a dict
virtual_account_refund_form_dict = virtual_account_refund.from_dict(virtual_account_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


