# Justice Matchmaking Service (2.10.0)

# Copyright (c) 2018 - 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

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
from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import Model

from ..models.models_player_result_request import ModelsPlayerResultRequest


class ModelsMatchResultRequest(Model):
    """Models match result request (models.MatchResultRequest)

    Properties:
        match_id: (match_id) REQUIRED str

        players: (players) REQUIRED List[ModelsPlayerResultRequest]
    """

    # region fields

    match_id: str                                                                                  # REQUIRED
    players: List[ModelsPlayerResultRequest]                                                       # REQUIRED

    # endregion fields

    # region with_x methods

    def with_match_id(self, value: str) -> ModelsMatchResultRequest:
        self.match_id = value
        return self

    def with_players(self, value: List[ModelsPlayerResultRequest]) -> ModelsMatchResultRequest:
        self.players = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "match_id"):
            result["match_id"] = str(self.match_id)
        elif include_empty:
            result["match_id"] = str()
        if hasattr(self, "players"):
            result["players"] = [i0.to_dict(include_empty=include_empty) for i0 in self.players]
        elif include_empty:
            result["players"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        match_id: str,
        players: List[ModelsPlayerResultRequest],
    ) -> ModelsMatchResultRequest:
        instance = cls()
        instance.match_id = match_id
        instance.players = players
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsMatchResultRequest:
        instance = cls()
        if not dict_:
            return instance
        if "match_id" in dict_ and dict_["match_id"] is not None:
            instance.match_id = str(dict_["match_id"])
        elif include_empty:
            instance.match_id = str()
        if "players" in dict_ and dict_["players"] is not None:
            instance.players = [ModelsPlayerResultRequest.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["players"]]
        elif include_empty:
            instance.players = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "match_id": "match_id",
            "players": "players",
        }

    # endregion static methods