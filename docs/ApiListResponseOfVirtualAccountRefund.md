# ApiListResponseOfVirtualAccountRefund


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**links** | [**ApiListResponseOfVirtualAccountRefundLinks**](ApiListResponseOfVirtualAccountRefundLinks.md) |  | [optional] 
**data** | [**List[VirtualAccountRefund]**](VirtualAccountRefund.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_virtual_account_refund import ApiListResponseOfVirtualAccountRefund

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfVirtualAccountRefund from a JSON string
api_list_response_of_virtual_account_refund_instance = ApiListResponseOfVirtualAccountRefund.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfVirtualAccountRefund.to_json()

# convert the object into a dict
api_list_response_of_virtual_account_refund_dict = api_list_response_of_virtual_account_refund_instance.to_dict()
# create an instance of ApiListResponseOfVirtualAccountRefund from a dict
api_list_response_of_virtual_account_refund_form_dict = api_list_response_of_virtual_account_refund.from_dict(api_list_response_of_virtual_account_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


