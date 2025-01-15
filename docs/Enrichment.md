# Enrichment

Enriched data that has been derived by Yapily using it's data processing and machine learning techniques.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categorisation** | [**Categorisation**](Categorisation.md) |  | [optional] 
**transaction_hash** | [**TransactionHash**](TransactionHash.md) |  | [optional] 
**cleansed_description** | **str** | Cleaned version of the &#x60;Transaction Description&#x60; that removes miscellaneous, generic and unhelpful text. | [optional] 
**merchant** | [**EnrichmentMerchant**](EnrichmentMerchant.md) |  | [optional] 
**location** | **str** | The location of where the transaction took place. | [optional] 
**payment_processor** | **str** | A payment provider that manages (credit/debit) transactions between the &#x60;Institution&#x60; and the merchant. | [optional] 
**corrected_date** | **datetime** | The likely date and time on which the transaction took place. This is distinct from &#x60;Booking Date Time&#x60; which usually refers to the post-clearing value. | [optional] 

## Example

```python
from yapily.models.enrichment import Enrichment

# TODO update the JSON string below
json = "{}"
# create an instance of Enrichment from a JSON string
enrichment_instance = Enrichment.from_json(json)
# print the JSON string representation of the object
print(Enrichment.to_json())

# convert the object into a dict
enrichment_dict = enrichment_instance.to_dict()
# create an instance of Enrichment from a dict
enrichment_from_dict = Enrichment.from_dict(enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


