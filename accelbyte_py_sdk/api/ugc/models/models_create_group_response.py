# justice-ugc-service (1.9.0)

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


class ModelsCreateGroupResponse(Model):
    """Models create group response (models.CreateGroupResponse)

    Properties:
        contents: (contents) REQUIRED List[str]

        created_at: (createdAt) REQUIRED str

        id_: (id) REQUIRED str

        name: (name) REQUIRED str

        namespace: (namespace) REQUIRED str

        user_id: (userId) REQUIRED str
    """

    # region fields

    contents: List[str]                                                                            # REQUIRED
    created_at: str                                                                                # REQUIRED
    id_: str                                                                                       # REQUIRED
    name: str                                                                                      # REQUIRED
    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_contents(self, value: List[str]) -> ModelsCreateGroupResponse:
        self.contents = value
        return self

    def with_created_at(self, value: str) -> ModelsCreateGroupResponse:
        self.created_at = value
        return self

    def with_id(self, value: str) -> ModelsCreateGroupResponse:
        self.id_ = value
        return self

    def with_name(self, value: str) -> ModelsCreateGroupResponse:
        self.name = value
        return self

    def with_namespace(self, value: str) -> ModelsCreateGroupResponse:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> ModelsCreateGroupResponse:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "contents"):
            result["contents"] = [str(i0) for i0 in self.contents]
        elif include_empty:
            result["contents"] = []
        if hasattr(self, "created_at"):
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "id_"):
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "name"):
            result["name"] = str(self.name)
        elif include_empty:
            result["name"] = str()
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
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
        contents: List[str],
        created_at: str,
        id_: str,
        name: str,
        namespace: str,
        user_id: str,
    ) -> ModelsCreateGroupResponse:
        instance = cls()
        instance.contents = contents
        instance.created_at = created_at
        instance.id_ = id_
        instance.name = name
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsCreateGroupResponse:
        instance = cls()
        if not dict_:
            return instance
        if "contents" in dict_ and dict_["contents"] is not None:
            instance.contents = [str(i0) for i0 in dict_["contents"]]
        elif include_empty:
            instance.contents = []
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "name" in dict_ and dict_["name"] is not None:
            instance.name = str(dict_["name"])
        elif include_empty:
            instance.name = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "contents": "contents",
            "createdAt": "created_at",
            "id": "id_",
            "name": "name",
            "namespace": "namespace",
            "userId": "user_id",
        }

    # endregion static methods