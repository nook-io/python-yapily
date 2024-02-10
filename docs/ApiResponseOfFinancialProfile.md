# ApiResponseOfFinancialProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**FinancialProfile**](FinancialProfile.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_financial_profile import ApiResponseOfFinancialProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfFinancialProfile from a JSON string
api_response_of_financial_profile_instance = ApiResponseOfFinancialProfile.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfFinancialProfile.to_json()

# convert the object into a dict
api_response_of_financial_profile_dict = api_response_of_financial_profile_instance.to_dict()
# create an instance of ApiResponseOfFinancialProfile from a dict
api_response_of_financial_profile_form_dict = api_response_of_financial_profile.from_dict(api_response_of_financial_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


