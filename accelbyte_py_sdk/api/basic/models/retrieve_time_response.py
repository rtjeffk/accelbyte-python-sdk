# Auto-generated at 2021-10-21T08:52:32.923085+08:00
# from: Justice basic Service (1.23.0)

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


class RetrieveTimeResponse(Model):
    """Retrieve time response (RetrieveTimeResponse)

    Properties:
        current_time: (currentTime) OPTIONAL str
    """

    # region fields

    current_time: str                                                                              # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_current_time(self, value: str) -> RetrieveTimeResponse:
        self.current_time = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "current_time") and self.current_time:
            result["currentTime"] = str(self.current_time)
        elif include_empty:
            result["currentTime"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        current_time: Optional[str] = None,
    ) -> RetrieveTimeResponse:
        instance = cls()
        if current_time is not None:
            instance.current_time = current_time
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> RetrieveTimeResponse:
        instance = cls()
        if not dict_:
            return instance
        if "currentTime" in dict_ and dict_["currentTime"] is not None:
            instance.current_time = str(dict_["currentTime"])
        elif include_empty:
            instance.current_time = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "currentTime": "current_time",
        }

    # endregion static methods