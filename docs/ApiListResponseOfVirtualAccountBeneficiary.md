# ApiListResponseOfVirtualAccountBeneficiary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**data** | [**List[VirtualAccountBeneficiary]**](VirtualAccountBeneficiary.md) |  | [optional] 
**forwarded_data** | [**List[ResponseForwardedData]**](ResponseForwardedData.md) |  | [optional] 
**tracing_id** | **str** |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_virtual_account_beneficiary import ApiListResponseOfVirtualAccountBeneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfVirtualAccountBeneficiary from a JSON string
api_list_response_of_virtual_account_beneficiary_instance = ApiListResponseOfVirtualAccountBeneficiary.from_json(json)
# print the JSON string representation of the object
print ApiListResponseOfVirtualAccountBeneficiary.to_json()

# convert the object into a dict
api_list_response_of_virtual_account_beneficiary_dict = api_list_response_of_virtual_account_beneficiary_instance.to_dict()
# create an instance of ApiListResponseOfVirtualAccountBeneficiary from a dict
api_list_response_of_virtual_account_beneficiary_form_dict = api_list_response_of_virtual_account_beneficiary.from_dict(api_list_response_of_virtual_account_beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


