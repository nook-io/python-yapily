# FinancialProfile

A financial profile for a User.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status, can be EMPTY, PARTIAL, PENDING, COMPLETED or ERROR. | [optional] 
**profile_consents** | [**List[ProfileConsent]**](ProfileConsent.md) | A list of ProfileConsent used in the financial profile. | [optional] 
**enrichment** | [**EnrichedWrapper**](EnrichedWrapper.md) |  | [optional] 

## Example

```python
from yapily.models.financial_profile import FinancialProfile

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialProfile from a JSON string
financial_profile_instance = FinancialProfile.from_json(json)
# print the JSON string representation of the object
print FinancialProfile.to_json()

# convert the object into a dict
financial_profile_dict = financial_profile_instance.to_dict()
# create an instance of FinancialProfile from a dict
financial_profile_form_dict = financial_profile.from_dict(financial_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


