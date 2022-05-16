# UserCredentials

__Conditional__. Used to capture the user's credentials to allow them to login to an `Institution` that uses the embedded account authorisation flow. <br><br>This is the first step required in the embedded account authorisation flow to authorise the `Consent`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | __Mandatory__. The login id for the user for a particular &#x60;Institution&#x60;. | 
**corporate_id** | **str** | __Conditional__. The corporate login for the user for a particular corporate &#x60;Institution&#x60;. | [optional] 
**password** | **str** | __Mandatory__. The password of the user to login to a particular &#x60;Institution&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


