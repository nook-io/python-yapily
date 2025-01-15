# ApiErrorResponseV2ErrorIssuesInner

Detailed information regarding the issue that was experienced during processing of the request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Category of the issue | [optional] 
**code** | **str** | 5 digit Error Code that uniquely identifies the type of issue, for full list of error codes pelase check our documentation | 
**message** | **str** | Human readable description of the issue that was experienced | 

## Example

```python
from yapily.models.api_error_response_v2_error_issues_inner import ApiErrorResponseV2ErrorIssuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorResponseV2ErrorIssuesInner from a JSON string
api_error_response_v2_error_issues_inner_instance = ApiErrorResponseV2ErrorIssuesInner.from_json(json)
# print the JSON string representation of the object
print ApiErrorResponseV2ErrorIssuesInner.to_json()

# convert the object into a dict
api_error_response_v2_error_issues_inner_dict = api_error_response_v2_error_issues_inner_instance.to_dict()
# create an instance of ApiErrorResponseV2ErrorIssuesInner from a dict
api_error_response_v2_error_issues_inner_from_dict = ApiErrorResponseV2ErrorIssuesInner.from_dict(api_error_response_v2_error_issues_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


