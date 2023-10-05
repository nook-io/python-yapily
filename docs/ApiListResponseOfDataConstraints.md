# ApiListResponseOfDataConstraints


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**List[DataConstraintsResponse]**](DataConstraintsResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_data_constraints import ApiListResponseOfDataConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfDataConstraints from a JSON string
api_list_response_of_data_constraints_instance = ApiListResponseOfDataConstraints.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfDataConstraints.to_json()

# convert the object into a dict
api_list_response_of_data_constraints_dict = api_list_response_of_data_constraints_instance.to_dict()
# create an instance of ApiListResponseOfDataConstraints from a dict
api_list_response_of_data_constraints_form_dict = api_list_response_of_data_constraints.from_dict(api_list_response_of_data_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


