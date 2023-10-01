# PeriodicPaymentRequest

__Conditional__. Used to specify properties to define a periodic payment. <br><br>Must be specified when the payment `type` is one of the following:<ul>     <li><code>DOMESTIC_PERIODIC_PAYMENT</code></li>     <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | [**FrequencyRequest**](FrequencyRequest.md) |  | 
**number_of_payments** | **int** | __Conditional__. Defines the total number of payments to be made.&lt;br&gt;&lt;br&gt;This is required if &#x60;finalPaymentDateTime&#x60; is not specified and it is intended for the periodic payment have a fixed amount of payments. | [optional] 
**next_payment_date_time** | **datetime** | __Conditional__. Defines when to start the recurring payment date and time. Specify this if you want the first payment to start on a different day than what the frequency object defines. | [optional] 
**next_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**final_payment_date_time** | **datetime** | __Conditional__. Defines the final payment date and time. To create an open-ended periodic payment, do not specify this property. | [optional] 
**final_payment_amount** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from yapily.models.periodic_payment_request import PeriodicPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodicPaymentRequest from a JSON string
periodic_payment_request_instance = PeriodicPaymentRequest.from_json(json)
# print the JSON string representation of the object
print PeriodicPaymentRequest.to_json()

# convert the object into a dict
periodic_payment_request_dict = periodic_payment_request_instance.to_dict()
# create an instance of PeriodicPaymentRequest from a dict
periodic_payment_request_form_dict = periodic_payment_request.from_dict(periodic_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


