# Justice QoS Manager Service ()

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


class ModelsSetAliasRequest(Model):
    """Models set alias request (models.SetAliasRequest)

    Properties:
        alias: (alias) REQUIRED str
    """

    # region fields

    alias: str                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_alias(self, value: str) -> ModelsSetAliasRequest:
        self.alias = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "alias"):
            result["alias"] = str(self.alias)
        elif include_empty:
            result["alias"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        alias: str,
    ) -> ModelsSetAliasRequest:
        instance = cls()
        instance.alias = alias
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsSetAliasRequest:
        instance = cls()
        if not dict_:
            return instance
        if "alias" in dict_ and dict_["alias"] is not None:
            instance.alias = str(dict_["alias"])
        elif include_empty:
            instance.alias = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "alias": "alias",
        }

    # endregion static methods
