# yapily.VirtualAccountsAccountsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_account**](VirtualAccountsAccountsApi.md#create_virtual_account) | **POST** /virtual-accounts/accounts | Create Account
[**get_virtual_account_by_id**](VirtualAccountsAccountsApi.md#get_virtual_account_by_id) | **GET** /virtual-accounts/accounts/{accountId} | Get Account
[**get_virtual_accounts**](VirtualAccountsAccountsApi.md#get_virtual_accounts) | **GET** /virtual-accounts/accounts | Get Accounts
[**update_virtual_account_by_id**](VirtualAccountsAccountsApi.md#update_virtual_account_by_id) | **PATCH** /virtual-accounts/accounts/{accountId} | Update Account


# **create_virtual_account**
> ApiResponseOfVirtualAccount create_virtual_account(client_id, virtual_account_request)

Create Account

Create a new virtual account

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account import ApiResponseOfVirtualAccount
from yapily.models.virtual_account_request import VirtualAccountRequest
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
    api_instance = yapily.VirtualAccountsAccountsApi(api_client)
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    virtual_account_request = {"nickname":"MyAccount123","currency":"GBP"} # VirtualAccountRequest | 

    try:
        # Create Account
        api_response = await api_instance.create_virtual_account(client_id, virtual_account_request)
        print("The response of VirtualAccountsAccountsApi->create_virtual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsAccountsApi->create_virtual_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **virtual_account_request** | [**VirtualAccountRequest**](VirtualAccountRequest.md)|  | 

### Return type

[**ApiResponseOfVirtualAccount**](ApiResponseOfVirtualAccount.md)

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

# **get_virtual_account_by_id**
> ApiResponseOfVirtualAccount get_virtual_account_by_id(account_id, client_id)

Get Account

Get the details of a specific account using its Id

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account import ApiResponseOfVirtualAccount
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
    api_instance = yapily.VirtualAccountsAccountsApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The Id of the account.
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for

    try:
        # Get Account
        api_response = await api_instance.get_virtual_account_by_id(account_id, client_id)
        print("The response of VirtualAccountsAccountsApi->get_virtual_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsAccountsApi->get_virtual_account_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The Id of the account. | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 

### Return type

[**ApiResponseOfVirtualAccount**](ApiResponseOfVirtualAccount.md)

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

# **get_virtual_accounts**
> ApiListResponseOfVirtualAccount get_virtual_accounts(client_id, nickname=nickname, currency=currency, status=status, cursor=cursor)

Get Accounts

Retrieve a list of all virtual accounts held

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_virtual_account import ApiListResponseOfVirtualAccount
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
    api_instance = yapily.VirtualAccountsAccountsApi(api_client)
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    nickname = 'nickname_example' # str | __Optional__. Filter accounts based on reference provided in order to help with identification of the account (optional)
    currency = 'currency_example' # str | __Optional__. Filter accounts based on three-letter ISO 4217 currency code (optional)
    status = 'status_example' # str | __Optional__. Filter accounts based on their current state. One of PENDING, ACTIVE, FAILED, SUSPENDED or CLOSED (optional)
    cursor = 'cursor_example' # str | __Optional__. Data required to provide pagination (optional)

    try:
        # Get Accounts
        api_response = await api_instance.get_virtual_accounts(client_id, nickname=nickname, currency=currency, status=status, cursor=cursor)
        print("The response of VirtualAccountsAccountsApi->get_virtual_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsAccountsApi->get_virtual_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **nickname** | **str**| __Optional__. Filter accounts based on reference provided in order to help with identification of the account | [optional] 
 **currency** | **str**| __Optional__. Filter accounts based on three-letter ISO 4217 currency code | [optional] 
 **status** | **str**| __Optional__. Filter accounts based on their current state. One of PENDING, ACTIVE, FAILED, SUSPENDED or CLOSED | [optional] 
 **cursor** | **str**| __Optional__. Data required to provide pagination | [optional] 

### Return type

[**ApiListResponseOfVirtualAccount**](ApiListResponseOfVirtualAccount.md)

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
**424** | A failure occurred during an interaction with a third party provider. |  -  |
**500** | Unexpected Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_account_by_id**
> ApiResponseOfVirtualAccount update_virtual_account_by_id(account_id, client_id, update_virtual_account_request)

Update Account

Update the details of a specific account using its Id

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account import ApiResponseOfVirtualAccount
from yapily.models.update_virtual_account_request import UpdateVirtualAccountRequest
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
    api_instance = yapily.VirtualAccountsAccountsApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The Id of the account.
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    update_virtual_account_request = {"nickname":"MyAccount456","status":"CLOSED"} # UpdateVirtualAccountRequest | 

    try:
        # Update Account
        api_response = await api_instance.update_virtual_account_by_id(account_id, client_id, update_virtual_account_request)
        print("The response of VirtualAccountsAccountsApi->update_virtual_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsAccountsApi->update_virtual_account_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The Id of the account. | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **update_virtual_account_request** | [**UpdateVirtualAccountRequest**](UpdateVirtualAccountRequest.md)|  | 

### Return type

[**ApiResponseOfVirtualAccount**](ApiResponseOfVirtualAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
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

