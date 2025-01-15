# RequestConstraints

Object defining the constraints rules applicable for a given requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**body** | [**ModelSchema**](ModelSchema.md) |  | 

## Example

```python
from yapily.models.request_constraints import RequestConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of RequestConstraints from a JSON string
request_constraints_instance = RequestConstraints.from_json(json)
# print the JSON string representation of the object
print RequestConstraints.to_json()

# convert the object into a dict
request_constraints_dict = request_constraints_instance.to_dict()
# create an instance of RequestConstraints from a dict
request_constraints_from_dict = RequestConstraints.from_dict(request_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


