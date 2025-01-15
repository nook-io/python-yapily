# RedirectRequest

__Optional__. The server to redirect the user to after the user complete the authorisation at the `Institution`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | __Mandatory__.Successful redirect after the user complete the authorisation at the &#x60;Institution&#x60;. | 

## Example

```python
from yapily.models.redirect_request import RedirectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectRequest from a JSON string
redirect_request_instance = RedirectRequest.from_json(json)
# print the JSON string representation of the object
print(RedirectRequest.to_json())

# convert the object into a dict
redirect_request_dict = redirect_request_instance.to_dict()
# create an instance of RedirectRequest from a dict
redirect_request_from_dict = RedirectRequest.from_dict(redirect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


