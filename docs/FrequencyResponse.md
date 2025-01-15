# FrequencyResponse

__Mandatory__. Defines the intervals at which payment should be made.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency_type** | [**FrequencyEnumExtended**](FrequencyEnumExtended.md) |  | [optional] 
**interval_week** | **int** | The weekly intervals at which a payment will be made. e.g. 1 &#x3D; Every months, 2 &#x3D; Every 2 months. | [optional] 
**interval_month** | **int** | The monthly intervals at which a payment will be made. e.g. 1 &#x3D; Every month, 2 &#x3D; Every 2 months | [optional] 
**execution_day** | **int** | The day on which a payment will be made, according to the weekly or monthly interval. | [optional] 

## Example

```python
from yapily.models.frequency_response import FrequencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FrequencyResponse from a JSON string
frequency_response_instance = FrequencyResponse.from_json(json)
# print the JSON string representation of the object
print FrequencyResponse.to_json()

# convert the object into a dict
frequency_response_dict = frequency_response_instance.to_dict()
# create an instance of FrequencyResponse from a dict
frequency_response_from_dict = FrequencyResponse.from_dict(frequency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


