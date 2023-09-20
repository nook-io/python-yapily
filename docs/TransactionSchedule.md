# TransactionSchedule

Part of a financial profile for a User.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | How often the transaction happens.  Can be &#39;Monthly&#39;, &#39;Twice monthly&#39;, &#39;Every two weeks&#39;, &#39;Every four weeks&#39;, &#39;Daily&#39;, &#39;Weekly&#39;, &#39;Every weekday&#39;, &#39;Twice daily&#39;, &#39;Twice every weekday&#39; | [optional] 
**detailed_frequency** | **str** | When in the cycle the transaction occurs.  Can be &#39;Daily&#39;, &#39;Twice daily&#39;, &#39;Twice every weekday&#39;, &#39;Every weekday&#39;, &#39;Weekly on day n&#39;, &#39;Every two weeks on day n&#39;, &#39;Monthly on working day before day n of month&#39;, &#39;Monthly on last working day of month&#39;, &#39;Twice a month on 15th and last working day of month&#39;, &#39;Every four weeks on day n&#39; | [optional] 
**detailed_frequency_parameter** | **float** | The n in detailedFrequency where there is one - for week-based frequencies, an integer from 0 to 6 where 0 is Monday or for month-based frequencies, an integer from 0 to 27 where 0 is the first day of the month | [optional] 

## Example

```python
from yapily.models.transaction_schedule import TransactionSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSchedule from a JSON string
transaction_schedule_instance = TransactionSchedule.from_json(json)
# print the JSON string representation of the object
print TransactionSchedule.to_json()

# convert the object into a dict
transaction_schedule_dict = transaction_schedule_instance.to_dict()
# create an instance of TransactionSchedule from a dict
transaction_schedule_form_dict = transaction_schedule.from_dict(transaction_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


