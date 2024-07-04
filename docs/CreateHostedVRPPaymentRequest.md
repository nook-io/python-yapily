# CreateHostedVRPPaymentRequest

__Mandatory__. The payment request object defining the details of the payment for execution under the Variable Recurring Payment consent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_idempotency_id** | **str** | __Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters. | 
**amount** | [**Amount**](Amount.md) |  | 

## Example

```python
from yapily.models.create_hosted_vrp_payment_request import CreateHostedVRPPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostedVRPPaymentRequest from a JSON string
create_hosted_vrp_payment_request_instance = CreateHostedVRPPaymentRequest.from_json(json)
# print the JSON string representation of the object
print CreateHostedVRPPaymentRequest.to_json()

# convert the object into a dict
create_hosted_vrp_payment_request_dict = create_hosted_vrp_payment_request_instance.to_dict()
# create an instance of CreateHostedVRPPaymentRequest from a dict
create_hosted_vrp_payment_request_form_dict = create_hosted_vrp_payment_request.from_dict(create_hosted_vrp_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


