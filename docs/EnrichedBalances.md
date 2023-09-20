# EnrichedBalances

Enriched Balance information generated which include historic aggregated balances and predicted balances

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **List[str]** | A list of Account Ids used to generate Balance Prediction Profile. | [optional] 
**institutions** | **List[str]** | A list of Institution Ids associated with the accounts used to generate Balance Prediction Profile. | [optional] 
**historic** | [**List[EnrichedHistoricBalance]**](EnrichedHistoricBalance.md) | A list of historic balances. Each balance in the list is an aggregation (sum) of the reported balance for each account within the profile at a point in time. | [optional] 
**predicted** | [**List[EnrichedPredictedBalance]**](EnrichedPredictedBalance.md) | A list of predicted balances. Each balance in the list is a projected balance of the profile at a future point in time. | [optional] 

## Example

```python
from yapily.models.enriched_balances import EnrichedBalances

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedBalances from a JSON string
enriched_balances_instance = EnrichedBalances.from_json(json)
# print the JSON string representation of the object
print EnrichedBalances.to_json()

# convert the object into a dict
enriched_balances_dict = enriched_balances_instance.to_dict()
# create an instance of EnrichedBalances from a dict
enriched_balances_form_dict = enriched_balances.from_dict(enriched_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


