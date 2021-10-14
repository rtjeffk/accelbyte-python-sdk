# Auto-generated at 2021-10-14T22:17:08.940300+08:00
# from: Justice DsmController Service (2.4.0)

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


class ModelsCountSessionResponse(Model):
    """Models count session response (models.CountSessionResponse)

    Properties:
        count: (count) REQUIRED int
    """

    # region fields

    count: int                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_count(self, value: int) -> ModelsCountSessionResponse:
        self.count = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "count") and self.count:
            result["count"] = int(self.count)
        elif include_empty:
            result["count"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        count: int,
    ) -> ModelsCountSessionResponse:
        instance = cls()
        instance.count = count
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsCountSessionResponse:
        instance = cls()
        if not dict_:
            return instance
        if "count" in dict_ and dict_["count"] is not None:
            instance.count = int(dict_["count"])
        elif include_empty:
            instance.count = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "count": "count",
        }

    # endregion static methods
