# PaymentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the payment. | [optional] 
**institution_consent_id** | **str** | Identification of the consent at the Institution. | [optional] 
**payment_idempotency_id** | **str** | __Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters. | [optional] 
**payment_lifecycle_id** | **str** |  | [optional] 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**status_details** | [**PaymentStatusDetails**](PaymentStatusDetails.md) |  | [optional] 
**payer** | [**Payer**](Payer.md) |  | [optional] 
**payee_details** | [**Payee**](Payee.md) |  | [optional] 
**reference** | **str** | __Optional__. The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**amount** | **float** | Monetary amount. | [optional] 
**currency** | **str** | Currency the payment amount is denoted in. Specified as a 3-letter ISO 4217 code. | [optional] 
**amount_details** | [**Amount**](Amount.md) |  | [optional] 
**created_at** | **datetime** | Date and time of when the payment request was created. | [optional] 
**first_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**first_payment_date_time** | **datetime** | Date and time of when the first payment request is to be made. | [optional] 
**next_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**next_payment_date_time** | **datetime** | __Conditional__. Defines when the recurring payment is to be made. | [optional] 
**final_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**final_payment_date_time** | **datetime** | Date and time of when the final payment is to be made. | [optional] 
**number_of_payments** | **int** | Number of recurring payment requests to be made as part of the instructed payment schedule. | [optional] 
**previous_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**previous_payment_date_time** | **datetime** | Date and time of when the previous payment request was posted. | [optional] 
**charge_details** | [**List[PaymentChargeDetails]**](PaymentChargeDetails.md) |  | [optional] 
**scheduled_payment_type** | **str** | Details the execution type and the payment date between the payer and the payee. | [optional] 
**scheduled_payment_date_time** | **datetime** | Date and time of when the scheduled payment request will be made. | [optional] 
**frequency** | [**FrequencyResponse**](FrequencyResponse.md) |  | [optional] 
**currency_of_transfer** | **str** | __Mandatory__. The currency to be transferred to the payee. This may differ from the currency the payment is denoted in and the currency of the payer&#39;s account. Specified as a 3-letter code (ISO 4217). | [optional] 
**purpose** | **str** | Specifies the external purpose code for the &#x60;Institution&#x60; - IS0 20022. | [optional] 
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
payment_response_from_dict = PaymentResponse.from_dict(payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


