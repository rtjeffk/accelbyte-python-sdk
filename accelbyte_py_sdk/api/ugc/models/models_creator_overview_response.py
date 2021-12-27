# justice-ugc-service (1.10.0)

# template file: justice_py_sdk_codegen/__main__.py

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


class ModelsCreatorOverviewResponse(Model):
    """Models creator overview response (models.CreatorOverviewResponse)

    Properties:
        follow_count: (followCount) REQUIRED int

        id_: (id) REQUIRED str

        namespace: (namespace) REQUIRED str
    """

    # region fields

    follow_count: int                                                                              # REQUIRED
    id_: str                                                                                       # REQUIRED
    namespace: str                                                                                 # REQUIRED

    # endregion fields

    # region with_x methods

    def with_follow_count(self, value: int) -> ModelsCreatorOverviewResponse:
        self.follow_count = value
        return self

    def with_id(self, value: str) -> ModelsCreatorOverviewResponse:
        self.id_ = value
        return self

    def with_namespace(self, value: str) -> ModelsCreatorOverviewResponse:
        self.namespace = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "follow_count"):
            result["followCount"] = int(self.follow_count)
        elif include_empty:
            result["followCount"] = int()
        if hasattr(self, "id_"):
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        follow_count: int,
        id_: str,
        namespace: str,
    ) -> ModelsCreatorOverviewResponse:
        instance = cls()
        instance.follow_count = follow_count
        instance.id_ = id_
        instance.namespace = namespace
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsCreatorOverviewResponse:
        instance = cls()
        if not dict_:
            return instance
        if "followCount" in dict_ and dict_["followCount"] is not None:
            instance.follow_count = int(dict_["followCount"])
        elif include_empty:
            instance.follow_count = int()
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "followCount": "follow_count",
            "id": "id_",
            "namespace": "namespace",
        }

    # endregion static methods
