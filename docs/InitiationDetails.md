# InitiationDetails

__Mandatory__. The payment initiation object defining the details of the payment under the Variable Recurring Payment consent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | __Optional__. The payment reference or description. Limited to a maximum of 18 characters long. | [optional] 
**payer** | [**Payer**](Payer.md) |  | [optional] 
**payee** | [**Payee**](Payee.md) |  | [optional] 

## Example

```python
from yapily.models.initiation_details import InitiationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InitiationDetails from a JSON string
initiation_details_instance = InitiationDetails.from_json(json)
# print the JSON string representation of the object
print(InitiationDetails.to_json())

# convert the object into a dict
initiation_details_dict = initiation_details_instance.to_dict()
# create an instance of InitiationDetails from a dict
initiation_details_from_dict = InitiationDetails.from_dict(initiation_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


