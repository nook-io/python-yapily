from __future__ import annotations

from datetime import datetime, date
from typing import Any, Dict, cast, Type as _Type

import yapily
from pydantic import BaseConfig, BaseModel, ConfigError
from pydantic.main import inherit_config
from pydantic.utils import is_valid_field

# ToDo use the libs version


def create_model_from_dict(
    __model_name: str,
    *,
    __config__: _Type[BaseConfig] = None,
    __base__: _Type["Model"] = None,
    __module__: str = __name__,
    __validators__: Dict[str, classmethod] = None,
    **field_definitions: Any,
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
        print(f'{name} = create_model_from_dict("{name}", __config__=Config, **yapily.{name}.openapi_types)')

for name, cls in models.__dict__.items():
    if isinstance(cls, type):
        print(f'{name}.update_forward_refs()')
"""


class Config(BaseConfig):
    arbitrary_types_allowed = True


Account = create_model_from_dict("Account", __config__=Config, **yapily.Account.openapi_types)
AccountApiListResponse = create_model_from_dict("AccountApiListResponse", __config__=Config, **yapily.AccountApiListResponse.openapi_types)
AccountAuthorisationRequest = create_model_from_dict("AccountAuthorisationRequest", __config__=Config, **yapily.AccountAuthorisationRequest.openapi_types)
AccountBalance = create_model_from_dict("AccountBalance", __config__=Config, **yapily.AccountBalance.openapi_types)
AccountBalanceType = create_model_from_dict("AccountBalanceType", __config__=Config, **yapily.AccountBalanceType.openapi_types)
AccountEmbeddedAuthorisationRequest = create_model_from_dict("AccountEmbeddedAuthorisationRequest", __config__=Config, **yapily.AccountEmbeddedAuthorisationRequest.openapi_types)
AccountIdentification = create_model_from_dict("AccountIdentification", __config__=Config, **yapily.AccountIdentification.openapi_types)
AccountIdentificationType = create_model_from_dict("AccountIdentificationType", __config__=Config, **yapily.AccountIdentificationType.openapi_types)
AccountInfo = create_model_from_dict("AccountInfo", __config__=Config, **yapily.AccountInfo.openapi_types)
AccountName = create_model_from_dict("AccountName", __config__=Config, **yapily.AccountName.openapi_types)
AccountRequest = create_model_from_dict("AccountRequest", __config__=Config, **yapily.AccountRequest.openapi_types)
AccountStatement = create_model_from_dict("AccountStatement", __config__=Config, **yapily.AccountStatement.openapi_types)
AccountType = create_model_from_dict("AccountType", __config__=Config, **yapily.AccountType.openapi_types)
Address = create_model_from_dict("Address", __config__=Config, **yapily.Address.openapi_types)
AddressDetails = create_model_from_dict("AddressDetails", __config__=Config, **yapily.AddressDetails.openapi_types)
AddressTypeEnum = create_model_from_dict("AddressTypeEnum", __config__=Config, **yapily.AddressTypeEnum.openapi_types)
Amount = create_model_from_dict("Amount", __config__=Config, **yapily.Amount.openapi_types)
ApiError = create_model_from_dict("ApiError", __config__=Config, **yapily.ApiError.openapi_types)
ApiListResponseOfAccountStatement = create_model_from_dict("ApiListResponseOfAccountStatement", __config__=Config, **yapily.ApiListResponseOfAccountStatement.openapi_types)
ApiListResponseOfBeneficiary = create_model_from_dict("ApiListResponseOfBeneficiary", __config__=Config, **yapily.ApiListResponseOfBeneficiary.openapi_types)
ApiListResponseOfCategory = create_model_from_dict("ApiListResponseOfCategory", __config__=Config, **yapily.ApiListResponseOfCategory.openapi_types)
ApiListResponseOfConsent = create_model_from_dict("ApiListResponseOfConsent", __config__=Config, **yapily.ApiListResponseOfConsent.openapi_types)
ApiListResponseOfDirectDebitResponse = create_model_from_dict("ApiListResponseOfDirectDebitResponse", __config__=Config, **yapily.ApiListResponseOfDirectDebitResponse.openapi_types)
ApiListResponseOfFeatureDetails = create_model_from_dict("ApiListResponseOfFeatureDetails", __config__=Config, **yapily.ApiListResponseOfFeatureDetails.openapi_types)
ApiListResponseOfInstitution = create_model_from_dict("ApiListResponseOfInstitution", __config__=Config, **yapily.ApiListResponseOfInstitution.openapi_types)
ApiListResponseOfPaymentResponse = create_model_from_dict("ApiListResponseOfPaymentResponse", __config__=Config, **yapily.ApiListResponseOfPaymentResponse.openapi_types)
ApiListResponseOfTransaction = create_model_from_dict("ApiListResponseOfTransaction", __config__=Config, **yapily.ApiListResponseOfTransaction.openapi_types)
ApiResponseError = create_model_from_dict("ApiResponseError", __config__=Config, **yapily.ApiResponseError.openapi_types)
ApiResponseOfAccount = create_model_from_dict("ApiResponseOfAccount", __config__=Config, **yapily.ApiResponseOfAccount.openapi_types)
ApiResponseOfAccountStatement = create_model_from_dict("ApiResponseOfAccountStatement", __config__=Config, **yapily.ApiResponseOfAccountStatement.openapi_types)
ApiResponseOfAuthorisationEmbeddedRequestResponse = create_model_from_dict("ApiResponseOfAuthorisationEmbeddedRequestResponse", __config__=Config, **yapily.ApiResponseOfAuthorisationEmbeddedRequestResponse.openapi_types)
ApiResponseOfAuthorisationRequestResponse = create_model_from_dict("ApiResponseOfAuthorisationRequestResponse", __config__=Config, **yapily.ApiResponseOfAuthorisationRequestResponse.openapi_types)
ApiResponseOfBalances = create_model_from_dict("ApiResponseOfBalances", __config__=Config, **yapily.ApiResponseOfBalances.openapi_types)
ApiResponseOfConsent = create_model_from_dict("ApiResponseOfConsent", __config__=Config, **yapily.ApiResponseOfConsent.openapi_types)
ApiResponseOfConsentDeleteResponse = create_model_from_dict("ApiResponseOfConsentDeleteResponse", __config__=Config, **yapily.ApiResponseOfConsentDeleteResponse.openapi_types)
ApiResponseOfIdentity = create_model_from_dict("ApiResponseOfIdentity", __config__=Config, **yapily.ApiResponseOfIdentity.openapi_types)
ApiResponseOfPaymentAuthorisationRequestResponse = create_model_from_dict("ApiResponseOfPaymentAuthorisationRequestResponse", __config__=Config, **yapily.ApiResponseOfPaymentAuthorisationRequestResponse.openapi_types)
ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse = create_model_from_dict("ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse", __config__=Config, **yapily.ApiResponseOfPaymentEmbeddedAuthorisationRequestResponse.openapi_types)
ApiResponseOfPaymentResponse = create_model_from_dict("ApiResponseOfPaymentResponse", __config__=Config, **yapily.ApiResponseOfPaymentResponse.openapi_types)
ApiResponseOfPaymentResponses = create_model_from_dict("ApiResponseOfPaymentResponses", __config__=Config, **yapily.ApiResponseOfPaymentResponses.openapi_types)
ApiResponseOfUserDeleteResponse = create_model_from_dict("ApiResponseOfUserDeleteResponse", __config__=Config, **yapily.ApiResponseOfUserDeleteResponse.openapi_types)
Application = create_model_from_dict("Application", __config__=Config, **yapily.Application.openapi_types)
ApplicationUser = create_model_from_dict("ApplicationUser", __config__=Config, **yapily.ApplicationUser.openapi_types)
AuthorisationEmbeddedRequestResponse = create_model_from_dict("AuthorisationEmbeddedRequestResponse", __config__=Config, **yapily.AuthorisationEmbeddedRequestResponse.openapi_types)
AuthorisationRequestResponse = create_model_from_dict("AuthorisationRequestResponse", __config__=Config, **yapily.AuthorisationRequestResponse.openapi_types)
AuthorisationStatus = create_model_from_dict("AuthorisationStatus", __config__=Config, **yapily.AuthorisationStatus.openapi_types)
Balances = create_model_from_dict("Balances", __config__=Config, **yapily.Balances.openapi_types)
Beneficiary = create_model_from_dict("Beneficiary", __config__=Config, **yapily.Beneficiary.openapi_types)
BeneficiaryPayee = create_model_from_dict("BeneficiaryPayee", __config__=Config, **yapily.BeneficiaryPayee.openapi_types)
BulkPaymentAuthorisationRequest = create_model_from_dict("BulkPaymentAuthorisationRequest", __config__=Config, **yapily.BulkPaymentAuthorisationRequest.openapi_types)
BulkPaymentEmbeddedAuthorisationRequest = create_model_from_dict("BulkPaymentEmbeddedAuthorisationRequest", __config__=Config, **yapily.BulkPaymentEmbeddedAuthorisationRequest.openapi_types)
BulkPaymentRequest = create_model_from_dict("BulkPaymentRequest", __config__=Config, **yapily.BulkPaymentRequest.openapi_types)
Categorisation = create_model_from_dict("Categorisation", __config__=Config, **yapily.Categorisation.openapi_types)
Category = create_model_from_dict("Category", __config__=Config, **yapily.Category.openapi_types)
ChargeBearerType = create_model_from_dict("ChargeBearerType", __config__=Config, **yapily.ChargeBearerType.openapi_types)
Consent = create_model_from_dict("Consent", __config__=Config, **yapily.Consent.openapi_types)
ConsentAuthCodeRequest = create_model_from_dict("ConsentAuthCodeRequest", __config__=Config, **yapily.ConsentAuthCodeRequest.openapi_types)
ConsentDeleteResponse = create_model_from_dict("ConsentDeleteResponse", __config__=Config, **yapily.ConsentDeleteResponse.openapi_types)
Country = create_model_from_dict("Country", __config__=Config, **yapily.Country.openapi_types)
CredentialsType = create_model_from_dict("CredentialsType", __config__=Config, **yapily.CredentialsType.openapi_types)
CreditLine = create_model_from_dict("CreditLine", __config__=Config, **yapily.CreditLine.openapi_types)
CreditLineType = create_model_from_dict("CreditLineType", __config__=Config, **yapily.CreditLineType.openapi_types)
CurrencyExchange = create_model_from_dict("CurrencyExchange", __config__=Config, **yapily.CurrencyExchange.openapi_types)
DeleteStatusEnum = create_model_from_dict("DeleteStatusEnum", __config__=Config, **yapily.DeleteStatusEnum.openapi_types)
DirectDebitPayee = create_model_from_dict("DirectDebitPayee", __config__=Config, **yapily.DirectDebitPayee.openapi_types)
DirectDebitResponse = create_model_from_dict("DirectDebitResponse", __config__=Config, **yapily.DirectDebitResponse.openapi_types)
EnrichedTransaction = create_model_from_dict("EnrichedTransaction", __config__=Config, **yapily.EnrichedTransaction.openapi_types)
EnrichedWrapper = create_model_from_dict("EnrichedWrapper", __config__=Config, **yapily.EnrichedWrapper.openapi_types)
Enrichment = create_model_from_dict("Enrichment", __config__=Config, **yapily.Enrichment.openapi_types)
EnrichmentMerchant = create_model_from_dict("EnrichmentMerchant", __config__=Config, **yapily.EnrichmentMerchant.openapi_types)
EnvironmentType = create_model_from_dict("EnvironmentType", __config__=Config, **yapily.EnvironmentType.openapi_types)
ExchangeRateInformation = create_model_from_dict("ExchangeRateInformation", __config__=Config, **yapily.ExchangeRateInformation.openapi_types)
ExchangeRateInformationResponse = create_model_from_dict("ExchangeRateInformationResponse", __config__=Config, **yapily.ExchangeRateInformationResponse.openapi_types)
FeatureDetails = create_model_from_dict("FeatureDetails", __config__=Config, **yapily.FeatureDetails.openapi_types)
FeatureEnum = create_model_from_dict("FeatureEnum", __config__=Config, **yapily.FeatureEnum.openapi_types)
FilterAndSort = create_model_from_dict("FilterAndSort", __config__=Config, **yapily.FilterAndSort.openapi_types)
FilteredClientPayloadListAccount = create_model_from_dict("FilteredClientPayloadListAccount", __config__=Config, **yapily.FilteredClientPayloadListAccount.openapi_types)
FilteredClientPayloadListAccountStatement = create_model_from_dict("FilteredClientPayloadListAccountStatement", __config__=Config, **yapily.FilteredClientPayloadListAccountStatement.openapi_types)
FilteredClientPayloadListCategory = create_model_from_dict("FilteredClientPayloadListCategory", __config__=Config, **yapily.FilteredClientPayloadListCategory.openapi_types)
FilteredClientPayloadListConsent = create_model_from_dict("FilteredClientPayloadListConsent", __config__=Config, **yapily.FilteredClientPayloadListConsent.openapi_types)
FilteredClientPayloadListDirectDebitResponse = create_model_from_dict("FilteredClientPayloadListDirectDebitResponse", __config__=Config, **yapily.FilteredClientPayloadListDirectDebitResponse.openapi_types)
FilteredClientPayloadListFeatureDetails = create_model_from_dict("FilteredClientPayloadListFeatureDetails", __config__=Config, **yapily.FilteredClientPayloadListFeatureDetails.openapi_types)
FilteredClientPayloadListInstitution = create_model_from_dict("FilteredClientPayloadListInstitution", __config__=Config, **yapily.FilteredClientPayloadListInstitution.openapi_types)
FilteredClientPayloadListPaymentResponse = create_model_from_dict("FilteredClientPayloadListPaymentResponse", __config__=Config, **yapily.FilteredClientPayloadListPaymentResponse.openapi_types)
FilteredClientPayloadListTransaction = create_model_from_dict("FilteredClientPayloadListTransaction", __config__=Config, **yapily.FilteredClientPayloadListTransaction.openapi_types)
FinancialProfile = create_model_from_dict("FinancialProfile", __config__=Config, **yapily.FinancialProfile.openapi_types)
FrequencyEnumExtended = create_model_from_dict("FrequencyEnumExtended", __config__=Config, **yapily.FrequencyEnumExtended.openapi_types)
FrequencyRequest = create_model_from_dict("FrequencyRequest", __config__=Config, **yapily.FrequencyRequest.openapi_types)
FrequencyResponse = create_model_from_dict("FrequencyResponse", __config__=Config, **yapily.FrequencyResponse.openapi_types)
Identity = create_model_from_dict("Identity", __config__=Config, **yapily.Identity.openapi_types)
IdentityAddress = create_model_from_dict("IdentityAddress", __config__=Config, **yapily.IdentityAddress.openapi_types)
Institution = create_model_from_dict("Institution", __config__=Config, **yapily.Institution.openapi_types)
InstitutionConsent = create_model_from_dict("InstitutionConsent", __config__=Config, **yapily.InstitutionConsent.openapi_types)
InstitutionError = create_model_from_dict("InstitutionError", __config__=Config, **yapily.InstitutionError.openapi_types)
InternationalPaymentRequest = create_model_from_dict("InternationalPaymentRequest", __config__=Config, **yapily.InternationalPaymentRequest.openapi_types)
IsoBankTransactionCode = create_model_from_dict("IsoBankTransactionCode", __config__=Config, **yapily.IsoBankTransactionCode.openapi_types)
IsoCodeDetails = create_model_from_dict("IsoCodeDetails", __config__=Config, **yapily.IsoCodeDetails.openapi_types)
Media = create_model_from_dict("Media", __config__=Config, **yapily.Media.openapi_types)
Merchant = create_model_from_dict("Merchant", __config__=Config, **yapily.Merchant.openapi_types)
MonitoringEndpointStatus = create_model_from_dict("MonitoringEndpointStatus", __config__=Config, **yapily.MonitoringEndpointStatus.openapi_types)
MonitoringFeatureStatus = create_model_from_dict("MonitoringFeatureStatus", __config__=Config, **yapily.MonitoringFeatureStatus.openapi_types)
MonitoringStatusEnum = create_model_from_dict("MonitoringStatusEnum", __config__=Config, **yapily.MonitoringStatusEnum.openapi_types)
MultiAuthorisation = create_model_from_dict("MultiAuthorisation", __config__=Config, **yapily.MultiAuthorisation.openapi_types)
NewApplicationUser = create_model_from_dict("NewApplicationUser", __config__=Config, **yapily.NewApplicationUser.openapi_types)
Next = create_model_from_dict("Next", __config__=Config, **yapily.Next.openapi_types)
OneTimeTokenRequest = create_model_from_dict("OneTimeTokenRequest", __config__=Config, **yapily.OneTimeTokenRequest.openapi_types)
Pagination = create_model_from_dict("Pagination", __config__=Config, **yapily.Pagination.openapi_types)
Payee = create_model_from_dict("Payee", __config__=Config, **yapily.Payee.openapi_types)
PayeeDetails = create_model_from_dict("PayeeDetails", __config__=Config, **yapily.PayeeDetails.openapi_types)
Payer = create_model_from_dict("Payer", __config__=Config, **yapily.Payer.openapi_types)
PayerDetails = create_model_from_dict("PayerDetails", __config__=Config, **yapily.PayerDetails.openapi_types)
PaymentAuthorisationRequest = create_model_from_dict("PaymentAuthorisationRequest", __config__=Config, **yapily.PaymentAuthorisationRequest.openapi_types)
PaymentAuthorisationRequestResponse = create_model_from_dict("PaymentAuthorisationRequestResponse", __config__=Config, **yapily.PaymentAuthorisationRequestResponse.openapi_types)
PaymentChargeDetails = create_model_from_dict("PaymentChargeDetails", __config__=Config, **yapily.PaymentChargeDetails.openapi_types)
PaymentContextType = create_model_from_dict("PaymentContextType", __config__=Config, **yapily.PaymentContextType.openapi_types)
PaymentEmbeddedAuthorisationRequest = create_model_from_dict("PaymentEmbeddedAuthorisationRequest", __config__=Config, **yapily.PaymentEmbeddedAuthorisationRequest.openapi_types)
PaymentEmbeddedAuthorisationRequestResponse = create_model_from_dict("PaymentEmbeddedAuthorisationRequestResponse", __config__=Config, **yapily.PaymentEmbeddedAuthorisationRequestResponse.openapi_types)
PaymentIsoStatus = create_model_from_dict("PaymentIsoStatus", __config__=Config, **yapily.PaymentIsoStatus.openapi_types)
PaymentIsoStatusCodeEnum = create_model_from_dict("PaymentIsoStatusCodeEnum", __config__=Config, **yapily.PaymentIsoStatusCodeEnum.openapi_types)
PaymentPreAuthorisationRequest = create_model_from_dict("PaymentPreAuthorisationRequest", __config__=Config, **yapily.PaymentPreAuthorisationRequest.openapi_types)
PaymentRequest = create_model_from_dict("PaymentRequest", __config__=Config, **yapily.PaymentRequest.openapi_types)
PaymentResponse = create_model_from_dict("PaymentResponse", __config__=Config, **yapily.PaymentResponse.openapi_types)
PaymentResponses = create_model_from_dict("PaymentResponses", __config__=Config, **yapily.PaymentResponses.openapi_types)
PaymentStatus = create_model_from_dict("PaymentStatus", __config__=Config, **yapily.PaymentStatus.openapi_types)
PaymentStatusDetails = create_model_from_dict("PaymentStatusDetails", __config__=Config, **yapily.PaymentStatusDetails.openapi_types)
PaymentType = create_model_from_dict("PaymentType", __config__=Config, **yapily.PaymentType.openapi_types)
PeriodicPaymentRequest = create_model_from_dict("PeriodicPaymentRequest", __config__=Config, **yapily.PeriodicPaymentRequest.openapi_types)
PreAuthorisationRequest = create_model_from_dict("PreAuthorisationRequest", __config__=Config, **yapily.PreAuthorisationRequest.openapi_types)
PriorityCodeEnum = create_model_from_dict("PriorityCodeEnum", __config__=Config, **yapily.PriorityCodeEnum.openapi_types)
ProfileConsent = create_model_from_dict("ProfileConsent", __config__=Config, **yapily.ProfileConsent.openapi_types)
ProprietaryBankTransactionCode = create_model_from_dict("ProprietaryBankTransactionCode", __config__=Config, **yapily.ProprietaryBankTransactionCode.openapi_types)
RateTypeEnum = create_model_from_dict("RateTypeEnum", __config__=Config, **yapily.RateTypeEnum.openapi_types)
RawRequest = create_model_from_dict("RawRequest", __config__=Config, **yapily.RawRequest.openapi_types)
RawResponse = create_model_from_dict("RawResponse", __config__=Config, **yapily.RawResponse.openapi_types)
RedirectRequest = create_model_from_dict("RedirectRequest", __config__=Config, **yapily.RedirectRequest.openapi_types)
RefundAccount = create_model_from_dict("RefundAccount", __config__=Config, **yapily.RefundAccount.openapi_types)
ResponseForwardedData = create_model_from_dict("ResponseForwardedData", __config__=Config, **yapily.ResponseForwardedData.openapi_types)
ResponseListMeta = create_model_from_dict("ResponseListMeta", __config__=Config, **yapily.ResponseListMeta.openapi_types)
ResponseMeta = create_model_from_dict("ResponseMeta", __config__=Config, **yapily.ResponseMeta.openapi_types)
ScaMethod = create_model_from_dict("ScaMethod", __config__=Config, **yapily.ScaMethod.openapi_types)
SortEnum = create_model_from_dict("SortEnum", __config__=Config, **yapily.SortEnum.openapi_types)
StatementReference = create_model_from_dict("StatementReference", __config__=Config, **yapily.StatementReference.openapi_types)
Subcategory = create_model_from_dict("Subcategory", __config__=Config, **yapily.Subcategory.openapi_types)
TerminatedTransactionStream = create_model_from_dict("TerminatedTransactionStream", __config__=Config, **yapily.TerminatedTransactionStream.openapi_types)
Transaction = create_model_from_dict("Transaction", __config__=Config, **yapily.Transaction.openapi_types)
TransactionBalance = create_model_from_dict("TransactionBalance", __config__=Config, **yapily.TransactionBalance.openapi_types)
TransactionChargeDetails = create_model_from_dict("TransactionChargeDetails", __config__=Config, **yapily.TransactionChargeDetails.openapi_types)
TransactionHash = create_model_from_dict("TransactionHash", __config__=Config, **yapily.TransactionHash.openapi_types)
TransactionSchedule = create_model_from_dict("TransactionSchedule", __config__=Config, **yapily.TransactionSchedule.openapi_types)
TransactionStatusEnum = create_model_from_dict("TransactionStatusEnum", __config__=Config, **yapily.TransactionStatusEnum.openapi_types)
TransactionStream = create_model_from_dict("TransactionStream", __config__=Config, **yapily.TransactionStream.openapi_types)
Type = create_model_from_dict("Type", __config__=Config, **yapily.Type.openapi_types)
UsageType = create_model_from_dict("UsageType", __config__=Config, **yapily.UsageType.openapi_types)
UserCredentials = create_model_from_dict("UserCredentials", __config__=Config, **yapily.UserCredentials.openapi_types)
UserDeleteResponse = create_model_from_dict("UserDeleteResponse", __config__=Config, **yapily.UserDeleteResponse.openapi_types)

Account.update_forward_refs()
AccountApiListResponse.update_forward_refs()
AccountAuthorisationRequest.update_forward_refs()
AccountBalance.update_forward_refs()
AccountBalanceType.update_forward_refs()
AccountEmbeddedAuthorisationRequest.update_forward_refs()
AccountIdentification.update_forward_refs()
AccountIdentificationType.update_forward_refs()
AccountInfo.update_forward_refs()
AccountName.update_forward_refs()
AccountRequest.update_forward_refs()
AccountStatement.update_forward_refs()
AccountType.update_forward_refs()
Address.update_forward_refs()
AddressDetails.update_forward_refs()
AddressTypeEnum.update_forward_refs()
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
AuthorisationStatus.update_forward_refs()
Balances.update_forward_refs()
Beneficiary.update_forward_refs()
BeneficiaryPayee.update_forward_refs()
BulkPaymentAuthorisationRequest.update_forward_refs()
BulkPaymentEmbeddedAuthorisationRequest.update_forward_refs()
BulkPaymentRequest.update_forward_refs()
Categorisation.update_forward_refs()
Category.update_forward_refs()
ChargeBearerType.update_forward_refs()
Consent.update_forward_refs()
ConsentAuthCodeRequest.update_forward_refs()
ConsentDeleteResponse.update_forward_refs()
Country.update_forward_refs()
CredentialsType.update_forward_refs()
CreditLine.update_forward_refs()
CreditLineType.update_forward_refs()
CurrencyExchange.update_forward_refs()
DeleteStatusEnum.update_forward_refs()
DirectDebitPayee.update_forward_refs()
DirectDebitResponse.update_forward_refs()
EnrichedTransaction.update_forward_refs()
EnrichedWrapper.update_forward_refs()
Enrichment.update_forward_refs()
EnrichmentMerchant.update_forward_refs()
EnvironmentType.update_forward_refs()
ExchangeRateInformation.update_forward_refs()
ExchangeRateInformationResponse.update_forward_refs()
FeatureDetails.update_forward_refs()
FeatureEnum.update_forward_refs()
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
FrequencyEnumExtended.update_forward_refs()
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
MonitoringStatusEnum.update_forward_refs()
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
PaymentContextType.update_forward_refs()
PaymentEmbeddedAuthorisationRequest.update_forward_refs()
PaymentEmbeddedAuthorisationRequestResponse.update_forward_refs()
PaymentIsoStatus.update_forward_refs()
PaymentIsoStatusCodeEnum.update_forward_refs()
PaymentPreAuthorisationRequest.update_forward_refs()
PaymentRequest.update_forward_refs()
PaymentResponse.update_forward_refs()
PaymentResponses.update_forward_refs()
PaymentStatus.update_forward_refs()
PaymentStatusDetails.update_forward_refs()
PaymentType.update_forward_refs()
PeriodicPaymentRequest.update_forward_refs()
PreAuthorisationRequest.update_forward_refs()
PriorityCodeEnum.update_forward_refs()
ProfileConsent.update_forward_refs()
ProprietaryBankTransactionCode.update_forward_refs()
RateTypeEnum.update_forward_refs()
RawRequest.update_forward_refs()
RawResponse.update_forward_refs()
RedirectRequest.update_forward_refs()
RefundAccount.update_forward_refs()
ResponseForwardedData.update_forward_refs()
ResponseListMeta.update_forward_refs()
ResponseMeta.update_forward_refs()
ScaMethod.update_forward_refs()
SortEnum.update_forward_refs()
StatementReference.update_forward_refs()
Subcategory.update_forward_refs()
TerminatedTransactionStream.update_forward_refs()
Transaction.update_forward_refs()
TransactionBalance.update_forward_refs()
TransactionChargeDetails.update_forward_refs()
TransactionHash.update_forward_refs()
TransactionSchedule.update_forward_refs()
TransactionStatusEnum.update_forward_refs()
TransactionStream.update_forward_refs()
Type.update_forward_refs()
UsageType.update_forward_refs()
UserCredentials.update_forward_refs()
UserDeleteResponse.update_forward_refs()