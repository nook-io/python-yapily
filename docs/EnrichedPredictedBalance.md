# EnrichedPredictedBalance

A list of Predicted Account Balances for future date range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date for which Balance amount is predicted. | [optional] 
**median_balance** | **float** | The median Balance amount for a future date. | [optional] 
**var_90percentile_balance** | **float** | The 90th percentile Balance amount for a future date. | [optional] 
**var_10percentile_balance** | **float** | The 10th percentile Balance amount for a future date. | [optional] 

## Example

```python
from yapily.models.enriched_predicted_balance import EnrichedPredictedBalance

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedPredictedBalance from a JSON string
enriched_predicted_balance_instance = EnrichedPredictedBalance.from_json(json)
# print the JSON string representation of the object
print EnrichedPredictedBalance.to_json()

# convert the object into a dict
enriched_predicted_balance_dict = enriched_predicted_balance_instance.to_dict()
# create an instance of EnrichedPredictedBalance from a dict
enriched_predicted_balance_form_dict = enriched_predicted_balance.from_dict(enriched_predicted_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


