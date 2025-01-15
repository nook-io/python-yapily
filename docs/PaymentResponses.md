# PaymentResponses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments** | [**List[PaymentResponse]**](PaymentResponse.md) |  | [optional] 

## Example

```python
from yapily.models.payment_responses import PaymentResponses

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponses from a JSON string
payment_responses_instance = PaymentResponses.from_json(json)
# print the JSON string representation of the object
print PaymentResponses.to_json()

# convert the object into a dict
payment_responses_dict = payment_responses_instance.to_dict()
# create an instance of PaymentResponses from a dict
payment_responses_from_dict = PaymentResponses.from_dict(payment_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


