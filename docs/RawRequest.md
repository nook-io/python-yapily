# RawRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**request_instant** | **datetime** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**body** | **object** |  | [optional] 
**body_parameters** | **Dict[str, str]** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 

## Example

```python
from yapily.models.raw_request import RawRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RawRequest from a JSON string
raw_request_instance = RawRequest.from_json(json)
# print the JSON string representation of the object
print RawRequest.to_json()

# convert the object into a dict
raw_request_dict = raw_request_instance.to_dict()
# create an instance of RawRequest from a dict
raw_request_form_dict = raw_request.from_dict(raw_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


