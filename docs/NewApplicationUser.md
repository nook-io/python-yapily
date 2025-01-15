# NewApplicationUser

Details of a new user to be created for the application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_user_id** | **str** | __Optional__. The unique identifier of the &#x60;Application User&#x60; assigned by the Application Owner. | [optional] 
**reference_id** | **str** | __Deprecated__. A non-unique reference Id for the &#x60;Application User&#x60;. | [optional] 

## Example

```python
from yapily.models.new_application_user import NewApplicationUser

# TODO update the JSON string below
json = "{}"
# create an instance of NewApplicationUser from a JSON string
new_application_user_instance = NewApplicationUser.from_json(json)
# print the JSON string representation of the object
print NewApplicationUser.to_json()

# convert the object into a dict
new_application_user_dict = new_application_user_instance.to_dict()
# create an instance of NewApplicationUser from a dict
new_application_user_from_dict = NewApplicationUser.from_dict(new_application_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


