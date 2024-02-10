# ApiResponseOfVirtualAccountPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**VirtualAccountPayment**](VirtualAccountPayment.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_virtual_account_payment import ApiResponseOfVirtualAccountPayment

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfVirtualAccountPayment from a JSON string
api_response_of_virtual_account_payment_instance = ApiResponseOfVirtualAccountPayment.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfVirtualAccountPayment.to_json()

# convert the object into a dict
api_response_of_virtual_account_payment_dict = api_response_of_virtual_account_payment_instance.to_dict()
# create an instance of ApiResponseOfVirtualAccountPayment from a dict
api_response_of_virtual_account_payment_form_dict = api_response_of_virtual_account_payment.from_dict(api_response_of_virtual_account_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


