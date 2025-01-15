# SubmissionDetails

__Mandatory__. The payment submission object defining the details of the payment instruction to be executed under the Variable Recurring Payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | __Optional__. The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**payee** | [**Payee**](Payee.md) |  | 
**payment_amount** | [**Amount**](Amount.md) |  | 

## Example

```python
from yapily.models.submission_details import SubmissionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionDetails from a JSON string
submission_details_instance = SubmissionDetails.from_json(json)
# print the JSON string representation of the object
print SubmissionDetails.to_json()

# convert the object into a dict
submission_details_dict = submission_details_instance.to_dict()
# create an instance of SubmissionDetails from a dict
submission_details_from_dict = SubmissionDetails.from_dict(submission_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


