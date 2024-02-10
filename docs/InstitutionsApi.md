# yapily.InstitutionsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feature_details**](InstitutionsApi.md#get_feature_details) | **GET** /features | Get Features
[**get_institution**](InstitutionsApi.md#get_institution) | **GET** /institutions/{institutionId} | Get Institution
[**get_institutions**](InstitutionsApi.md#get_institutions) | **GET** /institutions | Get Institutions


# **get_feature_details**
> ApiListResponseOfFeatureDetails get_feature_details()

Get Features

Used to retrieve all features available from Yapily. Each `Institution` supports a one, many or all of these features and can be seen in the features field of the `Institution` object.<br><br>Note: Every `Institution` does not necessarily support every feature. To see which features are available for a particular Institution, use either the [Get Institutions](https://docs.yapily.com/api/reference/#operation/getInstitutions) or [Get Institution](https://docs.yapily.com/api/reference/#operation/getInstitution) endpoint and check the features array within the `Institution` payload.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_list_response_of_feature_details import ApiListResponseOfFeatureDetails
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
    api_instance = yapily.InstitutionsApi(api_client)

    try:
        # Get Features
        api_response = await api_instance.get_feature_details()
        print("The response of InstitutionsApi->get_feature_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_feature_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiListResponseOfFeatureDetails**](ApiListResponseOfFeatureDetails.md)

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

# **get_institution**
> Institution get_institution(institution_id)

Get Institution

Used to retrieves details of a specific `Institution` within an application

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.institution import Institution
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
    api_instance = yapily.InstitutionsApi(api_client)
    institution_id = 'institution_id_example' # str | __Mandatory__. The Yapily institution Id for the `Institution`.

    try:
        # Get Institution
        api_response = await api_instance.get_institution(institution_id)
        print("The response of InstitutionsApi->get_institution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_institution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **str**| __Mandatory__. The Yapily institution Id for the &#x60;Institution&#x60;. | 

### Return type

[**Institution**](Institution.md)

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

# **get_institutions**
> ApiListResponseOfInstitution get_institutions()

Get Institutions

Used to retrieve all `Institutions` within an application

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_list_response_of_institution import ApiListResponseOfInstitution
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
    api_instance = yapily.InstitutionsApi(api_client)

    try:
        # Get Institutions
        api_response = await api_instance.get_institutions()
        print("The response of InstitutionsApi->get_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_institutions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiListResponseOfInstitution**](ApiListResponseOfInstitution.md)

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

