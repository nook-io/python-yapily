# BulkPaymentDetailsByIdResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetBulkPaymentStatus200ResponseMeta**](GetBulkPaymentStatus200ResponseMeta.md) |  | [optional] 
**data** | [**BulkPaymentDetailsByIdResponseData**](BulkPaymentDetailsByIdResponseData.md) |  | [optional] 

## Example

```python
from yapily.models.bulk_payment_details_by_id_response import BulkPaymentDetailsByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPaymentDetailsByIdResponse from a JSON string
bulk_payment_details_by_id_response_instance = BulkPaymentDetailsByIdResponse.from_json(json)
# print the JSON string representation of the object
print BulkPaymentDetailsByIdResponse.to_json()

# convert the object into a dict
bulk_payment_details_by_id_response_dict = bulk_payment_details_by_id_response_instance.to_dict()
# create an instance of BulkPaymentDetailsByIdResponse from a dict
bulk_payment_details_by_id_response_from_dict = BulkPaymentDetailsByIdResponse.from_dict(bulk_payment_details_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


