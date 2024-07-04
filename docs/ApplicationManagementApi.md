# yapily.ApplicationManagementApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_vrp_configuration_by_application_id**](ApplicationManagementApi.md#create_application_vrp_configuration_by_application_id) | **POST** /applications/{applicationId}/vrp | Create application VRP configuration by Application Id
[**create_sub_application**](ApplicationManagementApi.md#create_sub_application) | **POST** /applications | Creates a sub-application for the root application id provided in the authentication token
[**delete_application**](ApplicationManagementApi.md#delete_application) | **DELETE** /applications/{applicationId} | Delete an application
[**get_application_by_id**](ApplicationManagementApi.md#get_application_by_id) | **GET** /applications/{applicationId} | Get application details
[**get_application_vrp_configuration_by_application_id**](ApplicationManagementApi.md#get_application_vrp_configuration_by_application_id) | **GET** /applications/{applicationId}/vrp | Get application VRP configuration by Application Id
[**search_applications**](ApplicationManagementApi.md#search_applications) | **GET** /applications | Retrieve sub-applications for the root application provided in the authentication token.
[**update_application**](ApplicationManagementApi.md#update_application) | **PUT** /applications/{applicationId} | Update an Application
[**update_application_vrp_configuration_by_application_id**](ApplicationManagementApi.md#update_application_vrp_configuration_by_application_id) | **PUT** /applications/{applicationId}/vrp | Update application VRP configuration by Application Id


# **create_application_vrp_configuration_by_application_id**
> create_application_vrp_configuration_by_application_id(application_id, vrp_configuration)

Create application VRP configuration by Application Id

Create application vrp configuration

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.vrp_configuration import VrpConfiguration
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
    api_instance = yapily.ApplicationManagementApi(api_client)
    application_id = 'application_id_example' # str | The id of the application that vrp configuration being created for
    vrp_configuration = yapily.VrpConfiguration() # VrpConfiguration | The vrp configuration to create

    try:
        # Create application VRP configuration by Application Id
        api_instance.create_application_vrp_configuration_by_application_id(application_id, vrp_configuration)
    except Exception as e:
        print("Exception when calling ApplicationManagementApi->create_application_vrp_configuration_by_application_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application that vrp configuration being created for | 
 **vrp_configuration** | [**VrpConfiguration**](VrpConfiguration.md)| The vrp configuration to create | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Application vrp configuration was successfully created |  -  |
**400** | There are validation errors |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**403** | Forbidden from accessing the requested Application. |  -  |
**404** | VRP Configuration with given application id not found. |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sub_application**
> ApiResponseOfApplicationResponse create_sub_application(application_request)

Creates a sub-application for the root application id provided in the authentication token

Creates a sub-application under the given root application id provided in the authentication token. The sub-application can use the root's credentials to call the API

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_application_response import ApiResponseOfApplicationResponse
from yapily.models.application_request import ApplicationRequest
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
    api_instance = yapily.ApplicationManagementApi(api_client)
    application_request = yapily.ApplicationRequest() # ApplicationRequest | The sub-application to create

    try:
        # Creates a sub-application for the root application id provided in the authentication token
        api_response = api_instance.create_sub_application(application_request)
        print("The response of ApplicationManagementApi->create_sub_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagementApi->create_sub_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)| The sub-application to create | 

### Return type

[**ApiResponseOfApplicationResponse**](ApiResponseOfApplicationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sub-application was successfully created |  -  |
**400** | There are validation errors |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**403** | Forbidden from accessing the requested Application. |  -  |
**404** | Application with given root id not found. |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(application_id)

Delete an application

Deletes the application with the given ID in the path

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
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
    api_instance = yapily.ApplicationManagementApi(api_client)
    application_id = 'application_id_example' # str | The id of the application being deleted

    try:
        # Delete an application
        api_instance.delete_application(application_id)
    except Exception as e:
        print("Exception when calling ApplicationManagementApi->delete_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application being deleted | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Application was successfully deleted |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**403** | Forbidden from accessing the requested Application. |  -  |
**404** | Application with given id not found. |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_by_id**
> ApiResponseOfApplicationResponse get_application_by_id(application_id)

Get application details

Retrieves an application by the id provided in the path

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_application_response import ApiResponseOfApplicationResponse
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
    api_instance = yapily.ApplicationManagementApi(api_client)
    application_id = 'application_id_example' # str | The id of the application being fetched

    try:
        # Get application details
        api_response = api_instance.get_application_by_id(application_id)
        print("The response of ApplicationManagementApi->get_application_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagementApi->get_application_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application being fetched | 

### Return type

[**ApiResponseOfApplicationResponse**](ApiResponseOfApplicationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application was successfully fetched |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**403** | Forbidden from accessing the requested Application. |  -  |
**404** | Application with given id not found. |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_vrp_configuration_by_application_id**
> VrpConfiguration get_application_vrp_configuration_by_application_id(application_id)

Get application VRP configuration by Application Id

Get application vrp configuration

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.vrp_configuration import VrpConfiguration
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
    api_instance = yapily.ApplicationManagementApi(api_client)
    application_id = 'application_id_example' # str | The id of the application that vrp configuration being created for

    try:
        # Get application VRP configuration by Application Id
        api_response = api_instance.get_application_vrp_configuration_by_application_id(application_id)
        print("The response of ApplicationManagementApi->get_application_vrp_configuration_by_application_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagementApi->get_application_vrp_configuration_by_application_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application that vrp configuration being created for | 

### Return type

[**VrpConfiguration**](VrpConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application vrp configuration was successfully fetched |  -  |
**400** | There are validation errors |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**403** | Forbidden from accessing the requested Application. |  -  |
**404** | VRP Configuration with given application id not found. |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_applications**
> ApiListOfApplicationResponse search_applications(public_filter_values=public_filter_values)

Retrieve sub-applications for the root application provided in the authentication token.

Retrieves sub-applications for the root application provided in the authentication token. If a sub-application is provided in the authentication token, it will return an empty list.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_of_application_response import ApiListOfApplicationResponse
from yapily.models.search_applications_public_filter_values_parameter import SearchApplicationsPublicFilterValuesParameter
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
    api_instance = yapily.ApplicationManagementApi(api_client)
    public_filter_values = yapily.SearchApplicationsPublicFilterValuesParameter() # SearchApplicationsPublicFilterValuesParameter |  (optional)

    try:
        # Retrieve sub-applications for the root application provided in the authentication token.
        api_response = api_instance.search_applications(public_filter_values=public_filter_values)
        print("The response of ApplicationManagementApi->search_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagementApi->search_applications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_filter_values** | [**SearchApplicationsPublicFilterValuesParameter**](.md)|  | [optional] 

### Return type

[**ApiListOfApplicationResponse**](ApiListOfApplicationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sub-applications that are returned as part of the search results. |  -  |
**400** | There are validation errors |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**403** | Forbidden from accessing the requested Application. |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> ApiResponseOfApplicationResponse update_application(application_id, application_request)

Update an Application

Updates the application properties for the application with the given ID in the path

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_application_response import ApiResponseOfApplicationResponse
from yapily.models.application_request import ApplicationRequest
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
    api_instance = yapily.ApplicationManagementApi(api_client)
    application_id = 'application_id_example' # str | The id of the application being updated
    application_request = yapily.ApplicationRequest() # ApplicationRequest | The application to update

    try:
        # Update an Application
        api_response = api_instance.update_application(application_id, application_request)
        print("The response of ApplicationManagementApi->update_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationManagementApi->update_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application being updated | 
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)| The application to update | 

### Return type

[**ApiResponseOfApplicationResponse**](ApiResponseOfApplicationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application was successfully updated |  -  |
**400** | There are validation errors |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**403** | Forbidden from accessing the requested Application. |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_vrp_configuration_by_application_id**
> update_application_vrp_configuration_by_application_id(application_id, vrp_configuration)

Update application VRP configuration by Application Id

Update application vrp configuration

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.vrp_configuration import VrpConfiguration
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
    api_instance = yapily.ApplicationManagementApi(api_client)
    application_id = 'application_id_example' # str | The id of the application that vrp configuration being created for
    vrp_configuration = yapily.VrpConfiguration() # VrpConfiguration | The vrp configuration to create

    try:
        # Update application VRP configuration by Application Id
        api_instance.update_application_vrp_configuration_by_application_id(application_id, vrp_configuration)
    except Exception as e:
        print("Exception when calling ApplicationManagementApi->update_application_vrp_configuration_by_application_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application that vrp configuration being created for | 
 **vrp_configuration** | [**VrpConfiguration**](VrpConfiguration.md)| The vrp configuration to create | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Application vrp configuration was successfully updated |  -  |
**400** | There are validation errors |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**403** | Forbidden from accessing the requested Application. |  -  |
**404** | VRP Configuration with given application id not found. |  -  |
**500** | An unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

