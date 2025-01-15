# FrequencyRequest

__Mandatory__. Defines the intervals at which payment should be made.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FrequencyEnumExtended**](FrequencyEnumExtended.md) |  | 
**interval_week** | **int** | __Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information | [optional] 
**interval_month** | **int** | __Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information | [optional] 
**execution_day** | **int** | __Conditional__. See [payment frequency](/guides/payments/payment-execution/periodic-payments/#payment-frequency) for more information | [optional] 

## Example

```python
from yapily.models.frequency_request import FrequencyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FrequencyRequest from a JSON string
frequency_request_instance = FrequencyRequest.from_json(json)
# print the JSON string representation of the object
print FrequencyRequest.to_json()

# convert the object into a dict
frequency_request_dict = frequency_request_instance.to_dict()
# create an instance of FrequencyRequest from a dict
frequency_request_from_dict = FrequencyRequest.from_dict(frequency_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


