# FundsConfirmationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**reference** | **str** | The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**payment_amount** | [**Amount**](Amount.md) |  | 
**funds_available** | [**FundsAvailable**](FundsAvailable.md) |  | 

## Example

```python
from yapily.models.funds_confirmation_response import FundsConfirmationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FundsConfirmationResponse from a JSON string
funds_confirmation_response_instance = FundsConfirmationResponse.from_json(json)
# print the JSON string representation of the object
print FundsConfirmationResponse.to_json()

# convert the object into a dict
funds_confirmation_response_dict = funds_confirmation_response_instance.to_dict()
# create an instance of FundsConfirmationResponse from a dict
funds_confirmation_response_form_dict = funds_confirmation_response.from_dict(funds_confirmation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


