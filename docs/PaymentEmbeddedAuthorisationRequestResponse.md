# PaymentEmbeddedAuthorisationRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the embedded payment authorisation request. | [optional] 
**user_uuid** | **str** | The &#x60;User&#x60; that the authorisation request was created for. | [optional] 
**application_user_id** | **str** | The user-friendly reference to the &#x60;User&#x60; that the authorisation request was created for. | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_id** | **str** | The  &#x60;Institution&#x60; the authorisation request was sent to. | [optional] 
**status** | [**AuthorisationStatus**](AuthorisationStatus.md) |  | [optional] 
**created_at** | **datetime** | Date and time the embedded payment authorisation was created. | [optional] 
**transaction_from** | **datetime** | When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved. | [optional] 
**transaction_to** | **datetime** | When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved. | [optional] 
**expires_at** | **datetime** | Date and time the authorisation expires. Re-authorisation is needed to retain access. | [optional] 
**time_to_expire_in_millis** | **int** |  | [optional] 
**time_to_expire** | **str** |  | [optional] 
**feature_scope** | [**List[FeatureEnum]**](FeatureEnum.md) | The set of features the consent provides access to. | [optional] 
**consent_token** | **str** | Represents the authorisation to gain access to the requested features. Required to make a payment request. | [optional] 
**state** | **str** | Correlation ID used with the &#x60;Institution&#x60; during the authorisation process. | [optional] 
**authorized_at** | **datetime** | Date and time the request was authorised by the &#x60;Institution&#x60;. | [optional] 
**institution_consent_id** | **str** | Identification of the consent at the &#x60;Institution&#x60;. | [optional] 
**charges** | [**List[PaymentChargeDetails]**](PaymentChargeDetails.md) |  | [optional] 
**exchange_rate_information** | [**ExchangeRateInformationResponse**](ExchangeRateInformationResponse.md) |  | [optional] 
**authorisation_url** | **str** |  | [optional] 
**qr_code_url** | **str** | The URL link for the QR code that may be scanned via a mobile device to make an authorisation redirect to the bank (authURL encoded). | [optional] 
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


