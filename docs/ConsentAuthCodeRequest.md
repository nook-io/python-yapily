# ConsentAuthCodeRequest

The request body containing the `ConsentAuthCodeRequest` json payload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** | __Mandatory__. The authorisation code | 
**auth_state** | **str** | __Mandatory__. The authorisation state | 

## Example

```python
from yapily.models.consent_auth_code_request import ConsentAuthCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentAuthCodeRequest from a JSON string
consent_auth_code_request_instance = ConsentAuthCodeRequest.from_json(json)
# print the JSON string representation of the object
print ConsentAuthCodeRequest.to_json()

# convert the object into a dict
consent_auth_code_request_dict = consent_auth_code_request_instance.to_dict()
# create an instance of ConsentAuthCodeRequest from a dict
consent_auth_code_request_form_dict = consent_auth_code_request.from_dict(consent_auth_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


