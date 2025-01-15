# HostedPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The Unique Identifier of the payment. | [optional] 
**hosted_payment_id** | **str** | The Unique Identifier of the payment created using Yapily hosted application. | [optional] 
**consent_id** | **str** | The Unique Identifier of the consent. | [optional] 
**institution_identifiers** | [**InstitutionIdentifiersResponse**](InstitutionIdentifiersResponse.md) |  | [optional] 
**phases** | [**List[HostedPaymentPhase]**](HostedPaymentPhase.md) | The phase reached by the payment and its timestamp. | [optional] 
**payment_status** | **str** | Payment status based on latest HostedAuthPaymentPhase in phases. Value can be &lt;ul&gt; &lt;li&gt;PENDING  -  Payment pending processing&lt;/li&gt; &lt;li&gt;COMPLETED  -  Payment processing completed&lt;/li&gt; &lt;li&gt;FAILED  -  Payment process failed&lt;/li&gt;&lt;/ul&gt; | [optional] 
**status_details** | [**List[HostedPaymentStatusDetails]**](HostedPaymentStatusDetails.md) | Details of the payment status. | [optional] 
**institution_payment_id** | **str** | The Unique Identifier of the payment created with the &#x60;Institution&#x60;. | [optional] 
**payment_lifecycle_id** | **str** | The Unique Identifier provided by TPP in the Payment request to identify the payment. | [optional] 
**payment_idempotency_id** | **str** | A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters. | [optional] 
**reference** | **str** | The payment reference or description. Limited to a maximum of 18 characters for UK institutions. | [optional] 
**context_type** | [**PaymentContextTypeResponse**](PaymentContextTypeResponse.md) |  | [optional] 
**type** | [**PaymentTypeResponse**](PaymentTypeResponse.md) |  | [optional] 
**payee** | [**PayeeDetailsResponse**](PayeeDetailsResponse.md) |  | [optional] 
**payer** | [**PayerDetailsResponse**](PayerDetailsResponse.md) |  | [optional] 
**amount** | [**AmountDetailsResponse**](AmountDetailsResponse.md) |  | [optional] 

## Example

```python
from yapily.models.hosted_payment import HostedPayment

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPayment from a JSON string
hosted_payment_instance = HostedPayment.from_json(json)
# print the JSON string representation of the object
print HostedPayment.to_json()

# convert the object into a dict
hosted_payment_dict = hosted_payment_instance.to_dict()
# create an instance of HostedPayment from a dict
hosted_payment_from_dict = HostedPayment.from_dict(hosted_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


