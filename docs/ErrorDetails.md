# ErrorDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** | Unique identifier of the request, used by Yapily for support purposes | 
**code** | **int** | Numeric HTTP status code associated with the error | 
**status** | **str** | Textual description of the HTTP status | 
**support_url** | **str** | Link to where further information regarding the error can be found | [optional] 
**source** | **str** | Source of the error. This may be YAPILY, the INSTITUTION, or the USER | [optional] 
**issues** | [**List[ErrorIssue]**](ErrorIssue.md) | List of issues relating to the error | [optional] 

## Example

```python
from yapily.models.error_details import ErrorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetails from a JSON string
error_details_instance = ErrorDetails.from_json(json)
# print the JSON string representation of the object
print ErrorDetails.to_json()

# convert the object into a dict
error_details_dict = error_details_instance.to_dict()
# create an instance of ErrorDetails from a dict
error_details_from_dict = ErrorDetails.from_dict(error_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


