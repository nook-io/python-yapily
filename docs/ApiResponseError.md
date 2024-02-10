# ApiResponseError

Used to return errors from the bank from each request<ul><li>`400` - Returned by any `POST` endpoint when the body does not conform to the contract</li><li>`401` - Returned by any endpoint when an invalid `authToken` is used for authentication</li><li>`403` - Returned by any [Financial Data](https://docs.yapily.com/api/reference/#tag/Financial-Data) and any [Payments](https://docs.yapily.com/api/reference/#tag/Payments) endpoint when the `Consent` is no longer authorised to access financial data or to make a payment</li><li>`404` - Returned by any endpoint where there are path parameters and the path parameters supplied are unable to find the desired resource</li><li>`409` - Returned by any `POST` endpoint when creating a resource that conflicts with any other existing resource e.g. [Create User](https://docs.yapily.com/api/reference/#operation/addUser)</li><li>`424` - Returned by any [Financial Data](https://docs.yapily.com/api/reference/#tag/Financial-Data) and any [Payments](https://docs.yapily.com/api/reference/#tag/Payments) endpoint when the feature to be accessed is not supported by the `Institution`.</li><li>`500` - Returned by any endpoint when Yapily is down. If you encounter any false positives, please <a href=\"mailto:support@yapily.com\">notify us</a></li></ul>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ApiError**](ApiError.md) |  | [optional] 
**monitoring** | [**List[MonitoringEndpointStatus]**](MonitoringEndpointStatus.md) |  | [optional] 
**raw** | [**List[RawResponse]**](RawResponse.md) |  | [optional] 

## Example

```python
from yapily.models.api_response_error import ApiResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseError from a JSON string
api_response_error_instance = ApiResponseError.from_json(json)
# print the JSON string representation of the object
print ApiResponseError.to_json()

# convert the object into a dict
api_response_error_dict = api_response_error_instance.to_dict()
# create an instance of ApiResponseError from a dict
api_response_error_form_dict = api_response_error.from_dict(api_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


