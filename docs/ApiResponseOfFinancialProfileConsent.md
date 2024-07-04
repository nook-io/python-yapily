# ApiResponseOfFinancialProfileConsent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**ProfileConsent**](ProfileConsent.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_financial_profile_consent import ApiResponseOfFinancialProfileConsent

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfFinancialProfileConsent from a JSON string
api_response_of_financial_profile_consent_instance = ApiResponseOfFinancialProfileConsent.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfFinancialProfileConsent.to_json()

# convert the object into a dict
api_response_of_financial_profile_consent_dict = api_response_of_financial_profile_consent_instance.to_dict()
# create an instance of ApiResponseOfFinancialProfileConsent from a dict
api_response_of_financial_profile_consent_form_dict = api_response_of_financial_profile_consent.from_dict(api_response_of_financial_profile_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


