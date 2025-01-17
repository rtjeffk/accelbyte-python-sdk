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
from .....core import deprecated


@deprecated
class AddClientPermission(Operation):
    """Add Client Permission (AddClientPermission)

    ## The endpoint is going to be deprecated




    Required permission 'CLIENT:ADMIN [UPDATE]'
    Endpoint migration guide




      * Substitute endpoint: /iam/v3/admin/namespaces/{namespace}/clients/{clientId}/permissions [POST]


      * Note:

    Required Permission(s):
        - CLIENT:ADMIN [UPDATE]

    Properties:
        url: /iam/clients/{clientId}/clientpermissions/{resource}/{action}

        method: POST

        tags: ["Clients(Deprecated)"]

        consumes: ["*/*"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        action: (action) REQUIRED int in path

        client_id: (clientId) REQUIRED str in path

        resource: (resource) REQUIRED str in path

    Responses:
        204: No Content - (Operation succeeded)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)
    """

    # region fields

    _url: str = "/iam/clients/{clientId}/clientpermissions/{resource}/{action}"
    _method: str = "POST"
    _consumes: List[str] = ["*/*"]
    _produces: List[str] = ["application/json"]
    _securities: List[List[str]] = [["BEARER_AUTH"]]
    _location_query: str = None

    action: int  # REQUIRED in [path]
    client_id: str  # REQUIRED in [path]
    resource: str  # REQUIRED in [path]

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
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "action"):
            result["action"] = self.action
        if hasattr(self, "client_id"):
            result["clientId"] = self.client_id
        if hasattr(self, "resource"):
            result["resource"] = self.resource
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_action(self, value: int) -> AddClientPermission:
        self.action = value
        return self

    def with_client_id(self, value: str) -> AddClientPermission:
        self.client_id = value
        return self

    def with_resource(self, value: str) -> AddClientPermission:
        self.resource = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "action") and self.action:
            result["action"] = int(self.action)
        elif include_empty:
            result["action"] = 0
        if hasattr(self, "client_id") and self.client_id:
            result["clientId"] = str(self.client_id)
        elif include_empty:
            result["clientId"] = ""
        if hasattr(self, "resource") and self.resource:
            result["resource"] = str(self.resource)
        elif include_empty:
            result["resource"] = ""
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(
        self, code: int, content_type: str, content: Any
    ) -> Tuple[None, Union[None, HttpResponse]]:
        """Parse the given response.

        204: No Content - (Operation succeeded)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)

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

        if code == 204:
            return None, None
        if code == 400:
            return None, HttpResponse.create(code, "Bad Request")
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
        if code == 404:
            return None, HttpResponse.create(code, "Not Found")

        return None, self.handle_undocumented_response(
            code=code, content_type=content_type, content=content
        )

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        action: int,
        client_id: str,
        resource: str,
    ) -> AddClientPermission:
        instance = cls()
        instance.action = action
        instance.client_id = client_id
        instance.resource = resource
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> AddClientPermission:
        instance = cls()
        if "action" in dict_ and dict_["action"] is not None:
            instance.action = int(dict_["action"])
        elif include_empty:
            instance.action = 0
        if "clientId" in dict_ and dict_["clientId"] is not None:
            instance.client_id = str(dict_["clientId"])
        elif include_empty:
            instance.client_id = ""
        if "resource" in dict_ and dict_["resource"] is not None:
            instance.resource = str(dict_["resource"])
        elif include_empty:
            instance.resource = ""
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "action": "action",
            "clientId": "client_id",
            "resource": "resource",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "action": True,
            "clientId": True,
            "resource": True,
        }

    # endregion static methods
