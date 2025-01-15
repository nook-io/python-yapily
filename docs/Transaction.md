# Transaction

Details of a transaction (credit or debit) that has occurred on the account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the transaction. | [optional] 
**var_date** | **datetime** |  | [optional] 
**booking_date_time** | **datetime** | Date and time in UTC format of when a transaction was booked. | [optional] 
**value_date_time** | **datetime** | Date and time in UTC format when the funds either cease to be available (for debit transactions) or become available (for credit transactions) to the account owner. | [optional] 
**status** | [**TransactionStatusEnum**](TransactionStatusEnum.md) |  | [optional] 
**amount** | **float** | The transaction amount. | [optional] 
**currency** | **str** | Currency the transaction amount is denoted in. Specified as a 3-letter ISO 4217 code. | [optional] 
**transaction_amount** | [**Amount**](Amount.md) |  | [optional] 
**gross_amount** | [**Amount**](Amount.md) |  | [optional] 
**currency_exchange** | [**CurrencyExchange**](CurrencyExchange.md) |  | [optional] 
**charge_details** | [**TransactionChargeDetails**](TransactionChargeDetails.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**statement_references** | [**List[StatementReference]**](StatementReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**transaction_information** | **List[str]** | Further details on the transaction. This is narrative data, caught as unstructured text. | [optional] 
**address_details** | [**AddressDetails**](AddressDetails.md) |  | [optional] 
**iso_bank_transaction_code** | [**IsoBankTransactionCode**](IsoBankTransactionCode.md) |  | [optional] 
**proprietary_bank_transaction_code** | [**ProprietaryBankTransactionCode**](ProprietaryBankTransactionCode.md) |  | [optional] 
**balance** | [**TransactionBalance**](TransactionBalance.md) |  | [optional] 
**payee_details** | [**TransactionPayeeDetails**](TransactionPayeeDetails.md) |  | [optional] 
**payer_details** | [**TransactionPayerDetails**](TransactionPayerDetails.md) |  | [optional] 
**merchant** | [**Merchant**](Merchant.md) |  | [optional] 
**enrichment** | [**Enrichment**](Enrichment.md) |  | [optional] 
**supplementary_data** | **object** | Additional information that cannot be captured in a structured field or block. | [optional] 
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
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


