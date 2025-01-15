# InstitutionIdentifiersResponse

Specifies the institution selected for making the payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | Yapily identifier which identifies the &#x60;Institution&#x60; the payment request is sent to. | [optional] 
**institution_country_code** | **str** | 2 letter ISO Country code of the &#x60;Institution&#x60; the payment request is sent to. | [optional] 

## Example

```python
from yapily.models.institution_identifiers_response import InstitutionIdentifiersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionIdentifiersResponse from a JSON string
institution_identifiers_response_instance = InstitutionIdentifiersResponse.from_json(json)
# print the JSON string representation of the object
print(InstitutionIdentifiersResponse.to_json())

# convert the object into a dict
institution_identifiers_response_dict = institution_identifiers_response_instance.to_dict()
# create an instance of InstitutionIdentifiersResponse from a dict
institution_identifiers_response_from_dict = InstitutionIdentifiersResponse.from_dict(institution_identifiers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


