# GetBulkPaymentStatus200ResponseDataStatusDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Bulk file status. Enum: &#x60;COMPLETED&#x60; &#x60;PENDING&#x60; &#x60;FAILED&#x60; &#x60;UNKNOWN&#x60; | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from yapily.models.get_bulk_payment_status200_response_data_status_details import GetBulkPaymentStatus200ResponseDataStatusDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GetBulkPaymentStatus200ResponseDataStatusDetails from a JSON string
get_bulk_payment_status200_response_data_status_details_instance = GetBulkPaymentStatus200ResponseDataStatusDetails.from_json(json)
# print the JSON string representation of the object
print GetBulkPaymentStatus200ResponseDataStatusDetails.to_json()

# convert the object into a dict
get_bulk_payment_status200_response_data_status_details_dict = get_bulk_payment_status200_response_data_status_details_instance.to_dict()
# create an instance of GetBulkPaymentStatus200ResponseDataStatusDetails from a dict
get_bulk_payment_status200_response_data_status_details_from_dict = GetBulkPaymentStatus200ResponseDataStatusDetails.from_dict(get_bulk_payment_status200_response_data_status_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


