# ApiResponseOfFinancialProfileAuthorisationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**List[ProfileConsent]**](ProfileConsent.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_financial_profile_authorisation_response import ApiResponseOfFinancialProfileAuthorisationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfFinancialProfileAuthorisationResponse from a JSON string
api_response_of_financial_profile_authorisation_response_instance = ApiResponseOfFinancialProfileAuthorisationResponse.from_json(json)
# print the JSON string representation of the object
print(ApiResponseOfFinancialProfileAuthorisationResponse.to_json())

# convert the object into a dict
api_response_of_financial_profile_authorisation_response_dict = api_response_of_financial_profile_authorisation_response_instance.to_dict()
# create an instance of ApiResponseOfFinancialProfileAuthorisationResponse from a dict
api_response_of_financial_profile_authorisation_response_from_dict = ApiResponseOfFinancialProfileAuthorisationResponse.from_dict(api_response_of_financial_profile_authorisation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


