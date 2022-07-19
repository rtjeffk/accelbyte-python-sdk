# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
# 
# Code generated. DO NOT EDIT!

# template file: justice_py_sdk_codegen/__main__.py

# justice-iam-service (5.13.0)

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

from ..models.accountcommon_distinct_linked_platform_v3 import AccountcommonDistinctLinkedPlatformV3


class AccountcommonDistinctPlatformResponseV3(Model):
    """Accountcommon distinct platform response V3 (accountcommon.DistinctPlatformResponseV3)

    Properties:
        platforms: (platforms) REQUIRED List[AccountcommonDistinctLinkedPlatformV3]
    """

    # region fields

    platforms: List[AccountcommonDistinctLinkedPlatformV3]                                         # REQUIRED

    # endregion fields

    # region with_x methods

    def with_platforms(self, value: List[AccountcommonDistinctLinkedPlatformV3]) -> AccountcommonDistinctPlatformResponseV3:
        self.platforms = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "platforms"):
            result["platforms"] = [i0.to_dict(include_empty=include_empty) for i0 in self.platforms]
        elif include_empty:
            result["platforms"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        platforms: List[AccountcommonDistinctLinkedPlatformV3],
    ) -> AccountcommonDistinctPlatformResponseV3:
        instance = cls()
        instance.platforms = platforms
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonDistinctPlatformResponseV3:
        instance = cls()
        if not dict_:
            return instance
        if "platforms" in dict_ and dict_["platforms"] is not None:
            instance.platforms = [AccountcommonDistinctLinkedPlatformV3.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["platforms"]]
        elif include_empty:
            instance.platforms = []
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, AccountcommonDistinctPlatformResponseV3]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[AccountcommonDistinctPlatformResponseV3]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[AccountcommonDistinctPlatformResponseV3, List[AccountcommonDistinctPlatformResponseV3], Dict[Any, AccountcommonDistinctPlatformResponseV3]]:
        if many:
            if isinstance(any_, dict):
                return cls.create_many_from_dict(any_, include_empty=include_empty)
            elif isinstance(any_, list):
                return cls.create_many_from_list(any_, include_empty=include_empty)
            else:
                raise ValueError()
        else:
            return cls.create_from_dict(any_, include_empty=include_empty)

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "platforms": "platforms",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "platforms": True,
        }

    # endregion static methods
