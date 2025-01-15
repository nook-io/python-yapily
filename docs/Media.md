# Media

Details of the media held for the `Institution`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | __Mandatory__. URL from where the media can be retrieved. | [optional] 
**type** | **str** | __Mandatory__. The type of media e.g. (logo, icon). | [optional] 

## Example

```python
from yapily.models.media import Media

# TODO update the JSON string below
json = "{}"
# create an instance of Media from a JSON string
media_instance = Media.from_json(json)
# print the JSON string representation of the object
print(Media.to_json())

# convert the object into a dict
media_dict = media_instance.to_dict()
# create an instance of Media from a dict
media_from_dict = Media.from_dict(media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


