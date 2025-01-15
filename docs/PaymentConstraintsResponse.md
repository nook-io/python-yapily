# PaymentConstraintsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | The id to represent the &#x60;Institution&#x60;. | 
**institution_country_code** | **str** | 2 letter ISO Country code of the &#x60;Institution&#x60;. | [optional] 
**endpoint_path** | **str** | Define the applicable API end point. | [optional] 
**endpoint_method** | **str** | Https Method for the endpoint. | [optional] 
**payment_type** | [**PaymentTypeOfConstraints**](PaymentTypeOfConstraints.md) |  | 
**request** | [**RequestConstraints**](RequestConstraints.md) |  | 

## Example

```python
from yapily.models.payment_constraints_response import PaymentConstraintsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentConstraintsResponse from a JSON string
payment_constraints_response_instance = PaymentConstraintsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentConstraintsResponse.to_json())

# convert the object into a dict
payment_constraints_response_dict = payment_constraints_response_instance.to_dict()
# create an instance of PaymentConstraintsResponse from a dict
payment_constraints_response_from_dict = PaymentConstraintsResponse.from_dict(payment_constraints_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


