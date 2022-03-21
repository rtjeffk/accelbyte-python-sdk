# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-iam-service (5.4.0)

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


class ModelPublicUserInformationV3(Model):
    """Model public user information V3 (model.PublicUserInformationV3)

    Properties:
        created_at: (createdAt) REQUIRED str

        display_name: (displayName) REQUIRED str

        namespace: (namespace) REQUIRED str

        user_id: (userId) REQUIRED str

        user_name: (userName) REQUIRED str
    """

    # region fields

    created_at: str                                                                                # REQUIRED
    display_name: str                                                                              # REQUIRED
    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED
    user_name: str                                                                                 # REQUIRED

    # endregion fields

    # region with_x methods

    def with_created_at(self, value: str) -> ModelPublicUserInformationV3:
        self.created_at = value
        return self

    def with_display_name(self, value: str) -> ModelPublicUserInformationV3:
        self.display_name = value
        return self

    def with_namespace(self, value: str) -> ModelPublicUserInformationV3:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> ModelPublicUserInformationV3:
        self.user_id = value
        return self

    def with_user_name(self, value: str) -> ModelPublicUserInformationV3:
        self.user_name = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "created_at") or self.created_at is None:
            return False
        if not hasattr(self, "display_name") or self.display_name is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        if not hasattr(self, "user_name") or self.user_name is None:
            return False
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
        if hasattr(self, "user_id"):
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "user_name"):
            result["userName"] = str(self.user_name)
        elif include_empty:
            result["userName"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        created_at: str,
        display_name: str,
        namespace: str,
        user_id: str,
        user_name: str,
    ) -> ModelPublicUserInformationV3:
        instance = cls()
        instance.created_at = created_at
        instance.display_name = display_name
        instance.namespace = namespace
        instance.user_id = user_id
        instance.user_name = user_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelPublicUserInformationV3:
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
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "userName" in dict_ and dict_["userName"] is not None:
            instance.user_name = str(dict_["userName"])
        elif include_empty:
            instance.user_name = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, ModelPublicUserInformationV3]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[ModelPublicUserInformationV3]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[ModelPublicUserInformationV3, List[ModelPublicUserInformationV3]]:
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
            "userId": "user_id",
            "userName": "user_name",
        }

    # endregion static methods
