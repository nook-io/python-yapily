# PayeeDetails

__Mandatory__. Details of the beneficiary [person or business].

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | __Mandatory__. The account holder name of the beneficiary. | 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;Payee&#x60; bank account. | 
**country** | **str** | __Conditional__. The 2-letter ISO 3166 country code for the address. &lt;br&gt;&lt;br&gt;An &#x60;Institution&#x60; may require you to specify the &#x60;country&#x60; when used in the context of the &#x60;Payee&#x60; to be able to make a payment | 

## Example

```python
from yapily.models.payee_details import PayeeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeDetails from a JSON string
payee_details_instance = PayeeDetails.from_json(json)
# print the JSON string representation of the object
print PayeeDetails.to_json()

# convert the object into a dict
payee_details_dict = payee_details_instance.to_dict()
# create an instance of PayeeDetails from a dict
payee_details_form_dict = payee_details.from_dict(payee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


