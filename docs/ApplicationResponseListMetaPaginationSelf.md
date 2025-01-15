# ApplicationResponseListMetaPaginationSelf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | The number of skipped applications. | [optional] 
**limit** | **int** | The maximum number of applications for the current page. | [optional] 
**sort** | **str** | The field by which results are sorted by. Default direction is ascending, descending is identified by a \&quot;-\&quot; prefix. | [optional] 

## Example

```python
from yapily.models.application_response_list_meta_pagination_self import ApplicationResponseListMetaPaginationSelf

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResponseListMetaPaginationSelf from a JSON string
application_response_list_meta_pagination_self_instance = ApplicationResponseListMetaPaginationSelf.from_json(json)
# print the JSON string representation of the object
print ApplicationResponseListMetaPaginationSelf.to_json()

# convert the object into a dict
application_response_list_meta_pagination_self_dict = application_response_list_meta_pagination_self_instance.to_dict()
# create an instance of ApplicationResponseListMetaPaginationSelf from a dict
application_response_list_meta_pagination_self_from_dict = ApplicationResponseListMetaPaginationSelf.from_dict(application_response_list_meta_pagination_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


