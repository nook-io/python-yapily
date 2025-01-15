# SubmitBulkPaymentRequest

The payment request object defining the details of the bulk payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_id** | **str** | __Optional__. An alphanumeric string (1-40 chars) used for idempotency. Unique per consent ID for 24 hours. Prevents duplicate bulk file payment submissions. | [optional] 
**payments** | [**List[PaymentRequest]**](PaymentRequest.md) | __Mandatory__. The array of &#x60;PaymentRequest&#x60; objects to initiate in the bulk payment. | 
**originator_identification_number** | **str** | __Conditional__. The identification number of the originator.&lt;ul&gt;&lt;li&gt;Mandatory for AIB bulk payments&lt;/li&gt;&lt;/ul&gt; | [optional] 
**execution_date_time** | **datetime** | __Optional__. Used to schedule the bulk payment to be executed at a future date if supported by the &#x60;Institution&#x60;. | [optional] 

## Example

```python
from yapily.models.submit_bulk_payment_request import SubmitBulkPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitBulkPaymentRequest from a JSON string
submit_bulk_payment_request_instance = SubmitBulkPaymentRequest.from_json(json)
# print the JSON string representation of the object
print SubmitBulkPaymentRequest.to_json()

# convert the object into a dict
submit_bulk_payment_request_dict = submit_bulk_payment_request_instance.to_dict()
# create an instance of SubmitBulkPaymentRequest from a dict
submit_bulk_payment_request_from_dict = SubmitBulkPaymentRequest.from_dict(submit_bulk_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


