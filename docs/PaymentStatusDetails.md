# PaymentStatusDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**status_reason** | **str** |  | [optional] 
**status_reason_description** | **str** |  | [optional] 
**status_update_date** | **datetime** |  | [optional] 
**multi_authorisation_status** | [**MultiAuthorisation**](MultiAuthorisation.md) |  | [optional] 
**iso_status** | [**PaymentIsoStatus**](PaymentIsoStatus.md) |  | [optional] 

## Example

```python
from yapily.models.payment_status_details import PaymentStatusDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentStatusDetails from a JSON string
payment_status_details_instance = PaymentStatusDetails.from_json(json)
# print the JSON string representation of the object
print(PaymentStatusDetails.to_json())

# convert the object into a dict
payment_status_details_dict = payment_status_details_instance.to_dict()
# create an instance of PaymentStatusDetails from a dict
payment_status_details_from_dict = PaymentStatusDetails.from_dict(payment_status_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


