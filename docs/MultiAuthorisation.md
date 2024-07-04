# MultiAuthorisation

Details the additional levels of authorisation which are required from, and being managed by, the `Institution`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | _Mandatory_. Specifies the current status of the multi-authorisation flow. | [optional] 
**number_of_authorisation_required** | **int** | __Mandatory__. Total number of authorisations required. | [optional] 
**number_of_authorisation_received** | **int** | __Mandatory__. The total number of authorisations that have been recieved. | [optional] 
**last_updated_date_time** | **datetime** | __Mandatory__. Date and time of when the authorisation was last updated. | [optional] 
**expiration_date_time** | **datetime** | __Mandatory__. Date and time by when the authorisation flow must be completed before it expires and the authorisation request is terminated. | [optional] 

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


