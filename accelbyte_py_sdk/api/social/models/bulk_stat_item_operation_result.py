# justice-social-service (1.22.0)

# template file: justice_py_sdk_codegen/__main__.py

# Copyright (c) 2018 - 2021 AccelByte Inc. All Rights Reserved.
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


class BulkStatItemOperationResult(Model):
    """Bulk stat item operation result (BulkStatItemOperationResult)

    Properties:
        details: (details) OPTIONAL Dict[str, Any]

        stat_code: (statCode) OPTIONAL str

        success: (success) OPTIONAL bool
    """

    # region fields

    details: Dict[str, Any]                                                                        # OPTIONAL
    stat_code: str                                                                                 # OPTIONAL
    success: bool                                                                                  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_details(self, value: Dict[str, Any]) -> BulkStatItemOperationResult:
        self.details = value
        return self

    def with_stat_code(self, value: str) -> BulkStatItemOperationResult:
        self.stat_code = value
        return self

    def with_success(self, value: bool) -> BulkStatItemOperationResult:
        self.success = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "details"):
            result["details"] = {str(k0): v0 for k0, v0 in self.details.items()}
        elif include_empty:
            result["details"] = {}
        if hasattr(self, "stat_code"):
            result["statCode"] = str(self.stat_code)
        elif include_empty:
            result["statCode"] = str()
        if hasattr(self, "success"):
            result["success"] = bool(self.success)
        elif include_empty:
            result["success"] = bool()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        details: Optional[Dict[str, Any]] = None,
        stat_code: Optional[str] = None,
        success: Optional[bool] = None,
    ) -> BulkStatItemOperationResult:
        instance = cls()
        if details is not None:
            instance.details = details
        if stat_code is not None:
            instance.stat_code = stat_code
        if success is not None:
            instance.success = success
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> BulkStatItemOperationResult:
        instance = cls()
        if not dict_:
            return instance
        if "details" in dict_ and dict_["details"] is not None:
            instance.details = {str(k0): v0 for k0, v0 in dict_["details"].items()}
        elif include_empty:
            instance.details = {}
        if "statCode" in dict_ and dict_["statCode"] is not None:
            instance.stat_code = str(dict_["statCode"])
        elif include_empty:
            instance.stat_code = str()
        if "success" in dict_ and dict_["success"] is not None:
            instance.success = bool(dict_["success"])
        elif include_empty:
            instance.success = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "details": "details",
            "statCode": "stat_code",
            "success": "success",
        }

    # endregion static methods
