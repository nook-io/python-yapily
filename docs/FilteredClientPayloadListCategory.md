# FilteredClientPayloadListCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_call** | **object** |  | [optional] 
**data** | [**List[Category]**](Category.md) |  | [optional] 
**next_cursor_hash** | **str** |  | [optional] 
**next_link** | **str** |  | [optional] 
**paging_map** | [**Dict[str, FilterAndSort]**](FilterAndSort.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from yapily.models.filtered_client_payload_list_category import FilteredClientPayloadListCategory

# TODO update the JSON string below
json = "{}"
# create an instance of FilteredClientPayloadListCategory from a JSON string
filtered_client_payload_list_category_instance = FilteredClientPayloadListCategory.from_json(json)
# print the JSON string representation of the object
print FilteredClientPayloadListCategory.to_json()

# convert the object into a dict
filtered_client_payload_list_category_dict = filtered_client_payload_list_category_instance.to_dict()
# create an instance of FilteredClientPayloadListCategory from a dict
filtered_client_payload_list_category_form_dict = filtered_client_payload_list_category.from_dict(filtered_client_payload_list_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


