# TransactionStream

Lists all possible transaction streams identified for the `Application User`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Transaction Stream. | [optional] 
**transactions** | [**List[EnrichedTransaction]**](EnrichedTransaction.md) | A list of transaction details, identified by Yapily data services. | [optional] 
**transaction_schedule** | [**TransactionSchedule**](TransactionSchedule.md) |  | [optional] 
**schedule_consistency_score** | **float** | The consistency of the transaction.  This is a number between 0 and 1 with 1 being the most consistent schedule. | [optional] 
**next_expected_transaction_date** | **date** | When is the transaction expected to occur next. | [optional] 
**earliest_transaction_date** | **date** | When is the first recorded transaction date | [optional] 
**most_recent_transaction_date** | **date** | When is the most recent transaction date | [optional] 
**amount_consistency_score** | **float** | The consistency of the amount of the transaction.  This is a number between 0 and 1 with 1 being the most consistent amount. | [optional] 
**average_amount** | **float** | The average amount of the transaction stream | [optional] 

## Example

```python
from yapily.models.transaction_stream import TransactionStream

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionStream from a JSON string
transaction_stream_instance = TransactionStream.from_json(json)
# print the JSON string representation of the object
print TransactionStream.to_json()

# convert the object into a dict
transaction_stream_dict = transaction_stream_instance.to_dict()
# create an instance of TransactionStream from a dict
transaction_stream_from_dict = TransactionStream.from_dict(transaction_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


