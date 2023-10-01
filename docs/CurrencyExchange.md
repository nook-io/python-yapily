# CurrencyExchange

Provides details on the currrency exchange.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_currency** | **str** | Currency from which an amount is to be converted. | [optional] 
**target_currency** | **str** | Currency to which an amount is to be converted. | [optional] 
**unit_currency** | **str** | The currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP &#x3D; xxxCUR, the unit currency is GBP. | [optional] 
**exchange_rate** | **float** | The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency. | [optional] 

## Example

```python
from yapily.models.currency_exchange import CurrencyExchange

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchange from a JSON string
currency_exchange_instance = CurrencyExchange.from_json(json)
# print the JSON string representation of the object
print CurrencyExchange.to_json()

# convert the object into a dict
currency_exchange_dict = currency_exchange_instance.to_dict()
# create an instance of CurrencyExchange from a dict
currency_exchange_form_dict = currency_exchange.from_dict(currency_exchange_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


