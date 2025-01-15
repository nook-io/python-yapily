# yapily.FinancialProfileApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_profile_consent**](FinancialProfileApi.md#create_profile_consent) | **POST** /users/{userUuid}/profile/consents | Create Profile Consent
[**delete_profile_consent**](FinancialProfileApi.md#delete_profile_consent) | **DELETE** /users/{userUuid}/profile/consents/{profileConsentId} | Delete Profile Consent
[**get_balance_prediction**](FinancialProfileApi.md#get_balance_prediction) | **GET** /users/{userUuid}/profile/predicted-balances | Get Predicted Balances
[**get_profile_consent**](FinancialProfileApi.md#get_profile_consent) | **GET** /users/{userUuid}/profile/consents/{profileConsentId} | Get Profile Consent
[**get_user_profile**](FinancialProfileApi.md#get_user_profile) | **GET** /users/{userUuid}/profile/transaction-groups | Get Transaction Groups


# **create_profile_consent**
> ApiResponseOfFinancialProfileAuthorisationResponse create_profile_consent(user_uuid, consent)

Create Profile Consent

Used to add a consent to a `Financial Profile` for a `User`.  The response is asynchronous, returned with pending status, while retrieval of financial data is commenced.  There is a limit of 10,000 transactions for enrichment.

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_financial_profile_authorisation_response import ApiResponseOfFinancialProfileAuthorisationResponse
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
    api_instance = yapily.FinancialProfileApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.
    consent = 'consent_example' # str | __Mandatory__. The `consent-token` obtained from the original authorisation.

    try:
        # Create Profile Consent
        api_response = await api_instance.create_profile_consent(user_uuid, consent)
        print("The response of FinancialProfileApi->create_profile_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialProfileApi->create_profile_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. | 
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; obtained from the original authorisation. | 

### Return type

[**ApiResponseOfFinancialProfileAuthorisationResponse**](ApiResponseOfFinancialProfileAuthorisationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A successful response, returning a ApiResponseOfFinancialProfileAuthorisationResponse. |  -  |
**400** | Bad Request.  Returned if the userUuid is not a valid UUID. |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**404** | Not Found.  Returned if the userUuid is not found for the &#x60;Application&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile_consent**
> ApiResponseOfFinancialProfileConsentRemoveResponse delete_profile_consent(user_uuid, profile_consent_id)

Delete Profile Consent

Used to delete a `ProfileConsent` for a `User`. This will remove the consent and all associated financial data from the 'Financial Profile'.

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_financial_profile_consent_remove_response import ApiResponseOfFinancialProfileConsentRemoveResponse
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
    api_instance = yapily.FinancialProfileApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.
    profile_consent_id = 'profile_consent_id_example' # str | __Mandatory__. The ID of the ProfileConsent

    try:
        # Delete Profile Consent
        api_response = await api_instance.delete_profile_consent(user_uuid, profile_consent_id)
        print("The response of FinancialProfileApi->delete_profile_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialProfileApi->delete_profile_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. | 
 **profile_consent_id** | **str**| __Mandatory__. The ID of the ProfileConsent | 

### Return type

[**ApiResponseOfFinancialProfileConsentRemoveResponse**](ApiResponseOfFinancialProfileConsentRemoveResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ProfileConsent was deleted. |  -  |
**400** | Bad Request.  Returned if the userUuid is not a valid UUID. |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**404** | Not Found.  Returned if the userUuid or ProfileConsent is not found for the &#x60;Application&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_prediction**
> ApiResponseOfFinancialProfileBalancePrediction get_balance_prediction(user_uuid)

Get Predicted Balances

Used to retrieve a `Balance Prediction Profile` for a `User`.  Status will be `PENDING` until all ProfileConsents are `COMPLETED`.

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_financial_profile_balance_prediction import ApiResponseOfFinancialProfileBalancePrediction
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
    api_instance = yapily.FinancialProfileApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.

    try:
        # Get Predicted Balances
        api_response = await api_instance.get_balance_prediction(user_uuid)
        print("The response of FinancialProfileApi->get_balance_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialProfileApi->get_balance_prediction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. | 

### Return type

[**ApiResponseOfFinancialProfileBalancePrediction**](ApiResponseOfFinancialProfileBalancePrediction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response, returning a Balance Prediction Profile. |  -  |
**400** | Bad Request.  Returned if the userUuid is not a valid UUID. |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**404** | Not Found.  Returned if the userUuid is not found for the &#x60;Application&#x60;, or data not found for the userUuid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_consent**
> ApiResponseOfFinancialProfileConsent get_profile_consent(user_uuid, profile_consent_id)

Get Profile Consent

Used to retrieve a specific ProfileConsent for a User.

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_financial_profile_consent import ApiResponseOfFinancialProfileConsent
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
    api_instance = yapily.FinancialProfileApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.
    profile_consent_id = 'profile_consent_id_example' # str | __Mandatory__. The ID of the ProfileConsent

    try:
        # Get Profile Consent
        api_response = await api_instance.get_profile_consent(user_uuid, profile_consent_id)
        print("The response of FinancialProfileApi->get_profile_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialProfileApi->get_profile_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. | 
 **profile_consent_id** | **str**| __Mandatory__. The ID of the ProfileConsent | 

### Return type

[**ApiResponseOfFinancialProfileConsent**](ApiResponseOfFinancialProfileConsent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response, returning a ApiResponseOfFinancialProfileConsent. |  -  |
**400** | Bad Request.  Returned if the userUuid is not a valid UUID. |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**404** | Not Found.  Returned if the userUuid or ProfileConsent is not found for the &#x60;Application&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> ApiResponseOfFinancialProfile get_user_profile(user_uuid)

Get Transaction Groups

Used to retrieve a `TransactionGroups` for a `User`.  Status will be `PENDING` until all ProfileConsents are `COMPLETED`.

### Example

* Basic Authentication (basicAuth):

```python
import yapily
from yapily.models.api_response_of_financial_profile import ApiResponseOfFinancialProfile
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
    api_instance = yapily.FinancialProfileApi(api_client)
    user_uuid = 'user_uuid_example' # str | __Mandatory__. The Yapily generated UUID for the user.

    try:
        # Get Transaction Groups
        api_response = await api_instance.get_user_profile(user_uuid)
        print("The response of FinancialProfileApi->get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialProfileApi->get_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| __Mandatory__. The Yapily generated UUID for the user. | 

### Return type

[**ApiResponseOfFinancialProfile**](ApiResponseOfFinancialProfile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response, returning a ApiResponseOfFinancialProfile. |  -  |
**400** | Bad Request.  Returned if the userUuid is not a valid UUID. |  -  |
**401** | Either authentication credentials were not supplied, or they were invalid. |  -  |
**404** | Not Found.  Returned if the userUuid is not found for the &#x60;Application&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

