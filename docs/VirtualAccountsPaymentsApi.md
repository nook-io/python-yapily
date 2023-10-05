# yapily.VirtualAccountsPaymentsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_account_pay_out**](VirtualAccountsPaymentsApi.md#create_virtual_account_pay_out) | **POST** /virtual-accounts/payments/pay-outs | Create Pay Out
[**create_virtual_account_transfer**](VirtualAccountsPaymentsApi.md#create_virtual_account_transfer) | **POST** /virtual-accounts/payments/transfers | Create Virtual Account Transfer
[**get_pay_in_details**](VirtualAccountsPaymentsApi.md#get_pay_in_details) | **GET** /virtual-accounts/payments/{paymentId}/pay-in-details | Get Pay-In Details
[**get_payments_by_id**](VirtualAccountsPaymentsApi.md#get_payments_by_id) | **GET** /virtual-accounts/payments/{id} | Get Payment
[**get_virtual_account_payments**](VirtualAccountsPaymentsApi.md#get_virtual_account_payments) | **GET** /virtual-accounts/payments | Get Payments


# **create_virtual_account_pay_out**
> ApiResponseOfVirtualAccountPayment create_virtual_account_pay_out(idempotency_key, client_id, virtual_account_pay_out_request)

Create Pay Out

Initiate a payment from a specified virtual account to a previously added beneficiary using any of the schemes that it supports <br> When subscribed to virtualAccount.payOut.status notifications, further updates on payment processing status will be delivered asynchronously 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_payment import ApiResponseOfVirtualAccountPayment
from yapily.models.virtual_account_pay_out_request import VirtualAccountPayOutRequest
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
    api_instance = yapily.VirtualAccountsPaymentsApi(api_client)
    idempotency_key = 'a346fe67-1d81-4ccd-8409-bf9d6c07980f' # str | Uniquely identifies a request, such that requests made with a same value are considered retries <br> We recommend that a v4 UUID is supplied 
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    virtual_account_pay_out_request = {"accountId":"eb2ad083-a111-4143-8756-a3a3cef4031c","amount":{"amount":10.5,"currency":"GBP"},"reference":"Invoice 1267765","beneficiaryId":"sd6ad034-a111-4143-8756-a3a3cef4045v","paymentScheme":"FASTER_PAYMENTS","paymentDate":"2022-08-28"} # VirtualAccountPayOutRequest | 

    try:
        # Create Pay Out
        api_response = await api_instance.create_virtual_account_pay_out(idempotency_key, client_id, virtual_account_pay_out_request)
        print("The response of VirtualAccountsPaymentsApi->create_virtual_account_pay_out:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsPaymentsApi->create_virtual_account_pay_out: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Uniquely identifies a request, such that requests made with a same value are considered retries &lt;br&gt; We recommend that a v4 UUID is supplied  | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **virtual_account_pay_out_request** | [**VirtualAccountPayOutRequest**](VirtualAccountPayOutRequest.md)|  | 

### Return type

[**ApiResponseOfVirtualAccountPayment**](ApiResponseOfVirtualAccountPayment.md)

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

# **create_virtual_account_transfer**
> ApiResponseOfVirtualAccountPayment create_virtual_account_transfer(idempotency_key, client_id, virtual_account_transfer_request)

Create Virtual Account Transfer

Create a transfer between two virtual accounts

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_payment import ApiResponseOfVirtualAccountPayment
from yapily.models.virtual_account_transfer_request import VirtualAccountTransferRequest
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
    api_instance = yapily.VirtualAccountsPaymentsApi(api_client)
    idempotency_key = 'a346fe67-1d81-4ccd-8409-bf9d6c07980f' # str | Uniquely identifies a request, such that requests made with a same value are considered retries <br> We recommend that a v4 UUID is supplied 
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    virtual_account_transfer_request = {"amount":{"amount":10.5,"currency":"GBP"},"source":{"accountId":"a346fe67-1d81-4ccd-8409-bf9d6c07980f"},"destination":{"accountId":"e3465e67-1d81-4ccd-8409-tf9d6c07980r"},"reference":"Ref 86543"} # VirtualAccountTransferRequest | 

    try:
        # Create Virtual Account Transfer
        api_response = await api_instance.create_virtual_account_transfer(idempotency_key, client_id, virtual_account_transfer_request)
        print("The response of VirtualAccountsPaymentsApi->create_virtual_account_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsPaymentsApi->create_virtual_account_transfer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Uniquely identifies a request, such that requests made with a same value are considered retries &lt;br&gt; We recommend that a v4 UUID is supplied  | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **virtual_account_transfer_request** | [**VirtualAccountTransferRequest**](VirtualAccountTransferRequest.md)|  | 

### Return type

[**ApiResponseOfVirtualAccountPayment**](ApiResponseOfVirtualAccountPayment.md)

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

# **get_pay_in_details**
> ApiResponseOfVirtualAccountPayInDetails get_pay_in_details(payment_id, client_id)

Get Pay-In Details

Get the details of a pay-in transaction

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_pay_in_details import ApiResponseOfVirtualAccountPayInDetails
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
    api_instance = yapily.VirtualAccountsPaymentsApi(api_client)
    payment_id = '8b66abb5-5412-4454-aa7b-4e693ada6321' # str | Uniquely identifies a transaction
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for

    try:
        # Get Pay-In Details
        api_response = await api_instance.get_pay_in_details(payment_id, client_id)
        print("The response of VirtualAccountsPaymentsApi->get_pay_in_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsPaymentsApi->get_pay_in_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Uniquely identifies a transaction | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 

### Return type

[**ApiResponseOfVirtualAccountPayInDetails**](ApiResponseOfVirtualAccountPayInDetails.md)

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
**404** | Not Found. Requested beneficiary is not found. |  -  |
**424** | A failure occurred during an interaction with a third party provider. |  -  |
**500** | Unexpected Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_by_id**
> ApiResponseOfVirtualAccountPayment get_payments_by_id(id, client_id)

Get Payment

Get the details of a specific payment using its Id

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_payment import ApiResponseOfVirtualAccountPayment
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
    api_instance = yapily.VirtualAccountsPaymentsApi(api_client)
    id = 'id_example' # str | __Mandatory__. The id of the payment
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for

    try:
        # Get Payment
        api_response = await api_instance.get_payments_by_id(id, client_id)
        print("The response of VirtualAccountsPaymentsApi->get_payments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsPaymentsApi->get_payments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| __Mandatory__. The id of the payment | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 

### Return type

[**ApiResponseOfVirtualAccountPayment**](ApiResponseOfVirtualAccountPayment.md)

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
**404** | Not Found. Requested payment is not found. |  -  |
**424** | A failure occurred during an interaction with a third party provider. |  -  |
**500** | Unexpected Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_payments**
> ApiListResponseOfVirtualAccountPayment get_virtual_account_payments(client_id, account_id=account_id, created_date_time_from=created_date_time_from, created_date_time_to=created_date_time_to, status=status, type=type, cursor=cursor)

Get Payments

Retrieve a list of virtual account payments

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_virtual_account_payment import ApiListResponseOfVirtualAccountPayment
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
    api_instance = yapily.VirtualAccountsPaymentsApi(api_client)
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    account_id = 'eb2ad083-a111-4143-8756-a3a3cef4031c' # str | __Optional__. Filter payments based on accountId (optional)
    created_date_time_from = '2022-04-24T00:30:19.951Z' # datetime | __Optional__. Filter payments based on the createdDateTime (optional)
    created_date_time_to = '2022-04-24T00:30:19.951Z' # datetime | __Optional__. Filter payments based on the createdDateTime (optional)
    status = ['[\"INITIATED\",\"COMPLETED\"]'] # List[str] | __Optional__. Filter payments based on the payment status. One of INITIATED, PENDING, PROCESSING, COMPLETED, FAILED (optional)
    type = ['[\"PAY_IN\",\"PAY_OUT\"]'] # List[str] | __Optional__. Filter payments based on the payment type. One of PAY_IN, PAY_OUT, RETURN_IN, RETURN_OUT (optional)
    cursor = 'cursor_example' # str | __Optional__. Data required to provide pagination (optional)

    try:
        # Get Payments
        api_response = await api_instance.get_virtual_account_payments(client_id, account_id=account_id, created_date_time_from=created_date_time_from, created_date_time_to=created_date_time_to, status=status, type=type, cursor=cursor)
        print("The response of VirtualAccountsPaymentsApi->get_virtual_account_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsPaymentsApi->get_virtual_account_payments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **account_id** | **str**| __Optional__. Filter payments based on accountId | [optional] 
 **created_date_time_from** | **datetime**| __Optional__. Filter payments based on the createdDateTime | [optional] 
 **created_date_time_to** | **datetime**| __Optional__. Filter payments based on the createdDateTime | [optional] 
 **status** | [**List[str]**](str.md)| __Optional__. Filter payments based on the payment status. One of INITIATED, PENDING, PROCESSING, COMPLETED, FAILED | [optional] 
 **type** | [**List[str]**](str.md)| __Optional__. Filter payments based on the payment type. One of PAY_IN, PAY_OUT, RETURN_IN, RETURN_OUT | [optional] 
 **cursor** | **str**| __Optional__. Data required to provide pagination | [optional] 

### Return type

[**ApiListResponseOfVirtualAccountPayment**](ApiListResponseOfVirtualAccountPayment.md)

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

