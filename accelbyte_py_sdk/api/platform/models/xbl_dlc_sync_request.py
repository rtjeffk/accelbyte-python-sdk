# justice-platform-service (4.1.1)

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


class XblDLCSyncRequest(Model):
    """Xbl DLC sync request (XblDLCSyncRequest)

    Properties:
        xsts_token: (xstsToken) OPTIONAL str
    """

    # region fields

    xsts_token: str                                                                                # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_xsts_token(self, value: str) -> XblDLCSyncRequest:
        self.xsts_token = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "xsts_token"):
            result["xstsToken"] = str(self.xsts_token)
        elif include_empty:
            result["xstsToken"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        xsts_token: Optional[str] = None,
    ) -> XblDLCSyncRequest:
        instance = cls()
        if xsts_token is not None:
            instance.xsts_token = xsts_token
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> XblDLCSyncRequest:
        instance = cls()
        if not dict_:
            return instance
        if "xstsToken" in dict_ and dict_["xstsToken"] is not None:
            instance.xsts_token = str(dict_["xstsToken"])
        elif include_empty:
            instance.xsts_token = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "xstsToken": "xsts_token",
        }

    # endregion static methods
