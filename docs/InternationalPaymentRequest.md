# InternationalPaymentRequest

__Conditional__. Used to specify properties to define an international payment. <br><br>Must be specified when the payment `type` is one of the following:<ul>     <li><code>INTERNATIONAL_SINGLE_PAYMENT</code></li>     <li><code>INTERNATIONAL_SCHEDULED_PAYMENT</code></li>     <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_of_transfer** | **str** | __Mandatory__. The currency to be transferred to the payee. This may differ from the currency the payment is denoted in and the currency of the payer&#39;s account. Specified as a 3-letter code (ISO 4217). | 
**exchange_rate_information** | [**ExchangeRateInformation**](ExchangeRateInformation.md) |  | [optional] 
**purpose** | **str** | __Optional__. Used to indicate the external purpose as a [ISO20022 purpose code](https://www.rba.hr/documents/20182/183267/External+purpose+codes+list/8a28f888-1f83-5e29-d6ed-fce05f428689?version&#x3D;1.1) value. | [optional] 
**priority** | [**PriorityCodeEnum**](PriorityCodeEnum.md) |  | [optional] 
**charge_bearer** | [**ChargeBearerType**](ChargeBearerType.md) |  | [optional] 

## Example

```python
from yapily.models.international_payment_request import InternationalPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalPaymentRequest from a JSON string
international_payment_request_instance = InternationalPaymentRequest.from_json(json)
# print the JSON string representation of the object
print InternationalPaymentRequest.to_json()

# convert the object into a dict
international_payment_request_dict = international_payment_request_instance.to_dict()
# create an instance of InternationalPaymentRequest from a dict
international_payment_request_form_dict = international_payment_request.from_dict(international_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


