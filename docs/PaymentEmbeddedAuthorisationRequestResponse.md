# PaymentEmbeddedAuthorisationRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_uuid** | **str** |  | [optional] 
**application_user_id** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_id** | **str** |  | [optional] 
**status** | [**AuthorisationStatus**](AuthorisationStatus.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**transaction_from** | **datetime** |  | [optional] 
**transaction_to** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**time_to_expire_in_millis** | **int** |  | [optional] 
**time_to_expire** | **str** |  | [optional] 
**feature_scope** | [**List[FeatureEnum]**](FeatureEnum.md) |  | [optional] 
**consent_token** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**authorized_at** | **datetime** |  | [optional] 
**institution_consent_id** | **str** |  | [optional] 
**charges** | [**List[PaymentChargeDetails]**](PaymentChargeDetails.md) |  | [optional] 
**exchange_rate_information** | [**ExchangeRateInformationResponse**](ExchangeRateInformationResponse.md) |  | [optional] 
**authorisation_url** | **str** |  | [optional] 
**qr_code_url** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**sca_methods** | [**List[ScaMethod]**](ScaMethod.md) |  | [optional] 
**selected_sca_method** | [**ScaMethod**](ScaMethod.md) |  | [optional] 

## Example

```python
from yapily.models.payment_embedded_authorisation_request_response import PaymentEmbeddedAuthorisationRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentEmbeddedAuthorisationRequestResponse from a JSON string
payment_embedded_authorisation_request_response_instance = PaymentEmbeddedAuthorisationRequestResponse.from_json(json)
# print the JSON string representation of the object
print PaymentEmbeddedAuthorisationRequestResponse.to_json()

# convert the object into a dict
payment_embedded_authorisation_request_response_dict = payment_embedded_authorisation_request_response_instance.to_dict()
# create an instance of PaymentEmbeddedAuthorisationRequestResponse from a dict
payment_embedded_authorisation_request_response_form_dict = payment_embedded_authorisation_request_response.from_dict(payment_embedded_authorisation_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


