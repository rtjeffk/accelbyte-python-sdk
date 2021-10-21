# justice-dsm-controller-service (2.6.0)

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


class ModelsPodConfigRecord(Model):
    """Models pod config record (models.PodConfigRecord)

    Properties:
        cpu_limit: (cpu_limit) REQUIRED int

        created_at: (createdAt) REQUIRED str

        mem_limit: (mem_limit) REQUIRED int

        modified_by: (modifiedBy) REQUIRED str

        name: (name) REQUIRED str

        namespace: (namespace) REQUIRED str

        params: (params) REQUIRED str

        updated_at: (updatedAt) REQUIRED str
    """

    # region fields

    cpu_limit: int                                                                                 # REQUIRED
    created_at: str                                                                                # REQUIRED
    mem_limit: int                                                                                 # REQUIRED
    modified_by: str                                                                               # REQUIRED
    name: str                                                                                      # REQUIRED
    namespace: str                                                                                 # REQUIRED
    params: str                                                                                    # REQUIRED
    updated_at: str                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_cpu_limit(self, value: int) -> ModelsPodConfigRecord:
        self.cpu_limit = value
        return self

    def with_created_at(self, value: str) -> ModelsPodConfigRecord:
        self.created_at = value
        return self

    def with_mem_limit(self, value: int) -> ModelsPodConfigRecord:
        self.mem_limit = value
        return self

    def with_modified_by(self, value: str) -> ModelsPodConfigRecord:
        self.modified_by = value
        return self

    def with_name(self, value: str) -> ModelsPodConfigRecord:
        self.name = value
        return self

    def with_namespace(self, value: str) -> ModelsPodConfigRecord:
        self.namespace = value
        return self

    def with_params(self, value: str) -> ModelsPodConfigRecord:
        self.params = value
        return self

    def with_updated_at(self, value: str) -> ModelsPodConfigRecord:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "cpu_limit") and self.cpu_limit:
            result["cpu_limit"] = int(self.cpu_limit)
        elif include_empty:
            result["cpu_limit"] = int()
        if hasattr(self, "created_at") and self.created_at:
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "mem_limit") and self.mem_limit:
            result["mem_limit"] = int(self.mem_limit)
        elif include_empty:
            result["mem_limit"] = int()
        if hasattr(self, "modified_by") and self.modified_by:
            result["modifiedBy"] = str(self.modified_by)
        elif include_empty:
            result["modifiedBy"] = str()
        if hasattr(self, "name") and self.name:
            result["name"] = str(self.name)
        elif include_empty:
            result["name"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "params") and self.params:
            result["params"] = str(self.params)
        elif include_empty:
            result["params"] = str()
        if hasattr(self, "updated_at") and self.updated_at:
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        cpu_limit: int,
        created_at: str,
        mem_limit: int,
        modified_by: str,
        name: str,
        namespace: str,
        params: str,
        updated_at: str,
    ) -> ModelsPodConfigRecord:
        instance = cls()
        instance.cpu_limit = cpu_limit
        instance.created_at = created_at
        instance.mem_limit = mem_limit
        instance.modified_by = modified_by
        instance.name = name
        instance.namespace = namespace
        instance.params = params
        instance.updated_at = updated_at
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsPodConfigRecord:
        instance = cls()
        if not dict_:
            return instance
        if "cpu_limit" in dict_ and dict_["cpu_limit"] is not None:
            instance.cpu_limit = int(dict_["cpu_limit"])
        elif include_empty:
            instance.cpu_limit = int()
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "mem_limit" in dict_ and dict_["mem_limit"] is not None:
            instance.mem_limit = int(dict_["mem_limit"])
        elif include_empty:
            instance.mem_limit = int()
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
        if "params" in dict_ and dict_["params"] is not None:
            instance.params = str(dict_["params"])
        elif include_empty:
            instance.params = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "cpu_limit": "cpu_limit",
            "createdAt": "created_at",
            "mem_limit": "mem_limit",
            "modifiedBy": "modified_by",
            "name": "name",
            "namespace": "namespace",
            "params": "params",
            "updatedAt": "updated_at",
        }

    # endregion static methods
