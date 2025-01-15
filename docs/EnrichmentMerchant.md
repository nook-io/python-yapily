# EnrichmentMerchant

Details of the merchant, identified by Yapily data services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** | The name of the indivdual merchant involved in the transaction e.g. (TESCO Petrol). | [optional] 
**parent_group** | **str** | The parent organisation that the merchant belongs to e.g. (TESCO). | [optional] 

## Example

```python
from yapily.models.enrichment_merchant import EnrichmentMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentMerchant from a JSON string
enrichment_merchant_instance = EnrichmentMerchant.from_json(json)
# print the JSON string representation of the object
print(EnrichmentMerchant.to_json())

# convert the object into a dict
enrichment_merchant_dict = enrichment_merchant_instance.to_dict()
# create an instance of EnrichmentMerchant from a dict
enrichment_merchant_from_dict = EnrichmentMerchant.from_dict(enrichment_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


