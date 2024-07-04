# ApiResponseOfPaymentAuthorisationRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**PaymentAuthorisationRequestResponse**](PaymentAuthorisationRequestResponse.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_payment_authorisation_request_response import ApiResponseOfPaymentAuthorisationRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfPaymentAuthorisationRequestResponse from a JSON string
api_response_of_payment_authorisation_request_response_instance = ApiResponseOfPaymentAuthorisationRequestResponse.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfPaymentAuthorisationRequestResponse.to_json()

# convert the object into a dict
api_response_of_payment_authorisation_request_response_dict = api_response_of_payment_authorisation_request_response_instance.to_dict()
# create an instance of ApiResponseOfPaymentAuthorisationRequestResponse from a dict
api_response_of_payment_authorisation_request_response_form_dict = api_response_of_payment_authorisation_request_response.from_dict(api_response_of_payment_authorisation_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


