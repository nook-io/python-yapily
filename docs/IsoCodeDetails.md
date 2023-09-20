# IsoCodeDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] [default to 'UNKNOWN']
**name** | **str** |  | [optional] [default to 'UNKNOWN']

## Example

```python
from yapily.models.iso_code_details import IsoCodeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IsoCodeDetails from a JSON string
iso_code_details_instance = IsoCodeDetails.from_json(json)
# print the JSON string representation of the object
print IsoCodeDetails.to_json()

# convert the object into a dict
iso_code_details_dict = iso_code_details_instance.to_dict()
# create an instance of IsoCodeDetails from a dict
iso_code_details_form_dict = iso_code_details.from_dict(iso_code_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


