# Auto-generated at 2021-10-14T22:17:10.876092+08:00
# from: Justice Iam Service (4.1.0)

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

from ..models.accountcommon_pagination_v3 import AccountcommonPaginationV3
from ..models.model_assigned_user_v4_response import ModelAssignedUserV4Response


class ModelListAssignedUsersV4Response(Model):
    """Model list assigned users V4 response (model.ListAssignedUsersV4Response)

    Properties:
        data: (data) REQUIRED List[ModelAssignedUserV4Response]

        paging: (paging) REQUIRED AccountcommonPaginationV3
    """

    # region fields

    data: List[ModelAssignedUserV4Response]                                                        # REQUIRED
    paging: AccountcommonPaginationV3                                                              # REQUIRED

    # endregion fields

    # region with_x methods

    def with_data(self, value: List[ModelAssignedUserV4Response]) -> ModelListAssignedUsersV4Response:
        self.data = value
        return self

    def with_paging(self, value: AccountcommonPaginationV3) -> ModelListAssignedUsersV4Response:
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
            result["paging"] = AccountcommonPaginationV3()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        data: List[ModelAssignedUserV4Response],
        paging: AccountcommonPaginationV3,
    ) -> ModelListAssignedUsersV4Response:
        instance = cls()
        instance.data = data
        instance.paging = paging
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelListAssignedUsersV4Response:
        instance = cls()
        if not dict_:
            return instance
        if "data" in dict_ and dict_["data"] is not None:
            instance.data = [ModelAssignedUserV4Response.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["data"]]
        elif include_empty:
            instance.data = []
        if "paging" in dict_ and dict_["paging"] is not None:
            instance.paging = AccountcommonPaginationV3.create_from_dict(dict_["paging"], include_empty=include_empty)
        elif include_empty:
            instance.paging = AccountcommonPaginationV3()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "data": "data",
            "paging": "paging",
        }

    # endregion static methods
