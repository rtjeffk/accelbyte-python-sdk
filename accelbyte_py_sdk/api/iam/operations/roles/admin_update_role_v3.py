# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: justice_py_sdk_codegen/__main__.py

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

# justice-iam-service (5.13.0)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HeaderStr
from .....core import HttpResponse

from ...models import ModelRoleResponseV3
from ...models import ModelRoleUpdateRequestV3
from ...models import RestapiErrorResponse


class AdminUpdateRoleV3(Operation):
    """Update Role (AdminUpdateRoleV3)

    Required permission 'ADMIN:ROLE [UPDATE]'

    Update role request body:
    - roleName: specify role name, alphanumeric, cannot have special character (required)
    - isWildcard: specify if role can be assigned to wildcard (*) namespace (default false)
    - deletable: specify if role can be deleted or not (optional)


    action code: 10402

    Required Permission(s):
        - ADMIN:ROLE [UPDATE]

    Properties:
        url: /iam/v3/admin/roles/{roleId}

        method: PATCH

        tags: ["Roles"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        body: (body) REQUIRED ModelRoleUpdateRequestV3 in body

        role_id: (roleId) REQUIRED str in path

    Responses:
        200: OK - ModelRoleResponseV3 (OK)

        400: Bad Request - RestapiErrorResponse (20002: validation error | 20019: unable to parse request body)

        401: Unauthorized - RestapiErrorResponse (20001: unauthorized access)

        403: Forbidden - RestapiErrorResponse (20013: insufficient permissions)

        404: Not Found - RestapiErrorResponse (10456: role not found)
    """

    # region fields

    _url: str = "/iam/v3/admin/roles/{roleId}"
    _method: str = "PATCH"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _securities: List[List[str]] = [["BEARER_AUTH"]]
    _location_query: str = None

    body: ModelRoleUpdateRequestV3  # REQUIRED in [body]
    role_id: str  # REQUIRED in [path]

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
    def securities(self) -> List[List[str]]:
        return self._securities

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

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
        if hasattr(self, "role_id"):
            result["roleId"] = self.role_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelRoleUpdateRequestV3) -> AdminUpdateRoleV3:
        self.body = value
        return self

    def with_role_id(self, value: str) -> AdminUpdateRoleV3:
        self.role_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelRoleUpdateRequestV3()
        if hasattr(self, "role_id") and self.role_id:
            result["roleId"] = str(self.role_id)
        elif include_empty:
            result["roleId"] = ""
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(
        self, code: int, content_type: str, content: Any
    ) -> Tuple[
        Union[None, ModelRoleResponseV3],
        Union[None, HttpResponse, RestapiErrorResponse],
    ]:
        """Parse the given response.

        200: OK - ModelRoleResponseV3 (OK)

        400: Bad Request - RestapiErrorResponse (20002: validation error | 20019: unable to parse request body)

        401: Unauthorized - RestapiErrorResponse (20001: unauthorized access)

        403: Forbidden - RestapiErrorResponse (20013: insufficient permissions)

        404: Not Found - RestapiErrorResponse (10456: role not found)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        pre_processed_response, error = self.pre_process_response(
            code=code, content_type=content_type, content=content
        )
        if error is not None:
            return None, None if error.is_no_content() else error
        code, content_type, content = pre_processed_response

        if code == 200:
            return ModelRoleResponseV3.create_from_dict(content), None
        if code == 400:
            return None, RestapiErrorResponse.create_from_dict(content)
        if code == 401:
            return None, RestapiErrorResponse.create_from_dict(content)
        if code == 403:
            return None, RestapiErrorResponse.create_from_dict(content)
        if code == 404:
            return None, RestapiErrorResponse.create_from_dict(content)

        return None, self.handle_undocumented_response(
            code=code, content_type=content_type, content=content
        )

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: ModelRoleUpdateRequestV3,
        role_id: str,
    ) -> AdminUpdateRoleV3:
        instance = cls()
        instance.body = body
        instance.role_id = role_id
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> AdminUpdateRoleV3:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelRoleUpdateRequestV3.create_from_dict(
                dict_["body"], include_empty=include_empty
            )
        elif include_empty:
            instance.body = ModelRoleUpdateRequestV3()
        if "roleId" in dict_ and dict_["roleId"] is not None:
            instance.role_id = str(dict_["roleId"])
        elif include_empty:
            instance.role_id = ""
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "roleId": "role_id",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "body": True,
            "roleId": True,
        }

    # endregion static methods
