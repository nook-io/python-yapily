# yapily.FinancialDataApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](FinancialDataApi.md#get_account) | **GET** /accounts/{accountId} | Get Account
[**get_account_balances**](FinancialDataApi.md#get_account_balances) | **GET** /accounts/{accountId}/balances | Get Account Balances
[**get_account_direct_debits**](FinancialDataApi.md#get_account_direct_debits) | **GET** /accounts/{accountId}/direct-debits | Get Account Direct Debits
[**get_account_periodic_payments**](FinancialDataApi.md#get_account_periodic_payments) | **GET** /accounts/{accountId}/periodic-payments | Get Account Periodic Payments
[**get_account_scheduled_payments**](FinancialDataApi.md#get_account_scheduled_payments) | **GET** /accounts/{accountId}/scheduled-payments | Get Account Scheduled Payments
[**get_accounts**](FinancialDataApi.md#get_accounts) | **GET** /accounts | Get Accounts
[**get_beneficiaries**](FinancialDataApi.md#get_beneficiaries) | **GET** /accounts/{accountId}/beneficiaries | Get Account Beneficiaries
[**get_categories**](FinancialDataApi.md#get_categories) | **GET** /categories/{country} | Get Categories
[**get_identity**](FinancialDataApi.md#get_identity) | **GET** /identity | Get Identity
[**get_real_time_transactions**](FinancialDataApi.md#get_real_time_transactions) | **GET** /accounts/{accountId}/real-time/transactions | Get Real Time Account Transactions
[**get_statement**](FinancialDataApi.md#get_statement) | **GET** /accounts/{accountId}/statements/{statementId} | Get Account Statement
[**get_statement_file**](FinancialDataApi.md#get_statement_file) | **GET** /accounts/{accountId}/statements/{statementId}/file | Get Account Statement File
[**get_statements**](FinancialDataApi.md#get_statements) | **GET** /accounts/{accountId}/statements | Get Account Statements
[**get_transactions**](FinancialDataApi.md#get_transactions) | **GET** /accounts/{accountId}/transactions | Get Account Transactions


# **get_account**
> ApiResponseOfAccount get_account(account_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, raw=raw)

Get Account

Returns the account and balance information for a user's specified account.<br><br>Feature: `ACCOUNT`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_account import ApiResponseOfAccount
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
    api_instance = yapily.FinancialDataApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account
        api_response = await api_instance.get_account(account_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, raw=raw)
        print("The response of FinancialDataApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAccount**](ApiResponseOfAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_balances**
> ApiResponseOfBalances get_account_balances(account_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, raw=raw)

Get Account Balances

Returns the balance for the end user associated with the presented consent token.<br><br>Feature: `ACCOUNT_BALANCES`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_balances import ApiResponseOfBalances
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
    api_instance = yapily.FinancialDataApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Balances
        api_response = await api_instance.get_account_balances(account_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, raw=raw)
        print("The response of FinancialDataApi->get_account_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_account_balances: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfBalances**](ApiResponseOfBalances.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_direct_debits**
> ApiListResponseOfDirectDebitResponse get_account_direct_debits(account_id, consent, sub_application=sub_application, limit=limit, raw=raw)

Get Account Direct Debits

Returns the list of direct debits for an account.<br><br>Feature: `ACCOUNT_DIRECT_DEBITS`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_direct_debit_response import ApiListResponseOfDirectDebitResponse
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
    api_instance = yapily.FinancialDataApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Direct Debits
        api_response = await api_instance.get_account_direct_debits(account_id, consent, sub_application=sub_application, limit=limit, raw=raw)
        print("The response of FinancialDataApi->get_account_direct_debits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_account_direct_debits: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiListResponseOfDirectDebitResponse**](ApiListResponseOfDirectDebitResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_periodic_payments**
> ApiListResponseOfPaymentResponse get_account_periodic_payments(account_id, consent, sub_application=sub_application, limit=limit, raw=raw)

Get Account Periodic Payments

Returns the list of periodic payments (standing orders in the UK) for an account.<br><br>Feature: `ACCOUNT_PERIODIC_PAYMENTS`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_payment_response import ApiListResponseOfPaymentResponse
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
    api_instance = yapily.FinancialDataApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Periodic Payments
        api_response = await api_instance.get_account_periodic_payments(account_id, consent, sub_application=sub_application, limit=limit, raw=raw)
        print("The response of FinancialDataApi->get_account_periodic_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_account_periodic_payments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiListResponseOfPaymentResponse**](ApiListResponseOfPaymentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_scheduled_payments**
> ApiListResponseOfPaymentResponse get_account_scheduled_payments(account_id, consent, sub_application=sub_application, limit=limit, raw=raw)

Get Account Scheduled Payments

Returns the list of scheduled payments for an account.<br><br>Feature: `ACCOUNT_SCHEDULED_PAYMENTS`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_payment_response import ApiListResponseOfPaymentResponse
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
    api_instance = yapily.FinancialDataApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Scheduled Payments
        api_response = await api_instance.get_account_scheduled_payments(account_id, consent, sub_application=sub_application, limit=limit, raw=raw)
        print("The response of FinancialDataApi->get_account_scheduled_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_account_scheduled_payments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiListResponseOfPaymentResponse**](ApiListResponseOfPaymentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> AccountApiListResponse get_accounts(consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, raw=raw)

Get Accounts

Returns all accounts and balances for the end user associated with the presented consent token.<br><br>Feature: `ACCOUNTS`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.account_api_list_response import AccountApiListResponse
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
    api_instance = yapily.FinancialDataApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Accounts
        api_response = await api_instance.get_accounts(consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, raw=raw)
        print("The response of FinancialDataApi->get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**AccountApiListResponse**](AccountApiListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beneficiaries**
> ApiListResponseOfBeneficiary get_beneficiaries(account_id, consent, sub_application=sub_application, raw=raw)

Get Account Beneficiaries

Returns all the beneficiaries of a user's account.<br><br>Feature: `ACCOUNT_BENEFICIARIES`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_beneficiary import ApiListResponseOfBeneficiary
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
    api_instance = yapily.FinancialDataApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Beneficiaries
        api_response = await api_instance.get_beneficiaries(account_id, consent, sub_application=sub_application, raw=raw)
        print("The response of FinancialDataApi->get_beneficiaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_beneficiaries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiListResponseOfBeneficiary**](ApiListResponseOfBeneficiary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> ApiListResponseOfCategory get_categories(country)

Get Categories

Used to retrieve the list of categories returned by the Yapily Categorisation engine for a given locale. <br><br>See [Data Enrichment](https://docs.yapily.com/pages/key-concepts/account-data/data-enrichment/intro-to-data-enrichment/) for more information.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_category import ApiListResponseOfCategory
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
    api_instance = yapily.FinancialDataApi(api_client)
    country = 'country_example' # str | __Mandatory__. The 2 letter country code e.g. 'GB'.

    try:
        # Get Categories
        api_response = await api_instance.get_categories(country)
        print("The response of FinancialDataApi->get_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_categories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| __Mandatory__. The 2 letter country code e.g. &#39;GB&#39;. | 

### Return type

[**ApiListResponseOfCategory**](ApiListResponseOfCategory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity**
> ApiResponseOfIdentity get_identity(consent, sub_application=sub_application, raw=raw)

Get Identity

Returns the identity information for an account.<br><br>Feature: `IDENTITY`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_identity import ApiResponseOfIdentity
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
    api_instance = yapily.FinancialDataApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Identity
        api_response = await api_instance.get_identity(consent, sub_application=sub_application, raw=raw)
        print("The response of FinancialDataApi->get_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_identity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfIdentity**](ApiResponseOfIdentity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_real_time_transactions**
> ApiListResponseOfRealTimeTransaction get_real_time_transactions(account_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, var_from=var_from, before=before, cursor=cursor, raw=raw)

Get Real Time Account Transactions

Used to get the account transactions for an account in real time with cursor pagination<br><br>Feature: `ACCOUNT_TRANSACTIONS`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_real_time_transaction import ApiListResponseOfRealTimeTransaction
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
    api_instance = yapily.FinancialDataApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    var_from = 'var_from_example' # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
    before = 'before_example' # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
    cursor = 'cursor_example' # str | __Optional__. The cursor token supplied by a previous call. The cursor represents a location in the data set. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Real Time Account Transactions
        api_response = await api_instance.get_real_time_transactions(account_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, var_from=var_from, before=before, cursor=cursor, raw=raw)
        print("The response of FinancialDataApi->get_real_time_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_real_time_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **var_from** | **str**| __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional] 
 **before** | **str**| __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional] 
 **cursor** | **str**| __Optional__. The cursor token supplied by a previous call. The cursor represents a location in the data set. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiListResponseOfRealTimeTransaction**](ApiListResponseOfRealTimeTransaction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Error Response |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement**
> ApiResponseOfAccountStatement get_statement(consent, account_id, statement_id, sub_application=sub_application, raw=raw)

Get Account Statement

Returns a statement for an account.<br><br>Feature: `ACCOUNT_STATEMENT`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_account_statement import ApiResponseOfAccountStatement
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
    api_instance = yapily.FinancialDataApi(api_client)
    consent = 'consent_example' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    statement_id = 'statement_id_example' # str | __Mandatory__. The statement Id of the statement file.
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Statement
        api_response = await api_instance.get_statement(consent, account_id, statement_id, sub_application=sub_application, raw=raw)
        print("The response of FinancialDataApi->get_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_statement: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **statement_id** | **str**| __Mandatory__. The statement Id of the statement file. | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAccountStatement**](ApiResponseOfAccountStatement.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_file**
> bytearray get_statement_file(consent, account_id, statement_id, sub_application=sub_application, raw=raw)

Get Account Statement File

Returns a PDF file of a statement for an account.<br><br>Feature: `ACCOUNT_STATEMENT_FILE`

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
async with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.FinancialDataApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    statement_id = 'statement_id_example' # str | __Mandatory__. The statement Id of the statement file.
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Statement File
        api_response = await api_instance.get_statement_file(consent, account_id, statement_id, sub_application=sub_application, raw=raw)
        print("The response of FinancialDataApi->get_statement_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_statement_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **statement_id** | **str**| __Mandatory__. The statement Id of the statement file. | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements**
> ApiListResponseOfAccountStatement get_statements(consent, account_id, sub_application=sub_application, var_from=var_from, before=before, limit=limit, sort=sort, offset=offset, raw=raw)

Get Account Statements

Returns the list of statements for an account.<br><br>Feature: `ACCOUNT_STATEMENTS`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_account_statement import ApiListResponseOfAccountStatement
from yapily.models.sort_enum import SortEnum
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
    api_instance = yapily.FinancialDataApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    var_from = 'var_from_example' # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).  (optional)
    before = 'before_example' # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
    limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. (optional)
    sort = yapily.SortEnum() # SortEnum | __Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending (optional)
    offset = 56 # int | __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Statements
        api_response = await api_instance.get_statements(consent, account_id, sub_application=sub_application, var_from=var_from, before=before, limit=limit, sort=sort, offset=offset, raw=raw)
        print("The response of FinancialDataApi->get_statements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_statements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **var_from** | **str**| __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ).  | [optional] 
 **before** | **str**| __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional] 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. | [optional] 
 **sort** | [**SortEnum**](.md)| __Optional__. Sort transaction records by date ascending with &#39;date&#39; or descending with &#39;-date&#39;. The default sort order is descending | [optional] 
 **offset** | **int**| __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiListResponseOfAccountStatement**](ApiListResponseOfAccountStatement.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> ApiListResponseOfTransaction get_transactions(account_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, var_with=var_with, var_from=var_from, before=before, limit=limit, sort=sort, offset=offset, cursor=cursor, raw=raw)

Get Account Transactions

Returns the account transactions for an account.<br><br>Feature: `ACCOUNT_TRANSACTIONS`

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_transaction import ApiListResponseOfTransaction
from yapily.models.sort_enum import SortEnum
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
    api_instance = yapily.FinancialDataApi(api_client)
    account_id = 'account_id_example' # str | __Mandatory__. The account Id of the user's bank account.
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    sub_application = 'sub_application_example' # str | The sub-application ID to which event type is being subscribed to (optional)
    var_with = ['var_with_example'] # List[str] | __Optional__. Acceptable value: `categorisation`. When set, will include enrichment data in the transactions returned. <br><br>Enrichment data is optional, e.g. when 'categorisation' enrichment data is requested, the enrichment response will include categorisation data and merchant name, only if it can be evaluated from the transaction. This service is limited for UK institution transactions currently. __This is a legacy feature and will be deprecated. Date TBC__ (optional)
    var_from = 'var_from_example' # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).  (optional)
    before = 'before_example' # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
    limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. (optional)
    sort = yapily.SortEnum() # SortEnum | __Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending (optional)
    offset = 56 # int | __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. (optional)
    cursor = 'cursor_example' # str | __Optional__. This property is not currently in use. (optional)
    raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Get Account Transactions
        api_response = await api_instance.get_transactions(account_id, consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, sub_application=sub_application, var_with=var_with, var_from=var_from, before=before, limit=limit, sort=sort, offset=offset, cursor=cursor, raw=raw)
        print("The response of FinancialDataApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialDataApi->get_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| __Mandatory__. The account Id of the user&#39;s bank account. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **sub_application** | **str**| The sub-application ID to which event type is being subscribed to | [optional] 
 **var_with** | [**List[str]**](str.md)| __Optional__. Acceptable value: &#x60;categorisation&#x60;. When set, will include enrichment data in the transactions returned. &lt;br&gt;&lt;br&gt;Enrichment data is optional, e.g. when &#39;categorisation&#39; enrichment data is requested, the enrichment response will include categorisation data and merchant name, only if it can be evaluated from the transaction. This service is limited for UK institution transactions currently. __This is a legacy feature and will be deprecated. Date TBC__ | [optional] 
 **var_from** | **str**| __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ).  | [optional] 
 **before** | **str**| __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional] 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. | [optional] 
 **sort** | [**SortEnum**](.md)| __Optional__. Sort transaction records by date ascending with &#39;date&#39; or descending with &#39;-date&#39;. The default sort order is descending | [optional] 
 **offset** | **int**| __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. | [optional] 
 **cursor** | **str**| __Optional__. This property is not currently in use. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiListResponseOfTransaction**](ApiListResponseOfTransaction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

