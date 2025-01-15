# yapily.HostedPaymentPagesApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hosted_payment_request**](HostedPaymentPagesApi.md#create_hosted_payment_request) | **POST** /hosted/payment-requests | Create Hosted payment request
[**create_hosted_payment_request_link**](HostedPaymentPagesApi.md#create_hosted_payment_request_link) | **POST** /hosted/payment-requests/links | Create Pay By Link
[**create_hosted_vrp_consent_request**](HostedPaymentPagesApi.md#create_hosted_vrp_consent_request) | **POST** /hosted/vrp/consent-requests | Create VRP Consent
[**create_hosted_vrp_funds_confirmation**](HostedPaymentPagesApi.md#create_hosted_vrp_funds_confirmation) | **POST** /hosted/vrp/consent-requests/{consentRequestId}/funds-confirmation | Check Funds Availability
[**create_hosted_vrp_payment**](HostedPaymentPagesApi.md#create_hosted_vrp_payment) | **POST** /hosted/vrp/consent-requests/{consentRequestId}/payments | Create VRP Payment
[**get_hosted_payment_request**](HostedPaymentPagesApi.md#get_hosted_payment_request) | **GET** /hosted/payment-requests/{paymentRequestId} | Get Hosted payment request
[**get_hosted_vrp_consent_request**](HostedPaymentPagesApi.md#get_hosted_vrp_consent_request) | **GET** /hosted/vrp/consent-requests/{consentRequestId} | Get Hosted VRP Consent Request
[**get_hosted_vrp_consent_requests**](HostedPaymentPagesApi.md#get_hosted_vrp_consent_requests) | **GET** /hosted/vrp/consent-requests | Get Hosted VRP Consent Requests
[**get_hosted_vrp_payment_request**](HostedPaymentPagesApi.md#get_hosted_vrp_payment_request) | **GET** /hosted/vrp/consent-requests/{consentRequestId}/payments/{paymentId} | Get VRP payment
[**revoke_hosted_consent_request**](HostedPaymentPagesApi.md#revoke_hosted_consent_request) | **POST** /hosted/vrp/consent-requests/{consentRequestId}/revoke | Revoke Hosted VRP Consent Request


# **create_hosted_payment_request**
> ApiResponseOfCreateHostedPaymentRequest create_hosted_payment_request(create_hosted_payment_request)

Create Hosted payment request

Used to initiate a payment request using Yapily Hosted Pages.

### Example

* Basic Authentication (basicAuth):

```python
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    create_hosted_payment_request = yapily.CreateHostedPaymentRequest() # CreateHostedPaymentRequest | 

    try:
        # Create Hosted payment request
        api_response = await api_instance.create_hosted_payment_request(create_hosted_payment_request)
        print("The response of HostedPaymentPagesApi->create_hosted_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->create_hosted_payment_request: %s\n" % e)
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    create_hosted_payment_request_link = yapily.CreateHostedPaymentRequestLink() # CreateHostedPaymentRequestLink | 

    try:
        # Create Pay By Link
        api_response = await api_instance.create_hosted_payment_request_link(create_hosted_payment_request_link)
        print("The response of HostedPaymentPagesApi->create_hosted_payment_request_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->create_hosted_payment_request_link: %s\n" % e)
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

# **create_hosted_vrp_consent_request**
> ApiResponseOfCreateHostedVRPConsentRequest create_hosted_vrp_consent_request(sub_application, create_hosted_vrp_consent_request)

Create VRP Consent

Used to initiate a VRP consent / mandate request through Yapily Hosted Pages

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_create_hosted_vrp_consent_request import ApiResponseOfCreateHostedVRPConsentRequest
from yapily.models.create_hosted_vrp_consent_request import CreateHostedVRPConsentRequest
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    sub_application = 'sub_application_example' # str | __Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)
    create_hosted_vrp_consent_request = yapily.CreateHostedVRPConsentRequest() # CreateHostedVRPConsentRequest | 

    try:
        # Create VRP Consent
        api_response = await api_instance.create_hosted_vrp_consent_request(sub_application, create_hosted_vrp_consent_request)
        print("The response of HostedPaymentPagesApi->create_hosted_vrp_consent_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->create_hosted_vrp_consent_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_application** | **str**| __Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) | 
 **create_hosted_vrp_consent_request** | [**CreateHostedVRPConsentRequest**](CreateHostedVRPConsentRequest.md)|  | 

### Return type

[**ApiResponseOfCreateHostedVRPConsentRequest**](ApiResponseOfCreateHostedVRPConsentRequest.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hosted_vrp_funds_confirmation**
> ApiResponseOfFundsConfirmationResponse create_hosted_vrp_funds_confirmation(consent_request_id, consent_token, funds_confirmation_request, sub_application=sub_application)

Check Funds Availability

Confirms whether there are available funds on the Payer account to execute a Variable Recurring Payment after obtaining the user's authorisation. <br><br>Features:<ul><li>`VARIABLE_RECURRING_PAYMENT_FUNDS_CONFIRMATION`</li></ul>

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_funds_confirmation_response import ApiResponseOfFundsConfirmationResponse
from yapily.models.funds_confirmation_request import FundsConfirmationRequest
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    consent_request_id = 'consent_request_id_example' # str | Unique Identifier of the Consent Request
    consent_token = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    funds_confirmation_request = yapily.FundsConfirmationRequest() # FundsConfirmationRequest | 
    sub_application = 'sub_application_example' # str | The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) (optional)

    try:
        # Check Funds Availability
        api_response = await api_instance.create_hosted_vrp_funds_confirmation(consent_request_id, consent_token, funds_confirmation_request, sub_application=sub_application)
        print("The response of HostedPaymentPagesApi->create_hosted_vrp_funds_confirmation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->create_hosted_vrp_funds_confirmation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_request_id** | **str**| Unique Identifier of the Consent Request | 
 **consent_token** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **funds_confirmation_request** | [**FundsConfirmationRequest**](FundsConfirmationRequest.md)|  | 
 **sub_application** | **str**| The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) | [optional] 

### Return type

[**ApiResponseOfFundsConfirmationResponse**](ApiResponseOfFundsConfirmationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Error Response |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hosted_vrp_payment**
> ApiResponseOfCreateHostedVRPPaymentRequest create_hosted_vrp_payment(consent_request_id, consent_token, create_hosted_vrp_payment_request, sub_application=sub_application)

Create VRP Payment

Creates a Variable Recurring Payment

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_create_hosted_vrp_payment_request import ApiResponseOfCreateHostedVRPPaymentRequest
from yapily.models.create_hosted_vrp_payment_request import CreateHostedVRPPaymentRequest
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    consent_request_id = 'consent_request_id_example' # str | Unique Identifier of the Consent Request
    consent_token = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    create_hosted_vrp_payment_request = yapily.CreateHostedVRPPaymentRequest() # CreateHostedVRPPaymentRequest | 
    sub_application = 'sub_application_example' # str | The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) (optional)

    try:
        # Create VRP Payment
        api_response = await api_instance.create_hosted_vrp_payment(consent_request_id, consent_token, create_hosted_vrp_payment_request, sub_application=sub_application)
        print("The response of HostedPaymentPagesApi->create_hosted_vrp_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->create_hosted_vrp_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_request_id** | **str**| Unique Identifier of the Consent Request | 
 **consent_token** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **create_hosted_vrp_payment_request** | [**CreateHostedVRPPaymentRequest**](CreateHostedVRPPaymentRequest.md)|  | 
 **sub_application** | **str**| The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) | [optional] 

### Return type

[**ApiResponseOfCreateHostedVRPPaymentRequest**](ApiResponseOfCreateHostedVRPPaymentRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Error Response |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_payment_request**
> ApiResponseOfGetHostedPaymentRequest get_hosted_payment_request(payment_request_id)

Get Hosted payment request

Used to get details of a payment request

### Example

* Basic Authentication (basicAuth):

```python
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    payment_request_id = 'payment_request_id_example' # str | Unique Identifier of the payment request

    try:
        # Get Hosted payment request
        api_response = await api_instance.get_hosted_payment_request(payment_request_id)
        print("The response of HostedPaymentPagesApi->get_hosted_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->get_hosted_payment_request: %s\n" % e)
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

# **get_hosted_vrp_consent_request**
> ApiResponseOfGetHostedVRPConsentRequest get_hosted_vrp_consent_request(consent_request_id, sub_application=sub_application)

Get Hosted VRP Consent Request

Used to get details of a VRP Consent Request

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_get_hosted_vrp_consent_request import ApiResponseOfGetHostedVRPConsentRequest
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    consent_request_id = 'consent_request_id_example' # str | Unique Identifier of the Consent Request
    sub_application = 'sub_application_example' # str | The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) (optional)

    try:
        # Get Hosted VRP Consent Request
        api_response = await api_instance.get_hosted_vrp_consent_request(consent_request_id, sub_application=sub_application)
        print("The response of HostedPaymentPagesApi->get_hosted_vrp_consent_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->get_hosted_vrp_consent_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_request_id** | **str**| Unique Identifier of the Consent Request | 
 **sub_application** | **str**| The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) | [optional] 

### Return type

[**ApiResponseOfGetHostedVRPConsentRequest**](ApiResponseOfGetHostedVRPConsentRequest.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_vrp_consent_requests**
> ApiResponseOfGetHostedVRPConsentsRequest get_hosted_vrp_consent_requests(sub_application)

Get Hosted VRP Consent Requests

Used to get all VRP consent requests initiated through Yapily Hosted Pages

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_get_hosted_vrp_consents_request import ApiResponseOfGetHostedVRPConsentsRequest
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    sub_application = 'sub_application_example' # str | __Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant)

    try:
        # Get Hosted VRP Consent Requests
        api_response = await api_instance.get_hosted_vrp_consent_requests(sub_application)
        print("The response of HostedPaymentPagesApi->get_hosted_vrp_consent_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->get_hosted_vrp_consent_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_application** | **str**| __Mandatory__. The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) | 

### Return type

[**ApiResponseOfGetHostedVRPConsentsRequest**](ApiResponseOfGetHostedVRPConsentsRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. Credentials are missing or invalid |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_vrp_payment_request**
> ApiResponseOfGetHostedVRPPaymentRequest get_hosted_vrp_payment_request(consent_request_id, payment_id, sub_application=sub_application)

Get VRP payment

Used to get details of a VRP Payment

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_get_hosted_vrp_payment_request import ApiResponseOfGetHostedVRPPaymentRequest
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    consent_request_id = 'consent_request_id_example' # str | Unique Identifier of the Consent Request
    payment_id = 'payment_id_example' # str | Unique Identifier of the Consent Request
    sub_application = 'sub_application_example' # str | The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) (optional)

    try:
        # Get VRP payment
        api_response = await api_instance.get_hosted_vrp_payment_request(consent_request_id, payment_id, sub_application=sub_application)
        print("The response of HostedPaymentPagesApi->get_hosted_vrp_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->get_hosted_vrp_payment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_request_id** | **str**| Unique Identifier of the Consent Request | 
 **payment_id** | **str**| Unique Identifier of the Consent Request | 
 **sub_application** | **str**| The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) | [optional] 

### Return type

[**ApiResponseOfGetHostedVRPPaymentRequest**](ApiResponseOfGetHostedVRPPaymentRequest.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_hosted_consent_request**
> ApiResponseOfRevokeHostedVRPConsentRequest revoke_hosted_consent_request(consent_request_id, sub_application=sub_application)

Revoke Hosted VRP Consent Request

Revoke Hosted VRP Consent Request

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_revoke_hosted_vrp_consent_request import ApiResponseOfRevokeHostedVRPConsentRequest
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
    api_instance = yapily.HostedPaymentPagesApi(api_client)
    consent_request_id = 'consent_request_id_example' # str | Unique Identifier of the Consent Request
    sub_application = 'sub_application_example' # str | The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) (optional)

    try:
        # Revoke Hosted VRP Consent Request
        api_response = await api_instance.revoke_hosted_consent_request(consent_request_id, sub_application=sub_application)
        print("The response of HostedPaymentPagesApi->revoke_hosted_consent_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPaymentPagesApi->revoke_hosted_consent_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_request_id** | **str**| Unique Identifier of the Consent Request | 
 **sub_application** | **str**| The unique identifier of the sub application the request is being submitted on behalf of (e.g. an underlying merchant) | [optional] 

### Return type

[**ApiResponseOfRevokeHostedVRPConsentRequest**](ApiResponseOfRevokeHostedVRPConsentRequest.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

