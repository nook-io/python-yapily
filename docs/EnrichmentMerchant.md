# EnrichmentMerchant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** |  | [optional] 
**parent_group** | **str** |  | [optional] 

## Example

```python
from yapily.models.enrichment_merchant import EnrichmentMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentMerchant from a JSON string
enrichment_merchant_instance = EnrichmentMerchant.from_json(json)
# print the JSON string representation of the object
print EnrichmentMerchant.to_json()

# convert the object into a dict
enrichment_merchant_dict = enrichment_merchant_instance.to_dict()
# create an instance of EnrichmentMerchant from a dict
enrichment_merchant_form_dict = enrichment_merchant.from_dict(enrichment_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


