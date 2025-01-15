# ApiListResponseOfPaymentConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResponseListMeta**](ResponseListMeta.md) |  | [optional] 
**data** | [**List[PaymentConstraintsResponse]**](PaymentConstraintsResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_list_response_of_payment_constraints import ApiListResponseOfPaymentConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListResponseOfPaymentConstraints from a JSON string
api_list_response_of_payment_constraints_instance = ApiListResponseOfPaymentConstraints.from_json(json)
# print the JSON string representation of the object
print(ApiListResponseOfPaymentConstraints.to_json())

# convert the object into a dict
api_list_response_of_payment_constraints_dict = api_list_response_of_payment_constraints_instance.to_dict()
# create an instance of ApiListResponseOfPaymentConstraints from a dict
api_list_response_of_payment_constraints_from_dict = ApiListResponseOfPaymentConstraints.from_dict(api_list_response_of_payment_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


