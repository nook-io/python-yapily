# AccountStatement

Statement information belonging to the account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the statement. | [optional] 
**start_date_time** | **datetime** | Date and time of when the statement period starts. | [optional] 
**end_date_time** | **datetime** | Date and time of when the statement period ends. | [optional] 
**creation_date_time** | **datetime** | Date and time of when the statement was created. | [optional] 

## Example

```python
from yapily.models.account_statement import AccountStatement

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatement from a JSON string
account_statement_instance = AccountStatement.from_json(json)
# print the JSON string representation of the object
print AccountStatement.to_json()

# convert the object into a dict
account_statement_dict = account_statement_instance.to_dict()
# create an instance of AccountStatement from a dict
account_statement_form_dict = account_statement.from_dict(account_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


