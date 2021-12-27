# justice-event-log-service ()

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


class ModelsUserLastActivity(Model):
    """Models user last activity (models.UserLastActivity)

    Properties:
        last_activity_time: (LastActivityTime) REQUIRED str

        namespace: (Namespace) REQUIRED str

        user_id: (UserID) REQUIRED str
    """

    # region fields

    last_activity_time: str                                                                        # REQUIRED
    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_last_activity_time(self, value: str) -> ModelsUserLastActivity:
        self.last_activity_time = value
        return self

    def with_namespace(self, value: str) -> ModelsUserLastActivity:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> ModelsUserLastActivity:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "last_activity_time"):
            result["LastActivityTime"] = str(self.last_activity_time)
        elif include_empty:
            result["LastActivityTime"] = str()
        if hasattr(self, "namespace"):
            result["Namespace"] = str(self.namespace)
        elif include_empty:
            result["Namespace"] = str()
        if hasattr(self, "user_id"):
            result["UserID"] = str(self.user_id)
        elif include_empty:
            result["UserID"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        last_activity_time: str,
        namespace: str,
        user_id: str,
    ) -> ModelsUserLastActivity:
        instance = cls()
        instance.last_activity_time = last_activity_time
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsUserLastActivity:
        instance = cls()
        if not dict_:
            return instance
        if "LastActivityTime" in dict_ and dict_["LastActivityTime"] is not None:
            instance.last_activity_time = str(dict_["LastActivityTime"])
        elif include_empty:
            instance.last_activity_time = str()
        if "Namespace" in dict_ and dict_["Namespace"] is not None:
            instance.namespace = str(dict_["Namespace"])
        elif include_empty:
            instance.namespace = str()
        if "UserID" in dict_ and dict_["UserID"] is not None:
            instance.user_id = str(dict_["UserID"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "LastActivityTime": "last_activity_time",
            "Namespace": "namespace",
            "UserID": "user_id",
        }

    # endregion static methods
