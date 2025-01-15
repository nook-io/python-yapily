# ExchangeRateInformation

__Optional__. Used to provide details on the currency exchange rate and contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_currency** | **str** | __Mandatory__. The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP &#x3D; xxxCUR, the unit currency is &#x60;GBP&#x60;. | 
**rate** | **float** | __Optional__. The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency. | [optional] 
**rate_type** | [**RateTypeEnum**](RateTypeEnum.md) |  | 
**foreign_exchange_contract_reference** | **str** | __Optional__. The unique and unambiguous reference to the foreign exchange contract agreed between the initiating party/creditor and the debtor agent. | [optional] 

## Example

```python
from yapily.models.exchange_rate_information import ExchangeRateInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRateInformation from a JSON string
exchange_rate_information_instance = ExchangeRateInformation.from_json(json)
# print the JSON string representation of the object
print ExchangeRateInformation.to_json()

# convert the object into a dict
exchange_rate_information_dict = exchange_rate_information_instance.to_dict()
# create an instance of ExchangeRateInformation from a dict
exchange_rate_information_from_dict = ExchangeRateInformation.from_dict(exchange_rate_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


