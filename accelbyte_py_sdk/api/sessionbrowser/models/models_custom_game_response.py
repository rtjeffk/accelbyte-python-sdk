# Auto-generated at 2021-10-21T08:52:31.820086+08:00
# from: Justice sessionbrowser Service ()

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

from ..models.models_game_session_setting import ModelsGameSessionSetting
from ..models.models_server import ModelsServer


class ModelsCustomGameResponse(Model):
    """Models custom game response (models.CustomGameResponse)

    Properties:
        all_players: (all_players) REQUIRED List[str]

        created_at: (created_at) REQUIRED str

        game_session_setting: (game_session_setting) REQUIRED ModelsGameSessionSetting

        joinable: (joinable) REQUIRED bool

        namespace: (namespace) REQUIRED str

        players: (players) REQUIRED List[str]

        server: (server) REQUIRED ModelsServer

        session_id: (session_id) REQUIRED str

        session_type: (session_type) REQUIRED str

        spectators: (spectators) REQUIRED List[str]
    """

    # region fields

    all_players: List[str]                                                                         # REQUIRED
    created_at: str                                                                                # REQUIRED
    game_session_setting: ModelsGameSessionSetting                                                 # REQUIRED
    joinable: bool                                                                                 # REQUIRED
    namespace: str                                                                                 # REQUIRED
    players: List[str]                                                                             # REQUIRED
    server: ModelsServer                                                                           # REQUIRED
    session_id: str                                                                                # REQUIRED
    session_type: str                                                                              # REQUIRED
    spectators: List[str]                                                                          # REQUIRED

    # endregion fields

    # region with_x methods

    def with_all_players(self, value: List[str]) -> ModelsCustomGameResponse:
        self.all_players = value
        return self

    def with_created_at(self, value: str) -> ModelsCustomGameResponse:
        self.created_at = value
        return self

    def with_game_session_setting(self, value: ModelsGameSessionSetting) -> ModelsCustomGameResponse:
        self.game_session_setting = value
        return self

    def with_joinable(self, value: bool) -> ModelsCustomGameResponse:
        self.joinable = value
        return self

    def with_namespace(self, value: str) -> ModelsCustomGameResponse:
        self.namespace = value
        return self

    def with_players(self, value: List[str]) -> ModelsCustomGameResponse:
        self.players = value
        return self

    def with_server(self, value: ModelsServer) -> ModelsCustomGameResponse:
        self.server = value
        return self

    def with_session_id(self, value: str) -> ModelsCustomGameResponse:
        self.session_id = value
        return self

    def with_session_type(self, value: str) -> ModelsCustomGameResponse:
        self.session_type = value
        return self

    def with_spectators(self, value: List[str]) -> ModelsCustomGameResponse:
        self.spectators = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "all_players") and self.all_players:
            result["all_players"] = [str(i0) for i0 in self.all_players]
        elif include_empty:
            result["all_players"] = []
        if hasattr(self, "created_at") and self.created_at:
            result["created_at"] = str(self.created_at)
        elif include_empty:
            result["created_at"] = str()
        if hasattr(self, "game_session_setting") and self.game_session_setting:
            result["game_session_setting"] = self.game_session_setting.to_dict(include_empty=include_empty)
        elif include_empty:
            result["game_session_setting"] = ModelsGameSessionSetting()
        if hasattr(self, "joinable") and self.joinable:
            result["joinable"] = bool(self.joinable)
        elif include_empty:
            result["joinable"] = bool()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "players") and self.players:
            result["players"] = [str(i0) for i0 in self.players]
        elif include_empty:
            result["players"] = []
        if hasattr(self, "server") and self.server:
            result["server"] = self.server.to_dict(include_empty=include_empty)
        elif include_empty:
            result["server"] = ModelsServer()
        if hasattr(self, "session_id") and self.session_id:
            result["session_id"] = str(self.session_id)
        elif include_empty:
            result["session_id"] = str()
        if hasattr(self, "session_type") and self.session_type:
            result["session_type"] = str(self.session_type)
        elif include_empty:
            result["session_type"] = str()
        if hasattr(self, "spectators") and self.spectators:
            result["spectators"] = [str(i0) for i0 in self.spectators]
        elif include_empty:
            result["spectators"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        all_players: List[str],
        created_at: str,
        game_session_setting: ModelsGameSessionSetting,
        joinable: bool,
        namespace: str,
        players: List[str],
        server: ModelsServer,
        session_id: str,
        session_type: str,
        spectators: List[str],
    ) -> ModelsCustomGameResponse:
        instance = cls()
        instance.all_players = all_players
        instance.created_at = created_at
        instance.game_session_setting = game_session_setting
        instance.joinable = joinable
        instance.namespace = namespace
        instance.players = players
        instance.server = server
        instance.session_id = session_id
        instance.session_type = session_type
        instance.spectators = spectators
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsCustomGameResponse:
        instance = cls()
        if not dict_:
            return instance
        if "all_players" in dict_ and dict_["all_players"] is not None:
            instance.all_players = [str(i0) for i0 in dict_["all_players"]]
        elif include_empty:
            instance.all_players = []
        if "created_at" in dict_ and dict_["created_at"] is not None:
            instance.created_at = str(dict_["created_at"])
        elif include_empty:
            instance.created_at = str()
        if "game_session_setting" in dict_ and dict_["game_session_setting"] is not None:
            instance.game_session_setting = ModelsGameSessionSetting.create_from_dict(dict_["game_session_setting"], include_empty=include_empty)
        elif include_empty:
            instance.game_session_setting = ModelsGameSessionSetting()
        if "joinable" in dict_ and dict_["joinable"] is not None:
            instance.joinable = bool(dict_["joinable"])
        elif include_empty:
            instance.joinable = bool()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "players" in dict_ and dict_["players"] is not None:
            instance.players = [str(i0) for i0 in dict_["players"]]
        elif include_empty:
            instance.players = []
        if "server" in dict_ and dict_["server"] is not None:
            instance.server = ModelsServer.create_from_dict(dict_["server"], include_empty=include_empty)
        elif include_empty:
            instance.server = ModelsServer()
        if "session_id" in dict_ and dict_["session_id"] is not None:
            instance.session_id = str(dict_["session_id"])
        elif include_empty:
            instance.session_id = str()
        if "session_type" in dict_ and dict_["session_type"] is not None:
            instance.session_type = str(dict_["session_type"])
        elif include_empty:
            instance.session_type = str()
        if "spectators" in dict_ and dict_["spectators"] is not None:
            instance.spectators = [str(i0) for i0 in dict_["spectators"]]
        elif include_empty:
            instance.spectators = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "all_players": "all_players",
            "created_at": "created_at",
            "game_session_setting": "game_session_setting",
            "joinable": "joinable",
            "namespace": "namespace",
            "players": "players",
            "server": "server",
            "session_id": "session_id",
            "session_type": "session_type",
            "spectators": "spectators",
        }

    # endregion static methods