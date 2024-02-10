# ApiResponseOfConsent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseMeta**](ResponseMeta.md) |  | [optional] 
**data** | [**Consent**](Consent.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_response_of_consent import ApiResponseOfConsent

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseOfConsent from a JSON string
api_response_of_consent_instance = ApiResponseOfConsent.from_json(json)
# print the JSON string representation of the object
print ApiResponseOfConsent.to_json()

# convert the object into a dict
api_response_of_consent_dict = api_response_of_consent_instance.to_dict()
# create an instance of ApiResponseOfConsent from a dict
api_response_of_consent_form_dict = api_response_of_consent.from_dict(api_response_of_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


