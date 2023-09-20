# Consent


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
**last_confirmed_at** | **datetime** | The time that the PSU last confirmed access to their account information, either through full authentication with the institution, or through reconfirmation with the TPP. | [optional] 
**reconfirm_by** | **datetime** | The time by which the consent should be reconfirmed to ensure continued access to the account information. | [optional] 
**institution_consent_id** | **str** |  | [optional] 

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


