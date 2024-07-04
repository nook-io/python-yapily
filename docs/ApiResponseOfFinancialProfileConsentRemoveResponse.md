# ApiResponseOfFinancialProfileConsentRemoveResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_financial_profile_consent_remove_response import ApiResponseOfFinancialProfileConsentRemoveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfFinancialProfileConsentRemoveResponse from a JSON string
api_response_of_financial_profile_consent_remove_response_instance = ApiResponseOfFinancialProfileConsentRemoveResponse.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfFinancialProfileConsentRemoveResponse.to_json()

# convert the object into a dict
api_response_of_financial_profile_consent_remove_response_dict = api_response_of_financial_profile_consent_remove_response_instance.to_dict()
# create an instance of ApiResponseOfFinancialProfileConsentRemoveResponse from a dict
api_response_of_financial_profile_consent_remove_response_form_dict = api_response_of_financial_profile_consent_remove_response.from_dict(api_response_of_financial_profile_consent_remove_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


