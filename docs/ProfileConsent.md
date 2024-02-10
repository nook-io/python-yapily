# ProfileConsent

Object returned when creating a User Profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the ProfileConsent | [optional] 
**status** | **str** | The status, can be PENDING, COMPLETED or ERROR. | [optional] 
**user_id** | **str** | The userUuid. | [optional] 
**reference_consent_id** | **str** | The referenceConsentId. | [optional] 
**institution_id** | **str** | The id of the Institution. | [optional] 
**created_at** | **datetime** | When a profile consent is created. | [optional] 
**expires_at** | **datetime** | When a profile consent is expired after created + X. | [optional] 
**data_inserted_at** | **datetime** | After data retrieval from aggregated profile consent is completed. | [optional] 

## Example

```python
from yapily.models.profile_consent import ProfileConsent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileConsent from a JSON string
profile_consent_instance = ProfileConsent.from_json(json)
# print the JSON string representation of the object
print ProfileConsent.to_json()

# convert the object into a dict
profile_consent_dict = profile_consent_instance.to_dict()
# create an instance of ProfileConsent from a dict
profile_consent_form_dict = profile_consent.from_dict(profile_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


