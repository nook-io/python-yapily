# yapily.VirtualAccountsRefundsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_account_refund**](VirtualAccountsRefundsApi.md#create_virtual_account_refund) | **POST** /virtual-accounts/refunds | Create Refund
[**get_virtual_account_refund_by_id**](VirtualAccountsRefundsApi.md#get_virtual_account_refund_by_id) | **GET** /virtual-accounts/refunds/{id} | Get Refund By Id
[**get_virtual_account_refunds**](VirtualAccountsRefundsApi.md#get_virtual_account_refunds) | **GET** /virtual-accounts/refunds | Get list of refunds


# **create_virtual_account_refund**
> ApiResponseOfVirtualAccountRefund create_virtual_account_refund(idempotency_key, client_id, virtual_account_refund_request)

Create Refund

Create a refund for a payment received into a virtual account. Funds are returned to the source account. When subscribed to `virtualAccount.refund.status` notifications, updates on the refund status are delivered asynchronously.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_refund import ApiResponseOfVirtualAccountRefund
from yapily.models.virtual_account_refund_request import VirtualAccountRefundRequest
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
    api_instance = yapily.VirtualAccountsRefundsApi(api_client)
    idempotency_key = 'a346fe67-1d81-4ccd-8409-bf9d6c07980f' # str | Uniquely identifies a request, such that requests made with a same value are considered retries <br> We recommend that a v4 UUID is supplied 
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    virtual_account_refund_request = {"originalPayment":{"paymentInitiationId":"19d2fbfb-f30c-44eb-b3b5-978560d2b712"},"amount":{"amount":100,"currency":"GBP"},"reason":"REQUESTED_BY_CUSTOMER","paymentDate":"2022-11-11","reference":"Refund 123","refundTo":"SOURCE","beneficiaryType":"INDIVIDUAL"} # VirtualAccountRefundRequest | 

    try:
        # Create Refund
        api_response = await api_instance.create_virtual_account_refund(idempotency_key, client_id, virtual_account_refund_request)
        print("The response of VirtualAccountsRefundsApi->create_virtual_account_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsRefundsApi->create_virtual_account_refund: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Uniquely identifies a request, such that requests made with a same value are considered retries &lt;br&gt; We recommend that a v4 UUID is supplied  | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **virtual_account_refund_request** | [**VirtualAccountRefundRequest**](VirtualAccountRefundRequest.md)|  | 

### Return type

[**ApiResponseOfVirtualAccountRefund**](ApiResponseOfVirtualAccountRefund.md)

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

# **get_virtual_account_refund_by_id**
> ApiResponseOfVirtualAccountRefund get_virtual_account_refund_by_id(id, client_id)

Get Refund By Id

Get the details of a refund by its ID

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_refund import ApiResponseOfVirtualAccountRefund
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
    api_instance = yapily.VirtualAccountsRefundsApi(api_client)
    id = 'id_example' # str | __Mandatory__. The id of the refund
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for

    try:
        # Get Refund By Id
        api_response = await api_instance.get_virtual_account_refund_by_id(id, client_id)
        print("The response of VirtualAccountsRefundsApi->get_virtual_account_refund_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsRefundsApi->get_virtual_account_refund_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| __Mandatory__. The id of the refund | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 

### Return type

[**ApiResponseOfVirtualAccountRefund**](ApiResponseOfVirtualAccountRefund.md)

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

# **get_virtual_account_refunds**
> ApiListResponseOfVirtualAccountRefund get_virtual_account_refunds(client_id, payment_initiation_id=payment_initiation_id, status=status, created_date_time_after=created_date_time_after, created_date_time_before=created_date_time_before, cursor=cursor)

Get list of refunds

Retrieve a list of refunds

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_virtual_account_refund import ApiListResponseOfVirtualAccountRefund
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
    api_instance = yapily.VirtualAccountsRefundsApi(api_client)
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    payment_initiation_id = 'PDC_29bd8528-9b6f-4b6e-a963-9382944dc830' # str | __Optional__. Filter refunds based on unique ID of the original payment (optional)
    status = 'PROCESSING' # str | __Optional__.  Filter refunds based on refund status. One of INITIATED, SCHEDULED, PROCESSING, COMPLETED, FAILED (optional)
    created_date_time_after = '2023-01-13T16:41:51.136085Z' # datetime | __Optional__.  Filter to get refunds created on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ) (optional)
    created_date_time_before = '2023-02-13T16:41:51.136085Z' # datetime | __Optional__.  Filter to get refunds created on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ) (optional)
    cursor = 'cGF5bWVudEluaXRpYXRpb25JZD1QRENfMjliZDg1MjgtOWI2Zi00YjZlLWE5NjMtOTM4Mjk0NGRjODMwJnN0YXR1cz1GQUlMRUQmY3JlYXRlZERhdGVUaW1lRnJvbT0yMDIzLTAxLTEzVDE2OjQxOjUxLjEzNjA4NVomY3JlYXRlZERhdGVUaW1lVG89MjAyMy0wMi0xMFQxODo0Mjo1MS4xMzYwODVaJnBvaW50ZXI9MjAyMy0wMS0xM1QxNjo0MTo1MS4xMzYwODU=' # str | __Optional__. Encoded pagination cursor to fetch next page (optional)

    try:
        # Get list of refunds
        api_response = await api_instance.get_virtual_account_refunds(client_id, payment_initiation_id=payment_initiation_id, status=status, created_date_time_after=created_date_time_after, created_date_time_before=created_date_time_before, cursor=cursor)
        print("The response of VirtualAccountsRefundsApi->get_virtual_account_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsRefundsApi->get_virtual_account_refunds: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **payment_initiation_id** | **str**| __Optional__. Filter refunds based on unique ID of the original payment | [optional] 
 **status** | **str**| __Optional__.  Filter refunds based on refund status. One of INITIATED, SCHEDULED, PROCESSING, COMPLETED, FAILED | [optional] 
 **created_date_time_after** | **datetime**| __Optional__.  Filter to get refunds created on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ) | [optional] 
 **created_date_time_before** | **datetime**| __Optional__.  Filter to get refunds created on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ) | [optional] 
 **cursor** | **str**| __Optional__. Encoded pagination cursor to fetch next page | [optional] 

### Return type

[**ApiListResponseOfVirtualAccountRefund**](ApiListResponseOfVirtualAccountRefund.md)

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

