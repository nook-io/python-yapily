from __future__ import annotations
import pprint
import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class HostedVRPPhase(BaseModel):
    phase_name: Optional[StrictStr] = Field(
        default=None,
        description="The name of the hosted VRP consent process phase. Allowed values are : <ul> <li> INITIATED - Process initiated </li><li> DECLINED - Process failed and will not proceed further </li><li> INSTITUTION_SUBMITTED - Consent institution submitted </li><li> INPUT_CAPTURED - Additional input captured to process the Consent </li><li> IBAN_VALIDATED - Payer IBAN successfully validated </li><li> AUTHORISATION_CREATED - Consent authorisation request created with Institution, awaiting authorisation completion </li><li> AUTHORISATION_REJECTED - Consent Authorisation request rejected by Institution and will not proceed further </li><li> AUTHORISED - Consent authorisation completed </li><li> AUTHORISATION_FAILED - Consent authorisation failed and will not proceed further</li><li> SUBMITTED - Consent execution created and submitted to Institution </li><li> ACCEPTED - Consent execution accepted by Institution and awaiting settlement </li><li> REJECTED - Consent execution request rejected by Institution and will not proceed further </li><li> STATUS_POLLING_STARTED - Consent status polling started </li><li> STATUS_POLLING_ENDED - Consent status polling ended </li><li> MERCHANT_ACKNOWLEDGED - Consent acknowledgement received from merchant </li><li> FINISHED - Consent process completed </li> <li> REVOKED - Consent process completed </li>  </ul>",
        alias="phaseName",
    )
    phase_created_at: Optional[datetime] = Field(
        default=None,
        description="The date and time at which the phase of the hosted Consent was created.",
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
