# yapily.VirtualAccountsBeneficiariesApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_account_beneficiary**](VirtualAccountsBeneficiariesApi.md#create_virtual_account_beneficiary) | **POST** /virtual-accounts/beneficiaries | Create Beneficiary
[**delete_virtual_account_beneficiary**](VirtualAccountsBeneficiariesApi.md#delete_virtual_account_beneficiary) | **DELETE** /virtual-accounts/beneficiaries/{beneficiaryId} | Delete Beneficiary
[**get_virtual_account_beneficiaries**](VirtualAccountsBeneficiariesApi.md#get_virtual_account_beneficiaries) | **GET** /virtual-accounts/beneficiaries | Get List Of Beneficiaries
[**get_virtual_account_beneficiary**](VirtualAccountsBeneficiariesApi.md#get_virtual_account_beneficiary) | **GET** /virtual-accounts/beneficiaries/{beneficiaryId} | Get Beneficiary


# **create_virtual_account_beneficiary**
> ApiResponseOfVirtualAccountBeneficiary create_virtual_account_beneficiary(client_id, virtual_account_beneficiary_request)

Create Beneficiary

Create a new beneficiary (individual or business account) to which a Pay Out can be made. The beneficiary can be used from any virtual account that is held

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_beneficiary import ApiResponseOfVirtualAccountBeneficiary
from yapily.models.virtual_account_beneficiary_request import VirtualAccountBeneficiaryRequest
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
    api_instance = yapily.VirtualAccountsBeneficiariesApi(api_client)
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    virtual_account_beneficiary_request = {"nickname":"MyBeneficiary123","paymentSchemes":["FASTER_PAYMENTS","CHAPS"],"type":"INDIVIDUAL","name":"Mr Jack Williams","birthDate":"1999-10-04","address":{"addressLine":"12 New Street","townName":"London","postCode":"NE15 PLZ","country":"GB"},"account":{"currency":"GBP","bankName":"Lloyds Bank","bankAddress":"London, WE12 ABC","bankCountry":"GB","accountIdentifications":[{"type":"SORT_CODE","identification":"401016"},{"type":"ACCOUNT_NUMBER","identification":"71518920"}]}} # VirtualAccountBeneficiaryRequest | 

    try:
        # Create Beneficiary
        api_response = await api_instance.create_virtual_account_beneficiary(client_id, virtual_account_beneficiary_request)
        print("The response of VirtualAccountsBeneficiariesApi->create_virtual_account_beneficiary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsBeneficiariesApi->create_virtual_account_beneficiary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **virtual_account_beneficiary_request** | [**VirtualAccountBeneficiaryRequest**](VirtualAccountBeneficiaryRequest.md)|  | 

### Return type

[**ApiResponseOfVirtualAccountBeneficiary**](ApiResponseOfVirtualAccountBeneficiary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict with another beneficiary with same account identifications |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**424** | A failure occurred during an interaction with a third party provider. |  -  |
**500** | Unexpected Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_account_beneficiary**
> delete_virtual_account_beneficiary(beneficiary_id, client_id)

Delete Beneficiary

Delete a specific beneficiary (individual or business account)

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
    api_instance = yapily.VirtualAccountsBeneficiariesApi(api_client)
    beneficiary_id = 'beneficiary_id_example' # str | __Mandatory__. The Id of the beneficiary that will be deleted
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for

    try:
        # Delete Beneficiary
        await api_instance.delete_virtual_account_beneficiary(beneficiary_id, client_id)
    except Exception as e:
        print("Exception when calling VirtualAccountsBeneficiariesApi->delete_virtual_account_beneficiary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beneficiary_id** | **str**| __Mandatory__. The Id of the beneficiary that will be deleted | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorised. Credentials are missing or invalid |  -  |
**403** | Forbidden. Permission to access this endpoint is not granted. |  -  |
**404** | Not Found. Requested beneficiary is not found |  -  |
**424** | A failure occurred during an interaction with a third party provider. |  -  |
**500** | Unexpected Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_account_beneficiaries**
> ApiListResponseOfVirtualAccountBeneficiary get_virtual_account_beneficiaries(client_id, cursor=cursor)

Get List Of Beneficiaries

Gets the list of beneficiaries (individual or business account) to which a Pay Out can be made.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_virtual_account_beneficiary import ApiListResponseOfVirtualAccountBeneficiary
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
    api_instance = yapily.VirtualAccountsBeneficiariesApi(api_client)
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for
    cursor = 'cursor_example' # str | __Optional__. Data required to provide pagination (optional)

    try:
        # Get List Of Beneficiaries
        api_response = await api_instance.get_virtual_account_beneficiaries(client_id, cursor=cursor)
        print("The response of VirtualAccountsBeneficiariesApi->get_virtual_account_beneficiaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsBeneficiariesApi->get_virtual_account_beneficiaries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 
 **cursor** | **str**| __Optional__. Data required to provide pagination | [optional] 

### Return type

[**ApiListResponseOfVirtualAccountBeneficiary**](ApiListResponseOfVirtualAccountBeneficiary.md)

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

# **get_virtual_account_beneficiary**
> ApiResponseOfVirtualAccountBeneficiary get_virtual_account_beneficiary(beneficiary_id, client_id)

Get Beneficiary

Get the details of a specific beneficiary (individual or business account) to which a Pay Out can be made from its id.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_virtual_account_beneficiary import ApiResponseOfVirtualAccountBeneficiary
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
    api_instance = yapily.VirtualAccountsBeneficiariesApi(api_client)
    beneficiary_id = 'beneficiary_id_example' # str | __Mandatory__. The Id of the requested beneficiary.
    client_id = '5a7294ab-6b7d-4681-835a-f9b9775c75db' # str | The customer or sub-customer ID. Identifies the customer to perform the request for

    try:
        # Get Beneficiary
        api_response = await api_instance.get_virtual_account_beneficiary(beneficiary_id, client_id)
        print("The response of VirtualAccountsBeneficiariesApi->get_virtual_account_beneficiary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualAccountsBeneficiariesApi->get_virtual_account_beneficiary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beneficiary_id** | **str**| __Mandatory__. The Id of the requested beneficiary. | 
 **client_id** | **str**| The customer or sub-customer ID. Identifies the customer to perform the request for | 

### Return type

[**ApiResponseOfVirtualAccountBeneficiary**](ApiResponseOfVirtualAccountBeneficiary.md)

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

