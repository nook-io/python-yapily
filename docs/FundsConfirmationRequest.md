# FundsConfirmationRequest

The fund confirmation object defining the details of the account and funds to be checked under the Variable Recurring Payment consent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | __Optional__. The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**payment_amount** | [**Amount**](Amount.md) |  | 

## Example

```python
from yapily.models.funds_confirmation_request import FundsConfirmationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FundsConfirmationRequest from a JSON string
funds_confirmation_request_instance = FundsConfirmationRequest.from_json(json)
# print the JSON string representation of the object
print FundsConfirmationRequest.to_json()

# convert the object into a dict
funds_confirmation_request_dict = funds_confirmation_request_instance.to_dict()
# create an instance of FundsConfirmationRequest from a dict
funds_confirmation_request_form_dict = funds_confirmation_request.from_dict(funds_confirmation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


