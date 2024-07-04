# VRPSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer** | [**HostedVrpPayerResponse**](HostedVrpPayerResponse.md) |  | [optional] 
**payee** | [**Payee**](Payee.md) |  | 
**reference** | **str** | __Optional__. The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**limits** | [**HostedVRPLimits**](HostedVRPLimits.md) |  | [optional] 
**valid_from** | **datetime** | __Optional__. Start date when the consent becomes valid. | [optional] 
**valid_to** | **datetime** | __Optional__. End date when the consent expires and becomes invalid. | [optional] 
**recurring_payment_category** | **str** | The use-case for the VRP consent supported by the bank. Allowed values: &lt;br&gt;&#x60;ONGOING&#x60; &lt;br&gt;&#x60;SUBSCRIPTION&#x60; | [optional] 
**initial_payment** | [**Amount**](Amount.md) |  | [optional] 
**risk** | [**PaymentRisk**](PaymentRisk.md) |  | [optional] 

## Example

```python
from yapily.models.vrp_setup import VRPSetup

# TODO update the JSON string below
json = "{}"
# create an instance of VRPSetup from a JSON string
vrp_setup_instance = VRPSetup.from_json(json)
# print the JSON string representation of the object
print VRPSetup.to_json()

# convert the object into a dict
vrp_setup_dict = vrp_setup_instance.to_dict()
# create an instance of VRPSetup from a dict
vrp_setup_form_dict = vrp_setup.from_dict(vrp_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


