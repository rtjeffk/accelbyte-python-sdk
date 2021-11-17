# justice-event-log-service (1.18.3)

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


class ModelsAgentType(Model):
    """Models agent type (models.AgentType)

    Properties:
        agent_type: (AgentType) REQUIRED int

        description: (Description) REQUIRED str
    """

    # region fields

    agent_type: int                                                                                # REQUIRED
    description: str                                                                               # REQUIRED

    # endregion fields

    # region with_x methods

    def with_agent_type(self, value: int) -> ModelsAgentType:
        self.agent_type = value
        return self

    def with_description(self, value: str) -> ModelsAgentType:
        self.description = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "agent_type"):
            result["AgentType"] = int(self.agent_type)
        elif include_empty:
            result["AgentType"] = int()
        if hasattr(self, "description"):
            result["Description"] = str(self.description)
        elif include_empty:
            result["Description"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        agent_type: int,
        description: str,
    ) -> ModelsAgentType:
        instance = cls()
        instance.agent_type = agent_type
        instance.description = description
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsAgentType:
        instance = cls()
        if not dict_:
            return instance
        if "AgentType" in dict_ and dict_["AgentType"] is not None:
            instance.agent_type = int(dict_["AgentType"])
        elif include_empty:
            instance.agent_type = int()
        if "Description" in dict_ and dict_["Description"] is not None:
            instance.description = str(dict_["Description"])
        elif include_empty:
            instance.description = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "AgentType": "agent_type",
            "Description": "description",
        }

    # endregion static methods