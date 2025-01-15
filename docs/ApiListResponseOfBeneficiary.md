# ApiListResponseOfBeneficiary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[Beneficiary]**](Beneficiary.md) |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_beneficiary import ApiListResponseOfBeneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfBeneficiary from a JSON string
api_list_response_of_beneficiary_instance = ApiListResponseOfBeneficiary.from_json(json)
# print the JSON string representation of the object
print(ApiListResponseOfBeneficiary.to_json())

# convert the object into a dict
api_list_response_of_beneficiary_dict = api_list_response_of_beneficiary_instance.to_dict()
# create an instance of ApiListResponseOfBeneficiary from a dict
api_list_response_of_beneficiary_from_dict = ApiListResponseOfBeneficiary.from_dict(api_list_response_of_beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


