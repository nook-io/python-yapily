# PaymentRisk

Additional information about the payment that may be used for risk scoring

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | __Optional__. The payment context code. Allowed values are [BILL_IN_ADVANCE, BILL_IN_ARREARS, ECOMMERCE_MERCHANT, FACE_TO_FACE_POS, TRANSFER_TO_SELF,TRANSFER_TO_THIRD_PARTY, PISP_PAYEE ]. | [optional] 

## Example

```python
from yapily.models.payment_risk import PaymentRisk

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRisk from a JSON string
payment_risk_instance = PaymentRisk.from_json(json)
# print the JSON string representation of the object
print PaymentRisk.to_json()

# convert the object into a dict
payment_risk_dict = payment_risk_instance.to_dict()
# create an instance of PaymentRisk from a dict
payment_risk_form_dict = payment_risk.from_dict(payment_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


