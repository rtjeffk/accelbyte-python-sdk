# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# Analytics Game Telemetry (0.0.1)

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


class ValidationError(Model):
    """Validation error (ValidationError)

    Properties:
        loc: (loc) REQUIRED List[str]

        msg: (msg) REQUIRED str

        type_: (type) REQUIRED str
    """

    # region fields

    loc: List[str]                                                                                 # REQUIRED
    msg: str                                                                                       # REQUIRED
    type_: str                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_loc(self, value: List[str]) -> ValidationError:
        self.loc = value
        return self

    def with_msg(self, value: str) -> ValidationError:
        self.msg = value
        return self

    def with_type(self, value: str) -> ValidationError:
        self.type_ = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "loc") or self.loc is None:
            return False
        if not hasattr(self, "msg") or self.msg is None:
            return False
        if not hasattr(self, "type_") or self.type_ is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "loc"):
            result["loc"] = [str(i0) for i0 in self.loc]
        elif include_empty:
            result["loc"] = []
        if hasattr(self, "msg"):
            result["msg"] = str(self.msg)
        elif include_empty:
            result["msg"] = str()
        if hasattr(self, "type_"):
            result["type"] = str(self.type_)
        elif include_empty:
            result["type"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        loc: List[str],
        msg: str,
        type_: str,
    ) -> ValidationError:
        instance = cls()
        instance.loc = loc
        instance.msg = msg
        instance.type_ = type_
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ValidationError:
        instance = cls()
        if not dict_:
            return instance
        if "loc" in dict_ and dict_["loc"] is not None:
            instance.loc = [str(i0) for i0 in dict_["loc"]]
        elif include_empty:
            instance.loc = []
        if "msg" in dict_ and dict_["msg"] is not None:
            instance.msg = str(dict_["msg"])
        elif include_empty:
            instance.msg = str()
        if "type" in dict_ and dict_["type"] is not None:
            instance.type_ = str(dict_["type"])
        elif include_empty:
            instance.type_ = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, ValidationError]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[ValidationError]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[ValidationError, List[ValidationError]]:
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
            "loc": "loc",
            "msg": "msg",
            "type": "type_",
        }

    # endregion static methods
