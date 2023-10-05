# ResponseMetaWithCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from yapily.models.response_meta_with_count import ResponseMetaWithCount

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseMetaWithCount from a JSON string
response_meta_with_count_instance = ResponseMetaWithCount.from_json(json)
# print the JSON string representation of the object
print ResponseMetaWithCount.to_json()

# convert the object into a dict
response_meta_with_count_dict = response_meta_with_count_instance.to_dict()
# create an instance of ResponseMetaWithCount from a dict
response_meta_with_count_form_dict = response_meta_with_count.from_dict(response_meta_with_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


