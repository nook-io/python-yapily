# PaymentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**payment_idempotency_id** | **str** |  | [optional] 
**payment_lifecycle_id** | **str** |  | [optional] 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**status_details** | [**PaymentStatusDetails**](PaymentStatusDetails.md) |  | [optional] 
**payer** | [**Payer**](Payer.md) |  | [optional] 
**payee_details** | [**Payee**](Payee.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount_details** | [**Amount**](Amount.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**first_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**first_payment_date_time** | **datetime** |  | [optional] 
**next_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**next_payment_date_time** | **datetime** |  | [optional] 
**final_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**final_payment_date_time** | **datetime** |  | [optional] 
**number_of_payments** | **int** |  | [optional] 
**previous_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**previous_payment_date_time** | **datetime** |  | [optional] 
**charge_details** | [**List[PaymentChargeDetails]**](PaymentChargeDetails.md) |  | [optional] 
**scheduled_payment_type** | **str** |  | [optional] 
**scheduled_payment_date_time** | **datetime** |  | [optional] 
**frequency** | [**FrequencyResponse**](FrequencyResponse.md) |  | [optional] 
**currency_of_transfer** | **str** |  | [optional] 
**purpose** | **str** |  | [optional] 
**priority** | [**PriorityCodeEnum**](PriorityCodeEnum.md) |  | [optional] 
**exchange_rate** | [**ExchangeRateInformationResponse**](ExchangeRateInformationResponse.md) |  | [optional] 
**refund_account** | [**RefundAccount**](RefundAccount.md) |  | [optional] 
**bulk_amount_sum** | **float** |  | [optional] 

## Example

```python
from yapily.models.payment_response import PaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponse from a JSON string
payment_response_instance = PaymentResponse.from_json(json)
# print the JSON string representation of the object
print PaymentResponse.to_json()

# convert the object into a dict
payment_response_dict = payment_response_instance.to_dict()
# create an instance of PaymentResponse from a dict
payment_response_form_dict = payment_response.from_dict(payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


