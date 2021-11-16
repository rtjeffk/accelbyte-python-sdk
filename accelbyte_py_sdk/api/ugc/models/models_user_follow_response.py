# justice-ugc-service (1.9.0)

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


class ModelsUserFollowResponse(Model):
    """Models user follow response (models.UserFollowResponse)

    Properties:
        follow_status: (followStatus) REQUIRED bool

        user_id: (userId) REQUIRED str
    """

    # region fields

    follow_status: bool                                                                            # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_follow_status(self, value: bool) -> ModelsUserFollowResponse:
        self.follow_status = value
        return self

    def with_user_id(self, value: str) -> ModelsUserFollowResponse:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "follow_status"):
            result["followStatus"] = bool(self.follow_status)
        elif include_empty:
            result["followStatus"] = bool()
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
        follow_status: bool,
        user_id: str,
    ) -> ModelsUserFollowResponse:
        instance = cls()
        instance.follow_status = follow_status
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsUserFollowResponse:
        instance = cls()
        if not dict_:
            return instance
        if "followStatus" in dict_ and dict_["followStatus"] is not None:
            instance.follow_status = bool(dict_["followStatus"])
        elif include_empty:
            instance.follow_status = bool()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "followStatus": "follow_status",
            "userId": "user_id",
        }

    # endregion static methods
