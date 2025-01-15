# GetBulkPaymentStatus200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Bulk Payment | [optional] 
**consent_id** | **str** | Identification of the consent. | [optional] 
**status_details** | [**GetBulkPaymentStatus200ResponseDataStatusDetails**](GetBulkPaymentStatus200ResponseDataStatusDetails.md) |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from yapily.models.get_bulk_payment_status200_response_data import GetBulkPaymentStatus200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetBulkPaymentStatus200ResponseData from a JSON string
get_bulk_payment_status200_response_data_instance = GetBulkPaymentStatus200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetBulkPaymentStatus200ResponseData.to_json())

# convert the object into a dict
get_bulk_payment_status200_response_data_dict = get_bulk_payment_status200_response_data_instance.to_dict()
# create an instance of GetBulkPaymentStatus200ResponseData from a dict
get_bulk_payment_status200_response_data_from_dict = GetBulkPaymentStatus200ResponseData.from_dict(get_bulk_payment_status200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


