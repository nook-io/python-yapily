# yapily.WebhooksApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhook/events/{webhook_id} | Delete Webhook Event
[**get_registered_webhooks**](WebhooksApi.md#get_registered_webhooks) | **GET** /webhook/events | Retrieve All Webhook Events
[**get_webhook_events_categories**](WebhooksApi.md#get_webhook_events_categories) | **GET** /webhook/events/categories | Get Webhook Categories
[**register_webhook**](WebhooksApi.md#register_webhook) | **POST** /webhook/events | Register Webhook Event
[**webhook_secret_reset**](WebhooksApi.md#webhook_secret_reset) | **POST** /webhook/secrets/{webhook_id} | Reset Webhook Secret


# **delete_webhook**
> DeleteWebhook200Response delete_webhook(webhook_id, sub_application=sub_application)

Delete Webhook Event

Delete a webhook event for a specified webhook ID, unregistering it from receiving any further notifications for the subscribed event categories in your application.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.delete_webhook200_response import DeleteWebhook200Response
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
    api_instance = yapily.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | Registered webhook id
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)

    try:
        # Delete Webhook Event
        api_response = await api_instance.delete_webhook(webhook_id, sub_application=sub_application)
        print("The response of WebhooksApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Registered webhook id | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 

### Return type

[**DeleteWebhook200Response**](DeleteWebhook200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | delete webhook succeeded |  -  |
**401** | Authentication Error |  -  |
**400** | There are validation errors |  -  |
**404** | Webhook id not found |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_webhooks**
> GetRegisteredWebhooks200Response get_registered_webhooks(sub_application=sub_application)

Retrieve All Webhook Events

Retrieve the list of registered webhooks for your application

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.get_registered_webhooks200_response import GetRegisteredWebhooks200Response
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
    api_instance = yapily.WebhooksApi(api_client)
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)

    try:
        # Retrieve All Webhook Events
        api_response = await api_instance.get_registered_webhooks(sub_application=sub_application)
        print("The response of WebhooksApi->get_registered_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_registered_webhooks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 

### Return type

[**GetRegisteredWebhooks200Response**](GetRegisteredWebhooks200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | retrieve all registered webhook |  -  |
**401** | Authentication Error |  -  |
**400** | There are validation errors |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_events_categories**
> GetWebhookEventsCategories200Response get_webhook_events_categories()

Get Webhook Categories

Retrieve a comprehensive list of event categories that can be registered for webhook notifications in your application. These event categories can be used to subscribe a webhook to specific events, enabling your application to receive real-time notifications when these events occur.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.get_webhook_events_categories200_response import GetWebhookEventsCategories200Response
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
    api_instance = yapily.WebhooksApi(api_client)

    try:
        # Get Webhook Categories
        api_response = await api_instance.get_webhook_events_categories()
        print("The response of WebhooksApi->get_webhook_events_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_events_categories: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetWebhookEventsCategories200Response**](GetWebhookEventsCategories200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication Error |  -  |
**400** | There are validation errors |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_webhook**
> RegisterWebhook201Response register_webhook(sub_application=sub_application, register_webhook_request=register_webhook_request)

Register Webhook Event

Register a webhook to one or multiple event categories to receive real-time notifications when specific events occur in your application.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.register_webhook201_response import RegisterWebhook201Response
from yapily.models.register_webhook_request import RegisterWebhookRequest
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
    api_instance = yapily.WebhooksApi(api_client)
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    register_webhook_request = yapily.RegisterWebhookRequest() # RegisterWebhookRequest |  (optional)

    try:
        # Register Webhook Event
        api_response = await api_instance.register_webhook(sub_application=sub_application, register_webhook_request=register_webhook_request)
        print("The response of WebhooksApi->register_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->register_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **register_webhook_request** | [**RegisterWebhookRequest**](RegisterWebhookRequest.md)|  | [optional] 

### Return type

[**RegisterWebhook201Response**](RegisterWebhook201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | webhook details including the secret |  -  |
**401** | Authentication Error |  -  |
**400** | There are validation errors |  -  |
**406** | Maximum number of registered webhooks has been reached |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_secret_reset**
> RegisterWebhook201Response webhook_secret_reset(webhook_id, sub_application=sub_application, webhook_secret_reset_request=webhook_secret_reset_request)

Reset Webhook Secret

Reset webhook secret for a webhook that is already registered to your application

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.register_webhook201_response import RegisterWebhook201Response
from yapily.models.webhook_secret_reset_request import WebhookSecretResetRequest
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
    api_instance = yapily.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | Registered webhook id
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    webhook_secret_reset_request = yapily.WebhookSecretResetRequest() # WebhookSecretResetRequest |  (optional)

    try:
        # Reset Webhook Secret
        api_response = await api_instance.webhook_secret_reset(webhook_id, sub_application=sub_application, webhook_secret_reset_request=webhook_secret_reset_request)
        print("The response of WebhooksApi->webhook_secret_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhook_secret_reset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Registered webhook id | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **webhook_secret_reset_request** | [**WebhookSecretResetRequest**](WebhookSecretResetRequest.md)|  | [optional] 

### Return type

[**RegisterWebhook201Response**](RegisterWebhook201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | webhook details including the secret |  -  |
**401** | Authentication Error |  -  |
**400** | There are validation errors |  -  |
**404** | Webhook id not found |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

