# Payer

__Conditional__. The `Payer` object contains details of the benefactor [person or business]. If you define this in your payment request, you mustdefine this along with all of the nested mandatory properties.<ol>     <li>The `Payer` object is mandatory along with its mandatory properties when the account of the benefactor is from an `Institution` in Europe.          See [Berlin Group](https://docs.yapily.com/pages/knowledge/open-banking/berlin_group/) for more information.</li>     <li>The `Payer` should be specified if the `Payer` account is intended to be locked.</li></ol>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | __Mandatory__. The account holder name of the Payer. | [optional] 
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


