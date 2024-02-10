# ExtendConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_confirmed_at** | **datetime** | __Mandatory__. The time that the user confirmed access to their account information | 

## Example

```python
from yapily.models.extend_consent_request import ExtendConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendConsentRequest from a JSON string
extend_consent_request_instance = ExtendConsentRequest.from_json(json)
# print the JSON string representation of the object
print ExtendConsentRequest.to_json()

# convert the object into a dict
extend_consent_request_dict = extend_consent_request_instance.to_dict()
# create an instance of ExtendConsentRequest from a dict
extend_consent_request_form_dict = extend_consent_request.from_dict(extend_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


