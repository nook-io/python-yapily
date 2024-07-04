# SubmissionRequest

__Mandatory__. The payment request object defining the details of the payment for execution under the Variable Recurring Payment consent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_idempotency_id** | **str** | __Mandatory__. A unique identifier that you must provide to identify the payment. This can be any alpha-numeric string but is limited to a maximum of 35 characters. | 
**psu_authentication_method** | **str** | __Mandatory__. Chosen authentication method for submission step. Allowed values are [SCA_REQUIRED, SCA_NOT_REQUIRED]. | 
**context_type** | [**PaymentContextType**](PaymentContextType.md) |  | [optional] 
**payment_amount** | [**Amount**](Amount.md) |  | 

## Example

```python
from yapily.models.submission_request import SubmissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionRequest from a JSON string
submission_request_instance = SubmissionRequest.from_json(json)
# print the JSON string representation of the object
print SubmissionRequest.to_json()

# convert the object into a dict
submission_request_dict = submission_request_instance.to_dict()
# create an instance of SubmissionRequest from a dict
submission_request_form_dict = submission_request.from_dict(submission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


