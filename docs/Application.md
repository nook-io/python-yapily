# Application

Information about the application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identification for the &#x60;Application&#x60; as assigned by Yapily. | [optional] 
**name** | **str** | The individual name of the &#x60;Application&#x60;. | [optional] 
**active** | **bool** | States whether an &#x60;Application&#x60; is active. | [optional] 
**auth_callbacks** | **List[str]** |  | [optional] 
**institutions** | [**List[Institution]**](Institution.md) |  | [optional] 
**media** | [**List[Media]**](Media.md) |  | [optional] 
**created** | **datetime** | Date and time of when the application was created. | [optional] 
**updated** | **datetime** | Date and time of when the application was last updated. | [optional] 

## Example

```python
from yapily.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print Application.to_json()

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_form_dict = application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


