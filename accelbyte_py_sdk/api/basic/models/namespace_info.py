# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-basic-service (1.34.0)

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


class NamespaceInfo(Model):
    """Namespace info (NamespaceInfo)

    Properties:
        created_at: (createdAt) OPTIONAL str

        display_name: (displayName) OPTIONAL str

        namespace: (namespace) OPTIONAL str

        status: (status) OPTIONAL str

        updated_at: (updatedAt) OPTIONAL str
    """

    # region fields

    created_at: str                                                                                # OPTIONAL
    display_name: str                                                                              # OPTIONAL
    namespace: str                                                                                 # OPTIONAL
    status: str                                                                                    # OPTIONAL
    updated_at: str                                                                                # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_created_at(self, value: str) -> NamespaceInfo:
        self.created_at = value
        return self

    def with_display_name(self, value: str) -> NamespaceInfo:
        self.display_name = value
        return self

    def with_namespace(self, value: str) -> NamespaceInfo:
        self.namespace = value
        return self

    def with_status(self, value: str) -> NamespaceInfo:
        self.status = value
        return self

    def with_updated_at(self, value: str) -> NamespaceInfo:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "created_at"):
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "display_name"):
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = str()
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "status"):
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "updated_at"):
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        created_at: Optional[str] = None,
        display_name: Optional[str] = None,
        namespace: Optional[str] = None,
        status: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> NamespaceInfo:
        instance = cls()
        if created_at is not None:
            instance.created_at = created_at
        if display_name is not None:
            instance.display_name = display_name
        if namespace is not None:
            instance.namespace = namespace
        if status is not None:
            instance.status = status
        if updated_at is not None:
            instance.updated_at = updated_at
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> NamespaceInfo:
        instance = cls()
        if not dict_:
            return instance
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, NamespaceInfo]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[NamespaceInfo]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[NamespaceInfo, List[NamespaceInfo]]:
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
            "createdAt": "created_at",
            "displayName": "display_name",
            "namespace": "namespace",
            "status": "status",
            "updatedAt": "updated_at",
        }

    # endregion static methods
