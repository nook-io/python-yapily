# yapily.HostedPagesApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hosted_payment_request**](HostedPagesApi.md#create_hosted_payment_request) | **POST** /hosted/payment-requests | Create Hosted payment request
[**create_hosted_payment_request_link**](HostedPagesApi.md#create_hosted_payment_request_link) | **POST** /hosted/payment-requests/links | Create Pay By Link
[**get_hosted_payment_request**](HostedPagesApi.md#get_hosted_payment_request) | **GET** /hosted/payment-requests/{paymentRequestId} | Get Hosted payment request


# **create_hosted_payment_request**
> ApiResponseOfCreateHostedPaymentRequest create_hosted_payment_request(create_hosted_payment_request)

Create Hosted payment request

Used to initiate a payment request using Yapily Hosted Pages.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_create_hosted_payment_request import ApiResponseOfCreateHostedPaymentRequest
from yapily.models.create_hosted_payment_request import CreateHostedPaymentRequest
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
    api_instance = yapily.HostedPagesApi(api_client)
    create_hosted_payment_request = yapily.CreateHostedPaymentRequest() # CreateHostedPaymentRequest | 

    try:
        # Create Hosted payment request
        api_response = await api_instance.create_hosted_payment_request(create_hosted_payment_request)
        print("The response of HostedPagesApi->create_hosted_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->create_hosted_payment_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hosted_payment_request** | [**CreateHostedPaymentRequest**](CreateHostedPaymentRequest.md)|  | 

### Return type

[**ApiResponseOfCreateHostedPaymentRequest**](ApiResponseOfCreateHostedPaymentRequest.md)

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

# **create_hosted_payment_request_link**
> ApiResponseOfCreateHostedPaymentRequestLink create_hosted_payment_request_link(create_hosted_payment_request_link)

Create Pay By Link

Used to created a long lived payment request for Pay By Link

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_create_hosted_payment_request_link import ApiResponseOfCreateHostedPaymentRequestLink
from yapily.models.create_hosted_payment_request_link import CreateHostedPaymentRequestLink
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
    api_instance = yapily.HostedPagesApi(api_client)
    create_hosted_payment_request_link = yapily.CreateHostedPaymentRequestLink() # CreateHostedPaymentRequestLink | 

    try:
        # Create Pay By Link
        api_response = await api_instance.create_hosted_payment_request_link(create_hosted_payment_request_link)
        print("The response of HostedPagesApi->create_hosted_payment_request_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->create_hosted_payment_request_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hosted_payment_request_link** | [**CreateHostedPaymentRequestLink**](CreateHostedPaymentRequestLink.md)|  | 

### Return type

[**ApiResponseOfCreateHostedPaymentRequestLink**](ApiResponseOfCreateHostedPaymentRequestLink.md)

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

# **get_hosted_payment_request**
> ApiResponseOfGetHostedPaymentRequest get_hosted_payment_request(payment_request_id)

Get Hosted payment request

Used to get details of a payment request

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_get_hosted_payment_request import ApiResponseOfGetHostedPaymentRequest
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
    api_instance = yapily.HostedPagesApi(api_client)
    payment_request_id = 'payment_request_id_example' # str | Unique Identifier of the payment request

    try:
        # Get Hosted payment request
        api_response = await api_instance.get_hosted_payment_request(payment_request_id)
        print("The response of HostedPagesApi->get_hosted_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->get_hosted_payment_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| Unique Identifier of the payment request | 

### Return type

[**ApiResponseOfGetHostedPaymentRequest**](ApiResponseOfGetHostedPaymentRequest.md)

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

