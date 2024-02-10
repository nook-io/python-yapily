# FrequencyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency_type** | [**FrequencyEnumExtended**](FrequencyEnumExtended.md) |  | [optional] 
**interval_week** | **int** |  | [optional] 
**interval_month** | **int** |  | [optional] 
**execution_day** | **int** |  | [optional] 

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
frequency_response_form_dict = frequency_response.from_dict(frequency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


