# EnrichedTransaction

Details of the transaction, identified by Yapily data services.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique identifier of the transaction | [optional] 
**transaction_information** | **str** | Information for the transaction | [optional] 
**amount** | **float** | Monetary amount. | [optional] 
**institution** | **str** | The &#x60;Institution&#x60; that the transaction is sent to. | [optional] 
**booking_date_time** | **datetime** | Date and time of when a transaction entry occured and was posted to the account servicer&#39;s books. | [optional] 

## Example

```python
from yapily.models.enriched_transaction import EnrichedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedTransaction from a JSON string
enriched_transaction_instance = EnrichedTransaction.from_json(json)
# print the JSON string representation of the object
print EnrichedTransaction.to_json()

# convert the object into a dict
enriched_transaction_dict = enriched_transaction_instance.to_dict()
# create an instance of EnrichedTransaction from a dict
enriched_transaction_from_dict = EnrichedTransaction.from_dict(enriched_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


