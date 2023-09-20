# EnrichedTransaction

Part of a financial profile for a User.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The id of the transaction | [optional] 
**transaction_information** | **str** | Information for the transaction | [optional] 
**amount** | **float** | The amount of the transaction | [optional] 
**institution** | **str** | The id of the institution | [optional] 
**booking_date_time** | **datetime** | The datetime of the transaction | [optional] 

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
enriched_transaction_form_dict = enriched_transaction.from_dict(enriched_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


