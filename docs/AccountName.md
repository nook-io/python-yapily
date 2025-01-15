# AccountName


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The bank account holder&#39;s name given by the account owner. | [optional] 

## Example

```python
from yapily.models.account_name import AccountName

# TODO update the JSON string below
json = "{}"
# create an instance of AccountName from a JSON string
account_name_instance = AccountName.from_json(json)
# print the JSON string representation of the object
print AccountName.to_json()

# convert the object into a dict
account_name_dict = account_name_instance.to_dict()
# create an instance of AccountName from a dict
account_name_from_dict = AccountName.from_dict(account_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


