# HostedConsentPhase

The phase of the Consent Request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase_name** | **str** | The name of the hosted consent process phase. Allowed values are : &lt;ul&gt; &lt;li&gt; INITIATED - Process initiated &lt;/li&gt; &lt;li&gt; INSTITUTION_SUBMITTED - Consent institution submitted &lt;/li&gt; &lt;li&gt;    AUTHORISATION_INITIATED - All details required for consent initiation have been collected&lt;/li&gt; &lt;li&gt; AUTHORISATION_CREATED - Consent authorisation request created with Institution, awaiting authorisation completion &lt;/li&gt; &lt;li&gt; AUTHORISATION_FAILED - Consent authorisation failed and will not proceed further&lt;/li&gt; &lt;li&gt; AUTHORISATION_REJECTED - Consent Authorisation request rejected by Institution and will not proceed further &lt;/li&gt; &lt;li&gt;    DECOUPLED_AUTHORISATION - For embedded banks, decoupled authorisation was initiated by the bank&lt;/li&gt; &lt;li&gt;    EMBEDDED_CREDENTIAL_REQUESTED - For embedded banks, a UI element to collect user credentials was displayed&lt;/li&gt; &lt;li&gt;    EMBEDDED_CODE_REQUESTED - For embedded banks, a UI element to collect SCA for initiated consent was displayed&lt;/li&gt;&lt;li&gt;    EMBEDDED_TYPE_REQUESTED - For embedded banks, a UI element to allow the user to select their preferred SCA method for this consent authorisation was displayed&lt;/li&gt; &lt;li&gt;    EMBEDDED_CODE_COLLECTED - For embedded banks, SCA code was collected for consent authorisation&lt;/li&gt;&lt;li&gt;    EMBEDDED_TYPE_SELECTED - For embedded banks, preferred SCA method was selected for consent authorisation&lt;/li&gt; &lt;li&gt;    CONSENT_POLLING_STARTED - We start polling the bank for consent authorisation status&lt;/li&gt;&lt;li&gt;    CONSENT_POLLING_ENDED - We finish polling the bank for consent authorisation status&lt;/li&gt; &lt;li&gt; AUTHORISED - Consent authorisation completed &lt;/li&gt; &lt;li&gt; FINISHED - Process finished &lt;/li&gt;  &lt;/ul&gt; | [optional] 
**phase_created_at** | **datetime** | The date and time at which the phase of the hosted Consent was created. | [optional] 

## Example

```python
from yapily.models.hosted_consent_phase import HostedConsentPhase

# TODO update the JSON string below
json = "{}"
# create an instance of HostedConsentPhase from a JSON string
hosted_consent_phase_instance = HostedConsentPhase.from_json(json)
# print the JSON string representation of the object
print HostedConsentPhase.to_json()

# convert the object into a dict
hosted_consent_phase_dict = hosted_consent_phase_instance.to_dict()
# create an instance of HostedConsentPhase from a dict
hosted_consent_phase_from_dict = HostedConsentPhase.from_dict(hosted_consent_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


