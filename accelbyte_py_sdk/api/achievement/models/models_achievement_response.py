# justice-achievement-service (2.6.0)

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

from ..models.models_icon import ModelsIcon


class ModelsAchievementResponse(Model):
    """Models achievement response (models.AchievementResponse)

    Properties:
        achievement_code: (achievementCode) REQUIRED str

        created_at: (createdAt) REQUIRED str

        default_language: (defaultLanguage) REQUIRED str

        description: (description) REQUIRED Dict[str, str]

        hidden: (hidden) REQUIRED bool

        incremental: (incremental) REQUIRED bool

        list_order: (listOrder) REQUIRED int

        locked_icons: (lockedIcons) REQUIRED List[ModelsIcon]

        name: (name) REQUIRED Dict[str, str]

        namespace: (namespace) REQUIRED str

        tags: (tags) REQUIRED List[str]

        unlocked_icons: (unlockedIcons) REQUIRED List[ModelsIcon]

        updated_at: (updatedAt) REQUIRED str

        goal_value: (goalValue) OPTIONAL float

        stat_code: (statCode) OPTIONAL str
    """

    # region fields

    achievement_code: str                                                                          # REQUIRED
    created_at: str                                                                                # REQUIRED
    default_language: str                                                                          # REQUIRED
    description: Dict[str, str]                                                                    # REQUIRED
    hidden: bool                                                                                   # REQUIRED
    incremental: bool                                                                              # REQUIRED
    list_order: int                                                                                # REQUIRED
    locked_icons: List[ModelsIcon]                                                                 # REQUIRED
    name: Dict[str, str]                                                                           # REQUIRED
    namespace: str                                                                                 # REQUIRED
    tags: List[str]                                                                                # REQUIRED
    unlocked_icons: List[ModelsIcon]                                                               # REQUIRED
    updated_at: str                                                                                # REQUIRED
    goal_value: float                                                                              # OPTIONAL
    stat_code: str                                                                                 # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_achievement_code(self, value: str) -> ModelsAchievementResponse:
        self.achievement_code = value
        return self

    def with_created_at(self, value: str) -> ModelsAchievementResponse:
        self.created_at = value
        return self

    def with_default_language(self, value: str) -> ModelsAchievementResponse:
        self.default_language = value
        return self

    def with_description(self, value: Dict[str, str]) -> ModelsAchievementResponse:
        self.description = value
        return self

    def with_hidden(self, value: bool) -> ModelsAchievementResponse:
        self.hidden = value
        return self

    def with_incremental(self, value: bool) -> ModelsAchievementResponse:
        self.incremental = value
        return self

    def with_list_order(self, value: int) -> ModelsAchievementResponse:
        self.list_order = value
        return self

    def with_locked_icons(self, value: List[ModelsIcon]) -> ModelsAchievementResponse:
        self.locked_icons = value
        return self

    def with_name(self, value: Dict[str, str]) -> ModelsAchievementResponse:
        self.name = value
        return self

    def with_namespace(self, value: str) -> ModelsAchievementResponse:
        self.namespace = value
        return self

    def with_tags(self, value: List[str]) -> ModelsAchievementResponse:
        self.tags = value
        return self

    def with_unlocked_icons(self, value: List[ModelsIcon]) -> ModelsAchievementResponse:
        self.unlocked_icons = value
        return self

    def with_updated_at(self, value: str) -> ModelsAchievementResponse:
        self.updated_at = value
        return self

    def with_goal_value(self, value: float) -> ModelsAchievementResponse:
        self.goal_value = value
        return self

    def with_stat_code(self, value: str) -> ModelsAchievementResponse:
        self.stat_code = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "achievement_code"):
            result["achievementCode"] = str(self.achievement_code)
        elif include_empty:
            result["achievementCode"] = str()
        if hasattr(self, "created_at"):
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "default_language"):
            result["defaultLanguage"] = str(self.default_language)
        elif include_empty:
            result["defaultLanguage"] = str()
        if hasattr(self, "description"):
            result["description"] = {str(k0): str(v0) for k0, v0 in self.description.items()}
        elif include_empty:
            result["description"] = {}
        if hasattr(self, "hidden"):
            result["hidden"] = bool(self.hidden)
        elif include_empty:
            result["hidden"] = bool()
        if hasattr(self, "incremental"):
            result["incremental"] = bool(self.incremental)
        elif include_empty:
            result["incremental"] = bool()
        if hasattr(self, "list_order"):
            result["listOrder"] = int(self.list_order)
        elif include_empty:
            result["listOrder"] = int()
        if hasattr(self, "locked_icons"):
            result["lockedIcons"] = [i0.to_dict(include_empty=include_empty) for i0 in self.locked_icons]
        elif include_empty:
            result["lockedIcons"] = []
        if hasattr(self, "name"):
            result["name"] = {str(k0): str(v0) for k0, v0 in self.name.items()}
        elif include_empty:
            result["name"] = {}
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "tags"):
            result["tags"] = [str(i0) for i0 in self.tags]
        elif include_empty:
            result["tags"] = []
        if hasattr(self, "unlocked_icons"):
            result["unlockedIcons"] = [i0.to_dict(include_empty=include_empty) for i0 in self.unlocked_icons]
        elif include_empty:
            result["unlockedIcons"] = []
        if hasattr(self, "updated_at"):
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        if hasattr(self, "goal_value"):
            result["goalValue"] = float(self.goal_value)
        elif include_empty:
            result["goalValue"] = float()
        if hasattr(self, "stat_code"):
            result["statCode"] = str(self.stat_code)
        elif include_empty:
            result["statCode"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        achievement_code: str,
        created_at: str,
        default_language: str,
        description: Dict[str, str],
        hidden: bool,
        incremental: bool,
        list_order: int,
        locked_icons: List[ModelsIcon],
        name: Dict[str, str],
        namespace: str,
        tags: List[str],
        unlocked_icons: List[ModelsIcon],
        updated_at: str,
        goal_value: Optional[float] = None,
        stat_code: Optional[str] = None,
    ) -> ModelsAchievementResponse:
        instance = cls()
        instance.achievement_code = achievement_code
        instance.created_at = created_at
        instance.default_language = default_language
        instance.description = description
        instance.hidden = hidden
        instance.incremental = incremental
        instance.list_order = list_order
        instance.locked_icons = locked_icons
        instance.name = name
        instance.namespace = namespace
        instance.tags = tags
        instance.unlocked_icons = unlocked_icons
        instance.updated_at = updated_at
        if goal_value is not None:
            instance.goal_value = goal_value
        if stat_code is not None:
            instance.stat_code = stat_code
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsAchievementResponse:
        instance = cls()
        if not dict_:
            return instance
        if "achievementCode" in dict_ and dict_["achievementCode"] is not None:
            instance.achievement_code = str(dict_["achievementCode"])
        elif include_empty:
            instance.achievement_code = str()
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "defaultLanguage" in dict_ and dict_["defaultLanguage"] is not None:
            instance.default_language = str(dict_["defaultLanguage"])
        elif include_empty:
            instance.default_language = str()
        if "description" in dict_ and dict_["description"] is not None:
            instance.description = {str(k0): str(v0) for k0, v0 in dict_["description"].items()}
        elif include_empty:
            instance.description = {}
        if "hidden" in dict_ and dict_["hidden"] is not None:
            instance.hidden = bool(dict_["hidden"])
        elif include_empty:
            instance.hidden = bool()
        if "incremental" in dict_ and dict_["incremental"] is not None:
            instance.incremental = bool(dict_["incremental"])
        elif include_empty:
            instance.incremental = bool()
        if "listOrder" in dict_ and dict_["listOrder"] is not None:
            instance.list_order = int(dict_["listOrder"])
        elif include_empty:
            instance.list_order = int()
        if "lockedIcons" in dict_ and dict_["lockedIcons"] is not None:
            instance.locked_icons = [ModelsIcon.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["lockedIcons"]]
        elif include_empty:
            instance.locked_icons = []
        if "name" in dict_ and dict_["name"] is not None:
            instance.name = {str(k0): str(v0) for k0, v0 in dict_["name"].items()}
        elif include_empty:
            instance.name = {}
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "tags" in dict_ and dict_["tags"] is not None:
            instance.tags = [str(i0) for i0 in dict_["tags"]]
        elif include_empty:
            instance.tags = []
        if "unlockedIcons" in dict_ and dict_["unlockedIcons"] is not None:
            instance.unlocked_icons = [ModelsIcon.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["unlockedIcons"]]
        elif include_empty:
            instance.unlocked_icons = []
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        if "goalValue" in dict_ and dict_["goalValue"] is not None:
            instance.goal_value = float(dict_["goalValue"])
        elif include_empty:
            instance.goal_value = float()
        if "statCode" in dict_ and dict_["statCode"] is not None:
            instance.stat_code = str(dict_["statCode"])
        elif include_empty:
            instance.stat_code = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "achievementCode": "achievement_code",
            "createdAt": "created_at",
            "defaultLanguage": "default_language",
            "description": "description",
            "hidden": "hidden",
            "incremental": "incremental",
            "listOrder": "list_order",
            "lockedIcons": "locked_icons",
            "name": "name",
            "namespace": "namespace",
            "tags": "tags",
            "unlockedIcons": "unlocked_icons",
            "updatedAt": "updated_at",
            "goalValue": "goal_value",
            "statCode": "stat_code",
        }

    # endregion static methods