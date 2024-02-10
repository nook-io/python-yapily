# Enrichment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categorisation** | [**Categorisation**](Categorisation.md) |  | [optional] 
**transaction_hash** | [**TransactionHash**](TransactionHash.md) |  | [optional] 
**cleansed_description** | **str** |  | [optional] 
**merchant** | [**EnrichmentMerchant**](EnrichmentMerchant.md) |  | [optional] 
**location** | **str** |  | [optional] 
**payment_processor** | **str** |  | [optional] 
**corrected_date** | **datetime** |  | [optional] 

## Example

```python
from yapily.models.enrichment import Enrichment

# TODO update the JSON string below
json = "{}"
# create an instance of Enrichment from a JSON string
enrichment_instance = Enrichment.from_json(json)
# print the JSON string representation of the object
print Enrichment.to_json()

# convert the object into a dict
enrichment_dict = enrichment_instance.to_dict()
# create an instance of Enrichment from a dict
enrichment_form_dict = enrichment.from_dict(enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


