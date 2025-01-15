# RealTimeTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**booking_date_time** | **datetime** |  | [optional] 
**value_date_time** | **datetime** |  | [optional] 
**status** | [**TransactionStatusEnum**](TransactionStatusEnum.md) |  | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | [optional] 
**gross_amount** | [**Amount**](Amount.md) |  | [optional] 
**currency_exchange** | [**CurrencyExchange**](CurrencyExchange.md) |  | [optional] 
**charge_details** | [**TransactionChargeDetails**](TransactionChargeDetails.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**statement_references** | [**List[StatementReference]**](StatementReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**transaction_information** | **List[str]** |  | [optional] 
**address_details** | [**AddressDetails**](AddressDetails.md) |  | [optional] 
**iso_bank_transaction_code** | [**IsoBankTransactionCode**](IsoBankTransactionCode.md) |  | [optional] 
**proprietary_bank_transaction_code** | [**ProprietaryBankTransactionCode**](ProprietaryBankTransactionCode.md) |  | [optional] 
**balance** | [**TransactionBalance**](TransactionBalance.md) |  | [optional] 
**payee_details** | [**Payee**](Payee.md) |  | [optional] 
**payer_details** | [**Payer**](Payer.md) |  | [optional] 
**merchant** | [**Merchant**](Merchant.md) |  | [optional] 
**supplementary_data** | **object** |  | [optional] 

## Example

```python
from yapily.models.real_time_transaction import RealTimeTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of RealTimeTransaction from a JSON string
real_time_transaction_instance = RealTimeTransaction.from_json(json)
# print the JSON string representation of the object
print(RealTimeTransaction.to_json())

# convert the object into a dict
real_time_transaction_dict = real_time_transaction_instance.to_dict()
# create an instance of RealTimeTransaction from a dict
real_time_transaction_from_dict = RealTimeTransaction.from_dict(real_time_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


