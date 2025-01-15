# ApiResponseOfCreateHostedVRPPaymentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**HostedVRPPaymentResponse**](HostedVRPPaymentResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_create_hosted_vrp_payment_request import ApiResponseOfCreateHostedVRPPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfCreateHostedVRPPaymentRequest from a JSON string
api_response_of_create_hosted_vrp_payment_request_instance = ApiResponseOfCreateHostedVRPPaymentRequest.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfCreateHostedVRPPaymentRequest.to_json()

# convert the object into a dict
api_response_of_create_hosted_vrp_payment_request_dict = api_response_of_create_hosted_vrp_payment_request_instance.to_dict()
# create an instance of ApiResponseOfCreateHostedVRPPaymentRequest from a dict
api_response_of_create_hosted_vrp_payment_request_from_dict = ApiResponseOfCreateHostedVRPPaymentRequest.from_dict(api_response_of_create_hosted_vrp_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


