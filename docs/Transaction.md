# Transaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**booking_date_time** | **datetime** |  | [optional] 
**value_date_time** | **datetime** |  | [optional] 
**status** | [**TransactionStatusEnum**](TransactionStatusEnum.md) |  | [optional] 
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
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
**enrichment** | [**Enrichment**](Enrichment.md) |  | [optional] 
**supplementary_data** | **object** |  | [optional] 
**transaction_mutability** | **str** | __Optional__. Specifies the Mutability of the Transaction record.&lt;ul&gt;&lt;li&gt;A transaction with a &#x60;Status&#x60; of &#x60;Pending&#x60; is mutable.&lt;/li&gt;&lt;li&gt;A transaction with a &#x60;Status&#x60; of &#x60;Booked&#x60; where the &#x60;TransactionMutability&#x60; flag is not specified is not guaranteed to be immutable (although in most instances it will be).&lt;/li&gt;&lt;li&gt;A transaction with a &#x60;Status&#x60; of &#x60;Booked&#x60; with the &#x60;TransactionMutability&#x60; flag set to &#x60;Immutable&#x60; is immutable.&lt;/li&gt;&lt;li&gt;A transaction with a &#x60;Status&#x60; of &#x60;Booked&#x60; with the &#x60;TransactionMutability&#x60; flag set to &#x60;Mutable&#x60; is mutable.&lt;/li&gt;&lt;/ul&gt; | [optional] 

## Example

```python
from yapily.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print Transaction.to_json()

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_form_dict = transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


