# coding: utf-8

# flake8: noqa
"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 2.25.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from yapily.models.account import Account
from yapily.models.account_api_list_response import AccountApiListResponse
from yapily.models.account_authorisation_request import AccountAuthorisationRequest
from yapily.models.account_authorisation_response import AccountAuthorisationResponse
from yapily.models.account_balance import AccountBalance
from yapily.models.account_balance_type import AccountBalanceType
from yapily.models.account_identification import AccountIdentification
from yapily.models.account_identification_response import AccountIdentificationResponse
from yapily.models.account_identification_type import AccountIdentificationType
from yapily.models.account_identification_type_response import AccountIdentificationTypeResponse
from yapily.models.account_info import AccountInfo
from yapily.models.account_name import AccountName
from yapily.models.account_request import AccountRequest
from yapily.models.account_statement import AccountStatement
from yapily.models.account_type import AccountType
from yapily.models.address import Address
from yapily.models.address_details import AddressDetails
from yapily.models.address_response import AddressResponse
from yapily.models.address_type_enum import AddressTypeEnum
from yapily.models.address_type_enum_response import AddressTypeEnumResponse
from yapily.models.amount import Amount
from yapily.models.amount_details_response import AmountDetailsResponse
from yapily.models.api_error import ApiError
from yapily.models.api_error_response import ApiErrorResponse
from yapily.models.api_list_response_of_account_statement import ApiListResponseOfAccountStatement
from yapily.models.api_list_response_of_beneficiary import ApiListResponseOfBeneficiary
from yapily.models.api_list_response_of_category import ApiListResponseOfCategory
from yapily.models.api_list_response_of_consent import ApiListResponseOfConsent
from yapily.models.api_list_response_of_data_constraints import ApiListResponseOfDataConstraints
from yapily.models.api_list_response_of_direct_debit_response import ApiListResponseOfDirectDebitResponse
from yapily.models.api_list_response_of_event_subscription_response import ApiListResponseOfEventSubscriptionResponse
from yapily.models.api_list_response_of_feature_details import ApiListResponseOfFeatureDetails
from yapily.models.api_list_response_of_institution import ApiListResponseOfInstitution
from yapily.models.api_list_response_of_payment_constraints import ApiListResponseOfPaymentConstraints
from yapily.models.api_list_response_of_payment_response import ApiListResponseOfPaymentResponse
from yapily.models.api_list_response_of_real_time_transaction import ApiListResponseOfRealTimeTransaction
from yapily.models.api_list_response_of_real_time_transaction_links import ApiListResponseOfRealTimeTransactionLinks
from yapily.models.api_list_response_of_transaction import ApiListResponseOfTransaction
from yapily.models.api_list_response_of_virtual_account import ApiListResponseOfVirtualAccount
from yapily.models.api_list_response_of_virtual_account_beneficiary import ApiListResponseOfVirtualAccountBeneficiary
from yapily.models.api_list_response_of_virtual_account_client import ApiListResponseOfVirtualAccountClient
from yapily.models.api_list_response_of_virtual_account_payment import ApiListResponseOfVirtualAccountPayment
from yapily.models.api_list_response_of_virtual_account_refund import ApiListResponseOfVirtualAccountRefund
from yapily.models.api_list_response_of_virtual_account_refund_links import ApiListResponseOfVirtualAccountRefundLinks
from yapily.models.api_response_error import ApiResponseError
from yapily.models.api_response_of_account import ApiResponseOfAccount
from yapily.models.api_response_of_account_authorisation_response import ApiResponseOfAccountAuthorisationResponse
from yapily.models.api_response_of_account_statement import ApiResponseOfAccountStatement
from yapily.models.api_response_of_balances import ApiResponseOfBalances
from yapily.models.api_response_of_consent import ApiResponseOfConsent
from yapily.models.api_response_of_consent_delete_response import ApiResponseOfConsentDeleteResponse
from yapily.models.api_response_of_create_hosted_payment_request import ApiResponseOfCreateHostedPaymentRequest
from yapily.models.api_response_of_create_hosted_payment_request_link import ApiResponseOfCreateHostedPaymentRequestLink
from yapily.models.api_response_of_embedded_account_authorisation_response import ApiResponseOfEmbeddedAccountAuthorisationResponse
from yapily.models.api_response_of_event_subscription_delete_response import ApiResponseOfEventSubscriptionDeleteResponse
from yapily.models.api_response_of_event_subscription_response import ApiResponseOfEventSubscriptionResponse
from yapily.models.api_response_of_financial_profile import ApiResponseOfFinancialProfile
from yapily.models.api_response_of_financial_profile_authorisation_response import ApiResponseOfFinancialProfileAuthorisationResponse
from yapily.models.api_response_of_financial_profile_balance_prediction import ApiResponseOfFinancialProfileBalancePrediction
from yapily.models.api_response_of_financial_profile_consent import ApiResponseOfFinancialProfileConsent
from yapily.models.api_response_of_financial_profile_consent_remove_response import ApiResponseOfFinancialProfileConsentRemoveResponse
from yapily.models.api_response_of_funds_confirmation_response import ApiResponseOfFundsConfirmationResponse
from yapily.models.api_response_of_get_hosted_payment_request import ApiResponseOfGetHostedPaymentRequest
from yapily.models.api_response_of_identity import ApiResponseOfIdentity
from yapily.models.api_response_of_non_sweeping_authorisation_response import ApiResponseOfNonSweepingAuthorisationResponse
from yapily.models.api_response_of_payment_authorisation_request_response import ApiResponseOfPaymentAuthorisationRequestResponse
from yapily.models.api_response_of_payment_embedded_authorisation_request_response import ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse
from yapily.models.api_response_of_payment_response import ApiResponseOfPaymentResponse
from yapily.models.api_response_of_payment_responses import ApiResponseOfPaymentResponses
from yapily.models.api_response_of_pre_authorisation_response import ApiResponseOfPreAuthorisationResponse
from yapily.models.api_response_of_submission_response import ApiResponseOfSubmissionResponse
from yapily.models.api_response_of_sweeping_authorisation_response import ApiResponseOfSweepingAuthorisationResponse
from yapily.models.api_response_of_user_delete_response import ApiResponseOfUserDeleteResponse
from yapily.models.api_response_of_virtual_account import ApiResponseOfVirtualAccount
from yapily.models.api_response_of_virtual_account_beneficiary import ApiResponseOfVirtualAccountBeneficiary
from yapily.models.api_response_of_virtual_account_client import ApiResponseOfVirtualAccountClient
from yapily.models.api_response_of_virtual_account_pay_in_details import ApiResponseOfVirtualAccountPayInDetails
from yapily.models.api_response_of_virtual_account_payment import ApiResponseOfVirtualAccountPayment
from yapily.models.api_response_of_virtual_account_refund import ApiResponseOfVirtualAccountRefund
from yapily.models.application import Application
from yapily.models.application_user import ApplicationUser
from yapily.models.authorisation_status import AuthorisationStatus
from yapily.models.balance_prediction_profile import BalancePredictionProfile
from yapily.models.balances import Balances
from yapily.models.beneficiary import Beneficiary
from yapily.models.beneficiary_payee import BeneficiaryPayee
from yapily.models.bulk_payment_authorisation_request import BulkPaymentAuthorisationRequest
from yapily.models.bulk_payment_embedded_authorisation_request import BulkPaymentEmbeddedAuthorisationRequest
from yapily.models.bulk_payment_request import BulkPaymentRequest
from yapily.models.categorisation import Categorisation
from yapily.models.category import Category
from yapily.models.charge_bearer_type import ChargeBearerType
from yapily.models.compliance_data import ComplianceData
from yapily.models.compliance_data_address import ComplianceDataAddress
from yapily.models.compliance_data_business import ComplianceDataBusiness
from yapily.models.compliance_data_individual import ComplianceDataIndividual
from yapily.models.compliance_data_payer import ComplianceDataPayer
from yapily.models.consent import Consent
from yapily.models.consent_auth_code_request import ConsentAuthCodeRequest
from yapily.models.consent_delete_response import ConsentDeleteResponse
from yapily.models.consolidated_account_information import ConsolidatedAccountInformation
from yapily.models.country import Country
from yapily.models.create_hosted_payment_request import CreateHostedPaymentRequest
from yapily.models.create_hosted_payment_request_link import CreateHostedPaymentRequestLink
from yapily.models.credentials_type import CredentialsType
from yapily.models.credit_line import CreditLine
from yapily.models.credit_line_type import CreditLineType
from yapily.models.currency_exchange import CurrencyExchange
from yapily.models.data_constraints_response import DataConstraintsResponse
from yapily.models.delete_status_enum import DeleteStatusEnum
from yapily.models.direct_debit_payee import DirectDebitPayee
from yapily.models.direct_debit_response import DirectDebitResponse
from yapily.models.embedded_account_authorisation_request import EmbeddedAccountAuthorisationRequest
from yapily.models.embedded_account_authorisation_response import EmbeddedAccountAuthorisationResponse
from yapily.models.enriched_balances import EnrichedBalances
from yapily.models.enriched_historic_balance import EnrichedHistoricBalance
from yapily.models.enriched_predicted_balance import EnrichedPredictedBalance
from yapily.models.enriched_transaction import EnrichedTransaction
from yapily.models.enriched_wrapper import EnrichedWrapper
from yapily.models.enrichment import Enrichment
from yapily.models.enrichment_merchant import EnrichmentMerchant
from yapily.models.environment_type import EnvironmentType
from yapily.models.error_details import ErrorDetails
from yapily.models.error_issue import ErrorIssue
from yapily.models.event_subscription_delete_response import EventSubscriptionDeleteResponse
from yapily.models.event_subscription_request import EventSubscriptionRequest
from yapily.models.event_subscription_response import EventSubscriptionResponse
from yapily.models.exchange_rate_information import ExchangeRateInformation
from yapily.models.exchange_rate_information_response import ExchangeRateInformationResponse
from yapily.models.extend_consent_request import ExtendConsentRequest
from yapily.models.feature_details import FeatureDetails
from yapily.models.feature_enum import FeatureEnum
from yapily.models.filter_and_sort import FilterAndSort
from yapily.models.filtered_client_payload_list_account import FilteredClientPayloadListAccount
from yapily.models.filtered_client_payload_list_account_statement import FilteredClientPayloadListAccountStatement
from yapily.models.filtered_client_payload_list_category import FilteredClientPayloadListCategory
from yapily.models.filtered_client_payload_list_consent import FilteredClientPayloadListConsent
from yapily.models.filtered_client_payload_list_direct_debit_response import FilteredClientPayloadListDirectDebitResponse
from yapily.models.filtered_client_payload_list_feature_details import FilteredClientPayloadListFeatureDetails
from yapily.models.filtered_client_payload_list_institution import FilteredClientPayloadListInstitution
from yapily.models.filtered_client_payload_list_payment_response import FilteredClientPayloadListPaymentResponse
from yapily.models.filtered_client_payload_list_transaction import FilteredClientPayloadListTransaction
from yapily.models.financial_profile import FinancialProfile
from yapily.models.frequency_enum_extended import FrequencyEnumExtended
from yapily.models.frequency_request import FrequencyRequest
from yapily.models.frequency_response import FrequencyResponse
from yapily.models.funds_available import FundsAvailable
from yapily.models.funds_confirmation_request import FundsConfirmationRequest
from yapily.models.funds_confirmation_response import FundsConfirmationResponse
from yapily.models.hosted_amount_details import HostedAmountDetails
from yapily.models.hosted_payment import HostedPayment
from yapily.models.hosted_payment_details import HostedPaymentDetails
from yapily.models.hosted_payment_iso_status import HostedPaymentIsoStatus
from yapily.models.hosted_payment_phase import HostedPaymentPhase
from yapily.models.hosted_payment_request_details import HostedPaymentRequestDetails
from yapily.models.hosted_payment_request_details_link import HostedPaymentRequestDetailsLink
from yapily.models.hosted_payment_request_response import HostedPaymentRequestResponse
from yapily.models.hosted_payment_response_details import HostedPaymentResponseDetails
from yapily.models.hosted_payment_status_details import HostedPaymentStatusDetails
from yapily.models.identity import Identity
from yapily.models.identity_address import IdentityAddress
from yapily.models.initiation_details import InitiationDetails
from yapily.models.institution import Institution
from yapily.models.institution_consent import InstitutionConsent
from yapily.models.institution_error import InstitutionError
from yapily.models.institution_identifiers import InstitutionIdentifiers
from yapily.models.institution_identifiers_response import InstitutionIdentifiersResponse
from yapily.models.international_payment_request import InternationalPaymentRequest
from yapily.models.iso_bank_transaction_code import IsoBankTransactionCode
from yapily.models.iso_code_details import IsoCodeDetails
from yapily.models.links import Links
from yapily.models.media import Media
from yapily.models.merchant import Merchant
from yapily.models.model401_virtual_accounts_api_error_response import Model401VirtualAccountsApiErrorResponse
from yapily.models.model403_virtual_accounts_api_error_response import Model403VirtualAccountsApiErrorResponse
from yapily.models.model404_virtual_accounts_api_error_response import Model404VirtualAccountsApiErrorResponse
from yapily.models.model424_virtual_accounts_api_error_response import Model424VirtualAccountsApiErrorResponse
from yapily.models.model500_virtual_accounts_api_error_response import Model500VirtualAccountsApiErrorResponse
from yapily.models.model_schema import ModelSchema
from yapily.models.monitoring_endpoint_status import MonitoringEndpointStatus
from yapily.models.monitoring_feature_status import MonitoringFeatureStatus
from yapily.models.monitoring_status_enum import MonitoringStatusEnum
from yapily.models.multi_authorisation import MultiAuthorisation
from yapily.models.new_application_user import NewApplicationUser
from yapily.models.next import Next
from yapily.models.non_sweeping_authorisation_request import NonSweepingAuthorisationRequest
from yapily.models.non_sweeping_authorisation_response import NonSweepingAuthorisationResponse
from yapily.models.non_sweeping_control_parameters import NonSweepingControlParameters
from yapily.models.non_sweeping_periodic_limits import NonSweepingPeriodicLimits
from yapily.models.notification import Notification
from yapily.models.one_time_token_request import OneTimeTokenRequest
from yapily.models.pagination import Pagination
from yapily.models.payee import Payee
from yapily.models.payee_details import PayeeDetails
from yapily.models.payee_details_response import PayeeDetailsResponse
from yapily.models.payer import Payer
from yapily.models.payer_details import PayerDetails
from yapily.models.payer_details_response import PayerDetailsResponse
from yapily.models.payment_authorisation_request import PaymentAuthorisationRequest
from yapily.models.payment_authorisation_request_response import PaymentAuthorisationRequestResponse
from yapily.models.payment_charge_details import PaymentChargeDetails
from yapily.models.payment_constraints_response import PaymentConstraintsResponse
from yapily.models.payment_context_type import PaymentContextType
from yapily.models.payment_context_type_response import PaymentContextTypeResponse
from yapily.models.payment_embedded_authorisation_request import PaymentEmbeddedAuthorisationRequest
from yapily.models.payment_embedded_authorisation_request_response import PaymentEmbeddedAuthorisationRequestResponse
from yapily.models.payment_iso_status import PaymentIsoStatus
from yapily.models.payment_iso_status_code_enum import PaymentIsoStatusCodeEnum
from yapily.models.payment_pre_authorisation_request import PaymentPreAuthorisationRequest
from yapily.models.payment_request import PaymentRequest
from yapily.models.payment_response import PaymentResponse
from yapily.models.payment_responses import PaymentResponses
from yapily.models.payment_status import PaymentStatus
from yapily.models.payment_status_details import PaymentStatusDetails
from yapily.models.payment_type import PaymentType
from yapily.models.payment_type_of_constraints import PaymentTypeOfConstraints
from yapily.models.payment_type_response import PaymentTypeResponse
from yapily.models.periodic_payment_request import PeriodicPaymentRequest
from yapily.models.pre_authorisation_request import PreAuthorisationRequest
from yapily.models.pre_authorisation_response import PreAuthorisationResponse
from yapily.models.priority_code_enum import PriorityCodeEnum
from yapily.models.profile_consent import ProfileConsent
from yapily.models.proprietary_bank_transaction_code import ProprietaryBankTransactionCode
from yapily.models.rate_type_enum import RateTypeEnum
from yapily.models.raw_request import RawRequest
from yapily.models.raw_response import RawResponse
from yapily.models.real_time_transaction import RealTimeTransaction
from yapily.models.redirect_request import RedirectRequest
from yapily.models.refund_account import RefundAccount
from yapily.models.request_constraints import RequestConstraints
from yapily.models.response_forwarded_data import ResponseForwardedData
from yapily.models.response_list_meta import ResponseListMeta
from yapily.models.response_meta import ResponseMeta
from yapily.models.response_meta_with_count import ResponseMetaWithCount
from yapily.models.sca_method import ScaMethod
from yapily.models.schema_type import SchemaType
from yapily.models.schema_x_yapily_annotations import SchemaXYapilyAnnotations
from yapily.models.schema_x_yapily_validations import SchemaXYapilyValidations
from yapily.models.sort_enum import SortEnum
from yapily.models.statement_reference import StatementReference
from yapily.models.subcategory import Subcategory
from yapily.models.submission_details import SubmissionDetails
from yapily.models.submission_request import SubmissionRequest
from yapily.models.submission_response import SubmissionResponse
from yapily.models.sweeping_authorisation_request import SweepingAuthorisationRequest
from yapily.models.sweeping_authorisation_response import SweepingAuthorisationResponse
from yapily.models.sweeping_control_parameters import SweepingControlParameters
from yapily.models.sweeping_periodic_limits import SweepingPeriodicLimits
from yapily.models.terminated_transaction_stream import TerminatedTransactionStream
from yapily.models.transaction import Transaction
from yapily.models.transaction_balance import TransactionBalance
from yapily.models.transaction_charge_details import TransactionChargeDetails
from yapily.models.transaction_hash import TransactionHash
from yapily.models.transaction_payee_details import TransactionPayeeDetails
from yapily.models.transaction_payee_details_account_identifications_inner import TransactionPayeeDetailsAccountIdentificationsInner
from yapily.models.transaction_payer_details import TransactionPayerDetails
from yapily.models.transaction_schedule import TransactionSchedule
from yapily.models.transaction_status_enum import TransactionStatusEnum
from yapily.models.transaction_stream import TransactionStream
from yapily.models.type import Type
from yapily.models.update_virtual_account_request import UpdateVirtualAccountRequest
from yapily.models.usage_type import UsageType
from yapily.models.user_credentials import UserCredentials
from yapily.models.user_delete_response import UserDeleteResponse
from yapily.models.user_settings import UserSettings
from yapily.models.virtual_account import VirtualAccount
from yapily.models.virtual_account_address import VirtualAccountAddress
from yapily.models.virtual_account_balance import VirtualAccountBalance
from yapily.models.virtual_account_balance_type import VirtualAccountBalanceType
from yapily.models.virtual_account_bank_account import VirtualAccountBankAccount
from yapily.models.virtual_account_beneficiary import VirtualAccountBeneficiary
from yapily.models.virtual_account_beneficiary_account import VirtualAccountBeneficiaryAccount
from yapily.models.virtual_account_beneficiary_address import VirtualAccountBeneficiaryAddress
from yapily.models.virtual_account_beneficiary_request import VirtualAccountBeneficiaryRequest
from yapily.models.virtual_account_business_client import VirtualAccountBusinessClient
from yapily.models.virtual_account_client import VirtualAccountClient
from yapily.models.virtual_account_client_business_type import VirtualAccountClientBusinessType
from yapily.models.virtual_account_client_request import VirtualAccountClientRequest
from yapily.models.virtual_account_client_status import VirtualAccountClientStatus
from yapily.models.virtual_account_client_type import VirtualAccountClientType
from yapily.models.virtual_account_individual_client import VirtualAccountIndividualClient
from yapily.models.virtual_account_kyc_status import VirtualAccountKycStatus
from yapily.models.virtual_account_original_payment import VirtualAccountOriginalPayment
from yapily.models.virtual_account_pay_in_details import VirtualAccountPayInDetails
from yapily.models.virtual_account_pay_out_request import VirtualAccountPayOutRequest
from yapily.models.virtual_account_payment import VirtualAccountPayment
from yapily.models.virtual_account_payment_amount import VirtualAccountPaymentAmount
from yapily.models.virtual_account_payment_destination import VirtualAccountPaymentDestination
from yapily.models.virtual_account_payment_source import VirtualAccountPaymentSource
from yapily.models.virtual_account_refund import VirtualAccountRefund
from yapily.models.virtual_account_refund_request import VirtualAccountRefundRequest
from yapily.models.virtual_account_refund_request_amount import VirtualAccountRefundRequestAmount
from yapily.models.virtual_account_refund_request_beneficiary import VirtualAccountRefundRequestBeneficiary
from yapily.models.virtual_account_request import VirtualAccountRequest
from yapily.models.virtual_account_transfer_destination import VirtualAccountTransferDestination
from yapily.models.virtual_account_transfer_request import VirtualAccountTransferRequest
from yapily.models.virtual_account_transfer_source import VirtualAccountTransferSource
