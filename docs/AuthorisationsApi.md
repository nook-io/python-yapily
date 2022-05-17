# yapily.AuthorisationsApi

All URIs are relative to *https://api.yapily.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_payment_authorisation**](AuthorisationsApi.md#create_bulk_payment_authorisation) | **POST** /bulk-payment-auth-requests | Create Bulk Payment Authorisation
[**create_embedded_bulk_payment_authorisation**](AuthorisationsApi.md#create_embedded_bulk_payment_authorisation) | **POST** /embedded-bulk-payment-auth-requests | Create Embedded Bulk Payment Authorisation
[**create_embedded_payment_authorisation**](AuthorisationsApi.md#create_embedded_payment_authorisation) | **POST** /embedded-payment-auth-requests | Create Embedded Payment Authorisation
[**create_payment_authorisation**](AuthorisationsApi.md#create_payment_authorisation) | **POST** /payment-auth-requests | Create Payment Authorisation
[**create_payment_pre_authorisation_request**](AuthorisationsApi.md#create_payment_pre_authorisation_request) | **POST** /payment-pre-auth-requests | Create Payment Pre-authorisation
[**create_pre_authorisation_request**](AuthorisationsApi.md#create_pre_authorisation_request) | **POST** /pre-auth-requests | Create Pre-authorisation
[**initiate_account_request**](AuthorisationsApi.md#initiate_account_request) | **POST** /account-auth-requests | Create Account Authorisation
[**initiate_embedded_account_request**](AuthorisationsApi.md#initiate_embedded_account_request) | **POST** /embedded-account-auth-requests | Create Embedded Account Authorisation
[**re_authorise_account**](AuthorisationsApi.md#re_authorise_account) | **PATCH** /account-auth-requests | Re-authorise Account Consent
[**update_embedded_account_request**](AuthorisationsApi.md#update_embedded_account_request) | **PUT** /embedded-account-auth-requests/{consentId} | Update Embedded Account Authorisation
[**update_embedded_bulk_payment_authorisation**](AuthorisationsApi.md#update_embedded_bulk_payment_authorisation) | **PUT** /embedded-bulk-payment-auth-requests/{consentId} | Update Embedded Bulk Payment Authorisation
[**update_embedded_payment_authorisation**](AuthorisationsApi.md#update_embedded_payment_authorisation) | **PUT** /embedded-payment-auth-requests/{consentId} | Update Embedded Payment Authorisation
[**update_payment_authorisation**](AuthorisationsApi.md#update_payment_authorisation) | **PUT** /payment-auth-requests | Update Payment Pre-authorisation
[**update_pre_authorise_account_consent**](AuthorisationsApi.md#update_pre_authorise_account_consent) | **PUT** /account-auth-requests | Update Account Pre-authorisation


# **create_bulk_payment_authorisation**
> ApiResponseOfPaymentAuthorisationRequestResponse create_bulk_payment_authorisation(bulk_payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Create Bulk Payment Authorisation

Used to initiate the authorisation process and direct users to the login screen of their financial Institution in order to give their consent for a bulk payment. See [Bulk Payments](https://docs.yapily.com/guides/payments/payment-execution/bulk-payments) for more information. <br><br>See [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/redirect/) for more information about this flow.<br><br>Feature: `INITIATE_BULK_PAYMENT`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    bulk_payment_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"modelo-sandbox","callback":"https://display-parameters.com/","paymentRequest":{"payments":[{"type":"DOMESTIC_PAYMENT","paymentIdempotencyId":"d78fy48uh8f9odhde68dfi38di9","reference":"payment1","amount":{"amount":2.0,"currency":"GBP"},"payee":{"name":"Jane Doe","accountIdentifications":[{"type":"ACCOUNT_NUMBER","identification":"12345678"},{"type":"SORT_CODE","identification":"123456"}]}},{"type":"DOMESTIC_PAYMENT","paymentIdempotencyId":"4279gdy8t63dg73gd8gx87738dg","reference":"payment2","amount":{"amount":5.0,"currency":"GBP"},"payee":{"name":"John Doe","accountIdentifications":[{"type":"ACCOUNT_NUMBER","identification":"87654321"},{"type":"SORT_CODE","identification":"654321"}]}}]}} # BulkPaymentAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Create Bulk Payment Authorisation
        api_response = api_instance.create_bulk_payment_authorisation(bulk_payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->create_bulk_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_payment_authorisation_request** | [**BulkPaymentAuthorisationRequest**](BulkPaymentAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfPaymentAuthorisationRequestResponse**](ApiResponseOfPaymentAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embedded_bulk_payment_authorisation**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse create_embedded_bulk_payment_authorisation(bulk_payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Create Embedded Bulk Payment Authorisation

Used to initiate the embedded authorisation process for an `Institution` that contains the `INITIATE_EMBEDDED_BULK_PAYMENT` feature in order to obtain the the user's authorisation for a bulk payment. See [Bulk Payments](https://docs.yapily.com/guides/payments/payment-execution/bulk-payments) for more information. <br><br> See [Embedded Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/embedded/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_BULK_PAYMENT`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    bulk_payment_embedded_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"fiducia-sandbox","userCredentials":{"id":"VRK1234567890PLUS","password":"password"},"paymentRequest":{"executionDateTime":"2021-10-29T00:00:00Z","payments":[{"type":"DOMESTIC_PAYMENT","paymentIdempotencyId":"e4f913909a3d11eabb370242ac130002","reference":"REFERENCE","amount":{"amount":1.0,"currency":"EUR"},"payer":{"name":"John Doe","accountIdentifications":[{"type":"IBAN","identification":"DE39499999600000005111"}]},"payee":{"name":"Jane Doe","address":{"country":"DE"},"accountIdentifications":[{"type":"IBAN","identification":"DE12345678901234567890"}]}},{"type":"DOMESTIC_PAYMENT","paymentIdempotencyId":"e4f913909a3d11eabb370242ac130002","reference":"REFERENCE","amount":{"amount":1.0,"currency":"EUR"},"payer":{"name":"Jane Doe","accountIdentifications":[{"type":"IBAN","identification":"DE39499999600000005111"}]},"payee":{"name":"John Doe","address":{"country":"DE"},"accountIdentifications":[{"type":"IBAN","identification":"DE12345678900000000000"}]}}]}} # BulkPaymentEmbeddedAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Create Embedded Bulk Payment Authorisation
        api_response = api_instance.create_embedded_bulk_payment_authorisation(bulk_payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->create_embedded_bulk_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_payment_embedded_authorisation_request** | [**BulkPaymentEmbeddedAuthorisationRequest**](BulkPaymentEmbeddedAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embedded_payment_authorisation**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse create_embedded_payment_authorisation(payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Create Embedded Payment Authorisation

Used to initiate the embedded authorisation process for an `Institution` that contains the `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT` feature in order to obtain the the user's authorisation for a payment.<br><br> See [Embedded Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/embedded/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    payment_embedded_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"postbank-sandbox","userCredentials":{"id":"6154057725","password":"PISPWD12"},"paymentRequest":{"type":"DOMESTIC_PAYMENT","paymentIdempotencyId":"e4f913909a3d11eabb370242ac130002","reference":"REFERENCE","amount":{"amount":1.0,"currency":"EUR"},"payer":{"name":"John Doe","accountIdentifications":[{"type":"IBAN","identification":"DE12345678901234567890"}]},"payee":{"name":"Jane Doe","address":{"country":"DE"},"accountIdentifications":[{"type":"IBAN","identification":"DE09876543210987654321"}]}}} # PaymentEmbeddedAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Create Embedded Payment Authorisation
        api_response = api_instance.create_embedded_payment_authorisation(payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->create_embedded_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_embedded_authorisation_request** | [**PaymentEmbeddedAuthorisationRequest**](PaymentEmbeddedAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_authorisation**
> ApiResponseOfPaymentAuthorisationRequestResponse create_payment_authorisation(payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Create Payment Authorisation

Used to initiate the authorisation process and direct users to the login screen of their financial Institution in order to give their consent for a payment. This endpoint is used to initiate all the different payment listed below. Based on the type of payment you wish to make, you may be required to provide specific properties in [PaymentRequest](https://docs.yapily.com/api/#tocS_PaymentRequest). First make sure that the payment feature you wish to execute is supported by the bank by checking the features array in [GET Institution](https://docs.yapily.com/api/#get-institution). <br><br>See [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/redirect/) for more information about this flow.<br><br>Features:<ul><li>`INITIATE_DOMESTIC_PERIODIC_PAYMENT`</li><li>`INITIATE_DOMESTIC_SCHEDULED_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_INSTANT_PAYMENT`</li><li>`INITIATE_DOMESTIC_SINGLE_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_PERIODIC_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT`</li><li>`INITIATE_INTERNATIONAL_SINGLE_PAYMENT`</li></ul>

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    payment_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"bpm-sandbox","callback":"https://display-parameters.com/","paymentRequest":{"paymentIdempotencyId":"234g87t58tgeuo848wudjew489","payer":{"name":"John Doe","accountIdentifications":[{"type":"IBAN","identification":"DE12345678901234567890"}]},"amount":{"amount":1.0,"currency":"EUR"},"reference":"Bill Payment","type":"DOMESTIC_PAYMENT","payee":{"name":"Jane Doe","address":{"country":"BE"},"accountIdentifications":[{"type":"IBAN","identification":"BE12345678901234"}]}}} # PaymentAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Create Payment Authorisation
        api_response = api_instance.create_payment_authorisation(payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->create_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_authorisation_request** | [**PaymentAuthorisationRequest**](PaymentAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfPaymentAuthorisationRequestResponse**](ApiResponseOfPaymentAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_pre_authorisation_request**
> ApiResponseOfAuthorisationRequestResponse create_payment_pre_authorisation_request(payment_pre_authorisation_request, raw=raw)

Create Payment Pre-authorisation

Used to initiate the pre-authorisation process for payments for CbiGlobe `Institution` that contains the `INITIATE_ONETIME_PRE_AUTHORISATION_PAYMENTS` feature to authenticate the user. <br><br>Feature: `INITIATE_ONETIME_PRE_AUTHORISATION_PAYMENTS`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    payment_pre_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"n26","callback":"https://display-parameters.com/","scope":"PIS","reference":"Bill Payment","amount":{"amount":1.0,"currency":"EUR"},"payee":{"name":"Jane Doe","country":"BE","accountIdentifications":[{"type":"IBAN","identification":"BE12345678901234"}]},"payer":{"accountIdentifications":[{"type":"IBAN","identification":"DE12345678901234567890"}]}} # PaymentPreAuthorisationRequest | 
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Create Payment Pre-authorisation
        api_response = api_instance.create_payment_pre_authorisation_request(payment_pre_authorisation_request, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->create_payment_pre_authorisation_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_pre_authorisation_request** | [**PaymentPreAuthorisationRequest**](PaymentPreAuthorisationRequest.md)|  | 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pre_authorisation_request**
> ApiResponseOfAuthorisationRequestResponse create_pre_authorisation_request(pre_authorisation_request, raw=raw)

Create Pre-authorisation

Used to initiate the pre-authorisation process for any `Institution` that contains the `INITIATE_PRE_AUTHORISATION` feature to authenticate the user. <br><br>Feature: `INITIATE_PRE_AUTHORISATION`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    pre_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"n26","callback":"https://display-parameters.com/","scope":"AIS"} # PreAuthorisationRequest | 
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Create Pre-authorisation
        api_response = api_instance.create_pre_authorisation_request(pre_authorisation_request, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->create_pre_authorisation_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pre_authorisation_request** | [**PreAuthorisationRequest**](PreAuthorisationRequest.md)|  | 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_account_request**
> ApiResponseOfAuthorisationRequestResponse initiate_account_request(account_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Create Account Authorisation

Used to initiate the authorisation process and direct users to the login screen of their financial institution in order to give consent to access account data.<br><br>See [Redirect Account Flows](https://docs.yapily.com/guides/financial-data/account-authorisation-flows/redirect/) for more information about this flow.<br><br>Feature: `INITIATE_ACCOUNT_REQUEST`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    account_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"bpm-sandbox","callback":"https://display-parameters.com/","accountRequest":{"accountIdentifiersForBalance":[{"accountId":"account1234567","accountIdentification":{"type":"IBAN","identification":"IT77O0848283352871412938123"}}],"accountIdentifiersForTransaction":[{"accountId":"account1234567","accountIdentification":{"type":"IBAN","identification":"IT77O0848283352871412938123"}}]}} # AccountAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Create Account Authorisation
        api_response = api_instance.initiate_account_request(account_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->initiate_account_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_authorisation_request** | [**AccountAuthorisationRequest**](AccountAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_embedded_account_request**
> ApiResponseOfAuthorisationEmbeddedRequestResponse initiate_embedded_account_request(account_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Create Embedded Account Authorisation

Used to initiate the embedded authorisation process for an `Institution` that contains the `INITIATE_EMBEDDED_ACCOUNT_REQUEST` feature in order to obtain the the user's authorisation to access their account information. <br><br>See [Embedded Account Flows](https://docs.yapily.com/guides/financial-data/account-authorisation-flows/embedded/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_ACCOUNT_REQUEST`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    account_embedded_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"fiducia-sandbox","userCredentials":{"id":"6154057725","password":"PISPWD12"}} # AccountEmbeddedAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Create Embedded Account Authorisation
        api_response = api_instance.initiate_embedded_account_request(account_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->initiate_embedded_account_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_embedded_authorisation_request** | [**AccountEmbeddedAuthorisationRequest**](AccountEmbeddedAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAuthorisationEmbeddedRequestResponse**](ApiResponseOfAuthorisationEmbeddedRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_authorise_account**
> ApiResponseOfAuthorisationRequestResponse re_authorise_account(consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Re-authorise Account Consent

Used to prompt the account holder for continued access to their financial data. This endpoint should be used when a `Consent` that was previously `AUTHORIZED` can no longer be used to retrieve data.<br><br>See [Re-Authorisation](https://docs.yapily.com/guides/financial-data/consents/#re-authorisation) for more information.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Re-authorise Account Consent
        api_response = api_instance.re_authorise_account(consent, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->re_authorise_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_embedded_account_request**
> ApiResponseOfAuthorisationEmbeddedRequestResponse update_embedded_account_request(consent_id, account_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Update Embedded Account Authorisation

Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user where multiple SCA methods are supported by the `Institution`) in order to complete the embedded authorisation to access the user's financial data. <br><br>See [Embedded Account Flows](https://docs.yapily.com/guides/financial-data/account-authorisation-flows/embedded/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_ACCOUNT_REQUEST`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Consent` to update.
account_embedded_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"fiducia-sandbox","scaCode":"6154057725"} # AccountEmbeddedAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Update Embedded Account Authorisation
        api_response = api_instance.update_embedded_account_request(consent_id, account_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_account_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. | 
 **account_embedded_authorisation_request** | [**AccountEmbeddedAuthorisationRequest**](AccountEmbeddedAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAuthorisationEmbeddedRequestResponse**](ApiResponseOfAuthorisationEmbeddedRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_embedded_bulk_payment_authorisation**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse update_embedded_bulk_payment_authorisation(consent_id, bulk_payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Update Embedded Bulk Payment Authorisation

Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user where multiple SCA methods are supported by the `Institution`) in order to complete the embedded authorisation to initiate a bulk payment. See [Bulk Payments](https://docs.yapily.com/guides/payments/payment-execution/bulk-payments) for more information. <br><br>See [Embedded Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/embedded/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_BULK_PAYMENT`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Consent` to update.
bulk_payment_embedded_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"fiducia-sandbox","scaCode":"123456","paymentRequest":{"executionDateTime":"2021-10-29T00:00:00Z","payments":[{"type":"DOMESTIC_PAYMENT","paymentIdempotencyId":"e4f913909a3d11eabb370242ac130002","reference":"REFERENCE","amount":{"amount":1.0,"currency":"EUR"},"payer":{"name":"John Doe","accountIdentifications":[{"type":"IBAN","identification":"DE39499999600000005111"}]},"payee":{"name":"Jane Doe","address":{"country":"DE"},"accountIdentifications":[{"type":"IBAN","identification":"DE12345678901234567890"}]}},{"type":"DOMESTIC_PAYMENT","paymentIdempotencyId":"e4f913909a3d11eabb370242ac130002","reference":"REFERENCE","amount":{"amount":1.0,"currency":"EUR"},"payer":{"name":"Jane Doe","accountIdentifications":[{"type":"IBAN","identification":"DE39499999600000005111"}]},"payee":{"name":"John Doe","address":{"country":"DE"},"accountIdentifications":[{"type":"IBAN","identification":"DE12345678900000000000"}]}}]}} # BulkPaymentEmbeddedAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Update Embedded Bulk Payment Authorisation
        api_response = api_instance.update_embedded_bulk_payment_authorisation(consent_id, bulk_payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_bulk_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. | 
 **bulk_payment_embedded_authorisation_request** | [**BulkPaymentEmbeddedAuthorisationRequest**](BulkPaymentEmbeddedAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_embedded_payment_authorisation**
> ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse update_embedded_payment_authorisation(consent_id, payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Update Embedded Payment Authorisation

Used to pass the SCA Code received from the `Institution` (and the SCA method selected by the user where multiple SCA methods are supported by the `Institution`) in order to complete the embedded authorisation to initiate a payment. <br><br> See [Embedded Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/embedded/) for more information about this flow.<br><br>Feature: `INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    consent_id = 'consent_id_example' # str | __Mandatory__. The consent Id of the `Consent` to update.
payment_embedded_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"postbank-sandbox","scaCode":"325614","paymentRequest":{"type":"DOMESTIC_PAYMENT","paymentIdempotencyId":"e4f913909a3d11eabb370242ac130002","reference":"REFERENCE","amount":{"amount":1.0,"currency":"EUR"},"payer":{"name":"John Doe","accountIdentifications":[{"type":"IBAN","identification":"DE12345678901234567890"}]},"payee":{"name":"Jane Doe","address":{"country":"DE"},"accountIdentifications":[{"type":"IBAN","identification":"DE09876543210987654321"}]}}} # PaymentEmbeddedAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Update Embedded Payment Authorisation
        api_response = api_instance.update_embedded_payment_authorisation(consent_id, payment_embedded_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->update_embedded_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| __Mandatory__. The consent Id of the &#x60;Consent&#x60; to update. | 
 **payment_embedded_authorisation_request** | [**PaymentEmbeddedAuthorisationRequest**](PaymentEmbeddedAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse**](ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_authorisation**
> ApiResponseOfPaymentAuthorisationRequestResponse update_payment_authorisation(consent, payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Update Payment Pre-authorisation

Used to continue the authorisation process and for any `Institution` that contains the `INITIATE_PRE_AUTHORISATION` feature and direct user to the login screen of their financial institution in order to give consent to initiate a payment. <br><br>See [Redirect Payment Flows](https://docs.yapily.com/guides/payments/payment-authorisation-flows/redirect/) for more information about this flow. <br><br>Feature: `INITIATE_PRE_AUTHORISATION`

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
payment_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"n26","paymentRequest":{"paymentIdempotencyId":"234g87t58tgeuo848wudjew489","payer":{"name":"John Doe","accountIdentifications":[{"type":"IBAN","identification":"DE12345678901234567890"}]},"amount":{"amount":1.0,"currency":"EUR"},"reference":"Bill Payment","type":"DOMESTIC_PAYMENT","payee":{"name":"Jane Doe","address":{"country":"BE"},"accountIdentifications":[{"type":"IBAN","identification":"BE12345678901234"}]}}} # PaymentAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Update Payment Pre-authorisation
        api_response = api_instance.update_payment_authorisation(consent, payment_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->update_payment_authorisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **payment_authorisation_request** | [**PaymentAuthorisationRequest**](PaymentAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfPaymentAuthorisationRequestResponse**](ApiResponseOfPaymentAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pre_authorise_account_consent**
> ApiResponseOfAuthorisationRequestResponse update_pre_authorise_account_consent(consent, account_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)

Update Account Pre-authorisation

Used to continue the authorisation process and for any `Institution` that contains the `INITIATE_PRE_AUTHORISATION` feature and direct user to the login screen of their financial institution in order to give consent to access account data. <br><br>See [Redirect Account Flows](https://docs.yapily.com/guides/financial-data/account-authorisation-flows/redirect/) for more information about this flow. <br><br>Features: <ul><li>`INITIATE_ACCOUNT_REQUEST`</li><li>`INITIATE_PRE_AUTHORISATION`</li></ul>

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with yapily.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yapily.AuthorisationsApi(api_client)
    consent = '{consentToken}' # str | __Mandatory__. The `consent-token` containing the user's authorisation to make the request.
account_authorisation_request = {"applicationUserId":"john.doe@company.com","institutionId":"n26"} # AccountAuthorisationRequest | 
psu_id = 'psu_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_corporate_id = 'psu_corporate_id_example' # str | __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
psu_ip_address = 'psu_ip_address_example' # str | __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. (optional)
raw = True # bool | __Optional__. Used to obtain the raw request and response to and from the <code>Institution</code>. (optional)

    try:
        # Update Account Pre-authorisation
        api_response = api_instance.update_pre_authorise_account_consent(consent, account_authorisation_request, psu_id=psu_id, psu_corporate_id=psu_corporate_id, psu_ip_address=psu_ip_address, raw=raw)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthorisationsApi->update_pre_authorise_account_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| __Mandatory__. The &#x60;consent-token&#x60; containing the user&#39;s authorisation to make the request. | 
 **account_authorisation_request** | [**AccountAuthorisationRequest**](AccountAuthorisationRequest.md)|  | 
 **psu_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a personal account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_corporate_id** | **str**| __Conditional__. Represents the user&#39;s login ID for the &#x60;Institution&#x60; to a business account. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **psu_ip_address** | **str**| __Conditional__. The IP address of the PSU. &lt;br&gt;&lt;br&gt;See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required. | [optional] 
 **raw** | **bool**| __Optional__. Used to obtain the raw request and response to and from the &lt;code&gt;Institution&lt;/code&gt;. | [optional] 

### Return type

[**ApiResponseOfAuthorisationRequestResponse**](ApiResponseOfAuthorisationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

