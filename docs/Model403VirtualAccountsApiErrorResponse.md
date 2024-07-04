# Model403VirtualAccountsApiErrorResponse

Used to return errors from the bank from each request<ul><li>`400` - Returned by any `POST` endpoint when the body does not conform to the contract</li><li>`401` - Returned by any endpoint when an invalid `authToken` is used for authentication</li><li>`403` - Returned by any [Financial Data](https://docs.yapily.com/api/#yapily-api-financial-data) and any [Payments](https://docs.yapily.com/api/#yapily-api-payments) endpoint when the `Consent` is no longer authorised to access financial data or to make a payment</li><li>`404` - Returned by any endpoint where there are path parameters and the path parameters supplied are unable to find the desired resource</li><li>`409` - Returned by any `POST` endpoint when creating a resource that conflicts with any other existing resource e.g. [Create User](https://docs.yapily.com/api/#create-user)</li><li>`424` - Returned by any [Financial Data](https://docs.yapily.com/api/#yapily-api-financial-data) and any [Payments](https://docs.yapily.com/api/#yapily-api-payments) endpoint when the feature to be accessed is not supported by the `Institution`.</li><li>`500` - Returned by any endpoint when Yapily is down. If you encounter any false positives, please <a href=\"mailto:support@yapily.com\">notify us</a></li></ul>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 
**monitoring** | [**List[MonitoringEndpointStatus]**](MonitoringEndpointStatus.md) |  | [optional] 

## Example

```python
from yapily.models.model403_virtual_accounts_api_error_response import Model403VirtualAccountsApiErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Model403VirtualAccountsApiErrorResponse from a JSON string
model403_virtual_accounts_api_error_response_instance = Model403VirtualAccountsApiErrorResponse.from_json(json)
# print the JSON string representation of the object
print Model403VirtualAccountsApiErrorResponse.to_json()

# convert the object into a dict
model403_virtual_accounts_api_error_response_dict = model403_virtual_accounts_api_error_response_instance.to_dict()
# create an instance of Model403VirtualAccountsApiErrorResponse from a dict
model403_virtual_accounts_api_error_response_form_dict = model403_virtual_accounts_api_error_response.from_dict(model403_virtual_accounts_api_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


