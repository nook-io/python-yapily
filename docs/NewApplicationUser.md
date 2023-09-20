# NewApplicationUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_user_id** | **str** | __Optional__. An additional unique identifier that you can specify when creating a new &#x60;User&#x60; to more easily reference it | [optional] 
**reference_id** | **str** | __Deprecated__. A non-unique reference Id for the &#x60;User&#x60; | [optional] 

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
new_application_user_form_dict = new_application_user.from_dict(new_application_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


