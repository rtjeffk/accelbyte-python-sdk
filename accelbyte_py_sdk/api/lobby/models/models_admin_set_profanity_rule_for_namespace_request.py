# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-lobby-server (staging)

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


class ModelsAdminSetProfanityRuleForNamespaceRequest(Model):
    """Models admin set profanity rule for namespace request (models.AdminSetProfanityRuleForNamespaceRequest)

    Properties:
        rule: (rule) REQUIRED str
    """

    # region fields

    rule: str                                                                                      # REQUIRED

    # endregion fields

    # region with_x methods

    def with_rule(self, value: str) -> ModelsAdminSetProfanityRuleForNamespaceRequest:
        self.rule = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "rule") or self.rule is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "rule"):
            result["rule"] = str(self.rule)
        elif include_empty:
            result["rule"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        rule: str,
    ) -> ModelsAdminSetProfanityRuleForNamespaceRequest:
        instance = cls()
        instance.rule = rule
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsAdminSetProfanityRuleForNamespaceRequest:
        instance = cls()
        if not dict_:
            return instance
        if "rule" in dict_ and dict_["rule"] is not None:
            instance.rule = str(dict_["rule"])
        elif include_empty:
            instance.rule = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, ModelsAdminSetProfanityRuleForNamespaceRequest]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[ModelsAdminSetProfanityRuleForNamespaceRequest]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[ModelsAdminSetProfanityRuleForNamespaceRequest, List[ModelsAdminSetProfanityRuleForNamespaceRequest]]:
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
            "rule": "rule",
        }

    # endregion static methods
