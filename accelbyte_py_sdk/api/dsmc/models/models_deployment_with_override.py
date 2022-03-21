# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-dsm-controller-service (2.15.0)

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
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import Model

from ..models.models_deployment_config_override import ModelsDeploymentConfigOverride
from ..models.models_pod_count_config_override import ModelsPodCountConfigOverride


class ModelsDeploymentWithOverride(Model):
    """Models deployment with override (models.DeploymentWithOverride)

    Properties:
        allow_version_override: (allow_version_override) REQUIRED bool

        buffer_count: (buffer_count) REQUIRED int

        buffer_percent: (buffer_percent) REQUIRED int

        configuration: (configuration) REQUIRED str

        created_at: (createdAt) REQUIRED str

        enable_region_overrides: (enable_region_overrides) REQUIRED bool

        game_version: (game_version) REQUIRED str

        max_count: (max_count) REQUIRED int

        min_count: (min_count) REQUIRED int

        modified_by: (modifiedBy) REQUIRED str

        name: (name) REQUIRED str

        namespace: (namespace) REQUIRED str

        overrides: (overrides) REQUIRED Dict[str, ModelsDeploymentConfigOverride]

        region_overrides: (region_overrides) REQUIRED Dict[str, ModelsPodCountConfigOverride]

        regions: (regions) REQUIRED List[str]

        updated_at: (updatedAt) REQUIRED str

        use_buffer_percent: (use_buffer_percent) REQUIRED bool
    """

    # region fields

    allow_version_override: bool                                                                   # REQUIRED
    buffer_count: int                                                                              # REQUIRED
    buffer_percent: int                                                                            # REQUIRED
    configuration: str                                                                             # REQUIRED
    created_at: str                                                                                # REQUIRED
    enable_region_overrides: bool                                                                  # REQUIRED
    game_version: str                                                                              # REQUIRED
    max_count: int                                                                                 # REQUIRED
    min_count: int                                                                                 # REQUIRED
    modified_by: str                                                                               # REQUIRED
    name: str                                                                                      # REQUIRED
    namespace: str                                                                                 # REQUIRED
    overrides: Dict[str, ModelsDeploymentConfigOverride]                                           # REQUIRED
    region_overrides: Dict[str, ModelsPodCountConfigOverride]                                      # REQUIRED
    regions: List[str]                                                                             # REQUIRED
    updated_at: str                                                                                # REQUIRED
    use_buffer_percent: bool                                                                       # REQUIRED

    # endregion fields

    # region with_x methods

    def with_allow_version_override(self, value: bool) -> ModelsDeploymentWithOverride:
        self.allow_version_override = value
        return self

    def with_buffer_count(self, value: int) -> ModelsDeploymentWithOverride:
        self.buffer_count = value
        return self

    def with_buffer_percent(self, value: int) -> ModelsDeploymentWithOverride:
        self.buffer_percent = value
        return self

    def with_configuration(self, value: str) -> ModelsDeploymentWithOverride:
        self.configuration = value
        return self

    def with_created_at(self, value: str) -> ModelsDeploymentWithOverride:
        self.created_at = value
        return self

    def with_enable_region_overrides(self, value: bool) -> ModelsDeploymentWithOverride:
        self.enable_region_overrides = value
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

    def with_modified_by(self, value: str) -> ModelsDeploymentWithOverride:
        self.modified_by = value
        return self

    def with_name(self, value: str) -> ModelsDeploymentWithOverride:
        self.name = value
        return self

    def with_namespace(self, value: str) -> ModelsDeploymentWithOverride:
        self.namespace = value
        return self

    def with_overrides(self, value: Dict[str, ModelsDeploymentConfigOverride]) -> ModelsDeploymentWithOverride:
        self.overrides = value
        return self

    def with_region_overrides(self, value: Dict[str, ModelsPodCountConfigOverride]) -> ModelsDeploymentWithOverride:
        self.region_overrides = value
        return self

    def with_regions(self, value: List[str]) -> ModelsDeploymentWithOverride:
        self.regions = value
        return self

    def with_updated_at(self, value: str) -> ModelsDeploymentWithOverride:
        self.updated_at = value
        return self

    def with_use_buffer_percent(self, value: bool) -> ModelsDeploymentWithOverride:
        self.use_buffer_percent = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "allow_version_override") or self.allow_version_override is None:
            return False
        if not hasattr(self, "buffer_count") or self.buffer_count is None:
            return False
        if not hasattr(self, "buffer_percent") or self.buffer_percent is None:
            return False
        if not hasattr(self, "configuration") or self.configuration is None:
            return False
        if not hasattr(self, "created_at") or self.created_at is None:
            return False
        if not hasattr(self, "enable_region_overrides") or self.enable_region_overrides is None:
            return False
        if not hasattr(self, "game_version") or self.game_version is None:
            return False
        if not hasattr(self, "max_count") or self.max_count is None:
            return False
        if not hasattr(self, "min_count") or self.min_count is None:
            return False
        if not hasattr(self, "modified_by") or self.modified_by is None:
            return False
        if not hasattr(self, "name") or self.name is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "overrides") or self.overrides is None:
            return False
        if not hasattr(self, "region_overrides") or self.region_overrides is None:
            return False
        if not hasattr(self, "regions") or self.regions is None:
            return False
        if not hasattr(self, "updated_at") or self.updated_at is None:
            return False
        if not hasattr(self, "use_buffer_percent") or self.use_buffer_percent is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "allow_version_override"):
            result["allow_version_override"] = bool(self.allow_version_override)
        elif include_empty:
            result["allow_version_override"] = bool()
        if hasattr(self, "buffer_count"):
            result["buffer_count"] = int(self.buffer_count)
        elif include_empty:
            result["buffer_count"] = int()
        if hasattr(self, "buffer_percent"):
            result["buffer_percent"] = int(self.buffer_percent)
        elif include_empty:
            result["buffer_percent"] = int()
        if hasattr(self, "configuration"):
            result["configuration"] = str(self.configuration)
        elif include_empty:
            result["configuration"] = str()
        if hasattr(self, "created_at"):
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "enable_region_overrides"):
            result["enable_region_overrides"] = bool(self.enable_region_overrides)
        elif include_empty:
            result["enable_region_overrides"] = bool()
        if hasattr(self, "game_version"):
            result["game_version"] = str(self.game_version)
        elif include_empty:
            result["game_version"] = str()
        if hasattr(self, "max_count"):
            result["max_count"] = int(self.max_count)
        elif include_empty:
            result["max_count"] = int()
        if hasattr(self, "min_count"):
            result["min_count"] = int(self.min_count)
        elif include_empty:
            result["min_count"] = int()
        if hasattr(self, "modified_by"):
            result["modifiedBy"] = str(self.modified_by)
        elif include_empty:
            result["modifiedBy"] = str()
        if hasattr(self, "name"):
            result["name"] = str(self.name)
        elif include_empty:
            result["name"] = str()
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "overrides"):
            result["overrides"] = {str(k0): v0.to_dict(include_empty=include_empty) for k0, v0 in self.overrides.items()}
        elif include_empty:
            result["overrides"] = {}
        if hasattr(self, "region_overrides"):
            result["region_overrides"] = {str(k0): v0.to_dict(include_empty=include_empty) for k0, v0 in self.region_overrides.items()}
        elif include_empty:
            result["region_overrides"] = {}
        if hasattr(self, "regions"):
            result["regions"] = [str(i0) for i0 in self.regions]
        elif include_empty:
            result["regions"] = []
        if hasattr(self, "updated_at"):
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        if hasattr(self, "use_buffer_percent"):
            result["use_buffer_percent"] = bool(self.use_buffer_percent)
        elif include_empty:
            result["use_buffer_percent"] = bool()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        allow_version_override: bool,
        buffer_count: int,
        buffer_percent: int,
        configuration: str,
        created_at: str,
        enable_region_overrides: bool,
        game_version: str,
        max_count: int,
        min_count: int,
        modified_by: str,
        name: str,
        namespace: str,
        overrides: Dict[str, ModelsDeploymentConfigOverride],
        region_overrides: Dict[str, ModelsPodCountConfigOverride],
        regions: List[str],
        updated_at: str,
        use_buffer_percent: bool,
    ) -> ModelsDeploymentWithOverride:
        instance = cls()
        instance.allow_version_override = allow_version_override
        instance.buffer_count = buffer_count
        instance.buffer_percent = buffer_percent
        instance.configuration = configuration
        instance.created_at = created_at
        instance.enable_region_overrides = enable_region_overrides
        instance.game_version = game_version
        instance.max_count = max_count
        instance.min_count = min_count
        instance.modified_by = modified_by
        instance.name = name
        instance.namespace = namespace
        instance.overrides = overrides
        instance.region_overrides = region_overrides
        instance.regions = regions
        instance.updated_at = updated_at
        instance.use_buffer_percent = use_buffer_percent
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsDeploymentWithOverride:
        instance = cls()
        if not dict_:
            return instance
        if "allow_version_override" in dict_ and dict_["allow_version_override"] is not None:
            instance.allow_version_override = bool(dict_["allow_version_override"])
        elif include_empty:
            instance.allow_version_override = bool()
        if "buffer_count" in dict_ and dict_["buffer_count"] is not None:
            instance.buffer_count = int(dict_["buffer_count"])
        elif include_empty:
            instance.buffer_count = int()
        if "buffer_percent" in dict_ and dict_["buffer_percent"] is not None:
            instance.buffer_percent = int(dict_["buffer_percent"])
        elif include_empty:
            instance.buffer_percent = int()
        if "configuration" in dict_ and dict_["configuration"] is not None:
            instance.configuration = str(dict_["configuration"])
        elif include_empty:
            instance.configuration = str()
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "enable_region_overrides" in dict_ and dict_["enable_region_overrides"] is not None:
            instance.enable_region_overrides = bool(dict_["enable_region_overrides"])
        elif include_empty:
            instance.enable_region_overrides = bool()
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
        if "modifiedBy" in dict_ and dict_["modifiedBy"] is not None:
            instance.modified_by = str(dict_["modifiedBy"])
        elif include_empty:
            instance.modified_by = str()
        if "name" in dict_ and dict_["name"] is not None:
            instance.name = str(dict_["name"])
        elif include_empty:
            instance.name = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "overrides" in dict_ and dict_["overrides"] is not None:
            instance.overrides = {str(k0): ModelsDeploymentConfigOverride.create_from_dict(v0, include_empty=include_empty) for k0, v0 in dict_["overrides"].items()}
        elif include_empty:
            instance.overrides = {}
        if "region_overrides" in dict_ and dict_["region_overrides"] is not None:
            instance.region_overrides = {str(k0): ModelsPodCountConfigOverride.create_from_dict(v0, include_empty=include_empty) for k0, v0 in dict_["region_overrides"].items()}
        elif include_empty:
            instance.region_overrides = {}
        if "regions" in dict_ and dict_["regions"] is not None:
            instance.regions = [str(i0) for i0 in dict_["regions"]]
        elif include_empty:
            instance.regions = []
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        if "use_buffer_percent" in dict_ and dict_["use_buffer_percent"] is not None:
            instance.use_buffer_percent = bool(dict_["use_buffer_percent"])
        elif include_empty:
            instance.use_buffer_percent = bool()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, ModelsDeploymentWithOverride]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[ModelsDeploymentWithOverride]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[ModelsDeploymentWithOverride, List[ModelsDeploymentWithOverride]]:
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
            "allow_version_override": "allow_version_override",
            "buffer_count": "buffer_count",
            "buffer_percent": "buffer_percent",
            "configuration": "configuration",
            "createdAt": "created_at",
            "enable_region_overrides": "enable_region_overrides",
            "game_version": "game_version",
            "max_count": "max_count",
            "min_count": "min_count",
            "modifiedBy": "modified_by",
            "name": "name",
            "namespace": "namespace",
            "overrides": "overrides",
            "region_overrides": "region_overrides",
            "regions": "regions",
            "updatedAt": "updated_at",
            "use_buffer_percent": "use_buffer_percent",
        }

    # endregion static methods
