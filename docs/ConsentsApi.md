# yapily.ConsentsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consent_with_code**](ConsentsApi.md#create_consent_with_code) | **POST** /consent-auth-code | Exchange OAuth2 Code
[**delete**](ConsentsApi.md#delete) | **DELETE** /consents/{consentId} | Delete Consent
[**extend_consent**](ConsentsApi.md#extend_consent) | **POST** /consents/{consentId}/extend | Extend Consent
[**get_consent_by_id**](ConsentsApi.md#get_consent_by_id) | **GET** /consents/{consentId} | Get Consent
[**get_consent_by_single_access_consent**](ConsentsApi.md#get_consent_by_single_access_consent) | **POST** /consent-one-time-token | Exchange One Time Token
[**get_consents**](ConsentsApi.md#get_consents) | **GET** /consents | Get Consents


# **create_consent_with_code**
> Consent create_consent_with_code(consent_auth_code_request)

Exchange OAuth2 Code

Used to obtain a Yapily Consent object containing the `consentToken` once the user has authenticated and you have an OAuth2 authorisation code `auth-code` and state `auth-state`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.consent import Consent
from yapily.models.consent_auth_code_request import ConsentAuthCodeRequest
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
    api_instance = yapily.ConsentsApi(api_client)
    consent_auth_code_request = yapily.ConsentAuthCodeRequest() # ConsentAuthCodeRequest | 

    try:
        # Exchange OAuth2 Code
        api_response = await api_instance.create_consent_with_code(consent_auth_code_request)
        print("The response of ConsentsApi->create_consent_with_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsentsApi->create_consent_with_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_auth_code_request** | [**ConsentAuthCodeRequest**](ConsentAuthCodeRequest.md)|  | 

### Return type

[**Consent**](Consent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> ApiResponseOfConsentDeleteResponse delete(consent_id, force_delete=force_delete)

Delete Consent

Delete a consent using the consent Id

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_consent_delete_response import ApiResponseOfConsentDeleteResponse
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
    api_instance = yapily.ConsentsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Consent` to update.
    force_delete = True # bool | __Optional__. Whether to force the deletion. (optional) (default to True)

    try:
        # Delete Consent
        api_response = await api_instance.delete(consent_id, force_delete=force_delete)
        print("The response of ConsentsApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsentsApi->delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. | 
 **force_delete** | **bool**| __Optional__. Whether to force the deletion. | [optional] [default to True]

### Return type

[**ApiResponseOfConsentDeleteResponse**](ApiResponseOfConsentDeleteResponse.md)

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

# **extend_consent**
> ApiResponseOfConsent extend_consent(consent_id, extend_consent_request)

Extend Consent

Used to indicate to Yapily that reconfirmation has occurred for a given Consent, and to update lastUpdatedAt and reconfirmBy for that Consent. Returns the Consent.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_consent import ApiResponseOfConsent
from yapily.models.extend_consent_request import ExtendConsentRequest
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
    api_instance = yapily.ConsentsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Consent` to update.
    extend_consent_request = yapily.ExtendConsentRequest() # ExtendConsentRequest | 

    try:
        # Extend Consent
        api_response = await api_instance.extend_consent(consent_id, extend_consent_request)
        print("The response of ConsentsApi->extend_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsentsApi->extend_consent: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. | 
 **extend_consent_request** | [**ExtendConsentRequest**](ExtendConsentRequest.md)|  | 

### Return type

[**ApiResponseOfConsent**](ApiResponseOfConsent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Error Response. The supplied lastConfirmedAt date, Consent type, or Consent status is invalid. |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_by_id**
> ApiResponseOfConsent get_consent_by_id(consent_id)

Get Consent

Get consent using the consent Id

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_response_of_consent import ApiResponseOfConsent
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
    api_instance = yapily.ConsentsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Consent` to update.

    try:
        # Get Consent
        api_response = await api_instance.get_consent_by_id(consent_id)
        print("The response of ConsentsApi->get_consent_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsentsApi->get_consent_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. | 

### Return type

[**ApiResponseOfConsent**](ApiResponseOfConsent.md)

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

# **get_consent_by_single_access_consent**
> Consent get_consent_by_single_access_consent(one_time_token_request)

Exchange One Time Token

Exchange a One-time-token for the consent token

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.consent import Consent
from yapily.models.one_time_token_request import OneTimeTokenRequest
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
    api_instance = yapily.ConsentsApi(api_client)
    one_time_token_request = yapily.OneTimeTokenRequest() # OneTimeTokenRequest | 

    try:
        # Exchange One Time Token
        api_response = await api_instance.get_consent_by_single_access_consent(one_time_token_request)
        print("The response of ConsentsApi->get_consent_by_single_access_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsentsApi->get_consent_by_single_access_consent: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **one_time_token_request** | [**OneTimeTokenRequest**](OneTimeTokenRequest.md)|  | 

### Return type

[**Consent**](Consent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consents**
> ApiListResponseOfConsent get_consents(filter_application_user_id=filter_application_user_id, filter_user_uuid=filter_user_uuid, filter_institution=filter_institution, filter_status=filter_status, var_from=var_from, before=before, limit=limit, offset=offset)

Get Consents

Used to retrieve all the consents created for each user within an application

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import yapily
from yapily.models.api_list_response_of_consent import ApiListResponseOfConsent
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
    api_instance = yapily.ConsentsApi(api_client)
    filter_application_user_id = ['filter_application_user_id_example'] # List[str] | __Optional__. Filter records based on the list of `applicationUserId` users provided. (optional)
    filter_user_uuid = ['filter_user_uuid_example'] # List[str] | __Optional__. Filter records based on the list of `userUuid` users provided. (optional)
    filter_institution = ['filter_institution_example'] # List[str] | __Optional__. Filter records based on the list of `Institution` provided. (optional)
    filter_status = ['filter_status_example'] # List[str] | __Optional__. Filter records based on the list of `Consent` [statuses](https://docs.yapily.com/api/reference/#operation/getConsents!c=200&path=data/status&t=response). (optional)
    var_from = 'var_from_example' # str | __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).  (optional)
    before = 'before_example' # str | __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). (optional)
    limit = 56 # int | __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. (optional)
    offset = 0 # int | __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. (optional) (default to 0)

    try:
        # Get Consents
        api_response = await api_instance.get_consents(filter_application_user_id=filter_application_user_id, filter_user_uuid=filter_user_uuid, filter_institution=filter_institution, filter_status=filter_status, var_from=var_from, before=before, limit=limit, offset=offset)
        print("The response of ConsentsApi->get_consents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsentsApi->get_consents: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_application_user_id** | [**List[str]**](str.md)| __Optional__. Filter records based on the list of &#x60;applicationUserId&#x60; users provided. | [optional] 
 **filter_user_uuid** | [**List[str]**](str.md)| __Optional__. Filter records based on the list of &#x60;userUuid&#x60; users provided. | [optional] 
 **filter_institution** | [**List[str]**](str.md)| __Optional__. Filter records based on the list of &#x60;Institution&#x60; provided. | [optional] 
 **filter_status** | [**List[str]**](str.md)| __Optional__. Filter records based on the list of &#x60;Consent&#x60; [statuses](https://docs.yapily.com/api/reference/#operation/getConsents!c&#x3D;200&amp;path&#x3D;data/status&amp;t&#x3D;response). | [optional] 
 **var_from** | **str**| __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ).  | [optional] 
 **before** | **str**| __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ). | [optional] 
 **limit** | **int**| __Optional__. The maximum number of transaction records to be returned. Must be between 1 and 1000. | [optional] 
 **offset** | **int**| __Optional__. The number of transaction records to be skipped. Used primarily with paginated results. | [optional] [default to 0]

### Return type

[**ApiListResponseOfConsent**](ApiListResponseOfConsent.md)

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

