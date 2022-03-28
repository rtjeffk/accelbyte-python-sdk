# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-iam-service (5.5.1)

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


class ModelGetUserJusticePlatformAccountResponse(Model):
    """Model get user justice platform account response (model.GetUserJusticePlatformAccountResponse)

    Properties:
        designated_namespace: (DesignatedNamespace) REQUIRED str

        user_id: (UserID) REQUIRED str
    """

    # region fields

    designated_namespace: str                                                                      # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_designated_namespace(self, value: str) -> ModelGetUserJusticePlatformAccountResponse:
        self.designated_namespace = value
        return self

    def with_user_id(self, value: str) -> ModelGetUserJusticePlatformAccountResponse:
        self.user_id = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "designated_namespace") or self.designated_namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "designated_namespace"):
            result["DesignatedNamespace"] = str(self.designated_namespace)
        elif include_empty:
            result["DesignatedNamespace"] = str()
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
        designated_namespace: str,
        user_id: str,
    ) -> ModelGetUserJusticePlatformAccountResponse:
        instance = cls()
        instance.designated_namespace = designated_namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelGetUserJusticePlatformAccountResponse:
        instance = cls()
        if not dict_:
            return instance
        if "DesignatedNamespace" in dict_ and dict_["DesignatedNamespace"] is not None:
            instance.designated_namespace = str(dict_["DesignatedNamespace"])
        elif include_empty:
            instance.designated_namespace = str()
        if "UserID" in dict_ and dict_["UserID"] is not None:
            instance.user_id = str(dict_["UserID"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, ModelGetUserJusticePlatformAccountResponse]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[ModelGetUserJusticePlatformAccountResponse]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[ModelGetUserJusticePlatformAccountResponse, List[ModelGetUserJusticePlatformAccountResponse]]:
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
            "DesignatedNamespace": "designated_namespace",
            "UserID": "user_id",
        }

    # endregion static methods
