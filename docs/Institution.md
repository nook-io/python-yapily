# Institution

Typically, a bank or business unit within a bank e.g. (AIB Business, AIB Ireland, AIB UK).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the &#x60;Institution&#x60;. | [optional] 
**name** | **str** | The friendly name of the &#x60;Institution&#x60;. | [optional] 
**full_name** | **str** | The full name of the &#x60;Institution&#x60;. | [optional] 
**countries** | [**List[Country]**](Country.md) | An array of &#x60;Country&#x60; denoting which regions the &#x60;Institution&#x60; provides coverage for | [optional] 
**environment_type** | [**EnvironmentType**](EnvironmentType.md) |  | [optional] 
**credentials_type** | [**CredentialsType**](CredentialsType.md) |  | [optional] 
**media** | [**List[Media]**](Media.md) | Contains links to the logo and the icons for the &#x60;Institution&#x60; | [optional] 
**features** | [**List[FeatureEnum]**](FeatureEnum.md) |  | [optional] 

## Example

```python
from yapily.models.institution import Institution

# TODO update the JSON string below
json = "{}"
# create an instance of Institution from a JSON string
institution_instance = Institution.from_json(json)
# print the JSON string representation of the object
print Institution.to_json()

# convert the object into a dict
institution_dict = institution_instance.to_dict()
# create an instance of Institution from a dict
institution_from_dict = Institution.from_dict(institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


