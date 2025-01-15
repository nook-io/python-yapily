# BulkPaymentRequest

The payment request object defining the details of the bulk payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments** | [**List[PaymentRequest]**](PaymentRequest.md) | __Mandatory__. The array of &#x60;PaymentRequest&#x60; objects to initiate in the bulk payment. | 
**originator_identification_number** | **str** | __Conditional__. The identification number of the originator.&lt;ul&gt;&lt;li&gt;Mandatory for AIB bulk payments&lt;/li&gt;&lt;/ul&gt; | [optional] 
**execution_date_time** | **datetime** | __Optional__. Used to schedule the bulk payment to be executed at a future date if supported by the &#x60;Institution&#x60;. | [optional] 

## Example

```python
from yapily.models.bulk_payment_request import BulkPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPaymentRequest from a JSON string
bulk_payment_request_instance = BulkPaymentRequest.from_json(json)
# print the JSON string representation of the object
print BulkPaymentRequest.to_json()

# convert the object into a dict
bulk_payment_request_dict = bulk_payment_request_instance.to_dict()
# create an instance of BulkPaymentRequest from a dict
bulk_payment_request_from_dict = BulkPaymentRequest.from_dict(bulk_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


