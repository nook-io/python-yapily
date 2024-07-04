# yapily.EnrichmentApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_transactions_categorised**](EnrichmentApi.md#get_accounts_transactions_categorised) | **GET** /accounts/{accountId}/transactions/categorisation/{categorisationId} | Get Categorised Transactions
[**get_categorisation_account_type**](EnrichmentApi.md#get_categorisation_account_type) | **GET** /transactions/categorisation/categories/{accountType} | Get the list of all categories for a specific account type
[**post_accounts_account_id_transactions_categorisation**](EnrichmentApi.md#post_accounts_account_id_transactions_categorisation) | **POST** /accounts/{accountId}/transactions/categorisation | Trigger transaction categorisation


# **get_accounts_transactions_categorised**
> GetAccountsTransactionsCategorised200Response get_accounts_transactions_categorised(consent, account_id, categorisation_id, limit=limit)

Get Categorised Transactions

Retrieve a set of categorised transactions using a provided categorisation ID (__Note__: A categorisation ID will only be valid for 30 mins after a __transactions.categorisation.successful__ wedhook has be received)

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.get_accounts_transactions_categorised200_response import GetAccountsTransactionsCategorised200Response
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
    api_instance = yapily.EnrichmentApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    account_id = 'account_id_example' # str | Unique identifier for account
    categorisation_id = 'categorisation_id_example' # str | Unique identifier for transaction categorisation request
    limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. (optional)

    try:
        # Get Categorised Transactions
        api_response = api_instance.get_accounts_transactions_categorised(consent, account_id, categorisation_id, limit=limit)
        print("The response of EnrichmentApi->get_accounts_transactions_categorised:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrichmentApi->get_accounts_transactions_categorised: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_id** | **str**| Unique identifier for account | 
 **categorisation_id** | **str**| Unique identifier for transaction categorisation request | 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. | [optional] 

### Return type

[**GetAccountsTransactionsCategorised200Response**](GetAccountsTransactionsCategorised200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categorisation_account_type**
> GetCategorisationAccountType200Response get_categorisation_account_type(account_type)

Get the list of all categories for a specific account type

Returns the list of categories that can be returned for a specific account type (consumer or business)

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.get_categorisation_account_type200_response import GetCategorisationAccountType200Response
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
    api_instance = yapily.EnrichmentApi(api_client)
    account_type = 'account_type_example' # str | type of bank account (consumer or business)

    try:
        # Get the list of all categories for a specific account type
        api_response = api_instance.get_categorisation_account_type(account_type)
        print("The response of EnrichmentApi->get_categorisation_account_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrichmentApi->get_categorisation_account_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| type of bank account (consumer or business) | 

### Return type

[**GetCategorisationAccountType200Response**](GetCategorisationAccountType200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_accounts_account_id_transactions_categorisation**
> PostAccountsAccountIdTransactionsCategorisation201Response post_accounts_account_id_transactions_categorisation(consent, account_id, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, post_accounts_account_id_transactions_categorisation_request=post_accounts_account_id_transactions_categorisation_request)

Trigger transaction categorisation

Trigger categorisation for a specified set of transactions

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.post_accounts_account_id_transactions_categorisation201_response import PostAccountsAccountIdTransactionsCategorisation201Response
from yapily.models.post_accounts_account_id_transactions_categorisation_request import PostAccountsAccountIdTransactionsCategorisationRequest
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
    api_instance = yapily.EnrichmentApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    account_id = 'account_id_example' # str | Unique identifier for account
    psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. (optional)
    post_accounts_account_id_transactions_categorisation_request = {"countryCode":"GB","from":"2019-08-24T14:15:22Z","before":"2019-08-24T14:15:22Z","sort":"-date"} # PostAccountsAccountIdTransactionsCategorisationRequest |  (optional)

    try:
        # Trigger transaction categorisation
        api_response = api_instance.post_accounts_account_id_transactions_categorisation(consent, account_id, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, post_accounts_account_id_transactions_categorisation_request=post_accounts_account_id_transactions_categorisation_request)
        print("The response of EnrichmentApi->post_accounts_account_id_transactions_categorisation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrichmentApi->post_accounts_account_id_transactions_categorisation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_id** | **str**| Unique identifier for account | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/pages/knowledge/open-banking/psu_identifiers/) to see if this header is required. | [optional] 
 **post_accounts_account_id_transactions_categorisation_request** | [**PostAccountsAccountIdTransactionsCategorisationRequest**](PostAccountsAccountIdTransactionsCategorisationRequest.md)|  | [optional] 

### Return type

[**PostAccountsAccountIdTransactionsCategorisation201Response**](PostAccountsAccountIdTransactionsCategorisation201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

