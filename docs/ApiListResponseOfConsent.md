# ApiListResponseOfConsent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[Consent]**](Consent.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**paging** | [**FilteredClientPayloadListConsent**](FilteredClientPayloadListConsent.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_consent import ApiListResponseOfConsent

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfConsent from a JSON string
api_list_response_of_consent_instance = ApiListResponseOfConsent.from_json(json)
# print the JSON string representation of the object
print(ApiListResponseOfConsent.to_json())

# convert the object into a dict
api_list_response_of_consent_dict = api_list_response_of_consent_instance.to_dict()
# create an instance of ApiListResponseOfConsent from a dict
api_list_response_of_consent_from_dict = ApiListResponseOfConsent.from_dict(api_list_response_of_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


