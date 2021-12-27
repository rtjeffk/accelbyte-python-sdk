# justice-leaderboard-service (2.11.0)

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

from ..models.models_daily_config import ModelsDailyConfig
from ..models.models_monthly_config import ModelsMonthlyConfig
from ..models.models_weekly_config import ModelsWeeklyConfig


class ModelsLeaderboardConfigReq(Model):
    """Models leaderboard config req (models.LeaderboardConfigReq)

    Properties:
        daily: (daily) REQUIRED ModelsDailyConfig

        descending: (descending) REQUIRED bool

        icon_url: (iconURL) REQUIRED str

        leaderboard_code: (leaderboardCode) REQUIRED str

        monthly: (monthly) REQUIRED ModelsMonthlyConfig

        name: (name) REQUIRED str

        season_period: (seasonPeriod) REQUIRED int

        start_time: (startTime) REQUIRED str

        stat_code: (statCode) REQUIRED str

        weekly: (weekly) REQUIRED ModelsWeeklyConfig
    """

    # region fields

    daily: ModelsDailyConfig                                                                       # REQUIRED
    descending: bool                                                                               # REQUIRED
    icon_url: str                                                                                  # REQUIRED
    leaderboard_code: str                                                                          # REQUIRED
    monthly: ModelsMonthlyConfig                                                                   # REQUIRED
    name: str                                                                                      # REQUIRED
    season_period: int                                                                             # REQUIRED
    start_time: str                                                                                # REQUIRED
    stat_code: str                                                                                 # REQUIRED
    weekly: ModelsWeeklyConfig                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_daily(self, value: ModelsDailyConfig) -> ModelsLeaderboardConfigReq:
        self.daily = value
        return self

    def with_descending(self, value: bool) -> ModelsLeaderboardConfigReq:
        self.descending = value
        return self

    def with_icon_url(self, value: str) -> ModelsLeaderboardConfigReq:
        self.icon_url = value
        return self

    def with_leaderboard_code(self, value: str) -> ModelsLeaderboardConfigReq:
        self.leaderboard_code = value
        return self

    def with_monthly(self, value: ModelsMonthlyConfig) -> ModelsLeaderboardConfigReq:
        self.monthly = value
        return self

    def with_name(self, value: str) -> ModelsLeaderboardConfigReq:
        self.name = value
        return self

    def with_season_period(self, value: int) -> ModelsLeaderboardConfigReq:
        self.season_period = value
        return self

    def with_start_time(self, value: str) -> ModelsLeaderboardConfigReq:
        self.start_time = value
        return self

    def with_stat_code(self, value: str) -> ModelsLeaderboardConfigReq:
        self.stat_code = value
        return self

    def with_weekly(self, value: ModelsWeeklyConfig) -> ModelsLeaderboardConfigReq:
        self.weekly = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "daily"):
            result["daily"] = self.daily.to_dict(include_empty=include_empty)
        elif include_empty:
            result["daily"] = ModelsDailyConfig()
        if hasattr(self, "descending"):
            result["descending"] = bool(self.descending)
        elif include_empty:
            result["descending"] = bool()
        if hasattr(self, "icon_url"):
            result["iconURL"] = str(self.icon_url)
        elif include_empty:
            result["iconURL"] = str()
        if hasattr(self, "leaderboard_code"):
            result["leaderboardCode"] = str(self.leaderboard_code)
        elif include_empty:
            result["leaderboardCode"] = str()
        if hasattr(self, "monthly"):
            result["monthly"] = self.monthly.to_dict(include_empty=include_empty)
        elif include_empty:
            result["monthly"] = ModelsMonthlyConfig()
        if hasattr(self, "name"):
            result["name"] = str(self.name)
        elif include_empty:
            result["name"] = str()
        if hasattr(self, "season_period"):
            result["seasonPeriod"] = int(self.season_period)
        elif include_empty:
            result["seasonPeriod"] = int()
        if hasattr(self, "start_time"):
            result["startTime"] = str(self.start_time)
        elif include_empty:
            result["startTime"] = str()
        if hasattr(self, "stat_code"):
            result["statCode"] = str(self.stat_code)
        elif include_empty:
            result["statCode"] = str()
        if hasattr(self, "weekly"):
            result["weekly"] = self.weekly.to_dict(include_empty=include_empty)
        elif include_empty:
            result["weekly"] = ModelsWeeklyConfig()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        daily: ModelsDailyConfig,
        descending: bool,
        icon_url: str,
        leaderboard_code: str,
        monthly: ModelsMonthlyConfig,
        name: str,
        season_period: int,
        start_time: str,
        stat_code: str,
        weekly: ModelsWeeklyConfig,
    ) -> ModelsLeaderboardConfigReq:
        instance = cls()
        instance.daily = daily
        instance.descending = descending
        instance.icon_url = icon_url
        instance.leaderboard_code = leaderboard_code
        instance.monthly = monthly
        instance.name = name
        instance.season_period = season_period
        instance.start_time = start_time
        instance.stat_code = stat_code
        instance.weekly = weekly
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsLeaderboardConfigReq:
        instance = cls()
        if not dict_:
            return instance
        if "daily" in dict_ and dict_["daily"] is not None:
            instance.daily = ModelsDailyConfig.create_from_dict(dict_["daily"], include_empty=include_empty)
        elif include_empty:
            instance.daily = ModelsDailyConfig()
        if "descending" in dict_ and dict_["descending"] is not None:
            instance.descending = bool(dict_["descending"])
        elif include_empty:
            instance.descending = bool()
        if "iconURL" in dict_ and dict_["iconURL"] is not None:
            instance.icon_url = str(dict_["iconURL"])
        elif include_empty:
            instance.icon_url = str()
        if "leaderboardCode" in dict_ and dict_["leaderboardCode"] is not None:
            instance.leaderboard_code = str(dict_["leaderboardCode"])
        elif include_empty:
            instance.leaderboard_code = str()
        if "monthly" in dict_ and dict_["monthly"] is not None:
            instance.monthly = ModelsMonthlyConfig.create_from_dict(dict_["monthly"], include_empty=include_empty)
        elif include_empty:
            instance.monthly = ModelsMonthlyConfig()
        if "name" in dict_ and dict_["name"] is not None:
            instance.name = str(dict_["name"])
        elif include_empty:
            instance.name = str()
        if "seasonPeriod" in dict_ and dict_["seasonPeriod"] is not None:
            instance.season_period = int(dict_["seasonPeriod"])
        elif include_empty:
            instance.season_period = int()
        if "startTime" in dict_ and dict_["startTime"] is not None:
            instance.start_time = str(dict_["startTime"])
        elif include_empty:
            instance.start_time = str()
        if "statCode" in dict_ and dict_["statCode"] is not None:
            instance.stat_code = str(dict_["statCode"])
        elif include_empty:
            instance.stat_code = str()
        if "weekly" in dict_ and dict_["weekly"] is not None:
            instance.weekly = ModelsWeeklyConfig.create_from_dict(dict_["weekly"], include_empty=include_empty)
        elif include_empty:
            instance.weekly = ModelsWeeklyConfig()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "daily": "daily",
            "descending": "descending",
            "iconURL": "icon_url",
            "leaderboardCode": "leaderboard_code",
            "monthly": "monthly",
            "name": "name",
            "seasonPeriod": "season_period",
            "startTime": "start_time",
            "statCode": "stat_code",
            "weekly": "weekly",
        }

    # endregion static methods
