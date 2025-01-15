# StatementReference

Unique reference for a statement period. This may be optionally populated if available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 

## Example

```python
from yapily.models.statement_reference import StatementReference

# TODO update the JSON string below
json = "{}"
# create an instance of StatementReference from a JSON string
statement_reference_instance = StatementReference.from_json(json)
# print the JSON string representation of the object
print(StatementReference.to_json())

# convert the object into a dict
statement_reference_dict = statement_reference_instance.to_dict()
# create an instance of StatementReference from a dict
statement_reference_from_dict = StatementReference.from_dict(statement_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


