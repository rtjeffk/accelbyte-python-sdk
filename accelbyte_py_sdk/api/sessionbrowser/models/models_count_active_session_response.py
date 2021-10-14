# Auto-generated at 2021-10-21T08:52:31.818311+08:00
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


class ModelsCountActiveSessionResponse(Model):
    """Models count active session response (models.CountActiveSessionResponse)

    Properties:
        custom_game: (custom_game) REQUIRED int

        matchmaking_game: (matchmaking_game) REQUIRED int

        total: (total) REQUIRED int
    """

    # region fields

    custom_game: int                                                                               # REQUIRED
    matchmaking_game: int                                                                          # REQUIRED
    total: int                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_custom_game(self, value: int) -> ModelsCountActiveSessionResponse:
        self.custom_game = value
        return self

    def with_matchmaking_game(self, value: int) -> ModelsCountActiveSessionResponse:
        self.matchmaking_game = value
        return self

    def with_total(self, value: int) -> ModelsCountActiveSessionResponse:
        self.total = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "custom_game") and self.custom_game:
            result["custom_game"] = int(self.custom_game)
        elif include_empty:
            result["custom_game"] = int()
        if hasattr(self, "matchmaking_game") and self.matchmaking_game:
            result["matchmaking_game"] = int(self.matchmaking_game)
        elif include_empty:
            result["matchmaking_game"] = int()
        if hasattr(self, "total") and self.total:
            result["total"] = int(self.total)
        elif include_empty:
            result["total"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        custom_game: int,
        matchmaking_game: int,
        total: int,
    ) -> ModelsCountActiveSessionResponse:
        instance = cls()
        instance.custom_game = custom_game
        instance.matchmaking_game = matchmaking_game
        instance.total = total
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsCountActiveSessionResponse:
        instance = cls()
        if not dict_:
            return instance
        if "custom_game" in dict_ and dict_["custom_game"] is not None:
            instance.custom_game = int(dict_["custom_game"])
        elif include_empty:
            instance.custom_game = int()
        if "matchmaking_game" in dict_ and dict_["matchmaking_game"] is not None:
            instance.matchmaking_game = int(dict_["matchmaking_game"])
        elif include_empty:
            instance.matchmaking_game = int()
        if "total" in dict_ and dict_["total"] is not None:
            instance.total = int(dict_["total"])
        elif include_empty:
            instance.total = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "custom_game": "custom_game",
            "matchmaking_game": "matchmaking_game",
            "total": "total",
        }

    # endregion static methods