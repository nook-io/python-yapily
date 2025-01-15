# ApiListResponseOfPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[PaymentResponse]**](PaymentResponse.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListPaymentResponse**](FilteredClientPayloadListPaymentResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_payment_response import ApiListResponseOfPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfPaymentResponse from a JSON string
api_list_response_of_payment_response_instance = ApiListResponseOfPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(ApiListResponseOfPaymentResponse.to_json())

# convert the object into a dict
api_list_response_of_payment_response_dict = api_list_response_of_payment_response_instance.to_dict()
# create an instance of ApiListResponseOfPaymentResponse from a dict
api_list_response_of_payment_response_from_dict = ApiListResponseOfPaymentResponse.from_dict(api_list_response_of_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


