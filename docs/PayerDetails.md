# PayerDetails

__Conditional__. Details of the benefactor [person or business].

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;Payer&#x60; bank account. | 

## Example

```python
from yapily.models.payer_details import PayerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PayerDetails from a JSON string
payer_details_instance = PayerDetails.from_json(json)
# print the JSON string representation of the object
print PayerDetails.to_json()

# convert the object into a dict
payer_details_dict = payer_details_instance.to_dict()
# create an instance of PayerDetails from a dict
payer_details_from_dict = PayerDetails.from_dict(payer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


