# GetBulkPaymentStatus200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetBulkPaymentStatus200ResponseMeta**](GetBulkPaymentStatus200ResponseMeta.md) |  | [optional] 
**data** | [**GetBulkPaymentStatus200ResponseData**](GetBulkPaymentStatus200ResponseData.md) |  | [optional] 

## Example

```python
from yapily.models.get_bulk_payment_status200_response import GetBulkPaymentStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBulkPaymentStatus200Response from a JSON string
get_bulk_payment_status200_response_instance = GetBulkPaymentStatus200Response.from_json(json)
# print the JSON string representation of the object
print GetBulkPaymentStatus200Response.to_json()

# convert the object into a dict
get_bulk_payment_status200_response_dict = get_bulk_payment_status200_response_instance.to_dict()
# create an instance of GetBulkPaymentStatus200Response from a dict
get_bulk_payment_status200_response_from_dict = GetBulkPaymentStatus200Response.from_dict(get_bulk_payment_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


