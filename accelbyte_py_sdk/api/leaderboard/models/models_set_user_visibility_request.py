# justice-leaderboard-service (2.11.2)

# template file: justice_py_sdk_codegen/__main__.py

# Copyright (c) 2018 - 2022 AccelByte Inc. All Rights Reserved.
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


class ModelsSetUserVisibilityRequest(Model):
    """Models set user visibility request (models.SetUserVisibilityRequest)

    Properties:
        visibility: (visibility) REQUIRED bool
    """

    # region fields

    visibility: bool                                                                               # REQUIRED

    # endregion fields

    # region with_x methods

    def with_visibility(self, value: bool) -> ModelsSetUserVisibilityRequest:
        self.visibility = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "visibility"):
            result["visibility"] = bool(self.visibility)
        elif include_empty:
            result["visibility"] = bool()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        visibility: bool,
    ) -> ModelsSetUserVisibilityRequest:
        instance = cls()
        instance.visibility = visibility
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsSetUserVisibilityRequest:
        instance = cls()
        if not dict_:
            return instance
        if "visibility" in dict_ and dict_["visibility"] is not None:
            instance.visibility = bool(dict_["visibility"])
        elif include_empty:
            instance.visibility = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "visibility": "visibility",
        }

    # endregion static methods
