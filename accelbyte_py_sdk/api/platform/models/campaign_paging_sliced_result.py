# Auto-generated at 2021-10-21T08:52:30.635669+08:00
# from: Justice platform Service (3.34.0)

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

from ..models.campaign_info import CampaignInfo
from ..models.paging import Paging


class CampaignPagingSlicedResult(Model):
    """Campaign paging sliced result (CampaignPagingSlicedResult)

    Properties:
        data: (data) REQUIRED List[CampaignInfo]

        paging: (paging) OPTIONAL Paging
    """

    # region fields

    data: List[CampaignInfo]                                                                       # REQUIRED
    paging: Paging                                                                                 # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_data(self, value: List[CampaignInfo]) -> CampaignPagingSlicedResult:
        self.data = value
        return self

    def with_paging(self, value: Paging) -> CampaignPagingSlicedResult:
        self.paging = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "data") and self.data:
            result["data"] = [i0.to_dict(include_empty=include_empty) for i0 in self.data]
        elif include_empty:
            result["data"] = []
        if hasattr(self, "paging") and self.paging:
            result["paging"] = self.paging.to_dict(include_empty=include_empty)
        elif include_empty:
            result["paging"] = Paging()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        data: List[CampaignInfo],
        paging: Optional[Paging] = None,
    ) -> CampaignPagingSlicedResult:
        instance = cls()
        instance.data = data
        if paging is not None:
            instance.paging = paging
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> CampaignPagingSlicedResult:
        instance = cls()
        if not dict_:
            return instance
        if "data" in dict_ and dict_["data"] is not None:
            instance.data = [CampaignInfo.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["data"]]
        elif include_empty:
            instance.data = []
        if "paging" in dict_ and dict_["paging"] is not None:
            instance.paging = Paging.create_from_dict(dict_["paging"], include_empty=include_empty)
        elif include_empty:
            instance.paging = Paging()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "data": "data",
            "paging": "paging",
        }

    # endregion static methods