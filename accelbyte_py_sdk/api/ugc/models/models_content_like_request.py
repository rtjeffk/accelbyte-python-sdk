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


class ModelsContentLikeRequest(Model):
    """Models content like request (models.ContentLikeRequest)

    Properties:
        like_status: (likeStatus) REQUIRED bool
    """

    # region fields

    like_status: bool                                                                              # REQUIRED

    # endregion fields

    # region with_x methods

    def with_like_status(self, value: bool) -> ModelsContentLikeRequest:
        self.like_status = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "like_status"):
            result["likeStatus"] = bool(self.like_status)
        elif include_empty:
            result["likeStatus"] = bool()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        like_status: bool,
    ) -> ModelsContentLikeRequest:
        instance = cls()
        instance.like_status = like_status
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsContentLikeRequest:
        instance = cls()
        if not dict_:
            return instance
        if "likeStatus" in dict_ and dict_["likeStatus"] is not None:
            instance.like_status = bool(dict_["likeStatus"])
        elif include_empty:
            instance.like_status = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "likeStatus": "like_status",
        }

    # endregion static methods