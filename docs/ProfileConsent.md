# ProfileConsent

Details of a consent linked to a `User Profile`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the &#x60;consent&#x60; in context of a user&#39;s profile. | [optional] 
**status** | **str** | The status, can be PENDING, COMPLETED or ERROR. | [optional] 
**user_id** | **str** | The userUuid. | [optional] 
**reference_consent_id** | **str** | Unique identifier of the consent. | [optional] 
**institution_id** | **str** | __Mandatory__. The  &#x60;Institution&#x60; the authorisation request is sent to. | [optional] 
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
profile_consent_from_dict = ProfileConsent.from_dict(profile_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


