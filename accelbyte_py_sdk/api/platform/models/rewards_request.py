# justice-platform-service (4.1.1)

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

from ..models.platform_reward import PlatformReward


class RewardsRequest(Model):
    """A DTO object for rewards request API call. (RewardsRequest)

    Properties:
        rewards: (rewards) REQUIRED List[PlatformReward]

        source: (source) OPTIONAL str
    """

    # region fields

    rewards: List[PlatformReward]                                                                  # REQUIRED
    source: str                                                                                    # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_rewards(self, value: List[PlatformReward]) -> RewardsRequest:
        self.rewards = value
        return self

    def with_source(self, value: str) -> RewardsRequest:
        self.source = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "rewards"):
            result["rewards"] = [i0.to_dict(include_empty=include_empty) for i0 in self.rewards]
        elif include_empty:
            result["rewards"] = []
        if hasattr(self, "source"):
            result["source"] = str(self.source)
        elif include_empty:
            result["source"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        rewards: List[PlatformReward],
        source: Optional[str] = None,
    ) -> RewardsRequest:
        instance = cls()
        instance.rewards = rewards
        if source is not None:
            instance.source = source
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> RewardsRequest:
        instance = cls()
        if not dict_:
            return instance
        if "rewards" in dict_ and dict_["rewards"] is not None:
            instance.rewards = [PlatformReward.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["rewards"]]
        elif include_empty:
            instance.rewards = []
        if "source" in dict_ and dict_["source"] is not None:
            instance.source = str(dict_["source"])
        elif include_empty:
            instance.source = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, RewardsRequest]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[RewardsRequest]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[RewardsRequest, List[RewardsRequest]]:
        if many:
            if isinstance(any_, dict):
                cls.create_many_from_dict(any_, include_empty=include_empty)
            elif isinstance(any_, list):
                cls.create_many_from_list(any_, include_empty=include_empty)
        else:
            return cls.create_from_dict(any_, include_empty=include_empty)

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "rewards": "rewards",
            "source": "source",
        }

    # endregion static methods