# Auto-generated at 2021-10-21T08:52:24.253484+08:00
# from: Justice dsmc Service (2.6.0)

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

from ..models.models_request_matching_ally import ModelsRequestMatchingAlly


class ModelsCreateSessionRequest(Model):
    """Models create session request (models.CreateSessionRequest)

    Properties:
        client_version: (client_version) REQUIRED str

        configuration: (configuration) REQUIRED str

        deployment: (deployment) REQUIRED str

        game_mode: (game_mode) REQUIRED str

        matching_allies: (matching_allies) REQUIRED List[ModelsRequestMatchingAlly]

        namespace: (namespace) REQUIRED str

        pod_name: (pod_name) REQUIRED str

        region: (region) REQUIRED str

        session_id: (session_id) REQUIRED str
    """

    # region fields

    client_version: str                                                                            # REQUIRED
    configuration: str                                                                             # REQUIRED
    deployment: str                                                                                # REQUIRED
    game_mode: str                                                                                 # REQUIRED
    matching_allies: List[ModelsRequestMatchingAlly]                                               # REQUIRED
    namespace: str                                                                                 # REQUIRED
    pod_name: str                                                                                  # REQUIRED
    region: str                                                                                    # REQUIRED
    session_id: str                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_client_version(self, value: str) -> ModelsCreateSessionRequest:
        self.client_version = value
        return self

    def with_configuration(self, value: str) -> ModelsCreateSessionRequest:
        self.configuration = value
        return self

    def with_deployment(self, value: str) -> ModelsCreateSessionRequest:
        self.deployment = value
        return self

    def with_game_mode(self, value: str) -> ModelsCreateSessionRequest:
        self.game_mode = value
        return self

    def with_matching_allies(self, value: List[ModelsRequestMatchingAlly]) -> ModelsCreateSessionRequest:
        self.matching_allies = value
        return self

    def with_namespace(self, value: str) -> ModelsCreateSessionRequest:
        self.namespace = value
        return self

    def with_pod_name(self, value: str) -> ModelsCreateSessionRequest:
        self.pod_name = value
        return self

    def with_region(self, value: str) -> ModelsCreateSessionRequest:
        self.region = value
        return self

    def with_session_id(self, value: str) -> ModelsCreateSessionRequest:
        self.session_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "client_version") and self.client_version:
            result["client_version"] = str(self.client_version)
        elif include_empty:
            result["client_version"] = str()
        if hasattr(self, "configuration") and self.configuration:
            result["configuration"] = str(self.configuration)
        elif include_empty:
            result["configuration"] = str()
        if hasattr(self, "deployment") and self.deployment:
            result["deployment"] = str(self.deployment)
        elif include_empty:
            result["deployment"] = str()
        if hasattr(self, "game_mode") and self.game_mode:
            result["game_mode"] = str(self.game_mode)
        elif include_empty:
            result["game_mode"] = str()
        if hasattr(self, "matching_allies") and self.matching_allies:
            result["matching_allies"] = [i0.to_dict(include_empty=include_empty) for i0 in self.matching_allies]
        elif include_empty:
            result["matching_allies"] = []
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "pod_name") and self.pod_name:
            result["pod_name"] = str(self.pod_name)
        elif include_empty:
            result["pod_name"] = str()
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = str()
        if hasattr(self, "session_id") and self.session_id:
            result["session_id"] = str(self.session_id)
        elif include_empty:
            result["session_id"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        client_version: str,
        configuration: str,
        deployment: str,
        game_mode: str,
        matching_allies: List[ModelsRequestMatchingAlly],
        namespace: str,
        pod_name: str,
        region: str,
        session_id: str,
    ) -> ModelsCreateSessionRequest:
        instance = cls()
        instance.client_version = client_version
        instance.configuration = configuration
        instance.deployment = deployment
        instance.game_mode = game_mode
        instance.matching_allies = matching_allies
        instance.namespace = namespace
        instance.pod_name = pod_name
        instance.region = region
        instance.session_id = session_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsCreateSessionRequest:
        instance = cls()
        if not dict_:
            return instance
        if "client_version" in dict_ and dict_["client_version"] is not None:
            instance.client_version = str(dict_["client_version"])
        elif include_empty:
            instance.client_version = str()
        if "configuration" in dict_ and dict_["configuration"] is not None:
            instance.configuration = str(dict_["configuration"])
        elif include_empty:
            instance.configuration = str()
        if "deployment" in dict_ and dict_["deployment"] is not None:
            instance.deployment = str(dict_["deployment"])
        elif include_empty:
            instance.deployment = str()
        if "game_mode" in dict_ and dict_["game_mode"] is not None:
            instance.game_mode = str(dict_["game_mode"])
        elif include_empty:
            instance.game_mode = str()
        if "matching_allies" in dict_ and dict_["matching_allies"] is not None:
            instance.matching_allies = [ModelsRequestMatchingAlly.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["matching_allies"]]
        elif include_empty:
            instance.matching_allies = []
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "pod_name" in dict_ and dict_["pod_name"] is not None:
            instance.pod_name = str(dict_["pod_name"])
        elif include_empty:
            instance.pod_name = str()
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = str()
        if "session_id" in dict_ and dict_["session_id"] is not None:
            instance.session_id = str(dict_["session_id"])
        elif include_empty:
            instance.session_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "client_version": "client_version",
            "configuration": "configuration",
            "deployment": "deployment",
            "game_mode": "game_mode",
            "matching_allies": "matching_allies",
            "namespace": "namespace",
            "pod_name": "pod_name",
            "region": "region",
            "session_id": "session_id",
        }

    # endregion static methods