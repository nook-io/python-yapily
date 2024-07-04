# ResponseForwardedData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from yapily.models.response_forwarded_data import ResponseForwardedData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseForwardedData from a JSON string
response_forwarded_data_instance = ResponseForwardedData.from_json(json)
# print the JSON string representation of the object
print ResponseForwardedData.to_json()

# convert the object into a dict
response_forwarded_data_dict = response_forwarded_data_instance.to_dict()
# create an instance of ResponseForwardedData from a dict
response_forwarded_data_form_dict = response_forwarded_data.from_dict(response_forwarded_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


