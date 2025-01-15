# PayerDetailsResponse

Details of the benefactor [person or business].

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account holder name of the Payer. | [optional] 
**account_identifications** | [**List[AccountIdentificationResponse]**](AccountIdentificationResponse.md) | The account identifications that identify the &#x60;Payer&#x60; bank account. | [optional] 
**address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 

## Example

```python
from yapily.models.payer_details_response import PayerDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayerDetailsResponse from a JSON string
payer_details_response_instance = PayerDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PayerDetailsResponse.to_json())

# convert the object into a dict
payer_details_response_dict = payer_details_response_instance.to_dict()
# create an instance of PayerDetailsResponse from a dict
payer_details_response_from_dict = PayerDetailsResponse.from_dict(payer_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


