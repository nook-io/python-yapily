# yapily.VariableRecurringPaymentsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_non_sweeping_authorisation**](VariableRecurringPaymentsApi.md#create_non_sweeping_authorisation) | **POST** /variable-recurring-payments/non-sweeping/consents | Create Non-Sweeping Variable Recurring Payment Authorisation
[**create_sweeping_authorisation**](VariableRecurringPaymentsApi.md#create_sweeping_authorisation) | **POST** /variable-recurring-payments/sweeping/consents | Create Sweeping Variable Recurring Payment Authorisation
[**create_vrp_funds_confirmation**](VariableRecurringPaymentsApi.md#create_vrp_funds_confirmation) | **POST** /variable-recurring-payments/funds-confirmation | Confirm Funds for Variable Recurring Payment
[**create_vrp_payment**](VariableRecurringPaymentsApi.md#create_vrp_payment) | **POST** /variable-recurring-payments/payments | Create Variable Recurring Payment
[**get_sweeping_vrp_consent_by_id**](VariableRecurringPaymentsApi.md#get_sweeping_vrp_consent_by_id) | **GET** /variable-recurring-payments/sweeping/consents/{consentId} | Get Sweeping Variable Recurring Payment Consent Details
[**get_vrp_payment_details**](VariableRecurringPaymentsApi.md#get_vrp_payment_details) | **GET** /variable-recurring-payments/payments/{paymentId}/details | Get Variable Recurring Payment Details
[**getp_non_sweeping_vrp_consent_by_id**](VariableRecurringPaymentsApi.md#getp_non_sweeping_vrp_consent_by_id) | **GET** /variable-recurring-payments/non-sweeping/consents/{consentId} | Get Non-Sweeping Variable Recurring Payment Consent Details


# **create_non_sweeping_authorisation**
> ApiResponseOfNonSweepingAuthorisationResponse create_non_sweeping_authorisation(non_sweeping_authorisation_request)

Create Non-Sweeping Variable Recurring Payment Authorisation

Used to initiate the authorisation process and direct users to the login screen of their financial Institution in order to give their consent for Non-Sweeping Variable Recurring Payments. The request would return an Authorization URL and an Identifier for the consent created at the Institution. First make sure that the payment feature you wish to execute is supported by the bank by checking the features array in [GET Institution](https://docs.yapily.com/api/#get-institution). <br><br>See [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/redirect/) for more information about this flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_NONSWEEPING`</li></ul>

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_response_of_non_sweeping_authorisation_response import ApiResponseOfNonSweepingAuthorisationResponse
from yapily.models.non_sweeping_authorisation_request import NonSweepingAuthorisationRequest
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
    api_instance = yapily.VariableRecurringPaymentsApi(api_client)
    non_sweeping_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"modelo-sandbox","callback":"https://display-parameters.com/","controlParameters":{"psuAuthenticationMethods":["SCA_NOT_REQUIRED"],"periodicLimits":[{"totalMaxAmount":{"amount":100,"currency":"GBP"},"frequency":"DAILY","alignment":"CONSENT","maxNumberOfPayments":1}],"maxAmountPerPayment":{"amount":10,"currency":"GBP"},"maxCumulativeAmount":{"amount":100,"currency":"GBP"},"maxCumulativeNumberOfPayments":10},"initiationDetails":{"reference":"Bill Payment","payer":{"name":"John Doe","accountIdentifications":[{"type":"ACCOUNT_NUMBER","identification":"87654321"},{"type":"SORT_CODE","identification":"654321"}]},"payee":{"name":"Thames Water","accountIdentifications":[{"type":"ACCOUNT_NUMBER","identification":"12345678"},{"type":"SORT_CODE","identification":"123456"}]}}} # NonSweepingAuthorisationRequest | 

    try:
        # Create Non-Sweeping Variable Recurring Payment Authorisation
        api_response = await api_instance.create_non_sweeping_authorisation(non_sweeping_authorisation_request)
        print("The response of VariableRecurringPaymentsApi->create_non_sweeping_authorisation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableRecurringPaymentsApi->create_non_sweeping_authorisation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_sweeping_authorisation_request** | [**NonSweepingAuthorisationRequest**](NonSweepingAuthorisationRequest.md)|  | 

### Return type

[**ApiResponseOfNonSweepingAuthorisationResponse**](ApiResponseOfNonSweepingAuthorisationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Error Response |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sweeping_authorisation**
> ApiResponseOfSweepingAuthorisationResponse create_sweeping_authorisation(sweeping_authorisation_request)

Create Sweeping Variable Recurring Payment Authorisation

Used to initiate the authorisation process and direct users to the login screen of their financial Institution in order to give their consent for Sweeping Variable Recurring Payments. The request would return an Authorization URL and an Identifier for the consent created at the Institution. First make sure that the payment feature you wish to execute is supported by the bank by checking the features array in [GET Institution](https://docs.yapily.com/api/#get-institution). <br><br>See [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/redirect/) for more information about this flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li></ul>

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_response_of_sweeping_authorisation_response import ApiResponseOfSweepingAuthorisationResponse
from yapily.models.sweeping_authorisation_request import SweepingAuthorisationRequest
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
    api_instance = yapily.VariableRecurringPaymentsApi(api_client)
    sweeping_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"modelo-sandbox","callback":"https://display-parameters.com/","controlParameters":{"psuAuthenticationMethods":["SCA_NOT_REQUIRED"],"periodicLimits":[{"totalMaxAmount":{"amount":100,"currency":"GBP"},"frequency":"DAILY","alignment":"CONSENT"}],"maxAmountPerPayment":{"amount":10,"currency":"GBP"}},"initiationDetails":{"reference":"Own Account Sweeping","payer":{"name":"John Doe","accountIdentifications":[{"type":"ACCOUNT_NUMBER","identification":"87654321"},{"type":"SORT_CODE","identification":"654321"}]},"payee":{"name":"John Doe","accountIdentifications":[{"type":"ACCOUNT_NUMBER","identification":"12345678"},{"type":"SORT_CODE","identification":"123456"}]}}} # SweepingAuthorisationRequest | 

    try:
        # Create Sweeping Variable Recurring Payment Authorisation
        api_response = await api_instance.create_sweeping_authorisation(sweeping_authorisation_request)
        print("The response of VariableRecurringPaymentsApi->create_sweeping_authorisation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableRecurringPaymentsApi->create_sweeping_authorisation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sweeping_authorisation_request** | [**SweepingAuthorisationRequest**](SweepingAuthorisationRequest.md)|  | 

### Return type

[**ApiResponseOfSweepingAuthorisationResponse**](ApiResponseOfSweepingAuthorisationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Error Response |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vrp_funds_confirmation**
> ApiResponseOfFundsConfirmationResponse create_vrp_funds_confirmation(consent, funds_confirmation_request)

Confirm Funds for Variable Recurring Payment

Used to confirm funds on the Payer account to execute Variable Recurring Payments after obtaining the user's authorisation. <br><br>Features:<ul><li>`VARIABLE_RECURRING_PAYMENT_FUNDS_CONFIRMATION`</li></ul>

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_response_of_funds_confirmation_response import ApiResponseOfFundsConfirmationResponse
from yapily.models.funds_confirmation_request import FundsConfirmationRequest
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
    api_instance = yapily.VariableRecurringPaymentsApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    funds_confirmation_request = {"reference":"Own Account Sweeping","paymentAmount":{"amount":10,"currency":"GBP"}} # FundsConfirmationRequest | 

    try:
        # Confirm Funds for Variable Recurring Payment
        api_response = await api_instance.create_vrp_funds_confirmation(consent, funds_confirmation_request)
        print("The response of VariableRecurringPaymentsApi->create_vrp_funds_confirmation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableRecurringPaymentsApi->create_vrp_funds_confirmation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **funds_confirmation_request** | [**FundsConfirmationRequest**](FundsConfirmationRequest.md)|  | 

### Return type

[**ApiResponseOfFundsConfirmationResponse**](ApiResponseOfFundsConfirmationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Error Response |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vrp_payment**
> ApiResponseOfSubmissionResponse create_vrp_payment(consent, submission_request)

Create Variable Recurring Payment

Used to submit a Variable Recurring Payments transaction after obtaining the user's authorisation. First make sure that the payment feature you wish to execute is supported by the bank by checking the features array in [GET Institution](https://docs.yapily.com/api/#get-institution). <br><br>Features:<ul><li>`CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_SWEEPING`</li><li>`CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT_NONSWEEPING`</li></ul>

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_response_of_submission_response import ApiResponseOfSubmissionResponse
from yapily.models.submission_request import SubmissionRequest
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
    api_instance = yapily.VariableRecurringPaymentsApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
    submission_request = {"paymentIdempotencyId":"234g87t58tgeuo848wudjew489","psuAuthenticationMethod":"SCA_NOT_REQUIRED","paymentAmount":{"amount":10,"currency":"GBP"}} # SubmissionRequest | 

    try:
        # Create Variable Recurring Payment
        api_response = await api_instance.create_vrp_payment(consent, submission_request)
        print("The response of VariableRecurringPaymentsApi->create_vrp_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableRecurringPaymentsApi->create_vrp_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **submission_request** | [**SubmissionRequest**](SubmissionRequest.md)|  | 

### Return type

[**ApiResponseOfSubmissionResponse**](ApiResponseOfSubmissionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Error Response |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sweeping_vrp_consent_by_id**
> ApiResponseOfSweepingAuthorisationResponse get_sweeping_vrp_consent_by_id(consent_id)

Get Sweeping Variable Recurring Payment Consent Details

Get Sweeping Variable Recurring Payments consent details using the consent Id

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_response_of_sweeping_authorisation_response import ApiResponseOfSweepingAuthorisationResponse
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
    api_instance = yapily.VariableRecurringPaymentsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Variable Recurring Payments Consent` to retrieve.

    try:
        # Get Sweeping Variable Recurring Payment Consent Details
        api_response = await api_instance.get_sweeping_vrp_consent_by_id(consent_id)
        print("The response of VariableRecurringPaymentsApi->get_sweeping_vrp_consent_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableRecurringPaymentsApi->get_sweeping_vrp_consent_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Variable Recurring Payments Consent&#x60; to retrieve. | 

### Return type

[**ApiResponseOfSweepingAuthorisationResponse**](ApiResponseOfSweepingAuthorisationResponse.md)

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

# **get_vrp_payment_details**
> ApiResponseOfSubmissionResponse get_vrp_payment_details(payment_id, consent)

Get Variable Recurring Payment Details

Get Variable Recurring Payment details using the Payment Id

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_response_of_submission_response import ApiResponseOfSubmissionResponse
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
    api_instance = yapily.VariableRecurringPaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | __Mandatory__. The Payment Id of the `Variable Recurring Payments` to retrieve.
    consent = 'consent_example' # str | __Mandatory__. The consent token containing the user's authorisation to make the `Variable Recurring Payments` request.

    try:
        # Get Variable Recurring Payment Details
        api_response = await api_instance.get_vrp_payment_details(payment_id, consent)
        print("The response of VariableRecurringPaymentsApi->get_vrp_payment_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableRecurringPaymentsApi->get_vrp_payment_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| __Mandatory__. The Payment Id of the &#x60;Variable Recurring Payments&#x60; to retrieve. | 
 **consent** | **str**| __Mandatory__. The consent token containing the user&#39;s authorisation to make the &#x60;Variable Recurring Payments&#x60; request. | 

### Return type

[**ApiResponseOfSubmissionResponse**](ApiResponseOfSubmissionResponse.md)

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

# **getp_non_sweeping_vrp_consent_by_id**
> ApiResponseOfNonSweepingAuthorisationResponse getp_non_sweeping_vrp_consent_by_id(consent_id)

Get Non-Sweeping Variable Recurring Payment Consent Details

Get Non-Sweeping Variable Recurring Payments consent details using the consent Id

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import yapily
from yapily.models.api_response_of_non_sweeping_authorisation_response import ApiResponseOfNonSweepingAuthorisationResponse
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
    api_instance = yapily.VariableRecurringPaymentsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Variable Recurring Payments Consent` to retrieve.

    try:
        # Get Non-Sweeping Variable Recurring Payment Consent Details
        api_response = await api_instance.getp_non_sweeping_vrp_consent_by_id(consent_id)
        print("The response of VariableRecurringPaymentsApi->getp_non_sweeping_vrp_consent_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableRecurringPaymentsApi->getp_non_sweeping_vrp_consent_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Variable Recurring Payments Consent&#x60; to retrieve. | 

### Return type

[**ApiResponseOfNonSweepingAuthorisationResponse**](ApiResponseOfNonSweepingAuthorisationResponse.md)

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

