# FilteredClientPayloadListInstitution


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_call** | **object** |  | [optional] 
**data** | [**List[Institution]**](Institution.md) |  | [optional] 
**next_cursor_hash** | **str** |  | [optional] 
**next_link** | **str** |  | [optional] 
**paging_map** | [**Dict[str, FilterAndSort]**](FilterAndSort.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from yapily.models.filtered_client_payload_list_institution import FilteredClientPayloadListInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of FilteredClientPayloadListInstitution from a JSON string
filtered_client_payload_list_institution_instance = FilteredClientPayloadListInstitution.from_json(json)
# print the JSON string representation of the object
print FilteredClientPayloadListInstitution.to_json()

# convert the object into a dict
filtered_client_payload_list_institution_dict = filtered_client_payload_list_institution_instance.to_dict()
# create an instance of FilteredClientPayloadListInstitution from a dict
filtered_client_payload_list_institution_from_dict = FilteredClientPayloadListInstitution.from_dict(filtered_client_payload_list_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


