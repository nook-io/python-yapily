# FeatureDetails

Features that an individual `Institution` may support. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**FeatureEnum**](FeatureEnum.md) |  | [optional] 
**endpoint** | **str** | Endpoints that are associated with the feature e.g. (available for use if an Institution supports a feature). | [optional] 
**documentation_url** | **str** | The link to further documentation regarding the feature. | [optional] 

## Example

```python
from yapily.models.feature_details import FeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureDetails from a JSON string
feature_details_instance = FeatureDetails.from_json(json)
# print the JSON string representation of the object
print FeatureDetails.to_json()

# convert the object into a dict
feature_details_dict = feature_details_instance.to_dict()
# create an instance of FeatureDetails from a dict
feature_details_from_dict = FeatureDetails.from_dict(feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


