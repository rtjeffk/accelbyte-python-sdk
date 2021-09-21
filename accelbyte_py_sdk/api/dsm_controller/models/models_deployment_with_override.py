# Auto-generated at 2021-09-21T14:10:33.097578+08:00
# from: Justice DsmController Service (2.4.0)

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

from ..models.models_deployment_config import ModelsDeploymentConfig


class ModelsDeploymentWithOverride(Model):
    """Models deployment with override

    Properties:
        allow_version_override: (allow_version_override) REQUIRED bool

        buffer_count: (buffer_count) REQUIRED int

        configuration: (configuration) REQUIRED str

        game_version: (game_version) REQUIRED str

        max_count: (max_count) REQUIRED int

        min_count: (min_count) REQUIRED int

        overrides: (overrides) REQUIRED Dict[str, ModelsDeploymentConfig]

        regions: (regions) REQUIRED List[str]
    """

    # region fields

    allow_version_override: bool                                                                   # REQUIRED
    buffer_count: int                                                                              # REQUIRED
    configuration: str                                                                             # REQUIRED
    game_version: str                                                                              # REQUIRED
    max_count: int                                                                                 # REQUIRED
    min_count: int                                                                                 # REQUIRED
    overrides: Dict[str, ModelsDeploymentConfig]                                                   # REQUIRED
    regions: List[str]                                                                             # REQUIRED

    # endregion fields

    # region with_x methods

    def with_allow_version_override(self, value: bool) -> ModelsDeploymentWithOverride:
        self.allow_version_override = value
        return self

    def with_buffer_count(self, value: int) -> ModelsDeploymentWithOverride:
        self.buffer_count = value
        return self

    def with_configuration(self, value: str) -> ModelsDeploymentWithOverride:
        self.configuration = value
        return self

    def with_game_version(self, value: str) -> ModelsDeploymentWithOverride:
        self.game_version = value
        return self

    def with_max_count(self, value: int) -> ModelsDeploymentWithOverride:
        self.max_count = value
        return self

    def with_min_count(self, value: int) -> ModelsDeploymentWithOverride:
        self.min_count = value
        return self

    def with_overrides(self, value: Dict[str, ModelsDeploymentConfig]) -> ModelsDeploymentWithOverride:
        self.overrides = value
        return self

    def with_regions(self, value: List[str]) -> ModelsDeploymentWithOverride:
        self.regions = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "allow_version_override") and self.allow_version_override:
            result["allow_version_override"] = bool(self.allow_version_override)
        elif include_empty:
            result["allow_version_override"] = bool()
        if hasattr(self, "buffer_count") and self.buffer_count:
            result["buffer_count"] = int(self.buffer_count)
        elif include_empty:
            result["buffer_count"] = int()
        if hasattr(self, "configuration") and self.configuration:
            result["configuration"] = str(self.configuration)
        elif include_empty:
            result["configuration"] = str()
        if hasattr(self, "game_version") and self.game_version:
            result["game_version"] = str(self.game_version)
        elif include_empty:
            result["game_version"] = str()
        if hasattr(self, "max_count") and self.max_count:
            result["max_count"] = int(self.max_count)
        elif include_empty:
            result["max_count"] = int()
        if hasattr(self, "min_count") and self.min_count:
            result["min_count"] = int(self.min_count)
        elif include_empty:
            result["min_count"] = int()
        if hasattr(self, "overrides") and self.overrides:
            result["overrides"] = {str(k0): v0.to_dict(include_empty=include_empty) for k0, v0 in self.overrides.items()}
        elif include_empty:
            result["overrides"] = {}
        if hasattr(self, "regions") and self.regions:
            result["regions"] = [str(i0) for i0 in self.regions]
        elif include_empty:
            result["regions"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        allow_version_override: bool,
        buffer_count: int,
        configuration: str,
        game_version: str,
        max_count: int,
        min_count: int,
        overrides: Dict[str, ModelsDeploymentConfig],
        regions: List[str],
    ) -> ModelsDeploymentWithOverride:
        instance = cls()
        instance.allow_version_override = allow_version_override
        instance.buffer_count = buffer_count
        instance.configuration = configuration
        instance.game_version = game_version
        instance.max_count = max_count
        instance.min_count = min_count
        instance.overrides = overrides
        instance.regions = regions
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsDeploymentWithOverride:
        instance = cls()
        if "allow_version_override" in dict_ and dict_["allow_version_override"] is not None:
            instance.allow_version_override = bool(dict_["allow_version_override"])
        elif include_empty:
            instance.allow_version_override = bool()
        if "buffer_count" in dict_ and dict_["buffer_count"] is not None:
            instance.buffer_count = int(dict_["buffer_count"])
        elif include_empty:
            instance.buffer_count = int()
        if "configuration" in dict_ and dict_["configuration"] is not None:
            instance.configuration = str(dict_["configuration"])
        elif include_empty:
            instance.configuration = str()
        if "game_version" in dict_ and dict_["game_version"] is not None:
            instance.game_version = str(dict_["game_version"])
        elif include_empty:
            instance.game_version = str()
        if "max_count" in dict_ and dict_["max_count"] is not None:
            instance.max_count = int(dict_["max_count"])
        elif include_empty:
            instance.max_count = int()
        if "min_count" in dict_ and dict_["min_count"] is not None:
            instance.min_count = int(dict_["min_count"])
        elif include_empty:
            instance.min_count = int()
        if "overrides" in dict_ and dict_["overrides"] is not None:
            instance.overrides = {str(k0): ModelsDeploymentConfig.create_from_dict(v0, include_empty=include_empty) for k0, v0 in dict_["overrides"].items()}
        elif include_empty:
            instance.overrides = {}
        if "regions" in dict_ and dict_["regions"] is not None:
            instance.regions = [str(i0) for i0 in dict_["regions"]]
        elif include_empty:
            instance.regions = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "allow_version_override": "allow_version_override",
            "buffer_count": "buffer_count",
            "configuration": "configuration",
            "game_version": "game_version",
            "max_count": "max_count",
            "min_count": "min_count",
            "overrides": "overrides",
            "regions": "regions",
        }

    # endregion static methods
