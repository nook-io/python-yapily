# DirectDebitResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status_details** | [**PaymentStatusDetails**](PaymentStatusDetails.md) |  | [optional] 
**payee_details** | [**DirectDebitPayee**](DirectDebitPayee.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**previous_payment_amount** | [**Amount**](Amount.md) |  | [optional] 
**previous_payment_date_time** | **datetime** |  | [optional] 

## Example

```python
from yapily.models.direct_debit_response import DirectDebitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDebitResponse from a JSON string
direct_debit_response_instance = DirectDebitResponse.from_json(json)
# print the JSON string representation of the object
print DirectDebitResponse.to_json()

# convert the object into a dict
direct_debit_response_dict = direct_debit_response_instance.to_dict()
# create an instance of DirectDebitResponse from a dict
direct_debit_response_form_dict = direct_debit_response.from_dict(direct_debit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


