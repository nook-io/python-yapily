# yapily.VirtualAccountsClientsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_account_client**](VirtualAccountsClientsApi.md#create_virtual_account_client) | **POST** /virtual-accounts/clients | Create Virtual Account Client
[**get_virtual_account_client_by_id**](VirtualAccountsClientsApi.md#get_virtual_account_client_by_id) | **GET** /virtual-accounts/clients/{clientId} | Get a Virtual Account Client by ID
[**get_virtual_account_clients**](VirtualAccountsClientsApi.md#get_virtual_account_clients) | **GET** /virtual-accounts/clients | Get List of Virtual Account Clients


# **create_virtual_account_client**
> ApiResponseOfVirtualAccountClient create_virtual_account_client(client_id, virtual_account_client_request)

Create Virtual Account Client

Create a new virtual account client (individual or business client). Available for clients who have direct onboarding permissions only. Please contact your CSM to enquire about access

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_client import ApiResponseOfVirtualAccountClient
from yapily.models.virtual_account_client_request import VirtualAccountClientRequest
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
    api_instance = yapily.VirtualAccountsClientsApi(api_client)
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | __Mandatory__. This must be your master client-id (and not one associated with one of your clients)
    virtual_account_client_request = {"type":"BUSINESS","business":{"name":"Payments ltd company","type":"LIMITED_LIABILITY","registrationNumber":"1234567","contactName":"James Edward Rhodes","email":"james.rhodes@example.com","phone":"447006783009","registeredAddress":{"addressLine1":"123 Queens Street","addressLine2":"Unit 13","townName":"York","postCode":"12345","country":"GB"},"tradingAddress":{"addressLine1":"123 Queens Street","addressLine2":"Unit 13","townName":"York","postCode":"12345","country":"GB"}}} # VirtualAccountClientRequest | 

    try:
        # Create Virtual Account Client
        api_response = await api_instance.create_virtual_account_client(client_id, virtual_account_client_request)
        print("The response of VirtualAccountsClientsApi->create_virtual_account_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsClientsApi->create_virtual_account_client: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. This must be your master client-id (and not one associated with one of your clients) | 
 **virtual_account_client_request** | [**VirtualAccountClientRequest**](VirtualAccountClientRequest.md)|  | 

### Return type

[**ApiResponseOfVirtualAccountClient**](ApiResponseOfVirtualAccountClient.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occurred during an interaction with a third party provider. |  -  |
**500** | Unexpected Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_client_by_id**
> ApiResponseOfVirtualAccountClient get_virtual_account_client_by_id(client_id, client_id2)

Get a Virtual Account Client by ID

Get a Virtual Account Client using its ID. Restricted to applications with direct onboarding permissions only

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_client import ApiResponseOfVirtualAccountClient
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
    api_instance = yapily.VirtualAccountsClientsApi(api_client)
    client_id = 'client_id_example' # str | __Mandatory__. The ID of the client.
    client_id2 = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | __Mandatory__. This must be your master client-id (and not one associated with one of your clients)

    try:
        # Get a Virtual Account Client by ID
        api_response = await api_instance.get_virtual_account_client_by_id(client_id, client_id2)
        print("The response of VirtualAccountsClientsApi->get_virtual_account_client_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsClientsApi->get_virtual_account_client_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. The ID of the client. | 
 **client_id2** | **str**| __Mandatory__. This must be your master client-id (and not one associated with one of your clients) | 

### Return type

[**ApiResponseOfVirtualAccountClient**](ApiResponseOfVirtualAccountClient.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**404** | Not Found. Resource requested is not found. |  -  |
**424** | A failure occurred during an interaction with a third party provider. |  -  |
**500** | Unexpected Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_clients**
> ApiListResponseOfVirtualAccountClient get_virtual_account_clients(client_id, type=type, status=status, cursor=cursor)

Get List of Virtual Account Clients

Get Virtual Account Clients (individual or business client).

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_virtual_account_client import ApiListResponseOfVirtualAccountClient
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
    api_instance = yapily.VirtualAccountsClientsApi(api_client)
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | __Mandatory__. This must be your master client-id (and not one associated with one of your clients)
    type = 'BUSINESS' # str | __Optional__.  Filter clients based on client type. One of BUSINESS or INDIVIDUAL (optional)
    status = 'ACTIVE' # str | __Optional__.  Filter clients based on client status. One of ACTIVE, PENDING or SUSPENDED (optional)
    cursor = 'cursor_example' # str | __Optional__. Data required to provide pagination (optional)

    try:
        # Get List of Virtual Account Clients
        api_response = await api_instance.get_virtual_account_clients(client_id, type=type, status=status, cursor=cursor)
        print("The response of VirtualAccountsClientsApi->get_virtual_account_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsClientsApi->get_virtual_account_clients: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| __Mandatory__. This must be your master client-id (and not one associated with one of your clients) | 
 **type** | **str**| __Optional__.  Filter clients based on client type. One of BUSINESS or INDIVIDUAL | [optional] 
 **status** | **str**| __Optional__.  Filter clients based on client status. One of ACTIVE, PENDING or SUSPENDED | [optional] 
 **cursor** | **str**| __Optional__. Data required to provide pagination | [optional] 

### Return type

[**ApiListResponseOfVirtualAccountClient**](ApiListResponseOfVirtualAccountClient.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occured during interaction with a third party provider |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

