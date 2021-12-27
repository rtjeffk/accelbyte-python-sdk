# justice-achievement-service ()

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


class ModelsAdditionalInfo(Model):
    """Models additional info (models.AdditionalInfo)

    Properties:
        number_of_achievements: (numberOfAchievements) REQUIRED int

        number_of_hidden_achievements: (numberOfHiddenAchievements) REQUIRED int

        number_of_visible_achievements: (numberOfVisibleAchievements) REQUIRED int
    """

    # region fields

    number_of_achievements: int                                                                    # REQUIRED
    number_of_hidden_achievements: int                                                             # REQUIRED
    number_of_visible_achievements: int                                                            # REQUIRED

    # endregion fields

    # region with_x methods

    def with_number_of_achievements(self, value: int) -> ModelsAdditionalInfo:
        self.number_of_achievements = value
        return self

    def with_number_of_hidden_achievements(self, value: int) -> ModelsAdditionalInfo:
        self.number_of_hidden_achievements = value
        return self

    def with_number_of_visible_achievements(self, value: int) -> ModelsAdditionalInfo:
        self.number_of_visible_achievements = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "number_of_achievements"):
            result["numberOfAchievements"] = int(self.number_of_achievements)
        elif include_empty:
            result["numberOfAchievements"] = int()
        if hasattr(self, "number_of_hidden_achievements"):
            result["numberOfHiddenAchievements"] = int(self.number_of_hidden_achievements)
        elif include_empty:
            result["numberOfHiddenAchievements"] = int()
        if hasattr(self, "number_of_visible_achievements"):
            result["numberOfVisibleAchievements"] = int(self.number_of_visible_achievements)
        elif include_empty:
            result["numberOfVisibleAchievements"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        number_of_achievements: int,
        number_of_hidden_achievements: int,
        number_of_visible_achievements: int,
    ) -> ModelsAdditionalInfo:
        instance = cls()
        instance.number_of_achievements = number_of_achievements
        instance.number_of_hidden_achievements = number_of_hidden_achievements
        instance.number_of_visible_achievements = number_of_visible_achievements
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsAdditionalInfo:
        instance = cls()
        if not dict_:
            return instance
        if "numberOfAchievements" in dict_ and dict_["numberOfAchievements"] is not None:
            instance.number_of_achievements = int(dict_["numberOfAchievements"])
        elif include_empty:
            instance.number_of_achievements = int()
        if "numberOfHiddenAchievements" in dict_ and dict_["numberOfHiddenAchievements"] is not None:
            instance.number_of_hidden_achievements = int(dict_["numberOfHiddenAchievements"])
        elif include_empty:
            instance.number_of_hidden_achievements = int()
        if "numberOfVisibleAchievements" in dict_ and dict_["numberOfVisibleAchievements"] is not None:
            instance.number_of_visible_achievements = int(dict_["numberOfVisibleAchievements"])
        elif include_empty:
            instance.number_of_visible_achievements = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "numberOfAchievements": "number_of_achievements",
            "numberOfHiddenAchievements": "number_of_hidden_achievements",
            "numberOfVisibleAchievements": "number_of_visible_achievements",
        }

    # endregion static methods
