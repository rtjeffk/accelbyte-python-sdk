# justice-seasonpass-service (1.7.0)

# template file: justice_py_sdk_codegen/__main__.py

# Copyright (c) 2018 - 2022 AccelByte Inc. All Rights Reserved.
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


class UserPassGrant(Model):
    """A DTO object for granting user pass. (UserPassGrant)

    Properties:
        pass_code: (passCode) OPTIONAL str

        pass_item_id: (passItemId) OPTIONAL str
    """

    # region fields

    pass_code: str                                                                                 # OPTIONAL
    pass_item_id: str                                                                              # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_pass_code(self, value: str) -> UserPassGrant:
        self.pass_code = value
        return self

    def with_pass_item_id(self, value: str) -> UserPassGrant:
        self.pass_item_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "pass_code"):
            result["passCode"] = str(self.pass_code)
        elif include_empty:
            result["passCode"] = str()
        if hasattr(self, "pass_item_id"):
            result["passItemId"] = str(self.pass_item_id)
        elif include_empty:
            result["passItemId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        pass_code: Optional[str] = None,
        pass_item_id: Optional[str] = None,
    ) -> UserPassGrant:
        instance = cls()
        if pass_code is not None:
            instance.pass_code = pass_code
        if pass_item_id is not None:
            instance.pass_item_id = pass_item_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UserPassGrant:
        instance = cls()
        if not dict_:
            return instance
        if "passCode" in dict_ and dict_["passCode"] is not None:
            instance.pass_code = str(dict_["passCode"])
        elif include_empty:
            instance.pass_code = str()
        if "passItemId" in dict_ and dict_["passItemId"] is not None:
            instance.pass_item_id = str(dict_["passItemId"])
        elif include_empty:
            instance.pass_item_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "passCode": "pass_code",
            "passItemId": "pass_item_id",
        }

    # endregion static methods
