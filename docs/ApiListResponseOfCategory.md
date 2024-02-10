# ApiListResponseOfCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[Category]**](Category.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListCategory**](FilteredClientPayloadListCategory.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_category import ApiListResponseOfCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfCategory from a JSON string
api_list_response_of_category_instance = ApiListResponseOfCategory.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfCategory.to_json()

# convert the object into a dict
api_list_response_of_category_dict = api_list_response_of_category_instance.to_dict()
# create an instance of ApiListResponseOfCategory from a dict
api_list_response_of_category_form_dict = api_list_response_of_category.from_dict(api_list_response_of_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


