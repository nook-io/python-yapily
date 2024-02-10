# ApiListResponseOfVirtualAccountPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**data** | [**List[VirtualAccountPayment]**](VirtualAccountPayment.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_virtual_account_payment import ApiListResponseOfVirtualAccountPayment

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfVirtualAccountPayment from a JSON string
api_list_response_of_virtual_account_payment_instance = ApiListResponseOfVirtualAccountPayment.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfVirtualAccountPayment.to_json()

# convert the object into a dict
api_list_response_of_virtual_account_payment_dict = api_list_response_of_virtual_account_payment_instance.to_dict()
# create an instance of ApiListResponseOfVirtualAccountPayment from a dict
api_list_response_of_virtual_account_payment_form_dict = api_list_response_of_virtual_account_payment.from_dict(api_list_response_of_virtual_account_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


