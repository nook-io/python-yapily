# ApplicationResponseListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** |  | [optional] 
**count** | **int** | The number of applications in the current page. | [optional] 
**pagination** | [**ApplicationResponseListMetaPagination**](ApplicationResponseListMetaPagination.md) |  | [optional] 

## Example

```python
from yapily.models.application_response_list_meta import ApplicationResponseListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResponseListMeta from a JSON string
application_response_list_meta_instance = ApplicationResponseListMeta.from_json(json)
# print the JSON string representation of the object
print(ApplicationResponseListMeta.to_json())

# convert the object into a dict
application_response_list_meta_dict = application_response_list_meta_instance.to_dict()
# create an instance of ApplicationResponseListMeta from a dict
application_response_list_meta_from_dict = ApplicationResponseListMeta.from_dict(application_response_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


