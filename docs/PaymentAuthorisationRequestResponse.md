# PaymentAuthorisationRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the payment authorisation request. &lt;br&gt;&lt;br&gt;The &#x60;consentID&#x60; used to [retrieve a consent](/api/reference/#operation/getConsentById). | [optional] 
**user_uuid** | **str** | The &#x60;User&#x60; that the authorisation request was created for. | [optional] 
**application_user_id** | **str** | The user-friendly reference to the &#x60;User&#x60; that the authorisation request was created for. | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_id** | **str** | The &#x60;Institution&#x60; the authorisation request was sent to. | [optional] 
**status** | [**AuthorisationStatus**](AuthorisationStatus.md) |  | [optional] 
**created_at** | **datetime** | Date and time the consent was created. | [optional] 
**transaction_from** | **datetime** | When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved. | [optional] 
**transaction_to** | **datetime** | When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved. | [optional] 
**expires_at** | **datetime** | Date and time the authorisation expires. Re-authorisation is needed to retain access. | [optional] 
**time_to_expire_in_millis** | **int** |  | [optional] 
**time_to_expire** | **str** |  | [optional] 
**feature_scope** | [**List[FeatureEnum]**](FeatureEnum.md) | The set of features the consent provides access to. | [optional] 
**consent_token** | **str** | Represents the authorisation to gain access to the requested features. Required to make a payment request. | [optional] 
**state** | **str** | Correlation ID used with the &#x60;Institution&#x60; during the authorisation process. | [optional] 
**authorized_at** | **datetime** | Date and time the request was authorised by the &#x60;Institution&#x60;. | [optional] 
**institution_consent_id** | **str** | Unique identifier of the consent assigned by the &#x60;Institution&#x60;. | [optional] 
**charges** | [**List[PaymentChargeDetails]**](PaymentChargeDetails.md) |  | [optional] 
**exchange_rate_information** | [**ExchangeRateInformationResponse**](ExchangeRateInformationResponse.md) |  | [optional] 
**authorisation_url** | **str** |  | [optional] 
**qr_code_url** | **str** | The URL for a QR code that may be scanned via a mobile device to make a authorisation redirect to the bank (authURL encoded). | [optional] 
**explanation** | **str** | Message from the &#x60;Institution&#x60; received by Yapily, detailing the next action the user is required to take. This is used only for Decoupled flows. | [optional] 

## Example

```python
from yapily.models.payment_authorisation_request_response import PaymentAuthorisationRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAuthorisationRequestResponse from a JSON string
payment_authorisation_request_response_instance = PaymentAuthorisationRequestResponse.from_json(json)
# print the JSON string representation of the object
print PaymentAuthorisationRequestResponse.to_json()

# convert the object into a dict
payment_authorisation_request_response_dict = payment_authorisation_request_response_instance.to_dict()
# create an instance of PaymentAuthorisationRequestResponse from a dict
payment_authorisation_request_response_form_dict = payment_authorisation_request_response.from_dict(payment_authorisation_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


