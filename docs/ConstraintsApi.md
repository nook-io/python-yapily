# yapily.ConstraintsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_constraints_rules_by_institution**](ConstraintsApi.md#get_account_constraints_rules_by_institution) | **GET** /institutions/constraints/data | Get Data Constraints Rules
[**get_payment_constraints_rules_by_institution**](ConstraintsApi.md#get_payment_constraints_rules_by_institution) | **GET** /institutions/constraints/payments | Get Payment Constraints Rules


# **get_account_constraints_rules_by_institution**
> ApiListResponseOfDataConstraints get_account_constraints_rules_by_institution(institution_ids, institution_country_code, endpoint_path=endpoint_path, endpoint_method=endpoint_method)

Get Data Constraints Rules

Get Data Constraints Rules against an Institution for Account Authorisation requests

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_data_constraints import ApiListResponseOfDataConstraints
from yapily.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = yapily.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.ConstraintsApi(api_client)
    institution_ids = ['institution_ids_example'] # List[str] | Unique Id(s) of the `Institution`(s) to retrieve the Data Constraints for. Multiple institutionIds need to be separated by `,`
    institution_country_code = 'institution_country_code_example' # str | Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response.
    endpoint_path = 'endpoint_path_example' # str | The path on the API that is associated with the operation for which constraints are to be retrieved (optional)
    endpoint_method = 'endpoint_method_example' # str | The HTTP method that is associated with the operation for which constraints are to be retrieved (optional)

    try:
        # Get Data Constraints Rules
        api_response = api_instance.get_account_constraints_rules_by_institution(institution_ids, institution_country_code, endpoint_path=endpoint_path, endpoint_method=endpoint_method)
        print("The response of ConstraintsApi->get_account_constraints_rules_by_institution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstraintsApi->get_account_constraints_rules_by_institution: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_ids** | [**List[str]**](str.md)| Unique Id(s) of the &#x60;Institution&#x60;(s) to retrieve the Data Constraints for. Multiple institutionIds need to be separated by &#x60;,&#x60; | 
 **institution_country_code** | **str**| Country code of the &#x60;Institution&#x60;(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response. | 
 **endpoint_path** | **str**| The path on the API that is associated with the operation for which constraints are to be retrieved | [optional] 
 **endpoint_method** | **str**| The HTTP method that is associated with the operation for which constraints are to be retrieved | [optional] 

### Return type

[**ApiListResponseOfDataConstraints**](ApiListResponseOfDataConstraints.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request. |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**404** | Not Found. |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_constraints_rules_by_institution**
> ApiListResponseOfPaymentConstraints get_payment_constraints_rules_by_institution(institution_ids, institution_country_code, payment_type, endpoint_path=endpoint_path, endpoint_method=endpoint_method)

Get Payment Constraints Rules

Retrieve institution specific constraints for payment authorisation and submission requests

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_payment_constraints import ApiListResponseOfPaymentConstraints
from yapily.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = yapily.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.ConstraintsApi(api_client)
    institution_ids = ['institution_ids_example'] # List[str] | Unique Id(s) of the `Institution`(s) to retrieve the Payment Constraints for. Multiple institutionIds need to be separated by `,`
    institution_country_code = 'institution_country_code_example' # str | Country code of the `Institution`(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response.
    payment_type = 'payment_type_example' # str | Type of payment to retrieve payment constraints for
    endpoint_path = 'endpoint_path_example' # str | The path on the API that is associated with the operation for which constraints are to be retrieved (optional)
    endpoint_method = 'endpoint_method_example' # str | The HTTP method that is associated with the operation for which constraints are to be retrieved (optional)

    try:
        # Get Payment Constraints Rules
        api_response = api_instance.get_payment_constraints_rules_by_institution(institution_ids, institution_country_code, payment_type, endpoint_path=endpoint_path, endpoint_method=endpoint_method)
        print("The response of ConstraintsApi->get_payment_constraints_rules_by_institution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstraintsApi->get_payment_constraints_rules_by_institution: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_ids** | [**List[str]**](str.md)| Unique Id(s) of the &#x60;Institution&#x60;(s) to retrieve the Payment Constraints for. Multiple institutionIds need to be separated by &#x60;,&#x60; | 
 **institution_country_code** | **str**| Country code of the &#x60;Institution&#x60;(s). Ensure that the country code matches the respective institutionIds; any mismatch will result in an HTTP 404 error response. | 
 **payment_type** | **str**| Type of payment to retrieve payment constraints for | 
 **endpoint_path** | **str**| The path on the API that is associated with the operation for which constraints are to be retrieved | [optional] 
 **endpoint_method** | **str**| The HTTP method that is associated with the operation for which constraints are to be retrieved | [optional] 

### Return type

[**ApiListResponseOfPaymentConstraints**](ApiListResponseOfPaymentConstraints.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request. |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**404** | Not Found. |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

