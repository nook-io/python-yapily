# HostedPaymentPhase

The phase of the payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase_name** | **str** | The name of the hosted payment process phase. Allowed values are : &lt;ul&gt; &lt;li&gt;    INITIATED - Payment process initiated&lt;/li&gt;&lt;li&gt;    DECLINED - Payment process failed and will not proceed further&lt;/li&gt;&lt;li&gt;    INSTITUTION_SUBMITTED - Payment institution submitted&lt;/li&gt;&lt;li&gt;    EMBEDDED_CREDENTIAL_REQUESTED - For embedded banks, a UI element to collect user credentials was displayed&lt;/li&gt;&lt;li&gt;    CREDENTIALS_ERROR - embedded credentials refused by intittution&lt;/li&gt;&lt;li&gt;    AUTHORISATION_INITIATED - All details required for payment initiation have been collected&lt;/li&gt;&lt;li&gt;    VALIDATION_COMPLETED - The payment payload was validated successfully&lt;/li&gt;&lt;li&gt;    VALIDATION_FAILED - The payment data provided failed validation&lt;/li&gt;&lt;li&gt;    AUTHORISATION_CREATED - Payment authorisation request created with Institution&lt;/li&gt;&lt;li&gt;    EMBEDDED_CODE_REQUESTED - For embedded banks, a UI element to collect SCA for initiated consent was displayed&lt;/li&gt;&lt;li&gt;    EMBEDDED_TYPE_REQUESTED - For embedded banks, a UI element to allow the user to select their preferred SCA method for this consent authorisation was displayed&lt;/li&gt;&lt;li&gt;    DECOUPLED_AUTHORISATION - For embedded banks, decoupled authoirisation was initiated by the bank&lt;/li&gt;&lt;li&gt;    EMBEDDED_CODE_COLLECTED - For embedded banks, SCA code was collected for consent authorisation&lt;/li&gt;&lt;li&gt;    EMBEDDED_TYPE_SELECTED - For embedded banks, preferred SCA method was selected for consent authorisation&lt;/li&gt;&lt;li&gt;    PRE_AUTHORISED - pre authorisation was initiated by bank&lt;/li&gt;&lt;li&gt;    CONSENT_POLLING_STARTED - We start polling the bank for consent authorisation status&lt;/li&gt;&lt;li&gt;    CONSENT_POLLING_ENDED - We finish polling the bank for consent authorisation status&lt;/li&gt;&lt;li&gt;    AUTHORISED - Payment authorisation completed&lt;/li&gt;&lt;li&gt;    AUTHORISATION_FAILED - Payment authorisation failed and will not proceed further&lt;/li&gt;&lt;li&gt;    AUTHORISATION_REJECTED - Payment authorisation rejected and will not proceed further&lt;/li&gt;&lt;li&gt;    SUBMITTED - Payment execution created and submitted to Institution&lt;/li&gt;&lt;li&gt;    SUBMITTED_AUTO - Payment execution created and submitted to Institution&lt;/li&gt;&lt;li&gt;    ACCEPTED - Payment execution accepted by Institution and awaiting settlement&lt;/li&gt;&lt;li&gt;    REJECTED - Payment or Authorisation request rejected by Institution and will not proceed further&lt;/li&gt;&lt;li&gt;    SETTLEMENT_COMPLETED - Payment settlement completed&lt;/li&gt;&lt;li&gt;    STATUS_POLLING_STARTED - Payment status polling started&lt;/li&gt;&lt;li&gt;    STATUS_POLLING_ENDED - Payment status polling ended&lt;/li&gt;&lt;li&gt;    MERCHANT_ACKNOWLEDGED - Payment acknowledgement received from merchant&lt;/li&gt;&lt;li&gt;    FINISHED - Payment process completed&lt;/li&gt;&lt;/ul&gt; | [optional] 
**phase_created_at** | **datetime** | The date and time when phase of the hosted payment was inserted. | [optional] 

## Example

```python
from yapily.models.hosted_payment_phase import HostedPaymentPhase

# TODO update the JSON string below
json = "{}"
# create an instance of HostedPaymentPhase from a JSON string
hosted_payment_phase_instance = HostedPaymentPhase.from_json(json)
# print the JSON string representation of the object
print HostedPaymentPhase.to_json()

# convert the object into a dict
hosted_payment_phase_dict = hosted_payment_phase_instance.to_dict()
# create an instance of HostedPaymentPhase from a dict
hosted_payment_phase_from_dict = HostedPaymentPhase.from_dict(hosted_payment_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


