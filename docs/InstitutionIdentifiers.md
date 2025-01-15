# InstitutionIdentifiers

Specifies the institution requirements for making the payment. Skips the bank selection screen in payment flow if the `institutionId` and `institutionCountryCode` are provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | Yapily identifier which identifies the &#x60;Institution&#x60; the payment request is sent to. | [optional] 
**institution_country_code** | **str** | 2 letter ISO Country code of the &#x60;Institution&#x60; the payment request is sent to. | 

## Example

```python
from yapily.models.institution_identifiers import InstitutionIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionIdentifiers from a JSON string
institution_identifiers_instance = InstitutionIdentifiers.from_json(json)
# print the JSON string representation of the object
print(InstitutionIdentifiers.to_json())

# convert the object into a dict
institution_identifiers_dict = institution_identifiers_instance.to_dict()
# create an instance of InstitutionIdentifiers from a dict
institution_identifiers_from_dict = InstitutionIdentifiers.from_dict(institution_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


