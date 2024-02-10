# MultiAuthorisation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**number_of_authorisation_required** | **int** |  | [optional] 
**number_of_authorisation_received** | **int** |  | [optional] 
**last_updated_date_time** | **datetime** |  | [optional] 
**expiration_date_time** | **datetime** |  | [optional] 

## Example

```python
from yapily.models.multi_authorisation import MultiAuthorisation

# TODO update the JSON string below
json = "{}"
# create an instance of MultiAuthorisation from a JSON string
multi_authorisation_instance = MultiAuthorisation.from_json(json)
# print the JSON string representation of the object
print MultiAuthorisation.to_json()

# convert the object into a dict
multi_authorisation_dict = multi_authorisation_instance.to_dict()
# create an instance of MultiAuthorisation from a dict
multi_authorisation_form_dict = multi_authorisation.from_dict(multi_authorisation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


