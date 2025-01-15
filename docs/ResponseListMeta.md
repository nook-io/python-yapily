# ResponseListMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from yapily.models.response_list_meta import ResponseListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseListMeta from a JSON string
response_list_meta_instance = ResponseListMeta.from_json(json)
# print the JSON string representation of the object
print ResponseListMeta.to_json()

# convert the object into a dict
response_list_meta_dict = response_list_meta_instance.to_dict()
# create an instance of ResponseListMeta from a dict
response_list_meta_from_dict = ResponseListMeta.from_dict(response_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


