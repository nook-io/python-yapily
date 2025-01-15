# ApiListResponseOfInstitution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[Institution]**](Institution.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListInstitution**](FilteredClientPayloadListInstitution.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_institution import ApiListResponseOfInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfInstitution from a JSON string
api_list_response_of_institution_instance = ApiListResponseOfInstitution.from_json(json)
# print the JSON string representation of the object
print(ApiListResponseOfInstitution.to_json())

# convert the object into a dict
api_list_response_of_institution_dict = api_list_response_of_institution_instance.to_dict()
# create an instance of ApiListResponseOfInstitution from a dict
api_list_response_of_institution_from_dict = ApiListResponseOfInstitution.from_dict(api_list_response_of_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


