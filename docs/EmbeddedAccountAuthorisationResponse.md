# EmbeddedAccountAuthorisationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the embedded account authorisation request. | [optional] 
**user_uuid** | **str** | The &#x60;User&#x60; that the authorisation request was created for. | [optional] 
**application_user_id** | **str** | The user-friendly reference to the &#x60;User&#x60; that the authorisation request was created for. | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_id** | **str** | The &#x60;Institution&#x60; the authorisation request was sent to. | [optional] 
**status** | [**AuthorisationStatus**](AuthorisationStatus.md) |  | [optional] 
**created_at** | **datetime** | Date and time the embedded authorisation was created by the application user. | [optional] 
**transaction_from** | **datetime** | When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved. | [optional] 
**transaction_to** | **datetime** | When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved. | [optional] 
**expires_at** | **datetime** | Date and time the embedded authorisation expires. Re-authorisation is needed to retain access. | [optional] 
**time_to_expire_in_millis** | **int** |  | [optional] 
**time_to_expire** | **str** |  | [optional] 
**feature_scope** | [**List[FeatureEnum]**](FeatureEnum.md) | The set of features the consent provides access to. | [optional] 
**consent_token** | **str** | Represents the authorisation to gain access to the requested features. Required to access account information. | [optional] 
**state** | **str** | Correlation ID used when handshaking with a new institution via OAuth2 registration. | [optional] 
**authorized_at** | **datetime** | Date and time the request was authorised by the &#x60;Institution&#x60;. | [optional] 
**institution_consent_id** | **str** | Identification of the consent at the &#x60;Institution&#x60;. | [optional] 
**authorisation_url** | **str** |  | [optional] 
**qr_code_url** | **str** | The URL link for the QR code that may be scanned via a mobile device to make an authorisation redirect to the bank (authURL encoded). | [optional] 
**sca_methods** | [**List[ScaMethod]**](ScaMethod.md) | List of &#x60;SCA methods&#x60; that the &#x60;Institution&#x60; supports and are available for selection. | [optional] 
**selected_sca_method** | [**ScaMethod**](ScaMethod.md) |  | [optional] 

## Example

```python
from yapily.models.embedded_account_authorisation_response import EmbeddedAccountAuthorisationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedAccountAuthorisationResponse from a JSON string
embedded_account_authorisation_response_instance = EmbeddedAccountAuthorisationResponse.from_json(json)
# print the JSON string representation of the object
print EmbeddedAccountAuthorisationResponse.to_json()

# convert the object into a dict
embedded_account_authorisation_response_dict = embedded_account_authorisation_response_instance.to_dict()
# create an instance of EmbeddedAccountAuthorisationResponse from a dict
embedded_account_authorisation_response_from_dict = EmbeddedAccountAuthorisationResponse.from_dict(embedded_account_authorisation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


