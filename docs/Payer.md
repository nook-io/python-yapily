# Payer

__Conditional__. Details of the benefactor [person or business].

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account holder name of the Payer. | [optional] 
**account_identifications** | [**List[AccountIdentification]**](AccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;Payer&#x60; bank account. | 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from yapily.models.payer import Payer

# TODO update the JSON string below
json = "{}"
# create an instance of Payer from a JSON string
payer_instance = Payer.from_json(json)
# print the JSON string representation of the object
print Payer.to_json()

# convert the object into a dict
payer_dict = payer_instance.to_dict()
# create an instance of Payer from a dict
payer_form_dict = payer.from_dict(payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


