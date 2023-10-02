# Consent

Consent detailing the requested authorisation from a user to a specific `Institution`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the consent. | [optional] 
**user_uuid** | **str** |  | [optional] 
**application_user_id** | **str** | __Conditional__. The user-friendly reference to the &#x60;User&#x60; that will authorise the authorisation request. If a &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; exists, it will be used otherwise, a new &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; will be created and used. Either the &#x60;userUuid&#x60; or &#x60;applicationUserId&#x60; must be provided. | [optional] 
**reference_id** | **str** |  | [optional] 
**institution_id** | **str** | __Mandatory__. The &#x60;Institution&#x60; the authorisation request is sent to. | [optional] 
**status** | [**AuthorisationStatus**](AuthorisationStatus.md) |  | [optional] 
**created_at** | **datetime** | Date and time of when the consent was created. | [optional] 
**transaction_from** | **datetime** | When performing a transaction query using the consent, this is the earliest date of transaction records that can be retrieved. | [optional] 
**transaction_to** | **datetime** | When performing a transaction query using the consent, this is the latest date of transaction records that can be retrieved. | [optional] 
**expires_at** | **datetime** | Date and time of when the authorisation will expire by. Reauthorisation will be needed to retain access. | [optional] 
**time_to_expire_in_millis** | **int** |  | [optional] 
**time_to_expire** | **str** |  | [optional] 
**feature_scope** | [**List[FeatureEnum]**](FeatureEnum.md) | The set of features that the consent will provide access to. | [optional] 
**consent_token** | **str** | Represents the authorisation to gain access to the requested features. Required to access account information or make a payment request. | [optional] 
**state** | **str** | Correlation ID used with the &#x60;Institution&#x60; during the authorisation process. | [optional] 
**authorized_at** | **datetime** | Date and time of when the request was authorised by the Institution. | [optional] 
**last_confirmed_at** | **datetime** | The time that the PSU last confirmed access to their account information, either through full authentication with the institution, or through reconfirmation with the TPP. | [optional] 
**reconfirm_by** | **datetime** | The time by which the consent should be reconfirmed to ensure continued access to the account information. | [optional] 
**institution_consent_id** | **str** | Identification of the consent at the Institution. | [optional] 

## Example

```python
from yapily.models.consent import Consent

# TODO update the JSON string below
json = "{}"
# create an instance of Consent from a JSON string
consent_instance = Consent.from_json(json)
# print the JSON string representation of the object
print Consent.to_json()

# convert the object into a dict
consent_dict = consent_instance.to_dict()
# create an instance of Consent from a dict
consent_form_dict = consent.from_dict(consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


