# openapi-client
The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/#getting-started) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/guides/applications/institutions/sandbox/) maybe useful.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://docs.yapily.com/support/](https://docs.yapily.com/support/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.yapily.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.yapily.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApplicationApi(api_client)
    
    try:
        # Get Application Self
        api_response = api_instance.get_application_me()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->get_application_me: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.yapily.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationApi* | [**get_application_me**](docs/ApplicationApi.md#get_application_me) | **GET** /me | Get Application Self
*AuthorisationsApi* | [**create_bulk_payment_authorisation**](docs/AuthorisationsApi.md#create_bulk_payment_authorisation) | **POST** /bulk-payment-auth-requests | Create Bulk Payment Authorisation
*AuthorisationsApi* | [**create_embedded_bulk_payment_authorisation**](docs/AuthorisationsApi.md#create_embedded_bulk_payment_authorisation) | **POST** /embedded-bulk-payment-auth-requests | Create Embedded Bulk Payment Authorisation
*AuthorisationsApi* | [**create_embedded_payment_authorisation**](docs/AuthorisationsApi.md#create_embedded_payment_authorisation) | **POST** /embedded-payment-auth-requests | Create Embedded Payment Authorisation
*AuthorisationsApi* | [**create_payment_authorisation**](docs/AuthorisationsApi.md#create_payment_authorisation) | **POST** /payment-auth-requests | Create Payment Authorisation
*AuthorisationsApi* | [**create_payment_pre_authorisation_request**](docs/AuthorisationsApi.md#create_payment_pre_authorisation_request) | **POST** /payment-pre-auth-requests | Create Payment Pre-authorisation
*AuthorisationsApi* | [**create_pre_authorisation_request**](docs/AuthorisationsApi.md#create_pre_authorisation_request) | **POST** /pre-auth-requests | Create Pre-authorisation
*AuthorisationsApi* | [**initiate_account_request**](docs/AuthorisationsApi.md#initiate_account_request) | **POST** /account-auth-requests | Create Account Authorisation
*AuthorisationsApi* | [**initiate_embedded_account_request**](docs/AuthorisationsApi.md#initiate_embedded_account_request) | **POST** /embedded-account-auth-requests | Create Embedded Account Authorisation
*AuthorisationsApi* | [**re_authorise_account**](docs/AuthorisationsApi.md#re_authorise_account) | **PATCH** /account-auth-requests | Re-authorise Account Consent
*AuthorisationsApi* | [**update_embedded_account_request**](docs/AuthorisationsApi.md#update_embedded_account_request) | **PUT** /embedded-account-auth-requests/{consentId} | Update Embedded Account Authorisation
*AuthorisationsApi* | [**update_embedded_bulk_payment_authorisation**](docs/AuthorisationsApi.md#update_embedded_bulk_payment_authorisation) | **PUT** /embedded-bulk-payment-auth-requests/{consentId} | Update Embedded Bulk Payment Authorisation
*AuthorisationsApi* | [**update_embedded_payment_authorisation**](docs/AuthorisationsApi.md#update_embedded_payment_authorisation) | **PUT** /embedded-payment-auth-requests/{consentId} | Update Embedded Payment Authorisation
*AuthorisationsApi* | [**update_payment_authorisation**](docs/AuthorisationsApi.md#update_payment_authorisation) | **PUT** /payment-auth-requests | Update Payment Pre-authorisation
*AuthorisationsApi* | [**update_pre_authorise_account_consent**](docs/AuthorisationsApi.md#update_pre_authorise_account_consent) | **PUT** /account-auth-requests | Update Account Pre-authorisation
*ConsentsApi* | [**create_consent_with_code**](docs/ConsentsApi.md#create_consent_with_code) | **POST** /consent-auth-code | Exchange OAuth2 Code
*ConsentsApi* | [**delete**](docs/ConsentsApi.md#delete) | **DELETE** /consents/{consentId} | Delete Consent
*ConsentsApi* | [**get_consent_by_id**](docs/ConsentsApi.md#get_consent_by_id) | **GET** /consents/{consentId} | Get Consent
*ConsentsApi* | [**get_consent_by_single_access_consent**](docs/ConsentsApi.md#get_consent_by_single_access_consent) | **POST** /consent-one-time-token | Exchange One Time Token
*ConsentsApi* | [**get_consents**](docs/ConsentsApi.md#get_consents) | **GET** /consents | Get Consents
*FinancialDataApi* | [**get_account**](docs/FinancialDataApi.md#get_account) | **GET** /accounts/{accountId} | Get Account
*FinancialDataApi* | [**get_account_balances**](docs/FinancialDataApi.md#get_account_balances) | **GET** /accounts/{accountId}/balances | Get Account Balances
*FinancialDataApi* | [**get_account_direct_debits**](docs/FinancialDataApi.md#get_account_direct_debits) | **GET** /accounts/{accountId}/direct-debits | Get Account Direct Debits
*FinancialDataApi* | [**get_account_periodic_payments**](docs/FinancialDataApi.md#get_account_periodic_payments) | **GET** /accounts/{accountId}/periodic-payments | Get Account Periodic Payments
*FinancialDataApi* | [**get_account_scheduled_payments**](docs/FinancialDataApi.md#get_account_scheduled_payments) | **GET** /accounts/{accountId}/scheduled-payments | Get Account Scheduled Payments
*FinancialDataApi* | [**get_accounts**](docs/FinancialDataApi.md#get_accounts) | **GET** /accounts | Get Accounts
*FinancialDataApi* | [**get_beneficiaries**](docs/FinancialDataApi.md#get_beneficiaries) | **GET** /accounts/{accountId}/beneficiaries | Get Account Beneficiaries
*FinancialDataApi* | [**get_categories**](docs/FinancialDataApi.md#get_categories) | **GET** /categories/{country} | Get Categories
*FinancialDataApi* | [**get_identity**](docs/FinancialDataApi.md#get_identity) | **GET** /identity | Get Identity
*FinancialDataApi* | [**get_statement**](docs/FinancialDataApi.md#get_statement) | **GET** /accounts/{accountId}/statements/{statementId} | Get Account Statement
*FinancialDataApi* | [**get_statement_file**](docs/FinancialDataApi.md#get_statement_file) | **GET** /accounts/{accountId}/statements/{statementId}/file | Get Account Statement File
*FinancialDataApi* | [**get_statements**](docs/FinancialDataApi.md#get_statements) | **GET** /accounts/{accountId}/statements | Get Account Statements
*FinancialDataApi* | [**get_transactions**](docs/FinancialDataApi.md#get_transactions) | **GET** /accounts/{accountId}/transactions | Get Account Transactions
*FinancialProfileApi* | [**create_profile_consent**](docs/FinancialProfileApi.md#create_profile_consent) | **POST** /users/{userUuid}/profile/consents | Create Profile Consent
*FinancialProfileApi* | [**delete_profile_consent**](docs/FinancialProfileApi.md#delete_profile_consent) | **DELETE** /users/{userUuid}/profile/consents/{profileConsentId} | Delete Profile Consent
*FinancialProfileApi* | [**get_profile_consent**](docs/FinancialProfileApi.md#get_profile_consent) | **GET** /users/{userUuid}/profile/consents/{profileConsentId} | Get Profile Consent
*FinancialProfileApi* | [**get_user_profile**](docs/FinancialProfileApi.md#get_user_profile) | **GET** /users/{userUuid}/profile | Get User Profile
*InstitutionsApi* | [**get_feature_details**](docs/InstitutionsApi.md#get_feature_details) | **GET** /features | Get Features
*InstitutionsApi* | [**get_institution**](docs/InstitutionsApi.md#get_institution) | **GET** /institutions/{institutionId} | Get Institution
*InstitutionsApi* | [**get_institutions**](docs/InstitutionsApi.md#get_institutions) | **GET** /institutions | Get Institutions
*PaymentsApi* | [**create_bulk_payment**](docs/PaymentsApi.md#create_bulk_payment) | **POST** /bulk-payments | Create Bulk Payment
*PaymentsApi* | [**create_payment**](docs/PaymentsApi.md#create_payment) | **POST** /payments | Create Payment
*PaymentsApi* | [**get_payments**](docs/PaymentsApi.md#get_payments) | **GET** /payments/{paymentId}/details | Get Payment Details
*UsersApi* | [**add_user**](docs/UsersApi.md#add_user) | **POST** /users | Create User
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /users/{userUuid} | Delete User
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{userUuid} | Get User
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | Get Users


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountApiListResponse](docs/AccountApiListResponse.md)
 - [AccountAuthorisationRequest](docs/AccountAuthorisationRequest.md)
 - [AccountBalance](docs/AccountBalance.md)
 - [AccountBalanceType](docs/AccountBalanceType.md)
 - [AccountEmbeddedAuthorisationRequest](docs/AccountEmbeddedAuthorisationRequest.md)
 - [AccountIdentification](docs/AccountIdentification.md)
 - [AccountIdentificationType](docs/AccountIdentificationType.md)
 - [AccountInfo](docs/AccountInfo.md)
 - [AccountName](docs/AccountName.md)
 - [AccountRequest](docs/AccountRequest.md)
 - [AccountStatement](docs/AccountStatement.md)
 - [AccountType](docs/AccountType.md)
 - [Address](docs/Address.md)
 - [AddressDetails](docs/AddressDetails.md)
 - [AddressTypeEnum](docs/AddressTypeEnum.md)
 - [Amount](docs/Amount.md)
 - [ApiError](docs/ApiError.md)
 - [ApiListResponseOfAccountStatement](docs/ApiListResponseOfAccountStatement.md)
 - [ApiListResponseOfBeneficiary](docs/ApiListResponseOfBeneficiary.md)
 - [ApiListResponseOfCategory](docs/ApiListResponseOfCategory.md)
 - [ApiListResponseOfConsent](docs/ApiListResponseOfConsent.md)
 - [ApiListResponseOfDirectDebitResponse](docs/ApiListResponseOfDirectDebitResponse.md)
 - [ApiListResponseOfFeatureDetails](docs/ApiListResponseOfFeatureDetails.md)
 - [ApiListResponseOfInstitution](docs/ApiListResponseOfInstitution.md)
 - [ApiListResponseOfPaymentResponse](docs/ApiListResponseOfPaymentResponse.md)
 - [ApiListResponseOfTransaction](docs/ApiListResponseOfTransaction.md)
 - [ApiResponseError](docs/ApiResponseError.md)
 - [ApiResponseOfAccount](docs/ApiResponseOfAccount.md)
 - [ApiResponseOfAccountStatement](docs/ApiResponseOfAccountStatement.md)
 - [ApiResponseOfAuthorisationEmbeddedRequestResponse](docs/ApiResponseOfAuthorisationEmbeddedRequestResponse.md)
 - [ApiResponseOfAuthorisationRequestResponse](docs/ApiResponseOfAuthorisationRequestResponse.md)
 - [ApiResponseOfBalances](docs/ApiResponseOfBalances.md)
 - [ApiResponseOfConsent](docs/ApiResponseOfConsent.md)
 - [ApiResponseOfConsentDeleteResponse](docs/ApiResponseOfConsentDeleteResponse.md)
 - [ApiResponseOfIdentity](docs/ApiResponseOfIdentity.md)
 - [ApiResponseOfPaymentAuthorisationRequestResponse](docs/ApiResponseOfPaymentAuthorisationRequestResponse.md)
 - [ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse](docs/ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.md)
 - [ApiResponseOfPaymentResponse](docs/ApiResponseOfPaymentResponse.md)
 - [ApiResponseOfPaymentResponses](docs/ApiResponseOfPaymentResponses.md)
 - [ApiResponseOfUserDeleteResponse](docs/ApiResponseOfUserDeleteResponse.md)
 - [Application](docs/Application.md)
 - [ApplicationUser](docs/ApplicationUser.md)
 - [AuthorisationEmbeddedRequestResponse](docs/AuthorisationEmbeddedRequestResponse.md)
 - [AuthorisationRequestResponse](docs/AuthorisationRequestResponse.md)
 - [AuthorisationStatus](docs/AuthorisationStatus.md)
 - [Balances](docs/Balances.md)
 - [Beneficiary](docs/Beneficiary.md)
 - [BeneficiaryPayee](docs/BeneficiaryPayee.md)
 - [BulkPaymentAuthorisationRequest](docs/BulkPaymentAuthorisationRequest.md)
 - [BulkPaymentEmbeddedAuthorisationRequest](docs/BulkPaymentEmbeddedAuthorisationRequest.md)
 - [BulkPaymentRequest](docs/BulkPaymentRequest.md)
 - [Categorisation](docs/Categorisation.md)
 - [Category](docs/Category.md)
 - [ChargeBearerType](docs/ChargeBearerType.md)
 - [Consent](docs/Consent.md)
 - [ConsentAuthCodeRequest](docs/ConsentAuthCodeRequest.md)
 - [ConsentDeleteResponse](docs/ConsentDeleteResponse.md)
 - [Country](docs/Country.md)
 - [CredentialsType](docs/CredentialsType.md)
 - [CreditLine](docs/CreditLine.md)
 - [CreditLineType](docs/CreditLineType.md)
 - [CurrencyExchange](docs/CurrencyExchange.md)
 - [DeleteStatusEnum](docs/DeleteStatusEnum.md)
 - [DirectDebitPayee](docs/DirectDebitPayee.md)
 - [DirectDebitResponse](docs/DirectDebitResponse.md)
 - [EnrichedTransaction](docs/EnrichedTransaction.md)
 - [EnrichedWrapper](docs/EnrichedWrapper.md)
 - [Enrichment](docs/Enrichment.md)
 - [EnrichmentMerchant](docs/EnrichmentMerchant.md)
 - [EnvironmentType](docs/EnvironmentType.md)
 - [ExchangeRateInformation](docs/ExchangeRateInformation.md)
 - [ExchangeRateInformationResponse](docs/ExchangeRateInformationResponse.md)
 - [FeatureDetails](docs/FeatureDetails.md)
 - [FeatureEnum](docs/FeatureEnum.md)
 - [FilterAndSort](docs/FilterAndSort.md)
 - [FilteredClientPayloadListAccount](docs/FilteredClientPayloadListAccount.md)
 - [FilteredClientPayloadListAccountStatement](docs/FilteredClientPayloadListAccountStatement.md)
 - [FilteredClientPayloadListCategory](docs/FilteredClientPayloadListCategory.md)
 - [FilteredClientPayloadListConsent](docs/FilteredClientPayloadListConsent.md)
 - [FilteredClientPayloadListDirectDebitResponse](docs/FilteredClientPayloadListDirectDebitResponse.md)
 - [FilteredClientPayloadListFeatureDetails](docs/FilteredClientPayloadListFeatureDetails.md)
 - [FilteredClientPayloadListInstitution](docs/FilteredClientPayloadListInstitution.md)
 - [FilteredClientPayloadListPaymentResponse](docs/FilteredClientPayloadListPaymentResponse.md)
 - [FilteredClientPayloadListTransaction](docs/FilteredClientPayloadListTransaction.md)
 - [FinancialProfile](docs/FinancialProfile.md)
 - [FrequencyEnumExtended](docs/FrequencyEnumExtended.md)
 - [FrequencyRequest](docs/FrequencyRequest.md)
 - [FrequencyResponse](docs/FrequencyResponse.md)
 - [Identity](docs/Identity.md)
 - [IdentityAddress](docs/IdentityAddress.md)
 - [Institution](docs/Institution.md)
 - [InstitutionConsent](docs/InstitutionConsent.md)
 - [InstitutionError](docs/InstitutionError.md)
 - [InternationalPaymentRequest](docs/InternationalPaymentRequest.md)
 - [IsoBankTransactionCode](docs/IsoBankTransactionCode.md)
 - [IsoCodeDetails](docs/IsoCodeDetails.md)
 - [Media](docs/Media.md)
 - [Merchant](docs/Merchant.md)
 - [MonitoringEndpointStatus](docs/MonitoringEndpointStatus.md)
 - [MonitoringFeatureStatus](docs/MonitoringFeatureStatus.md)
 - [MonitoringStatusEnum](docs/MonitoringStatusEnum.md)
 - [MultiAuthorisation](docs/MultiAuthorisation.md)
 - [NewApplicationUser](docs/NewApplicationUser.md)
 - [Next](docs/Next.md)
 - [OneTimeTokenRequest](docs/OneTimeTokenRequest.md)
 - [Pagination](docs/Pagination.md)
 - [Payee](docs/Payee.md)
 - [PayeeDetails](docs/PayeeDetails.md)
 - [Payer](docs/Payer.md)
 - [PayerDetails](docs/PayerDetails.md)
 - [PaymentAuthorisationRequest](docs/PaymentAuthorisationRequest.md)
 - [PaymentAuthorisationRequestResponse](docs/PaymentAuthorisationRequestResponse.md)
 - [PaymentChargeDetails](docs/PaymentChargeDetails.md)
 - [PaymentContextType](docs/PaymentContextType.md)
 - [PaymentEmbeddedAuthorisationRequest](docs/PaymentEmbeddedAuthorisationRequest.md)
 - [PaymentEmbeddedAuthorisationRequestResponse](docs/PaymentEmbeddedAuthorisationRequestResponse.md)
 - [PaymentIsoStatus](docs/PaymentIsoStatus.md)
 - [PaymentIsoStatusCodeEnum](docs/PaymentIsoStatusCodeEnum.md)
 - [PaymentPreAuthorisationRequest](docs/PaymentPreAuthorisationRequest.md)
 - [PaymentRequest](docs/PaymentRequest.md)
 - [PaymentResponse](docs/PaymentResponse.md)
 - [PaymentResponses](docs/PaymentResponses.md)
 - [PaymentStatus](docs/PaymentStatus.md)
 - [PaymentStatusDetails](docs/PaymentStatusDetails.md)
 - [PaymentType](docs/PaymentType.md)
 - [PeriodicPaymentRequest](docs/PeriodicPaymentRequest.md)
 - [PreAuthorisationRequest](docs/PreAuthorisationRequest.md)
 - [PriorityCodeEnum](docs/PriorityCodeEnum.md)
 - [ProfileConsent](docs/ProfileConsent.md)
 - [ProprietaryBankTransactionCode](docs/ProprietaryBankTransactionCode.md)
 - [RateTypeEnum](docs/RateTypeEnum.md)
 - [RawRequest](docs/RawRequest.md)
 - [RawResponse](docs/RawResponse.md)
 - [RedirectRequest](docs/RedirectRequest.md)
 - [RefundAccount](docs/RefundAccount.md)
 - [ResponseForwardedData](docs/ResponseForwardedData.md)
 - [ResponseListMeta](docs/ResponseListMeta.md)
 - [ResponseMeta](docs/ResponseMeta.md)
 - [ScaMethod](docs/ScaMethod.md)
 - [SortEnum](docs/SortEnum.md)
 - [StatementReference](docs/StatementReference.md)
 - [Subcategory](docs/Subcategory.md)
 - [TerminatedTransactionStream](docs/TerminatedTransactionStream.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionBalance](docs/TransactionBalance.md)
 - [TransactionChargeDetails](docs/TransactionChargeDetails.md)
 - [TransactionHash](docs/TransactionHash.md)
 - [TransactionSchedule](docs/TransactionSchedule.md)
 - [TransactionStatusEnum](docs/TransactionStatusEnum.md)
 - [TransactionStream](docs/TransactionStream.md)
 - [Type](docs/Type.md)
 - [UsageType](docs/UsageType.md)
 - [UserCredentials](docs/UserCredentials.md)
 - [UserDeleteResponse](docs/UserDeleteResponse.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

support@yapily.com


