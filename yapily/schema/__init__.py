from __future__ import annotations
import enum
from datetime import datetime, date
from typing import Any, Dict, cast, Type as _Type

import yapily
from pydantic import BaseConfig, BaseModel, ConfigError
from pydantic.main import inherit_config
from pydantic.utils import is_valid_field

# ToDo use the libs version


def create_model_from_dict(
    __model_name: str,
    __model: Any,
    *,
    __config__: _Type[BaseConfig] = None,
    __base__: _Type["Model"] = None,
    __module__: str = __name__,
    __validators__: Dict[str, classmethod] = None,
) -> _Type["Model"]:
    """
    Dynamically create a model.
    :param __model_name: name of the created model
    :param __config__: config class to use for the new model
    :param __base__: base class for the new model to inherit from
    :param __module__: module of the created model
    :param __validators__: a dict of method names and @validator class methods
    :param field_definitions: fields of the model (or extra fields if a base is supplied)
        in the format `<name>=(<type>, <default default>)` or `<name>=<default value>, e.g.
        `foobar=(str, ...)` or `foobar=123`, or, for complex use-cases, in the format
        `<name>=<FieldInfo>`, e.g. `foo=Field(default_factory=datetime.utcnow, alias='bar')`
    """

    if __base__ is not None:
        if __config__ is not None:
            raise ConfigError("to avoid confusion __config__ and __base__ cannot be used together")
    else:
        __base__ = cast(_Type["Model"], BaseModel)

    fields = {}
    annotations = {}

    if hasattr(__model, "allowable_values"):
        return enum.Enum(__model_name, {value: value for value in __model.allowable_values})

    field_definitions = __model.openapi_types

    for f_name, f_def in field_definitions.items():
        if not is_valid_field(f_name):
            print(f"WARNING: fields may not start with an _, ignoring model {__model_name}: attribute {f_name}")

        if "dict" in f_def:
            f_def = f_def.replace("(", "[").replace(")", "]")
        if f_def == "file":
            # FIXME what is the correct python type, see: https://openapi-generator.tech/docs/generators/python/
            f_def = "str"
        annotations[f_name] = f_def
        fields[f_name] = None

    namespace: "DictStrAny" = {"__annotations__": annotations, "__module__": __module__}
    if __validators__:
        namespace.update(__validators__)
    namespace.update(fields)
    if __config__:
        namespace["Config"] = inherit_config(__config__, BaseConfig)

    return type(__model_name, (__base__,), namespace)


"""
# To build these class use this script

from yapily import models

for name, cls in models.__dict__.items():
    if isinstance(cls, type):
        print(f'{name} = create_model_from_dict("{name}", yapily.{name}, __config__=Config)')

for name, cls in models.__dict__.items():
    if isinstance(cls, type) and not hasattr(cls, "allowable_values"):
        print(f'{name}.update_forward_refs()')
"""


class Config(BaseConfig):
    arbitrary_types_allowed = True


Account = create_model_from_dict("Account", yapily.Account, __config__=Config)
AccountApiListResponse = create_model_from_dict("AccountApiListResponse", yapily.AccountApiListResponse, __config__=Config)
AccountAuthorisationRequest = create_model_from_dict("AccountAuthorisationRequest", yapily.AccountAuthorisationRequest, __config__=Config)
AccountBalance = create_model_from_dict("AccountBalance", yapily.AccountBalance, __config__=Config)
AccountBalanceType = create_model_from_dict("AccountBalanceType", yapily.AccountBalanceType, __config__=Config)
AccountEmbeddedAuthorisationRequest = create_model_from_dict("AccountEmbeddedAuthorisationRequest", yapily.AccountEmbeddedAuthorisationRequest, __config__=Config)
AccountIdentification = create_model_from_dict("AccountIdentification", yapily.AccountIdentification, __config__=Config)
AccountIdentificationType = create_model_from_dict("AccountIdentificationType", yapily.AccountIdentificationType, __config__=Config)
AccountInfo = create_model_from_dict("AccountInfo", yapily.AccountInfo, __config__=Config)
AccountName = create_model_from_dict("AccountName", yapily.AccountName, __config__=Config)
AccountRequest = create_model_from_dict("AccountRequest", yapily.AccountRequest, __config__=Config)
AccountStatement = create_model_from_dict("AccountStatement", yapily.AccountStatement, __config__=Config)
AccountType = create_model_from_dict("AccountType", yapily.AccountType, __config__=Config)
Address = create_model_from_dict("Address", yapily.Address, __config__=Config)
AddressDetails = create_model_from_dict("AddressDetails", yapily.AddressDetails, __config__=Config)
AddressTypeEnum = create_model_from_dict("AddressTypeEnum", yapily.AddressTypeEnum, __config__=Config)
Amount = create_model_from_dict("Amount", yapily.Amount, __config__=Config)
ApiError = create_model_from_dict("ApiError", yapily.ApiError, __config__=Config)
ApiListResponseOfAccountStatement = create_model_from_dict("ApiListResponseOfAccountStatement", yapily.ApiListResponseOfAccountStatement, __config__=Config)
ApiListResponseOfBeneficiary = create_model_from_dict("ApiListResponseOfBeneficiary", yapily.ApiListResponseOfBeneficiary, __config__=Config)
ApiListResponseOfCategory = create_model_from_dict("ApiListResponseOfCategory", yapily.ApiListResponseOfCategory, __config__=Config)
ApiListResponseOfConsent = create_model_from_dict("ApiListResponseOfConsent", yapily.ApiListResponseOfConsent, __config__=Config)
ApiListResponseOfDirectDebitResponse = create_model_from_dict("ApiListResponseOfDirectDebitResponse", yapily.ApiListResponseOfDirectDebitResponse, __config__=Config)
ApiListResponseOfFeatureDetails = create_model_from_dict("ApiListResponseOfFeatureDetails", yapily.ApiListResponseOfFeatureDetails, __config__=Config)
ApiListResponseOfInstitution = create_model_from_dict("ApiListResponseOfInstitution", yapily.ApiListResponseOfInstitution, __config__=Config)
ApiListResponseOfPaymentResponse = create_model_from_dict("ApiListResponseOfPaymentResponse", yapily.ApiListResponseOfPaymentResponse, __config__=Config)
ApiListResponseOfTransaction = create_model_from_dict("ApiListResponseOfTransaction", yapily.ApiListResponseOfTransaction, __config__=Config)
ApiResponseError = create_model_from_dict("ApiResponseError", yapily.ApiResponseError, __config__=Config)
ApiResponseOfAccount = create_model_from_dict("ApiResponseOfAccount", yapily.ApiResponseOfAccount, __config__=Config)
ApiResponseOfAccountStatement = create_model_from_dict("ApiResponseOfAccountStatement", yapily.ApiResponseOfAccountStatement, __config__=Config)
ApiResponseOfAuthorisationEmbeddedRequestResponse = create_model_from_dict("ApiResponseOfAuthorisationEmbeddedRequestResponse", yapily.ApiResponseOfAuthorisationEmbeddedRequestResponse, __config__=Config)
ApiResponseOfAuthorisationRequestResponse = create_model_from_dict("ApiResponseOfAuthorisationRequestResponse", yapily.ApiResponseOfAuthorisationRequestResponse, __config__=Config)
ApiResponseOfBalances = create_model_from_dict("ApiResponseOfBalances", yapily.ApiResponseOfBalances, __config__=Config)
ApiResponseOfConsent = create_model_from_dict("ApiResponseOfConsent", yapily.ApiResponseOfConsent, __config__=Config)
ApiResponseOfConsentDeleteResponse = create_model_from_dict("ApiResponseOfConsentDeleteResponse", yapily.ApiResponseOfConsentDeleteResponse, __config__=Config)
ApiResponseOfIdentity = create_model_from_dict("ApiResponseOfIdentity", yapily.ApiResponseOfIdentity, __config__=Config)
ApiResponseOfPaymentAuthorisationRequestResponse = create_model_from_dict("ApiResponseOfPaymentAuthorisationRequestResponse", yapily.ApiResponseOfPaymentAuthorisationRequestResponse, __config__=Config)
ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse = create_model_from_dict("ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse", yapily.ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse, __config__=Config)
ApiResponseOfPaymentResponse = create_model_from_dict("ApiResponseOfPaymentResponse", yapily.ApiResponseOfPaymentResponse, __config__=Config)
ApiResponseOfPaymentResponses = create_model_from_dict("ApiResponseOfPaymentResponses", yapily.ApiResponseOfPaymentResponses, __config__=Config)
ApiResponseOfUserDeleteResponse = create_model_from_dict("ApiResponseOfUserDeleteResponse", yapily.ApiResponseOfUserDeleteResponse, __config__=Config)
Application = create_model_from_dict("Application", yapily.Application, __config__=Config)
ApplicationUser = create_model_from_dict("ApplicationUser", yapily.ApplicationUser, __config__=Config)
AuthorisationEmbeddedRequestResponse = create_model_from_dict("AuthorisationEmbeddedRequestResponse", yapily.AuthorisationEmbeddedRequestResponse, __config__=Config)
AuthorisationRequestResponse = create_model_from_dict("AuthorisationRequestResponse", yapily.AuthorisationRequestResponse, __config__=Config)
AuthorisationStatus = create_model_from_dict("AuthorisationStatus", yapily.AuthorisationStatus, __config__=Config)
Balances = create_model_from_dict("Balances", yapily.Balances, __config__=Config)
Beneficiary = create_model_from_dict("Beneficiary", yapily.Beneficiary, __config__=Config)
BeneficiaryPayee = create_model_from_dict("BeneficiaryPayee", yapily.BeneficiaryPayee, __config__=Config)
BulkPaymentAuthorisationRequest = create_model_from_dict("BulkPaymentAuthorisationRequest", yapily.BulkPaymentAuthorisationRequest, __config__=Config)
BulkPaymentEmbeddedAuthorisationRequest = create_model_from_dict("BulkPaymentEmbeddedAuthorisationRequest", yapily.BulkPaymentEmbeddedAuthorisationRequest, __config__=Config)
BulkPaymentRequest = create_model_from_dict("BulkPaymentRequest", yapily.BulkPaymentRequest, __config__=Config)
Categorisation = create_model_from_dict("Categorisation", yapily.Categorisation, __config__=Config)
Category = create_model_from_dict("Category", yapily.Category, __config__=Config)
ChargeBearerType = create_model_from_dict("ChargeBearerType", yapily.ChargeBearerType, __config__=Config)
Consent = create_model_from_dict("Consent", yapily.Consent, __config__=Config)
ConsentAuthCodeRequest = create_model_from_dict("ConsentAuthCodeRequest", yapily.ConsentAuthCodeRequest, __config__=Config)
ConsentDeleteResponse = create_model_from_dict("ConsentDeleteResponse", yapily.ConsentDeleteResponse, __config__=Config)
Country = create_model_from_dict("Country", yapily.Country, __config__=Config)
CredentialsType = create_model_from_dict("CredentialsType", yapily.CredentialsType, __config__=Config)
CreditLine = create_model_from_dict("CreditLine", yapily.CreditLine, __config__=Config)
CreditLineType = create_model_from_dict("CreditLineType", yapily.CreditLineType, __config__=Config)
CurrencyExchange = create_model_from_dict("CurrencyExchange", yapily.CurrencyExchange, __config__=Config)
DeleteStatusEnum = create_model_from_dict("DeleteStatusEnum", yapily.DeleteStatusEnum, __config__=Config)
DirectDebitPayee = create_model_from_dict("DirectDebitPayee", yapily.DirectDebitPayee, __config__=Config)
DirectDebitResponse = create_model_from_dict("DirectDebitResponse", yapily.DirectDebitResponse, __config__=Config)
EnrichedTransaction = create_model_from_dict("EnrichedTransaction", yapily.EnrichedTransaction, __config__=Config)
EnrichedWrapper = create_model_from_dict("EnrichedWrapper", yapily.EnrichedWrapper, __config__=Config)
Enrichment = create_model_from_dict("Enrichment", yapily.Enrichment, __config__=Config)
EnrichmentMerchant = create_model_from_dict("EnrichmentMerchant", yapily.EnrichmentMerchant, __config__=Config)
EnvironmentType = create_model_from_dict("EnvironmentType", yapily.EnvironmentType, __config__=Config)
ExchangeRateInformation = create_model_from_dict("ExchangeRateInformation", yapily.ExchangeRateInformation, __config__=Config)
ExchangeRateInformationResponse = create_model_from_dict("ExchangeRateInformationResponse", yapily.ExchangeRateInformationResponse, __config__=Config)
FeatureDetails = create_model_from_dict("FeatureDetails", yapily.FeatureDetails, __config__=Config)
FeatureEnum = create_model_from_dict("FeatureEnum", yapily.FeatureEnum, __config__=Config)
FilterAndSort = create_model_from_dict("FilterAndSort", yapily.FilterAndSort, __config__=Config)
FilteredClientPayloadListAccount = create_model_from_dict("FilteredClientPayloadListAccount", yapily.FilteredClientPayloadListAccount, __config__=Config)
FilteredClientPayloadListAccountStatement = create_model_from_dict("FilteredClientPayloadListAccountStatement", yapily.FilteredClientPayloadListAccountStatement, __config__=Config)
FilteredClientPayloadListCategory = create_model_from_dict("FilteredClientPayloadListCategory", yapily.FilteredClientPayloadListCategory, __config__=Config)
FilteredClientPayloadListConsent = create_model_from_dict("FilteredClientPayloadListConsent", yapily.FilteredClientPayloadListConsent, __config__=Config)
FilteredClientPayloadListDirectDebitResponse = create_model_from_dict("FilteredClientPayloadListDirectDebitResponse", yapily.FilteredClientPayloadListDirectDebitResponse, __config__=Config)
FilteredClientPayloadListFeatureDetails = create_model_from_dict("FilteredClientPayloadListFeatureDetails", yapily.FilteredClientPayloadListFeatureDetails, __config__=Config)
FilteredClientPayloadListInstitution = create_model_from_dict("FilteredClientPayloadListInstitution", yapily.FilteredClientPayloadListInstitution, __config__=Config)
FilteredClientPayloadListPaymentResponse = create_model_from_dict("FilteredClientPayloadListPaymentResponse", yapily.FilteredClientPayloadListPaymentResponse, __config__=Config)
FilteredClientPayloadListTransaction = create_model_from_dict("FilteredClientPayloadListTransaction", yapily.FilteredClientPayloadListTransaction, __config__=Config)
FinancialProfile = create_model_from_dict("FinancialProfile", yapily.FinancialProfile, __config__=Config)
FrequencyEnumExtended = create_model_from_dict("FrequencyEnumExtended", yapily.FrequencyEnumExtended, __config__=Config)
FrequencyRequest = create_model_from_dict("FrequencyRequest", yapily.FrequencyRequest, __config__=Config)
FrequencyResponse = create_model_from_dict("FrequencyResponse", yapily.FrequencyResponse, __config__=Config)
Identity = create_model_from_dict("Identity", yapily.Identity, __config__=Config)
IdentityAddress = create_model_from_dict("IdentityAddress", yapily.IdentityAddress, __config__=Config)
Institution = create_model_from_dict("Institution", yapily.Institution, __config__=Config)
InstitutionConsent = create_model_from_dict("InstitutionConsent", yapily.InstitutionConsent, __config__=Config)
InstitutionError = create_model_from_dict("InstitutionError", yapily.InstitutionError, __config__=Config)
InternationalPaymentRequest = create_model_from_dict("InternationalPaymentRequest", yapily.InternationalPaymentRequest, __config__=Config)
IsoBankTransactionCode = create_model_from_dict("IsoBankTransactionCode", yapily.IsoBankTransactionCode, __config__=Config)
IsoCodeDetails = create_model_from_dict("IsoCodeDetails", yapily.IsoCodeDetails, __config__=Config)
Media = create_model_from_dict("Media", yapily.Media, __config__=Config)
Merchant = create_model_from_dict("Merchant", yapily.Merchant, __config__=Config)
MonitoringEndpointStatus = create_model_from_dict("MonitoringEndpointStatus", yapily.MonitoringEndpointStatus, __config__=Config)
MonitoringFeatureStatus = create_model_from_dict("MonitoringFeatureStatus", yapily.MonitoringFeatureStatus, __config__=Config)
MonitoringStatusEnum = create_model_from_dict("MonitoringStatusEnum", yapily.MonitoringStatusEnum, __config__=Config)
MultiAuthorisation = create_model_from_dict("MultiAuthorisation", yapily.MultiAuthorisation, __config__=Config)
NewApplicationUser = create_model_from_dict("NewApplicationUser", yapily.NewApplicationUser, __config__=Config)
Next = create_model_from_dict("Next", yapily.Next, __config__=Config)
OneTimeTokenRequest = create_model_from_dict("OneTimeTokenRequest", yapily.OneTimeTokenRequest, __config__=Config)
Pagination = create_model_from_dict("Pagination", yapily.Pagination, __config__=Config)
Payee = create_model_from_dict("Payee", yapily.Payee, __config__=Config)
PayeeDetails = create_model_from_dict("PayeeDetails", yapily.PayeeDetails, __config__=Config)
Payer = create_model_from_dict("Payer", yapily.Payer, __config__=Config)
PayerDetails = create_model_from_dict("PayerDetails", yapily.PayerDetails, __config__=Config)
PaymentAuthorisationRequest = create_model_from_dict("PaymentAuthorisationRequest", yapily.PaymentAuthorisationRequest, __config__=Config)
PaymentAuthorisationRequestResponse = create_model_from_dict("PaymentAuthorisationRequestResponse", yapily.PaymentAuthorisationRequestResponse, __config__=Config)
PaymentChargeDetails = create_model_from_dict("PaymentChargeDetails", yapily.PaymentChargeDetails, __config__=Config)
PaymentContextType = create_model_from_dict("PaymentContextType", yapily.PaymentContextType, __config__=Config)
PaymentEmbeddedAuthorisationRequest = create_model_from_dict("PaymentEmbeddedAuthorisationRequest", yapily.PaymentEmbeddedAuthorisationRequest, __config__=Config)
PaymentEmbeddedAuthorisationRequestResponse = create_model_from_dict("PaymentEmbeddedAuthorisationRequestResponse", yapily.PaymentEmbeddedAuthorisationRequestResponse, __config__=Config)
PaymentIsoStatus = create_model_from_dict("PaymentIsoStatus", yapily.PaymentIsoStatus, __config__=Config)
PaymentIsoStatusCodeEnum = create_model_from_dict("PaymentIsoStatusCodeEnum", yapily.PaymentIsoStatusCodeEnum, __config__=Config)
PaymentPreAuthorisationRequest = create_model_from_dict("PaymentPreAuthorisationRequest", yapily.PaymentPreAuthorisationRequest, __config__=Config)
PaymentRequest = create_model_from_dict("PaymentRequest", yapily.PaymentRequest, __config__=Config)
PaymentResponse = create_model_from_dict("PaymentResponse", yapily.PaymentResponse, __config__=Config)
PaymentResponses = create_model_from_dict("PaymentResponses", yapily.PaymentResponses, __config__=Config)
PaymentStatus = create_model_from_dict("PaymentStatus", yapily.PaymentStatus, __config__=Config)
PaymentStatusDetails = create_model_from_dict("PaymentStatusDetails", yapily.PaymentStatusDetails, __config__=Config)
PaymentType = create_model_from_dict("PaymentType", yapily.PaymentType, __config__=Config)
PeriodicPaymentRequest = create_model_from_dict("PeriodicPaymentRequest", yapily.PeriodicPaymentRequest, __config__=Config)
PreAuthorisationRequest = create_model_from_dict("PreAuthorisationRequest", yapily.PreAuthorisationRequest, __config__=Config)
PriorityCodeEnum = create_model_from_dict("PriorityCodeEnum", yapily.PriorityCodeEnum, __config__=Config)
ProfileConsent = create_model_from_dict("ProfileConsent", yapily.ProfileConsent, __config__=Config)
ProprietaryBankTransactionCode = create_model_from_dict("ProprietaryBankTransactionCode", yapily.ProprietaryBankTransactionCode, __config__=Config)
RateTypeEnum = create_model_from_dict("RateTypeEnum", yapily.RateTypeEnum, __config__=Config)
RawRequest = create_model_from_dict("RawRequest", yapily.RawRequest, __config__=Config)
RawResponse = create_model_from_dict("RawResponse", yapily.RawResponse, __config__=Config)
RedirectRequest = create_model_from_dict("RedirectRequest", yapily.RedirectRequest, __config__=Config)
RefundAccount = create_model_from_dict("RefundAccount", yapily.RefundAccount, __config__=Config)
ResponseForwardedData = create_model_from_dict("ResponseForwardedData", yapily.ResponseForwardedData, __config__=Config)
ResponseListMeta = create_model_from_dict("ResponseListMeta", yapily.ResponseListMeta, __config__=Config)
ResponseMeta = create_model_from_dict("ResponseMeta", yapily.ResponseMeta, __config__=Config)
ScaMethod = create_model_from_dict("ScaMethod", yapily.ScaMethod, __config__=Config)
SortEnum = create_model_from_dict("SortEnum", yapily.SortEnum, __config__=Config)
StatementReference = create_model_from_dict("StatementReference", yapily.StatementReference, __config__=Config)
Subcategory = create_model_from_dict("Subcategory", yapily.Subcategory, __config__=Config)
TerminatedTransactionStream = create_model_from_dict("TerminatedTransactionStream", yapily.TerminatedTransactionStream, __config__=Config)
Transaction = create_model_from_dict("Transaction", yapily.Transaction, __config__=Config)
TransactionBalance = create_model_from_dict("TransactionBalance", yapily.TransactionBalance, __config__=Config)
TransactionChargeDetails = create_model_from_dict("TransactionChargeDetails", yapily.TransactionChargeDetails, __config__=Config)
TransactionHash = create_model_from_dict("TransactionHash", yapily.TransactionHash, __config__=Config)
TransactionSchedule = create_model_from_dict("TransactionSchedule", yapily.TransactionSchedule, __config__=Config)
TransactionStatusEnum = create_model_from_dict("TransactionStatusEnum", yapily.TransactionStatusEnum, __config__=Config)
TransactionStream = create_model_from_dict("TransactionStream", yapily.TransactionStream, __config__=Config)
Type = create_model_from_dict("Type", yapily.Type, __config__=Config)
UsageType = create_model_from_dict("UsageType", yapily.UsageType, __config__=Config)
UserCredentials = create_model_from_dict("UserCredentials", yapily.UserCredentials, __config__=Config)
UserDeleteResponse = create_model_from_dict("UserDeleteResponse", yapily.UserDeleteResponse, __config__=Config)
Account.update_forward_refs()
AccountApiListResponse.update_forward_refs()
AccountAuthorisationRequest.update_forward_refs()
AccountBalance.update_forward_refs()
AccountEmbeddedAuthorisationRequest.update_forward_refs()
AccountIdentification.update_forward_refs()
AccountInfo.update_forward_refs()
AccountName.update_forward_refs()
AccountRequest.update_forward_refs()
AccountStatement.update_forward_refs()
Address.update_forward_refs()
AddressDetails.update_forward_refs()
Amount.update_forward_refs()
ApiError.update_forward_refs()
ApiListResponseOfAccountStatement.update_forward_refs()
ApiListResponseOfBeneficiary.update_forward_refs()
ApiListResponseOfCategory.update_forward_refs()
ApiListResponseOfConsent.update_forward_refs()
ApiListResponseOfDirectDebitResponse.update_forward_refs()
ApiListResponseOfFeatureDetails.update_forward_refs()
ApiListResponseOfInstitution.update_forward_refs()
ApiListResponseOfPaymentResponse.update_forward_refs()
ApiListResponseOfTransaction.update_forward_refs()
ApiResponseError.update_forward_refs()
ApiResponseOfAccount.update_forward_refs()
ApiResponseOfAccountStatement.update_forward_refs()
ApiResponseOfAuthorisationEmbeddedRequestResponse.update_forward_refs()
ApiResponseOfAuthorisationRequestResponse.update_forward_refs()
ApiResponseOfBalances.update_forward_refs()
ApiResponseOfConsent.update_forward_refs()
ApiResponseOfConsentDeleteResponse.update_forward_refs()
ApiResponseOfIdentity.update_forward_refs()
ApiResponseOfPaymentAuthorisationRequestResponse.update_forward_refs()
ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.update_forward_refs()
ApiResponseOfPaymentResponse.update_forward_refs()
ApiResponseOfPaymentResponses.update_forward_refs()
ApiResponseOfUserDeleteResponse.update_forward_refs()
Application.update_forward_refs()
ApplicationUser.update_forward_refs()
AuthorisationEmbeddedRequestResponse.update_forward_refs()
AuthorisationRequestResponse.update_forward_refs()
Balances.update_forward_refs()
Beneficiary.update_forward_refs()
BeneficiaryPayee.update_forward_refs()
BulkPaymentAuthorisationRequest.update_forward_refs()
BulkPaymentEmbeddedAuthorisationRequest.update_forward_refs()
BulkPaymentRequest.update_forward_refs()
Categorisation.update_forward_refs()
Category.update_forward_refs()
Consent.update_forward_refs()
ConsentAuthCodeRequest.update_forward_refs()
ConsentDeleteResponse.update_forward_refs()
Country.update_forward_refs()
CreditLine.update_forward_refs()
CurrencyExchange.update_forward_refs()
DirectDebitPayee.update_forward_refs()
DirectDebitResponse.update_forward_refs()
EnrichedTransaction.update_forward_refs()
EnrichedWrapper.update_forward_refs()
Enrichment.update_forward_refs()
EnrichmentMerchant.update_forward_refs()
ExchangeRateInformation.update_forward_refs()
ExchangeRateInformationResponse.update_forward_refs()
FeatureDetails.update_forward_refs()
FilterAndSort.update_forward_refs()
FilteredClientPayloadListAccount.update_forward_refs()
FilteredClientPayloadListAccountStatement.update_forward_refs()
FilteredClientPayloadListCategory.update_forward_refs()
FilteredClientPayloadListConsent.update_forward_refs()
FilteredClientPayloadListDirectDebitResponse.update_forward_refs()
FilteredClientPayloadListFeatureDetails.update_forward_refs()
FilteredClientPayloadListInstitution.update_forward_refs()
FilteredClientPayloadListPaymentResponse.update_forward_refs()
FilteredClientPayloadListTransaction.update_forward_refs()
FinancialProfile.update_forward_refs()
FrequencyRequest.update_forward_refs()
FrequencyResponse.update_forward_refs()
Identity.update_forward_refs()
IdentityAddress.update_forward_refs()
Institution.update_forward_refs()
InstitutionConsent.update_forward_refs()
InstitutionError.update_forward_refs()
InternationalPaymentRequest.update_forward_refs()
IsoBankTransactionCode.update_forward_refs()
IsoCodeDetails.update_forward_refs()
Media.update_forward_refs()
Merchant.update_forward_refs()
MonitoringEndpointStatus.update_forward_refs()
MonitoringFeatureStatus.update_forward_refs()
MultiAuthorisation.update_forward_refs()
NewApplicationUser.update_forward_refs()
Next.update_forward_refs()
OneTimeTokenRequest.update_forward_refs()
Pagination.update_forward_refs()
Payee.update_forward_refs()
PayeeDetails.update_forward_refs()
Payer.update_forward_refs()
PayerDetails.update_forward_refs()
PaymentAuthorisationRequest.update_forward_refs()
PaymentAuthorisationRequestResponse.update_forward_refs()
PaymentChargeDetails.update_forward_refs()
PaymentEmbeddedAuthorisationRequest.update_forward_refs()
PaymentEmbeddedAuthorisationRequestResponse.update_forward_refs()
PaymentIsoStatus.update_forward_refs()
PaymentPreAuthorisationRequest.update_forward_refs()
PaymentRequest.update_forward_refs()
PaymentResponse.update_forward_refs()
PaymentResponses.update_forward_refs()
PaymentStatusDetails.update_forward_refs()
PeriodicPaymentRequest.update_forward_refs()
PreAuthorisationRequest.update_forward_refs()
ProfileConsent.update_forward_refs()
ProprietaryBankTransactionCode.update_forward_refs()
RawRequest.update_forward_refs()
RawResponse.update_forward_refs()
RedirectRequest.update_forward_refs()
RefundAccount.update_forward_refs()
ResponseForwardedData.update_forward_refs()
ResponseListMeta.update_forward_refs()
ResponseMeta.update_forward_refs()
ScaMethod.update_forward_refs()
StatementReference.update_forward_refs()
Subcategory.update_forward_refs()
TerminatedTransactionStream.update_forward_refs()
Transaction.update_forward_refs()
TransactionBalance.update_forward_refs()
TransactionChargeDetails.update_forward_refs()
TransactionHash.update_forward_refs()
TransactionSchedule.update_forward_refs()
TransactionStream.update_forward_refs()
UserCredentials.update_forward_refs()
UserDeleteResponse.update_forward_refs()
