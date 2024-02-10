# TerminatedTransactionStream

Terminated transaction stream generated as part of the financial profile for a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the TransactionStream | [optional] 
**transactions** | [**List[EnrichedTransaction]**](EnrichedTransaction.md) | A list of Transactions from the transaction stream. | [optional] 
**transaction_schedule** | [**TransactionSchedule**](TransactionSchedule.md) |  | [optional] 
**schedule_consistency_score** | **float** | The consistency of the transaction.  This is a number between 0 and 1 with 1 being the most consistent schedule. | [optional] 
**next_expected_transaction_date** | **date** | When is the transaction expected to occur next. | [optional] 
**earliest_transaction_date** | **date** | When is the first recorded transaction date | [optional] 
**most_recent_transaction_date** | **date** | When is the most recent transaction date | [optional] 
**amount_consistency_score** | **float** | The consistency of the amount of the transaction.  This is a number between 0 and 1 with 1 being the most consistent amount. | [optional] 
**average_amount** | **float** | The average amount of the transaction stream | [optional] 
**missed_transactions** | **int** | Missed transactions of transaction stream | [optional] 

## Example

```python
from yapily.models.terminated_transaction_stream import TerminatedTransactionStream

# TODO update the JSON string below
json = "{}"
# create an instance of TerminatedTransactionStream from a JSON string
terminated_transaction_stream_instance = TerminatedTransactionStream.from_json(json)
# print the JSON string representation of the object
print TerminatedTransactionStream.to_json()

# convert the object into a dict
terminated_transaction_stream_dict = terminated_transaction_stream_instance.to_dict()
# create an instance of TerminatedTransactionStream from a dict
terminated_transaction_stream_form_dict = terminated_transaction_stream.from_dict(terminated_transaction_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


