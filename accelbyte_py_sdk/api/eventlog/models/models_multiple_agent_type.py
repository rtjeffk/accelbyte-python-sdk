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

from ..models.models_agent_type import ModelsAgentType


class ModelsMultipleAgentType(Model):
    """Models multiple agent type (models.MultipleAgentType)

    Properties:
        agent_types: (AgentTypes) REQUIRED List[ModelsAgentType]
    """

    # region fields

    agent_types: List[ModelsAgentType]                                                             # REQUIRED

    # endregion fields

    # region with_x methods

    def with_agent_types(self, value: List[ModelsAgentType]) -> ModelsMultipleAgentType:
        self.agent_types = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "agent_types"):
            result["AgentTypes"] = [i0.to_dict(include_empty=include_empty) for i0 in self.agent_types]
        elif include_empty:
            result["AgentTypes"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        agent_types: List[ModelsAgentType],
    ) -> ModelsMultipleAgentType:
        instance = cls()
        instance.agent_types = agent_types
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsMultipleAgentType:
        instance = cls()
        if not dict_:
            return instance
        if "AgentTypes" in dict_ and dict_["AgentTypes"] is not None:
            instance.agent_types = [ModelsAgentType.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["AgentTypes"]]
        elif include_empty:
            instance.agent_types = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "AgentTypes": "agent_types",
        }

    # endregion static methods