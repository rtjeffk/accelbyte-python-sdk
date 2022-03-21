# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# Justice QoS Manager Service ()

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

from ..models.models_server import ModelsServer


class ModelsListServerResponse(Model):
    """Models list server response (models.ListServerResponse)

    Properties:
        servers: (servers) REQUIRED List[ModelsServer]
    """

    # region fields

    servers: List[ModelsServer]                                                                    # REQUIRED

    # endregion fields

    # region with_x methods

    def with_servers(self, value: List[ModelsServer]) -> ModelsListServerResponse:
        self.servers = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "servers") or self.servers is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "servers"):
            result["servers"] = [i0.to_dict(include_empty=include_empty) for i0 in self.servers]
        elif include_empty:
            result["servers"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        servers: List[ModelsServer],
    ) -> ModelsListServerResponse:
        instance = cls()
        instance.servers = servers
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsListServerResponse:
        instance = cls()
        if not dict_:
            return instance
        if "servers" in dict_ and dict_["servers"] is not None:
            instance.servers = [ModelsServer.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["servers"]]
        elif include_empty:
            instance.servers = []
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, ModelsListServerResponse]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[ModelsListServerResponse]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[ModelsListServerResponse, List[ModelsListServerResponse]]:
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
            "servers": "servers",
        }

    # endregion static methods
