# EnrichedWrapper

A financial profile for a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**income_streams** | [**List[TransactionStream]**](TransactionStream.md) | A list of transaction streams | 
**expenditure_streams** | [**List[TransactionStream]**](TransactionStream.md) | A list of transaction streams | 
**recently_terminated_income_streams** | [**List[TerminatedTransactionStream]**](TerminatedTransactionStream.md) | A list of terminated transaction income streams | 
**recently_terminated_expenditure_streams** | [**List[TerminatedTransactionStream]**](TerminatedTransactionStream.md) | A list of terminated transaction expenditure streams | 

## Example

```python
from yapily.models.enriched_wrapper import EnrichedWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedWrapper from a JSON string
enriched_wrapper_instance = EnrichedWrapper.from_json(json)
# print the JSON string representation of the object
print EnrichedWrapper.to_json()

# convert the object into a dict
enriched_wrapper_dict = enriched_wrapper_instance.to_dict()
# create an instance of EnrichedWrapper from a dict
enriched_wrapper_form_dict = enriched_wrapper.from_dict(enriched_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


