# justice-platform-service (3.40.0)

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

from .....core import Operation
from .....core import HttpResponse

from ...models import ConditionMatchResult
from ...models import ErrorEntity
from ...models import EventPayload


class CheckEventCondition(Operation):
    """Check if event payload match reward condition (checkEventCondition)

    <b>[TEST FACILITY ONLY] Forbidden in live environment. </b>Other detail info:
    <ul><li><i>Required permission</i>:
    resource="ADMIN:NAMESPACE:{namespace}:REWARD", action=2
    (READ)</li><li><i>Returns</i>: match result</li></ul>


    Properties:
        url: /platform/admin/namespaces/{namespace}/rewards/{rewardId}/match

        method: PUT

        tags: ["Reward"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        body: (body) OPTIONAL EventPayload in body

        namespace: (namespace) REQUIRED str in path

        reward_id: (rewardId) REQUIRED str in path

    Responses:
        200: OK - ConditionMatchResult (successful operation)

        404: Not Found - ErrorEntity (34041: Reward [{rewardId}] does not exist in namespace [{namespace}])
    """

    # region fields

    _url: str = "/platform/admin/namespaces/{namespace}/rewards/{rewardId}/match"
    _method: str = "PUT"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: EventPayload                                                                             # OPTIONAL in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    reward_id: str                                                                                 # REQUIRED in [path]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def security_type(self) -> Optional[str]:
        return self._security_type

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        return self.create_full_url(
            url=self.url,
            base_url=base_url,
            path_params=self.get_path_params(),
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
            "reward_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
        }

    def get_body_params(self) -> Any:
        if not hasattr(self, "body") or self.body is None:
            return None
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "reward_id"):
            result["rewardId"] = self.reward_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "reward_id") or self.reward_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: EventPayload) -> CheckEventCondition:
        self.body = value
        return self

    def with_namespace(self, value: str) -> CheckEventCondition:
        self.namespace = value
        return self

    def with_reward_id(self, value: str) -> CheckEventCondition:
        self.reward_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = EventPayload()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "reward_id") and self.reward_id:
            result["rewardId"] = str(self.reward_id)
        elif include_empty:
            result["rewardId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ConditionMatchResult], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - ConditionMatchResult (successful operation)

        404: Not Found - ErrorEntity (34041: Reward [{rewardId}] does not exist in namespace [{namespace}])
        """
        if code == 200:
            return ConditionMatchResult.create_from_dict(content), None
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            if undocumented_response.is_no_content():
                return None, None
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        reward_id: str,
        body: Optional[EventPayload] = None,
    ) -> CheckEventCondition:
        instance = cls()
        instance.namespace = namespace
        instance.reward_id = reward_id
        if body is not None:
            instance.body = body
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> CheckEventCondition:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = EventPayload.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = EventPayload()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "rewardId" in dict_ and dict_["rewardId"] is not None:
            instance.reward_id = str(dict_["rewardId"])
        elif include_empty:
            instance.reward_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "rewardId": "reward_id",
        }

    # endregion static methods