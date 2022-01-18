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


class ModelsUpdateUserPointAdminV1Response(Model):
    """Models update user point admin V1 response (models.UpdateUserPointAdminV1Response)

    Properties:
        point: (point) REQUIRED float

        user_id: (userId) REQUIRED str
    """

    # region fields

    point: float                                                                                   # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_point(self, value: float) -> ModelsUpdateUserPointAdminV1Response:
        self.point = value
        return self

    def with_user_id(self, value: str) -> ModelsUpdateUserPointAdminV1Response:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "point"):
            result["point"] = float(self.point)
        elif include_empty:
            result["point"] = float()
        if hasattr(self, "user_id"):
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        point: float,
        user_id: str,
    ) -> ModelsUpdateUserPointAdminV1Response:
        instance = cls()
        instance.point = point
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsUpdateUserPointAdminV1Response:
        instance = cls()
        if not dict_:
            return instance
        if "point" in dict_ and dict_["point"] is not None:
            instance.point = float(dict_["point"])
        elif include_empty:
            instance.point = float()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "point": "point",
            "userId": "user_id",
        }

    # endregion static methods
