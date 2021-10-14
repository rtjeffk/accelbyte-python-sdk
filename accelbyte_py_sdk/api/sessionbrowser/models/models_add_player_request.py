# Auto-generated at 2021-10-21T08:52:31.815355+08:00
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


class ModelsAddPlayerRequest(Model):
    """Models add player request (models.AddPlayerRequest)

    Properties:
        as_spectator: (as_spectator) REQUIRED bool

        user_id: (user_id) REQUIRED str
    """

    # region fields

    as_spectator: bool                                                                             # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_as_spectator(self, value: bool) -> ModelsAddPlayerRequest:
        self.as_spectator = value
        return self

    def with_user_id(self, value: str) -> ModelsAddPlayerRequest:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "as_spectator") and self.as_spectator:
            result["as_spectator"] = bool(self.as_spectator)
        elif include_empty:
            result["as_spectator"] = bool()
        if hasattr(self, "user_id") and self.user_id:
            result["user_id"] = str(self.user_id)
        elif include_empty:
            result["user_id"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        as_spectator: bool,
        user_id: str,
    ) -> ModelsAddPlayerRequest:
        instance = cls()
        instance.as_spectator = as_spectator
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsAddPlayerRequest:
        instance = cls()
        if not dict_:
            return instance
        if "as_spectator" in dict_ and dict_["as_spectator"] is not None:
            instance.as_spectator = bool(dict_["as_spectator"])
        elif include_empty:
            instance.as_spectator = bool()
        if "user_id" in dict_ and dict_["user_id"] is not None:
            instance.user_id = str(dict_["user_id"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "as_spectator": "as_spectator",
            "user_id": "user_id",
        }

    # endregion static methods