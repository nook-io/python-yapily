# DataConstraintsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | The id to represent the &#x60;Institution&#x60;. | 
**institution_country_code** | **str** | 2 letter ISO Country code of the &#x60;Institution&#x60;. | [optional] 
**endpoint_path** | **str** | Define the applicable API end point. | [optional] 
**endpoint_method** | **str** | Https Method for the endpoint. | [optional] 
**request** | [**RequestConstraints**](RequestConstraints.md) |  | 

## Example

```python
from yapily.models.data_constraints_response import DataConstraintsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataConstraintsResponse from a JSON string
data_constraints_response_instance = DataConstraintsResponse.from_json(json)
# print the JSON string representation of the object
print(DataConstraintsResponse.to_json())

# convert the object into a dict
data_constraints_response_dict = data_constraints_response_instance.to_dict()
# create an instance of DataConstraintsResponse from a dict
data_constraints_response_from_dict = DataConstraintsResponse.from_dict(data_constraints_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


