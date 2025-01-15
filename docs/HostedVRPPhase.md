# HostedVRPPhase

The phase of the VRP Consent Request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase_name** | **str** | The name of the hosted VRP consent process phase. Allowed values are : &lt;ul&gt; &lt;li&gt; INITIATED - Process initiated &lt;/li&gt;&lt;li&gt; DECLINED - Process failed and will not proceed further &lt;/li&gt;&lt;li&gt; INSTITUTION_SUBMITTED - Consent institution submitted &lt;/li&gt;&lt;li&gt; INPUT_CAPTURED - Additional input captured to process the Consent &lt;/li&gt;&lt;li&gt; IBAN_VALIDATED - Payer IBAN successfully validated &lt;/li&gt;&lt;li&gt; AUTHORISATION_CREATED - Consent authorisation request created with Institution, awaiting authorisation completion &lt;/li&gt;&lt;li&gt; AUTHORISATION_REJECTED - Consent Authorisation request rejected by Institution and will not proceed further &lt;/li&gt;&lt;li&gt; AUTHORISED - Consent authorisation completed &lt;/li&gt;&lt;li&gt; AUTHORISATION_FAILED - Consent authorisation failed and will not proceed further&lt;/li&gt;&lt;li&gt; SUBMITTED - Consent execution created and submitted to Institution &lt;/li&gt;&lt;li&gt; ACCEPTED - Consent execution accepted by Institution and awaiting settlement &lt;/li&gt;&lt;li&gt; REJECTED - Consent execution request rejected by Institution and will not proceed further &lt;/li&gt;&lt;li&gt; STATUS_POLLING_STARTED - Consent status polling started &lt;/li&gt;&lt;li&gt; STATUS_POLLING_ENDED - Consent status polling ended &lt;/li&gt;&lt;li&gt; MERCHANT_ACKNOWLEDGED - Consent acknowledgement received from merchant &lt;/li&gt;&lt;li&gt; FINISHED - Consent process completed &lt;/li&gt; &lt;li&gt; REVOKED - Consent process completed &lt;/li&gt;  &lt;/ul&gt; | [optional] 
**phase_created_at** | **datetime** | The date and time at which the phase of the hosted Consent was created. | [optional] 

## Example

```python
from yapily.models.hosted_vrp_phase import HostedVRPPhase

# TODO update the JSON string below
json = "{}"
# create an instance of HostedVRPPhase from a JSON string
hosted_vrp_phase_instance = HostedVRPPhase.from_json(json)
# print the JSON string representation of the object
print HostedVRPPhase.to_json()

# convert the object into a dict
hosted_vrp_phase_dict = hosted_vrp_phase_instance.to_dict()
# create an instance of HostedVRPPhase from a dict
hosted_vrp_phase_from_dict = HostedVRPPhase.from_dict(hosted_vrp_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


