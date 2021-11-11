# justice-dsm-controller-service (2.8.0)

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

from ..models.models_deployment_with_override import ModelsDeploymentWithOverride
from ..models.models_paging_cursor import ModelsPagingCursor


class ModelsListDeploymentResponse(Model):
    """Models list deployment response (models.ListDeploymentResponse)

    Properties:
        deployments: (deployments) REQUIRED List[ModelsDeploymentWithOverride]

        paging: (paging) REQUIRED ModelsPagingCursor
    """

    # region fields

    deployments: List[ModelsDeploymentWithOverride]                                                # REQUIRED
    paging: ModelsPagingCursor                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_deployments(self, value: List[ModelsDeploymentWithOverride]) -> ModelsListDeploymentResponse:
        self.deployments = value
        return self

    def with_paging(self, value: ModelsPagingCursor) -> ModelsListDeploymentResponse:
        self.paging = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "deployments"):
            result["deployments"] = [i0.to_dict(include_empty=include_empty) for i0 in self.deployments]
        elif include_empty:
            result["deployments"] = []
        if hasattr(self, "paging"):
            result["paging"] = self.paging.to_dict(include_empty=include_empty)
        elif include_empty:
            result["paging"] = ModelsPagingCursor()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        deployments: List[ModelsDeploymentWithOverride],
        paging: ModelsPagingCursor,
    ) -> ModelsListDeploymentResponse:
        instance = cls()
        instance.deployments = deployments
        instance.paging = paging
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsListDeploymentResponse:
        instance = cls()
        if not dict_:
            return instance
        if "deployments" in dict_ and dict_["deployments"] is not None:
            instance.deployments = [ModelsDeploymentWithOverride.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["deployments"]]
        elif include_empty:
            instance.deployments = []
        if "paging" in dict_ and dict_["paging"] is not None:
            instance.paging = ModelsPagingCursor.create_from_dict(dict_["paging"], include_empty=include_empty)
        elif include_empty:
            instance.paging = ModelsPagingCursor()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "deployments": "deployments",
            "paging": "paging",
        }

    # endregion static methods
