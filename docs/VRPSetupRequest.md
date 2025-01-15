# VRPSetupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer** | [**Payer**](Payer.md) |  | [optional] 
**payee** | [**Payee**](Payee.md) |  | 
**reference** | **str** | __Optional__. The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**limits** | [**HostedVRPLimitsRequest**](HostedVRPLimitsRequest.md) |  | [optional] 
**valid_from** | **datetime** | __Optional__. Start date when the consent becomes valid. | [optional] 
**valid_to** | **datetime** | __Optional__. End date when the consent expires and becomes invalid. | [optional] 
**recurring_payment_category** | **str** | The use-case for the VRP consent supported by the bank. Allowed values: &lt;br&gt;&#x60;ONGOING&#x60; &lt;br&gt;&#x60;SUBSCRIPTION&#x60; | [optional] 
**initial_payment** | [**Amount**](Amount.md) | __Optional__. Initial payment to be charged under this consent. If enforced, this amount must match the first payment amount executed using this consent. | [optional] 
**risk** | [**PaymentRisk**](PaymentRisk.md) |  | [optional] 

## Example

```python
from yapily.models.vrp_setup_request import VRPSetupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VRPSetupRequest from a JSON string
vrp_setup_request_instance = VRPSetupRequest.from_json(json)
# print the JSON string representation of the object
print VRPSetupRequest.to_json()

# convert the object into a dict
vrp_setup_request_dict = vrp_setup_request_instance.to_dict()
# create an instance of VRPSetupRequest from a dict
vrp_setup_request_from_dict = VRPSetupRequest.from_dict(vrp_setup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


