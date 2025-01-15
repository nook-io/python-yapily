# AmountDetailsResponse

Monetary Amount.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The monetary value | [optional] 
**currency** | **str** | The [ISO 4217](https://www.xe.com/iso4217.php) currency code | [optional] 

## Example

```python
from yapily.models.amount_details_response import AmountDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AmountDetailsResponse from a JSON string
amount_details_response_instance = AmountDetailsResponse.from_json(json)
# print the JSON string representation of the object
print AmountDetailsResponse.to_json()

# convert the object into a dict
amount_details_response_dict = amount_details_response_instance.to_dict()
# create an instance of AmountDetailsResponse from a dict
amount_details_response_from_dict = AmountDetailsResponse.from_dict(amount_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


