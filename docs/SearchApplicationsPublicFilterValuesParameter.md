# SearchApplicationsPublicFilterValuesParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **List[str]** | Sub-application ids to filter the results for. If provided, the results will only include sub-applications with the given ids. Non-existent ids will be ignored. | [optional] 
**offset** | **int** | The number of results to skip. | [optional] [default to 0]
**limit** | **int** | The maximum number of results to return. | [optional] [default to 1000]
**sort** | **str** | The field to sort the results by.&lt;br&gt;&lt;br&gt;Possible values:&lt;ul&gt;&lt;li&gt;&#x60;last_updated&#x60; (ascending)&lt;/li&gt;&lt;li&gt;&#x60;-last_updated&#x60; (descending)&lt;/li&gt;&lt;li&gt;&#x60;name&#x60; (ascending)&lt;/li&gt;&lt;li&gt;&#x60;-name&#x60; (descending)&lt;/li&gt;&lt;li&gt;&#x60;uuid&#x60; (ascending)&lt;/li&gt;&lt;li&gt;&#x60;-uuid&#x60; (descending)&lt;/li&gt;&lt;/ul&gt; | [optional] [default to 'name']

## Example

```python
from yapily.models.search_applications_public_filter_values_parameter import SearchApplicationsPublicFilterValuesParameter

# TODO update the JSON string below
json = "{}"
# create an instance of SearchApplicationsPublicFilterValuesParameter from a JSON string
search_applications_public_filter_values_parameter_instance = SearchApplicationsPublicFilterValuesParameter.from_json(json)
# print the JSON string representation of the object
print SearchApplicationsPublicFilterValuesParameter.to_json()

# convert the object into a dict
search_applications_public_filter_values_parameter_dict = search_applications_public_filter_values_parameter_instance.to_dict()
# create an instance of SearchApplicationsPublicFilterValuesParameter from a dict
search_applications_public_filter_values_parameter_form_dict = search_applications_public_filter_values_parameter.from_dict(search_applications_public_filter_values_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


