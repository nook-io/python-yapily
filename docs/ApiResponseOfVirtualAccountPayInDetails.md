# ApiResponseOfVirtualAccountPayInDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**data** | [**VirtualAccountPayInDetails**](VirtualAccountPayInDetails.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_virtual_account_pay_in_details import ApiResponseOfVirtualAccountPayInDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfVirtualAccountPayInDetails from a JSON string
api_response_of_virtual_account_pay_in_details_instance = ApiResponseOfVirtualAccountPayInDetails.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfVirtualAccountPayInDetails.to_json()

# convert the object into a dict
api_response_of_virtual_account_pay_in_details_dict = api_response_of_virtual_account_pay_in_details_instance.to_dict()
# create an instance of ApiResponseOfVirtualAccountPayInDetails from a dict
api_response_of_virtual_account_pay_in_details_form_dict = api_response_of_virtual_account_pay_in_details.from_dict(api_response_of_virtual_account_pay_in_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


