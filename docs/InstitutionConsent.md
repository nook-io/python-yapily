# InstitutionConsent

`Institution` authorised consents which are currently in place for the `Application User`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | __Mandatory__. The &#x60;Institution&#x60; the authorisation request is sent to. | [optional] 

## Example

```python
from yapily.models.institution_consent import InstitutionConsent

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionConsent from a JSON string
institution_consent_instance = InstitutionConsent.from_json(json)
# print the JSON string representation of the object
print InstitutionConsent.to_json()

# convert the object into a dict
institution_consent_dict = institution_consent_instance.to_dict()
# create an instance of InstitutionConsent from a dict
institution_consent_form_dict = institution_consent.from_dict(institution_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


