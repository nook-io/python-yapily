# ConsentDeleteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | __Conditional__. User-friendly identifier of the &#x60;User&#x60; that provides authorisation. If a &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; exists, it will be used otherwise, a new &#x60;User&#x60; with the specified &#x60;applicationUserId&#x60; will be created and used. Either the &#x60;userUuid&#x60; or &#x60;applicationUserId&#x60; must be provided. | [optional] 
**delete_status** | [**DeleteStatusEnum**](DeleteStatusEnum.md) |  | [optional] 
**institution_id** | **str** | __Mandatory__. The &#x60;Institution&#x60; the authorisation request is sent to. | [optional] 
**institution_consent_id** | **str** | Identification of the consent at the Institution. | [optional] 
**creation_date** | **datetime** | Date and time of when the consent was authorised. | [optional] 

## Example

```python
from yapily.models.consent_delete_response import ConsentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentDeleteResponse from a JSON string
consent_delete_response_instance = ConsentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print ConsentDeleteResponse.to_json()

# convert the object into a dict
consent_delete_response_dict = consent_delete_response_instance.to_dict()
# create an instance of ConsentDeleteResponse from a dict
consent_delete_response_from_dict = ConsentDeleteResponse.from_dict(consent_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


