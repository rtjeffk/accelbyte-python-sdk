# justice-platform-service (3.37.1)

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


class OrderStatistics(Model):
    """Order statistics (OrderStatistics)

    Properties:
        status_count: (statusCount) REQUIRED Dict[str, int]

        total: (total) REQUIRED int
    """

    # region fields

    status_count: Dict[str, int]                                                                   # REQUIRED
    total: int                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_status_count(self, value: Dict[str, int]) -> OrderStatistics:
        self.status_count = value
        return self

    def with_total(self, value: int) -> OrderStatistics:
        self.total = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "status_count"):
            result["statusCount"] = {str(k0): int(v0) for k0, v0 in self.status_count.items()}
        elif include_empty:
            result["statusCount"] = {}
        if hasattr(self, "total"):
            result["total"] = int(self.total)
        elif include_empty:
            result["total"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        status_count: Dict[str, int],
        total: int,
    ) -> OrderStatistics:
        instance = cls()
        instance.status_count = status_count
        instance.total = total
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> OrderStatistics:
        instance = cls()
        if not dict_:
            return instance
        if "statusCount" in dict_ and dict_["statusCount"] is not None:
            instance.status_count = {str(k0): int(v0) for k0, v0 in dict_["statusCount"].items()}
        elif include_empty:
            instance.status_count = {}
        if "total" in dict_ and dict_["total"] is not None:
            instance.total = int(dict_["total"])
        elif include_empty:
            instance.total = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "statusCount": "status_count",
            "total": "total",
        }

    # endregion static methods
