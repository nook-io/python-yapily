# ApiError

Provides details of the error that has occurred.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | _Mandatory_. Numeric &#x60;HTTP&#x60; status code associated with the error. | [optional] 
**institution_error** | [**InstitutionError**](InstitutionError.md) |  | [optional] 
**message** | **str** | __Mandatory__. Description of the exact error that has been experienced. | [optional] 
**source** | **str** |  | [optional] 
**status** | **str** | __Mandatory__. Textual description of the &#x60;HTTP&#x60; error status type. | [optional] 
**tracing_id** | **str** | _Optional_.  A unique identifier assigned by Yapily for the request that can be used for support purposes. | [optional] 

## Example

```python
from yapily.models.api_error import ApiError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiError from a JSON string
api_error_instance = ApiError.from_json(json)
# print the JSON string representation of the object
print ApiError.to_json()

# convert the object into a dict
api_error_dict = api_error_instance.to_dict()
# create an instance of ApiError from a dict
api_error_from_dict = ApiError.from_dict(api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


