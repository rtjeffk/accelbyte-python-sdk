# justice-seasonpass-service (1.6.0)

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

from ..models.season_summary import SeasonSummary


class ListUserSeasonInfo(Model):
    """A DTO object for listing user season data. (ListUserSeasonInfo)

    Properties:
        cleared: (cleared) REQUIRED bool

        current_tier_index: (currentTierIndex) REQUIRED int

        enrolled_at: (enrolledAt) REQUIRED str

        id_: (id) REQUIRED str

        last_tier_index: (lastTierIndex) REQUIRED int

        namespace: (namespace) REQUIRED str

        season: (season) REQUIRED SeasonSummary

        season_id: (seasonId) REQUIRED str

        user_id: (userId) REQUIRED str
    """

    # region fields

    cleared: bool                                                                                  # REQUIRED
    current_tier_index: int                                                                        # REQUIRED
    enrolled_at: str                                                                               # REQUIRED
    id_: str                                                                                       # REQUIRED
    last_tier_index: int                                                                           # REQUIRED
    namespace: str                                                                                 # REQUIRED
    season: SeasonSummary                                                                          # REQUIRED
    season_id: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_cleared(self, value: bool) -> ListUserSeasonInfo:
        self.cleared = value
        return self

    def with_current_tier_index(self, value: int) -> ListUserSeasonInfo:
        self.current_tier_index = value
        return self

    def with_enrolled_at(self, value: str) -> ListUserSeasonInfo:
        self.enrolled_at = value
        return self

    def with_id(self, value: str) -> ListUserSeasonInfo:
        self.id_ = value
        return self

    def with_last_tier_index(self, value: int) -> ListUserSeasonInfo:
        self.last_tier_index = value
        return self

    def with_namespace(self, value: str) -> ListUserSeasonInfo:
        self.namespace = value
        return self

    def with_season(self, value: SeasonSummary) -> ListUserSeasonInfo:
        self.season = value
        return self

    def with_season_id(self, value: str) -> ListUserSeasonInfo:
        self.season_id = value
        return self

    def with_user_id(self, value: str) -> ListUserSeasonInfo:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "cleared"):
            result["cleared"] = bool(self.cleared)
        elif include_empty:
            result["cleared"] = bool()
        if hasattr(self, "current_tier_index"):
            result["currentTierIndex"] = int(self.current_tier_index)
        elif include_empty:
            result["currentTierIndex"] = int()
        if hasattr(self, "enrolled_at"):
            result["enrolledAt"] = str(self.enrolled_at)
        elif include_empty:
            result["enrolledAt"] = str()
        if hasattr(self, "id_"):
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "last_tier_index"):
            result["lastTierIndex"] = int(self.last_tier_index)
        elif include_empty:
            result["lastTierIndex"] = int()
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "season"):
            result["season"] = self.season.to_dict(include_empty=include_empty)
        elif include_empty:
            result["season"] = SeasonSummary()
        if hasattr(self, "season_id"):
            result["seasonId"] = str(self.season_id)
        elif include_empty:
            result["seasonId"] = str()
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
        cleared: bool,
        current_tier_index: int,
        enrolled_at: str,
        id_: str,
        last_tier_index: int,
        namespace: str,
        season: SeasonSummary,
        season_id: str,
        user_id: str,
    ) -> ListUserSeasonInfo:
        instance = cls()
        instance.cleared = cleared
        instance.current_tier_index = current_tier_index
        instance.enrolled_at = enrolled_at
        instance.id_ = id_
        instance.last_tier_index = last_tier_index
        instance.namespace = namespace
        instance.season = season
        instance.season_id = season_id
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ListUserSeasonInfo:
        instance = cls()
        if not dict_:
            return instance
        if "cleared" in dict_ and dict_["cleared"] is not None:
            instance.cleared = bool(dict_["cleared"])
        elif include_empty:
            instance.cleared = bool()
        if "currentTierIndex" in dict_ and dict_["currentTierIndex"] is not None:
            instance.current_tier_index = int(dict_["currentTierIndex"])
        elif include_empty:
            instance.current_tier_index = int()
        if "enrolledAt" in dict_ and dict_["enrolledAt"] is not None:
            instance.enrolled_at = str(dict_["enrolledAt"])
        elif include_empty:
            instance.enrolled_at = str()
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "lastTierIndex" in dict_ and dict_["lastTierIndex"] is not None:
            instance.last_tier_index = int(dict_["lastTierIndex"])
        elif include_empty:
            instance.last_tier_index = int()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "season" in dict_ and dict_["season"] is not None:
            instance.season = SeasonSummary.create_from_dict(dict_["season"], include_empty=include_empty)
        elif include_empty:
            instance.season = SeasonSummary()
        if "seasonId" in dict_ and dict_["seasonId"] is not None:
            instance.season_id = str(dict_["seasonId"])
        elif include_empty:
            instance.season_id = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "cleared": "cleared",
            "currentTierIndex": "current_tier_index",
            "enrolledAt": "enrolled_at",
            "id": "id_",
            "lastTierIndex": "last_tier_index",
            "namespace": "namespace",
            "season": "season",
            "seasonId": "season_id",
            "userId": "user_id",
        }

    # endregion static methods