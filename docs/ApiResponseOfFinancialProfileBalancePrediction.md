# ApiResponseOfFinancialProfileBalancePrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**BalancePredictionProfile**](BalancePredictionProfile.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_financial_profile_balance_prediction import ApiResponseOfFinancialProfileBalancePrediction

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfFinancialProfileBalancePrediction from a JSON string
api_response_of_financial_profile_balance_prediction_instance = ApiResponseOfFinancialProfileBalancePrediction.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfFinancialProfileBalancePrediction.to_json()

# convert the object into a dict
api_response_of_financial_profile_balance_prediction_dict = api_response_of_financial_profile_balance_prediction_instance.to_dict()
# create an instance of ApiResponseOfFinancialProfileBalancePrediction from a dict
api_response_of_financial_profile_balance_prediction_form_dict = api_response_of_financial_profile_balance_prediction.from_dict(api_response_of_financial_profile_balance_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


