# RawResponse

Interaction (raw request and response) that occured with the `Institution` in order to fulfil a request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**RawRequest**](RawRequest.md) |  | [optional] 
**duration** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**result_code** | **int** |  | [optional] 
**result** | **object** |  | [optional] 

## Example

```python
from yapily.models.raw_response import RawResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RawResponse from a JSON string
raw_response_instance = RawResponse.from_json(json)
# print the JSON string representation of the object
print(RawResponse.to_json())

# convert the object into a dict
raw_response_dict = raw_response_instance.to_dict()
# create an instance of RawResponse from a dict
raw_response_from_dict = RawResponse.from_dict(raw_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


