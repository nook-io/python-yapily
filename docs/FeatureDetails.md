# FeatureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**FeatureEnum**](FeatureEnum.md) |  | [optional] 
**endpoint** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 

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
feature_details_form_dict = feature_details.from_dict(feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


