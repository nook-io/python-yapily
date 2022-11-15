# VirtualAccountPaymentSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of source for a payment. One of ACCOUNT or EXTERNAL | 
**account_id** | **str** | Only present if type is ACCOUNT. Identifies the Virtual Account from which the payment was made | [optional] 
**account_identifications** | [**list[AccountIdentification]**](AccountIdentification.md) | Only present if type is EXTERNAL. The account identifications that identify an external source | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


