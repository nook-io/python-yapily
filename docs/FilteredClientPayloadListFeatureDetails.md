# FilteredClientPayloadListFeatureDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_call** | **object** |  | [optional] 
**data** | [**List[FeatureDetails]**](FeatureDetails.md) |  | [optional] 
**next_cursor_hash** | **str** |  | [optional] 
**next_link** | **str** |  | [optional] 
**paging_map** | [**Dict[str, FilterAndSort]**](FilterAndSort.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from yapily.models.filtered_client_payload_list_feature_details import FilteredClientPayloadListFeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FilteredClientPayloadListFeatureDetails from a JSON string
filtered_client_payload_list_feature_details_instance = FilteredClientPayloadListFeatureDetails.from_json(json)
# print the JSON string representation of the object
print FilteredClientPayloadListFeatureDetails.to_json()

# convert the object into a dict
filtered_client_payload_list_feature_details_dict = filtered_client_payload_list_feature_details_instance.to_dict()
# create an instance of FilteredClientPayloadListFeatureDetails from a dict
filtered_client_payload_list_feature_details_form_dict = filtered_client_payload_list_feature_details.from_dict(filtered_client_payload_list_feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


