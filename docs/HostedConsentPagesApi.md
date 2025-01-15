# yapily.HostedConsentPagesApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hosted_consent_request**](HostedConsentPagesApi.md#create_hosted_consent_request) | **POST** /hosted/consent-requests | Create Hosted Consent Request
[**get_hosted_consent_request**](HostedConsentPagesApi.md#get_hosted_consent_request) | **GET** /hosted/consent-requests/{consentRequestId} | Get Hosted Consent Request


# **create_hosted_consent_request**
> ApiResponseOfCreateHostedConsentRequest create_hosted_consent_request(create_hosted_consent_request)

Create Hosted Consent Request

Used to initiate a consent request using Yapily Hosted Pages.

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_create_hosted_consent_request import ApiResponseOfCreateHostedConsentRequest
from yapily.models.create_hosted_consent_request import CreateHostedConsentRequest
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
async with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.HostedConsentPagesApi(api_client)
    create_hosted_consent_request = yapily.CreateHostedConsentRequest() # CreateHostedConsentRequest | 

    try:
        # Create Hosted Consent Request
        api_response = await api_instance.create_hosted_consent_request(create_hosted_consent_request)
        print("The response of HostedConsentPagesApi->create_hosted_consent_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedConsentPagesApi->create_hosted_consent_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hosted_consent_request** | [**CreateHostedConsentRequest**](CreateHostedConsentRequest.md)|  | 

### Return type

[**ApiResponseOfCreateHostedConsentRequest**](ApiResponseOfCreateHostedConsentRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. Credentials are missing or invalid |  -  |
**500** | Unexpected Error |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_consent_request**
> ApiResponseOfGetHostedConsentRequest get_hosted_consent_request(consent_request_id)

Get Hosted Consent Request

Used to get details of a hosted consent request

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_get_hosted_consent_request import ApiResponseOfGetHostedConsentRequest
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
async with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.HostedConsentPagesApi(api_client)
    consent_request_id = 'consent_request_id_example' # str | Unique Identifier of the consent request

    try:
        # Get Hosted Consent Request
        api_response = await api_instance.get_hosted_consent_request(consent_request_id)
        print("The response of HostedConsentPagesApi->get_hosted_consent_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedConsentPagesApi->get_hosted_consent_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_request_id** | **str**| Unique Identifier of the consent request | 

### Return type

[**ApiResponseOfGetHostedConsentRequest**](ApiResponseOfGetHostedConsentRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Unexpected Error |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

