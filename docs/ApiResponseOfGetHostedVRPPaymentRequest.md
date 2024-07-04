# ApiResponseOfGetHostedVRPPaymentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**HostedVRPPaymentResponse**](HostedVRPPaymentResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_get_hosted_vrp_payment_request import ApiResponseOfGetHostedVRPPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfGetHostedVRPPaymentRequest from a JSON string
api_response_of_get_hosted_vrp_payment_request_instance = ApiResponseOfGetHostedVRPPaymentRequest.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfGetHostedVRPPaymentRequest.to_json()

# convert the object into a dict
api_response_of_get_hosted_vrp_payment_request_dict = api_response_of_get_hosted_vrp_payment_request_instance.to_dict()
# create an instance of ApiResponseOfGetHostedVRPPaymentRequest from a dict
api_response_of_get_hosted_vrp_payment_request_form_dict = api_response_of_get_hosted_vrp_payment_request.from_dict(api_response_of_get_hosted_vrp_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


