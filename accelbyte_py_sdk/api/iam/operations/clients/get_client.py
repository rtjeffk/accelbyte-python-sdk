# Auto-generated at 2021-09-21T14:10:34.874997+08:00
# from: Justice Iam Service (4.1.0)

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

from ...models import ClientmodelClientResponse


class GetClient(Operation):
    """Get Client (GetClient)

    Properties:
        url: /iam/clients/{clientId}

        method: GET

        tags: Clients

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        client_id: (clientId) REQUIRED str in path

    Responses:
        200: OK - ClientmodelClientResponse (OK)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)
    """

    # region fields

    _url: str = "/iam/clients/{clientId}"
    _method: str = "GET"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    client_id: str                                                                                 # REQUIRED in [path]

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
            "client_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "client_id"):
            result["clientId"] = self.client_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "client_id") or self.client_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_client_id(self, value: str) -> GetClient:
        self.client_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "client_id") and self.client_id:
            result["clientId"] = str(self.client_id)
        elif include_empty:
            result["clientId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ClientmodelClientResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - ClientmodelClientResponse (OK)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)
        """
        if code == 200:
            return ClientmodelClientResponse.create_from_dict(content), None
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
        if code == 404:
            return None, HttpResponse.create(code, "Not Found")
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        client_id: str,
    ) -> GetClient:
        instance = cls()
        instance.client_id = client_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetClient:
        instance = cls()
        if "clientId" in dict_ and dict_["clientId"] is not None:
            instance.client_id = str(dict_["clientId"])
        elif include_empty:
            instance.client_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "clientId": "client_id",
        }

    # endregion static methods
