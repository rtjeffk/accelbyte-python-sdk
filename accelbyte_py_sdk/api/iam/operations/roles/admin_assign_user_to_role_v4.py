# justice-iam-service (4.4.1)

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

from ...models import ModelAssignUserV4Request
from ...models import ModelAssignedUserV4Response
from ...models import RestErrorResponse


class AdminAssignUserToRoleV4(Operation):
    """Assign User to Role (AdminAssignUserToRoleV4)

    Required permission ADMIN:ROLE [UPDATE] Parameters: - userId: string
    (required) - namespace: string (user’s namespace) (required) -
    assignedNamespaces: array of string (namespaces to be assigned on role)
    (required) action code: 10410


    Properties:
        url: /iam/v4/admin/roles/{roleId}/users

        method: POST

        tags: ["Roles"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        body: (body) REQUIRED ModelAssignUserV4Request in body

        role_id: (roleId) REQUIRED str in path

    Responses:
        201: Created - ModelAssignedUserV4Response (Operation succeeded)

        400: Bad Request - RestErrorResponse (20002: validation error | 20019: unable to parse request body | 10457: specified role is not admin role)

        401: Unauthorized - RestErrorResponse (20001: unauthorized access)

        403: Forbidden - RestErrorResponse (20013: insufficient permissions | 10459: operator is not a role manager)

        404: Not Found - RestErrorResponse (10456: role not found | 20008: user not found)

        409: Conflict - RestErrorResponse (10469: role member exist)

        422: Unprocessable Entity - RestErrorResponse (10183: unprocessable entity)
    """

    # region fields

    _url: str = "/iam/v4/admin/roles/{roleId}/users"
    _method: str = "POST"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelAssignUserV4Request                                                                 # REQUIRED in [body]
    role_id: str                                                                                   # REQUIRED in [path]

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
            url = url.replace(f"{{{k}}}", str(v))
        result += url

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "body",
            "role_id",
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
        if hasattr(self, "role_id"):
            result["roleId"] = self.role_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "role_id") or self.role_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelAssignUserV4Request) -> AdminAssignUserToRoleV4:
        self.body = value
        return self

    def with_role_id(self, value: str) -> AdminAssignUserToRoleV4:
        self.role_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelAssignUserV4Request()
        if hasattr(self, "role_id") and self.role_id:
            result["roleId"] = str(self.role_id)
        elif include_empty:
            result["roleId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelAssignedUserV4Response], Union[None, RestErrorResponse]]:
        """Parse the given response.

        201: Created - ModelAssignedUserV4Response (Operation succeeded)

        400: Bad Request - RestErrorResponse (20002: validation error | 20019: unable to parse request body | 10457: specified role is not admin role)

        401: Unauthorized - RestErrorResponse (20001: unauthorized access)

        403: Forbidden - RestErrorResponse (20013: insufficient permissions | 10459: operator is not a role manager)

        404: Not Found - RestErrorResponse (10456: role not found | 20008: user not found)

        409: Conflict - RestErrorResponse (10469: role member exist)

        422: Unprocessable Entity - RestErrorResponse (10183: unprocessable entity)
        """
        if code == 201:
            return ModelAssignedUserV4Response.create_from_dict(content), None
        if code == 400:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 401:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 403:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 404:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 409:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 422:
            return None, RestErrorResponse.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: ModelAssignUserV4Request,
        role_id: str,
    ) -> AdminAssignUserToRoleV4:
        instance = cls()
        instance.body = body
        instance.role_id = role_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminAssignUserToRoleV4:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelAssignUserV4Request.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelAssignUserV4Request()
        if "roleId" in dict_ and dict_["roleId"] is not None:
            instance.role_id = str(dict_["roleId"])
        elif include_empty:
            instance.role_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "roleId": "role_id",
        }

    # endregion static methods
