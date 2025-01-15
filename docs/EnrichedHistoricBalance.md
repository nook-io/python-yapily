# EnrichedHistoricBalance

A list of Aggregated Account Balances for historic date range.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date for which Aggregated Balance amount across Bank accounts is calculated. | [optional] 
**balance** | **float** | The Aggregated Balance amount for a specific date. | [optional] 

## Example

```python
from yapily.models.enriched_historic_balance import EnrichedHistoricBalance

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedHistoricBalance from a JSON string
enriched_historic_balance_instance = EnrichedHistoricBalance.from_json(json)
# print the JSON string representation of the object
print EnrichedHistoricBalance.to_json()

# convert the object into a dict
enriched_historic_balance_dict = enriched_historic_balance_instance.to_dict()
# create an instance of EnrichedHistoricBalance from a dict
enriched_historic_balance_from_dict = EnrichedHistoricBalance.from_dict(enriched_historic_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


