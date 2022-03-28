# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-basic-service (1.35.0)

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


class ADTOForUpdateEqu8ConfigAPICall(Model):
    """A DTO for update equ8 config API call (A DTO for update equ8 config API call.)

    Properties:
        api_key: (apiKey) OPTIONAL str
    """

    # region fields

    api_key: str                                                                                   # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_api_key(self, value: str) -> ADTOForUpdateEqu8ConfigAPICall:
        self.api_key = value
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
        if hasattr(self, "api_key"):
            result["apiKey"] = str(self.api_key)
        elif include_empty:
            result["apiKey"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
    ) -> ADTOForUpdateEqu8ConfigAPICall:
        instance = cls()
        if api_key is not None:
            instance.api_key = api_key
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ADTOForUpdateEqu8ConfigAPICall:
        instance = cls()
        if not dict_:
            return instance
        if "apiKey" in dict_ and dict_["apiKey"] is not None:
            instance.api_key = str(dict_["apiKey"])
        elif include_empty:
            instance.api_key = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, ADTOForUpdateEqu8ConfigAPICall]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[ADTOForUpdateEqu8ConfigAPICall]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[ADTOForUpdateEqu8ConfigAPICall, List[ADTOForUpdateEqu8ConfigAPICall]]:
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
            "apiKey": "api_key",
        }

    # endregion static methods
