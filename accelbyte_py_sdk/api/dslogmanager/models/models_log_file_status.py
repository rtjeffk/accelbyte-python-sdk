# justice-ds-log-manager-service (1.3.0)

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


class ModelsLogFileStatus(Model):
    """Models log file status (models.LogFileStatus)

    Properties:
        log_existence: (log_existence) REQUIRED bool
    """

    # region fields

    log_existence: bool                                                                            # REQUIRED

    # endregion fields

    # region with_x methods

    def with_log_existence(self, value: bool) -> ModelsLogFileStatus:
        self.log_existence = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "log_existence"):
            result["log_existence"] = bool(self.log_existence)
        elif include_empty:
            result["log_existence"] = bool()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        log_existence: bool,
    ) -> ModelsLogFileStatus:
        instance = cls()
        instance.log_existence = log_existence
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsLogFileStatus:
        instance = cls()
        if not dict_:
            return instance
        if "log_existence" in dict_ and dict_["log_existence"] is not None:
            instance.log_existence = bool(dict_["log_existence"])
        elif include_empty:
            instance.log_existence = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "log_existence": "log_existence",
        }

    # endregion static methods