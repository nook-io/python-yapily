# SubmissionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**payment_idempotency_id** | **str** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**status_details** | [**PaymentStatusDetails**](PaymentStatusDetails.md) |  | [optional] 
**initiation_details** | [**InitiationDetails**](InitiationDetails.md) |  | 
**submission_details** | [**SubmissionDetails**](SubmissionDetails.md) |  | 
**payer** | [**Payer**](Payer.md) |  | [optional] 
**refund_account** | [**RefundAccount**](RefundAccount.md) |  | [optional] 
**expected_execution_time** | **datetime** |  | [optional] 
**expected_settlement_time** | **datetime** |  | [optional] 

## Example

```python
from yapily.models.submission_response import SubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionResponse from a JSON string
submission_response_instance = SubmissionResponse.from_json(json)
# print the JSON string representation of the object
print SubmissionResponse.to_json()

# convert the object into a dict
submission_response_dict = submission_response_instance.to_dict()
# create an instance of SubmissionResponse from a dict
submission_response_form_dict = submission_response.from_dict(submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


