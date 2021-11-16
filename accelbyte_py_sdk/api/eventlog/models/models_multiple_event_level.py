# justice-event-log-service (1.18.3)

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

from ..models.models_event_level import ModelsEventLevel


class ModelsMultipleEventLevel(Model):
    """Models multiple event level (models.MultipleEventLevel)

    Properties:
        event_level: (EventLevel) REQUIRED List[ModelsEventLevel]
    """

    # region fields

    event_level: List[ModelsEventLevel]                                                            # REQUIRED

    # endregion fields

    # region with_x methods

    def with_event_level(self, value: List[ModelsEventLevel]) -> ModelsMultipleEventLevel:
        self.event_level = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "event_level"):
            result["EventLevel"] = [i0.to_dict(include_empty=include_empty) for i0 in self.event_level]
        elif include_empty:
            result["EventLevel"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        event_level: List[ModelsEventLevel],
    ) -> ModelsMultipleEventLevel:
        instance = cls()
        instance.event_level = event_level
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsMultipleEventLevel:
        instance = cls()
        if not dict_:
            return instance
        if "EventLevel" in dict_ and dict_["EventLevel"] is not None:
            instance.event_level = [ModelsEventLevel.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["EventLevel"]]
        elif include_empty:
            instance.event_level = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "EventLevel": "event_level",
        }

    # endregion static methods
