# HostedAmountDetails

The payment amount and currency

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_to_pay** | **float** | The payment amount | 
**currency** | **str** | The [ISO 4217](https://www.xe.com/iso4217.php) currency code | 

## Example

```python
from yapily.models.hosted_amount_details import HostedAmountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostedAmountDetails from a JSON string
hosted_amount_details_instance = HostedAmountDetails.from_json(json)
# print the JSON string representation of the object
print HostedAmountDetails.to_json()

# convert the object into a dict
hosted_amount_details_dict = hosted_amount_details_instance.to_dict()
# create an instance of HostedAmountDetails from a dict
hosted_amount_details_from_dict = HostedAmountDetails.from_dict(hosted_amount_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


