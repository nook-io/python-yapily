# ScaMethod

__Conditional__. Used to update the authorisation with the sca method of the user's choice for the `Institution` that uses the embedded authorisation flow. If the user has multiple sca methods configured, the `Institution` will allow the user to select from each of these options. <br><br>When the user has multiple sca methods for the `Institution`, this is the second step required in the embedded authorisation flow to authorise the `Consent`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | __Mandatory__. The id of the sca method provided by the &#x60;Institution&#x60; | 
**type** | [**Type**](Type.md) |  | [optional] 
**description** | **str** | __Optional__. A description of the sca method if provided by the &#x60;Institution&#x60; | [optional] 
**information** | **str** | Additional information from the institution to provide to the PSU to help with the selected SCA method. The language is determined by the institution and may vary. | [optional] 
**data** | **List[str]** | Data from the institution to provide to the PSU to complete authorisation. The language is determined by the institution and may vary. | [optional] 

## Example

```python
from yapily.models.sca_method import ScaMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ScaMethod from a JSON string
sca_method_instance = ScaMethod.from_json(json)
# print the JSON string representation of the object
print(ScaMethod.to_json())

# convert the object into a dict
sca_method_dict = sca_method_instance.to_dict()
# create an instance of ScaMethod from a dict
sca_method_from_dict = ScaMethod.from_dict(sca_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


