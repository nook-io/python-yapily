from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class HostedPaymentPhase(BaseModel):
    phase_name: Optional[StrictStr] = Field(
        default=None,
        description="The name of the hosted payment process phase. Allowed values are : <ul> <li>    INITIATED - Payment process initiated</li><li>    DECLINED - Payment process failed and will not proceed further</li><li>    INSTITUTION_SUBMITTED - Payment institution submitted</li><li>    EMBEDDED_CREDENTIAL_REQUESTED - For embedded banks, a UI element to collect user credentials was displayed</li><li>    CREDENTIALS_ERROR - embedded credentials refused by intittution</li><li>    AUTHORISATION_INITIATED - All details required for payment initiation have been collected</li><li>    VALIDATION_COMPLETED - The payment payload was validated successfully</li><li>    VALIDATION_FAILED - The payment data provided failed validation</li><li>    AUTHORISATION_CREATED - Payment authorisation request created with Institution</li><li>    EMBEDDED_CODE_REQUESTED - For embedded banks, a UI element to collect SCA for initiated consent was displayed</li><li>    EMBEDDED_TYPE_REQUESTED - For embedded banks, a UI element to allow the user to select their preferred SCA method for this consent authorisation was displayed</li><li>    DECOUPLED_AUTHORISATION - For embedded banks, decoupled authoirisation was initiated by the bank</li><li>    EMBEDDED_CODE_COLLECTED - For embedded banks, SCA code was collected for consent authorisation</li><li>    EMBEDDED_TYPE_SELECTED - For embedded banks, preferred SCA method was selected for consent authorisation</li><li>    PRE_AUTHORISED - pre authorisation was initiated by bank</li><li>    CONSENT_POLLING_STARTED - We start polling the bank for consent authorisation status</li><li>    CONSENT_POLLING_ENDED - We finish polling the bank for consent authorisation status</li><li>    AUTHORISED - Payment authorisation completed</li><li>    AUTHORISATION_FAILED - Payment authorisation failed and will not proceed further</li><li>    AUTHORISATION_REJECTED - Payment authorisation rejected and will not proceed further</li><li>    SUBMITTED - Payment execution created and submitted to Institution</li><li>    SUBMITTED_AUTO - Payment execution created and submitted to Institution</li><li>    ACCEPTED - Payment execution accepted by Institution and awaiting settlement</li><li>    REJECTED - Payment or Authorisation request rejected by Institution and will not proceed further</li><li>    SETTLEMENT_COMPLETED - Payment settlement completed</li><li>    STATUS_POLLING_STARTED - Payment status polling started</li><li>    STATUS_POLLING_ENDED - Payment status polling ended</li><li>    MERCHANT_ACKNOWLEDGED - Payment acknowledgement received from merchant</li><li>    FINISHED - Payment process completed</li></ul>",
        alias="phaseName",
    )
    phase_created_at: Optional[datetime] = Field(
        default=None,
        description="The date and time when phase of the hosted payment was inserted.",
        alias="phaseCreatedAt",
    )
    __properties: ClassVar[List[str]] = ["phaseName", "phaseCreatedAt"]
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        _obj = cls.model_validate(
            {
                "phaseName": obj.get("phaseName"),
                "phaseCreatedAt": obj.get("phaseCreatedAt"),
            }
        )
        return _obj
