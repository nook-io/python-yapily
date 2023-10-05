# PayeeDetailsResponse

 Details of the beneficiary [person or business].

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account holder name of the beneficiary. | [optional] 
**account_identifications** | [**List[AccountIdentificationResponse]**](AccountIdentificationResponse.md) | The account identifications that identify the &#x60;Payee&#x60; bank account. | [optional] 
**address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 
**merchant_id** | **str** | The merchant ID is a unique code provided by the payment processor to the merchant. | [optional] 
**merchant_category_code** | **str** | The category code of the merchant in case the &#x60;Payee&#x60; is a business. Specified as a 3-letter ISO 18245 code. | [optional] 

## Example

```python
from yapily.models.payee_details_response import PayeeDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeDetailsResponse from a JSON string
payee_details_response_instance = PayeeDetailsResponse.from_json(json)
# print the JSON string representation of the object
print PayeeDetailsResponse.to_json()

# convert the object into a dict
payee_details_response_dict = payee_details_response_instance.to_dict()
# create an instance of PayeeDetailsResponse from a dict
payee_details_response_form_dict = payee_details_response.from_dict(payee_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


