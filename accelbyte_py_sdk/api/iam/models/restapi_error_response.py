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


class RestapiErrorResponse(Model):
    """Restapi error response (restapi.ErrorResponse)

    Properties:
        message: (Message) REQUIRED str

        code: (Code) OPTIONAL int
    """

    # region fields

    message: str                                                                                   # REQUIRED
    code: int                                                                                      # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_message(self, value: str) -> RestapiErrorResponse:
        self.message = value
        return self

    def with_code(self, value: int) -> RestapiErrorResponse:
        self.code = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "message") or self.message is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "message"):
            result["Message"] = str(self.message)
        elif include_empty:
            result["Message"] = str()
        if hasattr(self, "code"):
            result["Code"] = int(self.code)
        elif include_empty:
            result["Code"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        message: str,
        code: Optional[int] = None,
    ) -> RestapiErrorResponse:
        instance = cls()
        instance.message = message
        if code is not None:
            instance.code = code
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> RestapiErrorResponse:
        instance = cls()
        if not dict_:
            return instance
        if "Message" in dict_ and dict_["Message"] is not None:
            instance.message = str(dict_["Message"])
        elif include_empty:
            instance.message = str()
        if "Code" in dict_ and dict_["Code"] is not None:
            instance.code = int(dict_["Code"])
        elif include_empty:
            instance.code = int()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, RestapiErrorResponse]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[RestapiErrorResponse]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[RestapiErrorResponse, List[RestapiErrorResponse]]:
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
            "Message": "message",
            "Code": "code",
        }

    # endregion static methods
