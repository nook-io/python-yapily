# ApiResponseOfGetHostedPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**HostedPaymentDetails**](HostedPaymentDetails.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_of_get_hosted_payment_request import ApiResponseOfGetHostedPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfGetHostedPaymentRequest from a JSON string
api_response_of_get_hosted_payment_request_instance = ApiResponseOfGetHostedPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(ApiResponseOfGetHostedPaymentRequest.to_json())

# convert the object into a dict
api_response_of_get_hosted_payment_request_dict = api_response_of_get_hosted_payment_request_instance.to_dict()
# create an instance of ApiResponseOfGetHostedPaymentRequest from a dict
api_response_of_get_hosted_payment_request_from_dict = ApiResponseOfGetHostedPaymentRequest.from_dict(api_response_of_get_hosted_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


