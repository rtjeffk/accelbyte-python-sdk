# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

from __future__ import annotations
import json
from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import WebSocketMessage

from ....core import WebSocketMessageParserError

from ....core import WebSocketMessageParserException
from ....core import generate_websocket_message_id


class PartyCreateResponse(WebSocketMessage):

    # region fields

    id_: str
    code: str
    party_id: str
    leader_id: str
    members: str
    invitees: str
    invitation_token: str

    # endregion fields

    # region methods

    # noinspection PyMethodMayBeStatic
    def to_wsm(self) -> str:
        # pylint: disable=no-self-use
        wsm = [f"type: {PartyCreateResponse.get_type()}"]
        wsm.append(self.id_ if hasattr(self, "id_") else generate_websocket_message_id())
        if hasattr(self, "code") and self.code:
            wsm.append(f"code: {self.code}")
        if hasattr(self, "party_id") and self.party_id:
            wsm.append(f"partyId: {self.party_id}")
        if hasattr(self, "leader_id") and self.leader_id:
            wsm.append(f"leaderId: {self.leader_id}")
        if hasattr(self, "members") and self.members:
            wsm.append(f"members: {self.members}")
        if hasattr(self, "invitees") and self.invitees:
            wsm.append(f"invitees: {self.invitees}")
        if hasattr(self, "invitation_token") and self.invitation_token:
            wsm.append(f"invitationToken: {self.invitation_token}")
        return "\n".join(wsm)

    # endregion methods

    # region static methods

    @classmethod
    def create_from_wsm(cls, wsm: str, is_strict: bool = False) -> PartyCreateResponse:
        instance = cls()
        if not wsm:
            return instance
        lines = wsm.splitlines(keepends=False)
        if len(lines) < 2:
            raise WebSocketMessageParserException(WebSocketMessageParserError.TypeFormatInvalid)
        instance.id_ = lines[1]
        for line in lines[2:]:
            parts = line.split(":", 1)
            if len(parts) != 2:
                raise WebSocketMessageParserException(WebSocketMessageParserError.FieldFormatInvalid)
            name, value = parts[0].strip(), parts[1].strip()
            if name == "code":
                instance.code = value
                continue
            if name == "partyId":
                instance.party_id = value
                continue
            if name == "leaderId":
                instance.leader_id = value
                continue
            if name == "members":
                instance.members = value
                continue
            if name == "invitees":
                instance.invitees = value
                continue
            if name == "invitationToken":
                instance.invitation_token = value
                continue
            if is_strict:
                raise WebSocketMessageParserException(WebSocketMessageParserError.FieldTypeNotSupported)
        return instance

    @staticmethod
    def get_type() -> str:
        return "partyCreateResponse"

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "id": "id_",
            "code": "code",
            "partyId": "party_id",
            "leaderId": "leader_id",
            "members": "members",
            "invitees": "invitees",
            "invitationToken": "invitation_token",
        }

    # endregion static methods
