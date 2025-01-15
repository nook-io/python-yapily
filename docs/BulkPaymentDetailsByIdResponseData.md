# BulkPaymentDetailsByIdResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**consent_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**payments** | [**List[BulkPaymentDetailsByIdResponseDataPaymentsInner]**](BulkPaymentDetailsByIdResponseDataPaymentsInner.md) |  | [optional] 

## Example

```python
from yapily.models.bulk_payment_details_by_id_response_data import BulkPaymentDetailsByIdResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPaymentDetailsByIdResponseData from a JSON string
bulk_payment_details_by_id_response_data_instance = BulkPaymentDetailsByIdResponseData.from_json(json)
# print the JSON string representation of the object
print BulkPaymentDetailsByIdResponseData.to_json()

# convert the object into a dict
bulk_payment_details_by_id_response_data_dict = bulk_payment_details_by_id_response_data_instance.to_dict()
# create an instance of BulkPaymentDetailsByIdResponseData from a dict
bulk_payment_details_by_id_response_data_from_dict = BulkPaymentDetailsByIdResponseData.from_dict(bulk_payment_details_by_id_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


