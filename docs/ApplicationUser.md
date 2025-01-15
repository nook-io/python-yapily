# ApplicationUser

Information about a user of an application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | A unique identifier for the &#39;User&#39; assigned by Yapily. | [optional] 
**application_uuid** | **str** | Unique identifier of the application the user is associated with. | [optional] 
**application_user_id** | **str** | __Conditional__. The user-friendly reference to the &#x60;User&#x60;. | [optional] 
**reference_id** | **str** |  | [optional] 
**created_at** | **datetime** | Date and time of when the user was created. | [optional] 
**institution_consents** | [**List[InstitutionConsent]**](InstitutionConsent.md) |  | [optional] 

## Example

```python
from yapily.models.application_user import ApplicationUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUser from a JSON string
application_user_instance = ApplicationUser.from_json(json)
# print the JSON string representation of the object
print ApplicationUser.to_json()

# convert the object into a dict
application_user_dict = application_user_instance.to_dict()
# create an instance of ApplicationUser from a dict
application_user_from_dict = ApplicationUser.from_dict(application_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


