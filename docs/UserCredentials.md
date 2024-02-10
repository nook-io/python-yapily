# UserCredentials

__Conditional__. Used to capture the user's credentials to allow them to login to an `Institution` that uses the embedded account authorisation flow. <br><br>This is the first step required in the embedded account authorisation flow to authorise the `Consent`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | __Mandatory__. The login id for the user for a particular &#x60;Institution&#x60;. | 
**corporate_id** | **str** | __Conditional__. The corporate login for the user for a particular corporate &#x60;Institution&#x60;. | [optional] 
**password** | **str** | __Mandatory__. The password of the user to login to a particular &#x60;Institution&#x60;. | 

## Example

```python
from yapily.models.user_credentials import UserCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of UserCredentials from a JSON string
user_credentials_instance = UserCredentials.from_json(json)
# print the JSON string representation of the object
print UserCredentials.to_json()

# convert the object into a dict
user_credentials_dict = user_credentials_instance.to_dict()
# create an instance of UserCredentials from a dict
user_credentials_form_dict = user_credentials.from_dict(user_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


