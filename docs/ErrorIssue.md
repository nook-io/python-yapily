# ErrorIssue

Detailed information regarding the issue that was experienced during processing of the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Category of the issue | 
**code** | **str** | Code that uniquely identifies the type of issue | 
**parameter** | **str** | Identfies the parameter / property within the request (headers, query parameters or body) that the issue relates to. For headers and query parameters, it refers to the parameter name. For the body, it refers to the JSONPath of the property | [optional] 
**message** | **str** | Human readable description of the issue that was experienced | [optional] 
**institution_error** | [**InstitutionError**](InstitutionError.md) |  | [optional] 

## Example

```python
from yapily.models.error_issue import ErrorIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorIssue from a JSON string
error_issue_instance = ErrorIssue.from_json(json)
# print the JSON string representation of the object
print ErrorIssue.to_json()

# convert the object into a dict
error_issue_dict = error_issue_instance.to_dict()
# create an instance of ErrorIssue from a dict
error_issue_form_dict = error_issue.from_dict(error_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


