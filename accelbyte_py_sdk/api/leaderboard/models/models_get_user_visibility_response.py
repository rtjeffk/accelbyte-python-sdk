# justice-leaderboard-service (2.11.0)

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


class ModelsGetUserVisibilityResponse(Model):
    """Models get user visibility response (models.GetUserVisibilityResponse)

    Properties:
        namespace: (namespace) REQUIRED str

        user_id: (userId) REQUIRED str

        visibility: (visibility) REQUIRED bool
    """

    # region fields

    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED
    visibility: bool                                                                               # REQUIRED

    # endregion fields

    # region with_x methods

    def with_namespace(self, value: str) -> ModelsGetUserVisibilityResponse:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> ModelsGetUserVisibilityResponse:
        self.user_id = value
        return self

    def with_visibility(self, value: bool) -> ModelsGetUserVisibilityResponse:
        self.visibility = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id"):
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
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
        namespace: str,
        user_id: str,
        visibility: bool,
    ) -> ModelsGetUserVisibilityResponse:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        instance.visibility = visibility
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsGetUserVisibilityResponse:
        instance = cls()
        if not dict_:
            return instance
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "visibility" in dict_ and dict_["visibility"] is not None:
            instance.visibility = bool(dict_["visibility"])
        elif include_empty:
            instance.visibility = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "userId": "user_id",
            "visibility": "visibility",
        }

    # endregion static methods