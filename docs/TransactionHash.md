# TransactionHash

An unique identifier for the transaction that was generated by Yapily. This is a hash of transaction attributes and may be useful an id is not present (and therefore hasn't been provided by an Institution).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | [optional] 

## Example

```python
from yapily.models.transaction_hash import TransactionHash

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionHash from a JSON string
transaction_hash_instance = TransactionHash.from_json(json)
# print the JSON string representation of the object
print TransactionHash.to_json()

# convert the object into a dict
transaction_hash_dict = transaction_hash_instance.to_dict()
# create an instance of TransactionHash from a dict
transaction_hash_from_dict = TransactionHash.from_dict(transaction_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


