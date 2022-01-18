# justice-seasonpass-service (1.7.0)

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

from ..models.list_user_season_info import ListUserSeasonInfo
from ..models.paging import Paging


class ListUserSeasonInfoPagingSlicedResult(Model):
    """List user season info paging sliced result (ListUserSeasonInfoPagingSlicedResult)

    Properties:
        data: (data) REQUIRED List[ListUserSeasonInfo]

        paging: (paging) OPTIONAL Paging

        total: (total) OPTIONAL int
    """

    # region fields

    data: List[ListUserSeasonInfo]                                                                 # REQUIRED
    paging: Paging                                                                                 # OPTIONAL
    total: int                                                                                     # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_data(self, value: List[ListUserSeasonInfo]) -> ListUserSeasonInfoPagingSlicedResult:
        self.data = value
        return self

    def with_paging(self, value: Paging) -> ListUserSeasonInfoPagingSlicedResult:
        self.paging = value
        return self

    def with_total(self, value: int) -> ListUserSeasonInfoPagingSlicedResult:
        self.total = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "data"):
            result["data"] = [i0.to_dict(include_empty=include_empty) for i0 in self.data]
        elif include_empty:
            result["data"] = []
        if hasattr(self, "paging"):
            result["paging"] = self.paging.to_dict(include_empty=include_empty)
        elif include_empty:
            result["paging"] = Paging()
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
        data: List[ListUserSeasonInfo],
        paging: Optional[Paging] = None,
        total: Optional[int] = None,
    ) -> ListUserSeasonInfoPagingSlicedResult:
        instance = cls()
        instance.data = data
        if paging is not None:
            instance.paging = paging
        if total is not None:
            instance.total = total
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ListUserSeasonInfoPagingSlicedResult:
        instance = cls()
        if not dict_:
            return instance
        if "data" in dict_ and dict_["data"] is not None:
            instance.data = [ListUserSeasonInfo.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["data"]]
        elif include_empty:
            instance.data = []
        if "paging" in dict_ and dict_["paging"] is not None:
            instance.paging = Paging.create_from_dict(dict_["paging"], include_empty=include_empty)
        elif include_empty:
            instance.paging = Paging()
        if "total" in dict_ and dict_["total"] is not None:
            instance.total = int(dict_["total"])
        elif include_empty:
            instance.total = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "data": "data",
            "paging": "paging",
            "total": "total",
        }

    # endregion static methods
