# GetCategorisationAccountType200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetBulkPaymentStatus200ResponseMeta**](GetBulkPaymentStatus200ResponseMeta.md) |  | [optional] 
**data** | [**GetCategoriesResponse**](GetCategoriesResponse.md) |  | [optional] 

## Example

```python
from yapily.models.get_categorisation_account_type200_response import GetCategorisationAccountType200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategorisationAccountType200Response from a JSON string
get_categorisation_account_type200_response_instance = GetCategorisationAccountType200Response.from_json(json)
# print the JSON string representation of the object
print GetCategorisationAccountType200Response.to_json()

# convert the object into a dict
get_categorisation_account_type200_response_dict = get_categorisation_account_type200_response_instance.to_dict()
# create an instance of GetCategorisationAccountType200Response from a dict
get_categorisation_account_type200_response_from_dict = GetCategorisationAccountType200Response.from_dict(get_categorisation_account_type200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


