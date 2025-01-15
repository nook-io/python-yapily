# FilteredClientPayloadListDirectDebitResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_call** | **object** |  | [optional] 
**data** | [**List[DirectDebitResponse]**](DirectDebitResponse.md) |  | [optional] 
**next_cursor_hash** | **str** |  | [optional] 
**next_link** | **str** |  | [optional] 
**paging_map** | [**Dict[str, FilterAndSort]**](FilterAndSort.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from yapily.models.filtered_client_payload_list_direct_debit_response import FilteredClientPayloadListDirectDebitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilteredClientPayloadListDirectDebitResponse from a JSON string
filtered_client_payload_list_direct_debit_response_instance = FilteredClientPayloadListDirectDebitResponse.from_json(json)
# print the JSON string representation of the object
print FilteredClientPayloadListDirectDebitResponse.to_json()

# convert the object into a dict
filtered_client_payload_list_direct_debit_response_dict = filtered_client_payload_list_direct_debit_response_instance.to_dict()
# create an instance of FilteredClientPayloadListDirectDebitResponse from a dict
filtered_client_payload_list_direct_debit_response_from_dict = FilteredClientPayloadListDirectDebitResponse.from_dict(filtered_client_payload_list_direct_debit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


