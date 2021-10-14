# Auto-generated at 2021-10-14T22:17:18.540102+08:00
# from: Justice Group Service (2.4.0)

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

from .....core import Operation
from .....core import HttpResponse

from ...models import ModelsGroupResponseV1
from ...models import ModelsUpdateGroupPredefinedRuleRequestV1
from ...models import ResponseErrorResponse


class UpdateGroupPredefinedRulePublicV1(Operation):
    """update predefined group rule (updateGroupPredefinedRulePublicV1)

    Required valid user authentication

    Required Member Role Permission: "GROUP [UPDATE]"

    Update predefined group rule. This endpoint will check the group ID of the
    user based on the access token and compare it with the group ID in path
    parameter. It will also check the member role of the user based on the access
    token

    If the rule action is not defined in the group, it wil be added immediately to
    the predefined group rule

    Action Code: 73310


    Properties:
        url: /group/v1/public/namespaces/{namespace}/groups/{groupId}/rules/defined/{allowedAction}

        method: PUT

        tags: ["Group"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        body: (body) REQUIRED ModelsUpdateGroupPredefinedRuleRequestV1 in body

        namespace: (namespace) REQUIRED str in path

        group_id: (groupId) REQUIRED str in path

        allowed_action: (allowedAction) REQUIRED str in path

    Responses:
        200: OK - ModelsGroupResponseV1 (OK)

        400: Bad Request - ResponseErrorResponse (20019: unable to parse request body | 20002: validation error)

        401: Unauthorized - ResponseErrorResponse (20001: unauthorized access)

        403: Forbidden - ResponseErrorResponse (20013: insufficient permissions | 20022: token is not user token | 73036: insufficient member role permission)

        404: Not Found - ResponseErrorResponse (73333: group not found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
    """

    # region fields

    _url: str = "/group/v1/public/namespaces/{namespace}/groups/{groupId}/rules/defined/{allowedAction}"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelsUpdateGroupPredefinedRuleRequestV1                                                 # REQUIRED in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    group_id: str                                                                                  # REQUIRED in [path]
    allowed_action: str                                                                            # REQUIRED in [path]

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
    def security(self) -> Optional[str]:
        return self._security

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        result = base_url if base_url is not None else ""

        # path params
        url = self.url
        for k, v in self.get_path_params().items():
            url = url.replace(f"{{{k}}}", v)
        result += url

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "body",
            "namespace",
            "group_id",
            "allowed_action",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
        }

    def get_body_params(self) -> Any:
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "group_id"):
            result["groupId"] = self.group_id
        if hasattr(self, "allowed_action"):
            result["allowedAction"] = self.allowed_action
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "group_id") or self.group_id is None:
            return False
        if not hasattr(self, "allowed_action") or self.allowed_action is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelsUpdateGroupPredefinedRuleRequestV1) -> UpdateGroupPredefinedRulePublicV1:
        self.body = value
        return self

    def with_namespace(self, value: str) -> UpdateGroupPredefinedRulePublicV1:
        self.namespace = value
        return self

    def with_group_id(self, value: str) -> UpdateGroupPredefinedRulePublicV1:
        self.group_id = value
        return self

    def with_allowed_action(self, value: str) -> UpdateGroupPredefinedRulePublicV1:
        self.allowed_action = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelsUpdateGroupPredefinedRuleRequestV1()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "group_id") and self.group_id:
            result["groupId"] = str(self.group_id)
        elif include_empty:
            result["groupId"] = str()
        if hasattr(self, "allowed_action") and self.allowed_action:
            result["allowedAction"] = str(self.allowed_action)
        elif include_empty:
            result["allowedAction"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsGroupResponseV1], Union[None, ResponseErrorResponse]]:
        """Parse the given response.

        200: OK - ModelsGroupResponseV1 (OK)

        400: Bad Request - ResponseErrorResponse (20019: unable to parse request body | 20002: validation error)

        401: Unauthorized - ResponseErrorResponse (20001: unauthorized access)

        403: Forbidden - ResponseErrorResponse (20013: insufficient permissions | 20022: token is not user token | 73036: insufficient member role permission)

        404: Not Found - ResponseErrorResponse (73333: group not found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
        """
        if code == 200:
            return ModelsGroupResponseV1.create_from_dict(content), None
        if code == 400:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 401:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 403:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 404:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 500:
            return None, ResponseErrorResponse.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: ModelsUpdateGroupPredefinedRuleRequestV1,
        namespace: str,
        group_id: str,
        allowed_action: str,
    ) -> UpdateGroupPredefinedRulePublicV1:
        instance = cls()
        instance.body = body
        instance.namespace = namespace
        instance.group_id = group_id
        instance.allowed_action = allowed_action
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UpdateGroupPredefinedRulePublicV1:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelsUpdateGroupPredefinedRuleRequestV1.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelsUpdateGroupPredefinedRuleRequestV1()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "groupId" in dict_ and dict_["groupId"] is not None:
            instance.group_id = str(dict_["groupId"])
        elif include_empty:
            instance.group_id = str()
        if "allowedAction" in dict_ and dict_["allowedAction"] is not None:
            instance.allowed_action = str(dict_["allowedAction"])
        elif include_empty:
            instance.allowed_action = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "groupId": "group_id",
            "allowedAction": "allowed_action",
        }

    # endregion static methods
