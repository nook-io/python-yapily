# UserDeleteResponse

Deletion of the user. Includes the user profile and all associate consents.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the user. | [optional] 
**delete_status** | [**DeleteStatusEnum**](DeleteStatusEnum.md) |  | [optional] 
**creation_date** | **datetime** | Date and time that the user was created. | [optional] 
**user_consents** | [**List[ConsentDeleteResponse]**](ConsentDeleteResponse.md) |  | [optional] 

## Example

```python
from yapily.models.user_delete_response import UserDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeleteResponse from a JSON string
user_delete_response_instance = UserDeleteResponse.from_json(json)
# print the JSON string representation of the object
print UserDeleteResponse.to_json()

# convert the object into a dict
user_delete_response_dict = user_delete_response_instance.to_dict()
# create an instance of UserDeleteResponse from a dict
user_delete_response_form_dict = user_delete_response.from_dict(user_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


