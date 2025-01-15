# PreAuthorisationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the pre-authorisation request. | [optional] 
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
**consent_token** | **str** | Represents the authorisation to gain access to the requested features. Required to access account information or make a payment request. | [optional] 
**state** | **str** | Corellation ID used with the &#x60;Institution&#x60; during the authorisation process. | [optional] 
**authorized_at** | **datetime** | Date and time the request was authorised by the &#x60;Institution&#x60;. | [optional] 
**institution_consent_id** | **str** | Unique identifier of the consent assigned by the &#x60;Institution&#x60;. | [optional] 
**authorisation_url** | **str** |  | [optional] 
**qr_code_url** | **str** | The URL link for the QR code that may be scanned via a mobile device to make a authorisation redirect to the bank (authURL encoded). | [optional] 

## Example

```python
from yapily.models.pre_authorisation_response import PreAuthorisationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PreAuthorisationResponse from a JSON string
pre_authorisation_response_instance = PreAuthorisationResponse.from_json(json)
# print the JSON string representation of the object
print(PreAuthorisationResponse.to_json())

# convert the object into a dict
pre_authorisation_response_dict = pre_authorisation_response_instance.to_dict()
# create an instance of PreAuthorisationResponse from a dict
pre_authorisation_response_from_dict = PreAuthorisationResponse.from_dict(pre_authorisation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


