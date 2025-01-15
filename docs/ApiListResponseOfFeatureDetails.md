# ApiListResponseOfFeatureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[FeatureDetails]**](FeatureDetails.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListFeatureDetails**](FilteredClientPayloadListFeatureDetails.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_feature_details import ApiListResponseOfFeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfFeatureDetails from a JSON string
api_list_response_of_feature_details_instance = ApiListResponseOfFeatureDetails.from_json(json)
# print the JSON string representation of the object
print(ApiListResponseOfFeatureDetails.to_json())

# convert the object into a dict
api_list_response_of_feature_details_dict = api_list_response_of_feature_details_instance.to_dict()
# create an instance of ApiListResponseOfFeatureDetails from a dict
api_list_response_of_feature_details_from_dict = ApiListResponseOfFeatureDetails.from_dict(api_list_response_of_feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


