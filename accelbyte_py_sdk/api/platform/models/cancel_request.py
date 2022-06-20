# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
# 
# Code generated. DO NOT EDIT!

# template file: justice_py_sdk_codegen/__main__.py

# justice-platform-service (4.10.0)

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


class CancelRequest(Model):
    """Cancel request (CancelRequest)

    Properties:
        immediate: (immediate) OPTIONAL bool

        reason: (reason) OPTIONAL str
    """

    # region fields

    immediate: bool                                                                                # OPTIONAL
    reason: str                                                                                    # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_immediate(self, value: bool) -> CancelRequest:
        self.immediate = value
        return self

    def with_reason(self, value: str) -> CancelRequest:
        self.reason = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "immediate"):
            result["immediate"] = bool(self.immediate)
        elif include_empty:
            result["immediate"] = False
        if hasattr(self, "reason"):
            result["reason"] = str(self.reason)
        elif include_empty:
            result["reason"] = ""
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        immediate: Optional[bool] = None,
        reason: Optional[str] = None,
    ) -> CancelRequest:
        instance = cls()
        if immediate is not None:
            instance.immediate = immediate
        if reason is not None:
            instance.reason = reason
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> CancelRequest:
        instance = cls()
        if not dict_:
            return instance
        if "immediate" in dict_ and dict_["immediate"] is not None:
            instance.immediate = bool(dict_["immediate"])
        elif include_empty:
            instance.immediate = False
        if "reason" in dict_ and dict_["reason"] is not None:
            instance.reason = str(dict_["reason"])
        elif include_empty:
            instance.reason = ""
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, CancelRequest]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[CancelRequest]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[CancelRequest, List[CancelRequest], Dict[Any, CancelRequest]]:
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
            "immediate": "immediate",
            "reason": "reason",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "immediate": False,
            "reason": False,
        }

    # endregion static methods
