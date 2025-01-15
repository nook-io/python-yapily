# HostedVrpPayerResponse

__Conditional__. Details of the benefactor [person or business].

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The account holder name of the Payer. | [optional] 
**account_identifications** | [**List[HostedVrpAccountIdentification]**](HostedVrpAccountIdentification.md) | __Mandatory__. The account identifications that identify the &#x60;Payer&#x60; bank account. | 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from yapily.models.hosted_vrp_payer_response import HostedVrpPayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostedVrpPayerResponse from a JSON string
hosted_vrp_payer_response_instance = HostedVrpPayerResponse.from_json(json)
# print the JSON string representation of the object
print HostedVrpPayerResponse.to_json()

# convert the object into a dict
hosted_vrp_payer_response_dict = hosted_vrp_payer_response_instance.to_dict()
# create an instance of HostedVrpPayerResponse from a dict
hosted_vrp_payer_response_from_dict = HostedVrpPayerResponse.from_dict(hosted_vrp_payer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


