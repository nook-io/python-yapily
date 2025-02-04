# yapily.NotificationsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_subscription**](NotificationsApi.md#create_event_subscription) | **POST** /notifications/event-subscriptions | Create Event Subscription
[**delete_event_subscription_by_id**](NotificationsApi.md#delete_event_subscription_by_id) | **DELETE** /notifications/event-subscriptions/{eventTypeId} | Delete Event Subscription
[**get_event_subscription_by_id**](NotificationsApi.md#get_event_subscription_by_id) | **GET** /notifications/event-subscriptions/{eventTypeId} | Get Event Subscription
[**get_event_subscriptions**](NotificationsApi.md#get_event_subscriptions) | **GET** /notifications/event-subscriptions | Get Event Subscriptions


# **create_event_subscription**
> ApiResponseOfEventSubscriptionResponse create_event_subscription(event_subscription_request, sub_application=sub_application)

Create Event Subscription

Used to subscribe to notifications relating to a specified event type.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_event_subscription_response import ApiResponseOfEventSubscriptionResponse
from yapily.models.event_subscription_request import EventSubscriptionRequest
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
    api_instance = yapily.NotificationsApi(api_client)
    event_subscription_request = yapily.EventSubscriptionRequest() # EventSubscriptionRequest | 
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)

    try:
        # Create Event Subscription
        api_response = await api_instance.create_event_subscription(event_subscription_request, sub_application=sub_application)
        print("The response of NotificationsApi->create_event_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->create_event_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_subscription_request** | [**EventSubscriptionRequest**](EventSubscriptionRequest.md)|  | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 

### Return type

[**ApiResponseOfEventSubscriptionResponse**](ApiResponseOfEventSubscriptionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Event subscription created successfully |  -  |
**400** | Bad request for missing required properties |  -  |
**401** | Unauthorized |  -  |
**409** | Event subscription already exist for the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_subscription_by_id**
> ApiResponseOfEventSubscriptionDeleteResponse delete_event_subscription_by_id(event_type_id, sub_application=sub_application)

Delete Event Subscription

Used to unsubscribe to notifications relating to a specified event type.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_event_subscription_delete_response import ApiResponseOfEventSubscriptionDeleteResponse
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
    api_instance = yapily.NotificationsApi(api_client)
    event_type_id = 'event_type_id_example' # str | Unique identifier of the event type (for which notifications will be sent). 
    sub_application = 'sub_application_example' # str | The sub-application ID for which event type will be deleted (optional)

    try:
        # Delete Event Subscription
        api_response = await api_instance.delete_event_subscription_by_id(event_type_id, sub_application=sub_application)
        print("The response of NotificationsApi->delete_event_subscription_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_event_subscription_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **str**| Unique identifier of the event type (for which notifications will be sent).  | 
 **sub_application** | **str**| The sub-application ID for which event type will be deleted | [optional] 

### Return type

[**ApiResponseOfEventSubscriptionDeleteResponse**](ApiResponseOfEventSubscriptionDeleteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event subscription deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Event subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_subscription_by_id**
> ApiResponseOfEventSubscriptionResponse get_event_subscription_by_id(event_type_id, sub_application=sub_application)

Get Event Subscription

Used to get details of your subscription to a specified event type.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_event_subscription_response import ApiResponseOfEventSubscriptionResponse
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
    api_instance = yapily.NotificationsApi(api_client)
    event_type_id = 'event_type_id_example' # str | Unique identifier of the event type (for which notifications will be sent). 
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)

    try:
        # Get Event Subscription
        api_response = await api_instance.get_event_subscription_by_id(event_type_id, sub_application=sub_application)
        print("The response of NotificationsApi->get_event_subscription_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_event_subscription_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **str**| Unique identifier of the event type (for which notifications will be sent).  | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 

### Return type

[**ApiResponseOfEventSubscriptionResponse**](ApiResponseOfEventSubscriptionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event subscription data found |  -  |
**401** | Unauthorized |  -  |
**404** | Event subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_subscriptions**
> ApiListResponseOfEventSubscriptionResponse get_event_subscriptions(sub_application=sub_application)

Get Event Subscriptions

Get all event subscriptions that your application is subscribed to

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_event_subscription_response import ApiListResponseOfEventSubscriptionResponse
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
    api_instance = yapily.NotificationsApi(api_client)
    sub_application = 'sub_application_example' # str | The sub-application ID for which all event subscriptions will be returned (optional)

    try:
        # Get Event Subscriptions
        api_response = await api_instance.get_event_subscriptions(sub_application=sub_application)
        print("The response of NotificationsApi->get_event_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_event_subscriptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_application** | **str**| The sub-application ID for which all event subscriptions will be returned | [optional] 

### Return type

[**ApiListResponseOfEventSubscriptionResponse**](ApiListResponseOfEventSubscriptionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event subscriptions for the application |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

