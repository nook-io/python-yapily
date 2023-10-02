# FilterAndSort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | __Optional__. The earliest date and time of resources / records that should be returned. | [optional] 
**before** | **datetime** | __Optional__. The latest date and time of resources / records that should be returned. | [optional] 
**limit** | **int** | __Optional__. The maximum number of resources / records that should be returned. | [optional] 
**sort** | [**SortEnum**](SortEnum.md) |  | [optional] 
**offset** | **int** |  | [optional] 
**cursor** | **str** |  | [optional] 

## Example

```python
from yapily.models.filter_and_sort import FilterAndSort

# TODO update the JSON string below
json = "{}"
# create an instance of FilterAndSort from a JSON string
filter_and_sort_instance = FilterAndSort.from_json(json)
# print the JSON string representation of the object
print FilterAndSort.to_json()

# convert the object into a dict
filter_and_sort_dict = filter_and_sort_instance.to_dict()
# create an instance of FilterAndSort from a dict
filter_and_sort_form_dict = filter_and_sort.from_dict(filter_and_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


