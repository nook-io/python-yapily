# BalancePredictionProfile

A Balance Prediction profile for a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status, will be COMPLETED which represents successful retreival of profile. | [optional] 
**profile_consents** | [**List[ProfileConsent]**](ProfileConsent.md) | A list of ProfileConsents used in the Balance Prediction profile. | [optional] 
**enriched_balances** | [**List[EnrichedBalances]**](EnrichedBalances.md) | A list of Balances returned by Balance Prediction profile. | [optional] 

## Example

```python
from yapily.models.balance_prediction_profile import BalancePredictionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BalancePredictionProfile from a JSON string
balance_prediction_profile_instance = BalancePredictionProfile.from_json(json)
# print the JSON string representation of the object
print BalancePredictionProfile.to_json()

# convert the object into a dict
balance_prediction_profile_dict = balance_prediction_profile_instance.to_dict()
# create an instance of BalancePredictionProfile from a dict
balance_prediction_profile_form_dict = balance_prediction_profile.from_dict(balance_prediction_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


