# UserSettings

Specifies the language and location preferences of the user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | 2 letter ISO Language code which denotes the language preference for the &#x60;User&#x60;. | [optional] 
**location** | **str** | 2 letter ISO Country code which denotes the location preference for the &#x60;User&#x60;. | [optional] 

## Example

```python
from yapily.models.user_settings import UserSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettings from a JSON string
user_settings_instance = UserSettings.from_json(json)
# print the JSON string representation of the object
print UserSettings.to_json()

# convert the object into a dict
user_settings_dict = user_settings_instance.to_dict()
# create an instance of UserSettings from a dict
user_settings_from_dict = UserSettings.from_dict(user_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


