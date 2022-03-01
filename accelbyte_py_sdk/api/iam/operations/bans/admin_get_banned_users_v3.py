# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

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

# justice-iam-service (5.3.0)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse

from ...models import ModelGetUserBanV3Response


class AdminGetBannedUsersV3(Operation):
    """Get list of user filtered by ban types (AdminGetBannedUsersV3)

    Required permission 'ADMIN:BAN [READ]'
    Ban type is the code
    available for ban assignment. It is applicable globally for any namespace.
    action code : 10201

    Required Permission(s):
        - ADMIN:BAN [READ]

    Properties:
        url: /iam/v3/admin/namespaces/{namespace}/bans/users

        method: GET

        tags: ["Bans"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        namespace: (namespace) REQUIRED str in path

        active_only: (activeOnly) OPTIONAL bool in query

        ban_type: (banType) OPTIONAL str in query

        limit: (limit) OPTIONAL int in query

        offset: (offset) OPTIONAL int in query

    Responses:
        200: OK - ModelGetUserBanV3Response (OK)

        401: Unauthorized - ModelGetUserBanV3Response (20001: unauthorized access)

        403: Forbidden - ModelGetUserBanV3Response (20013: insufficient permissions)
    """

    # region fields

    _url: str = "/iam/v3/admin/namespaces/{namespace}/bans/users"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    active_only: bool                                                                              # OPTIONAL in [query]
    ban_type: str                                                                                  # OPTIONAL in [query]
    limit: int                                                                                     # OPTIONAL in [query]
    offset: int                                                                                    # OPTIONAL in [query]

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

    def get_full_url(self, base_url: Union[None, str] = None, collection_format_map: Optional[Dict[str, Optional[str]]] = None) -> str:
        return self.create_full_url(
            url=self.url,
            base_url=base_url,
            path_params=self.get_path_params(),
            query_params=self.get_query_params(),
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "active_only"):
            result["activeOnly"] = self.active_only
        if hasattr(self, "ban_type"):
            result["banType"] = self.ban_type
        if hasattr(self, "limit"):
            result["limit"] = self.limit
        if hasattr(self, "offset"):
            result["offset"] = self.offset
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> AdminGetBannedUsersV3:
        self.namespace = value
        return self

    def with_active_only(self, value: bool) -> AdminGetBannedUsersV3:
        self.active_only = value
        return self

    def with_ban_type(self, value: str) -> AdminGetBannedUsersV3:
        self.ban_type = value
        return self

    def with_limit(self, value: int) -> AdminGetBannedUsersV3:
        self.limit = value
        return self

    def with_offset(self, value: int) -> AdminGetBannedUsersV3:
        self.offset = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "active_only") and self.active_only:
            result["activeOnly"] = bool(self.active_only)
        elif include_empty:
            result["activeOnly"] = bool()
        if hasattr(self, "ban_type") and self.ban_type:
            result["banType"] = str(self.ban_type)
        elif include_empty:
            result["banType"] = str()
        if hasattr(self, "limit") and self.limit:
            result["limit"] = int(self.limit)
        elif include_empty:
            result["limit"] = int()
        if hasattr(self, "offset") and self.offset:
            result["offset"] = int(self.offset)
        elif include_empty:
            result["offset"] = int()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelGetUserBanV3Response], Union[None, ModelGetUserBanV3Response]]:
        """Parse the given response.

        200: OK - ModelGetUserBanV3Response (OK)

        401: Unauthorized - ModelGetUserBanV3Response (20001: unauthorized access)

        403: Forbidden - ModelGetUserBanV3Response (20013: insufficient permissions)
        """
        if code == 200:
            return ModelGetUserBanV3Response.create_from_dict(content), None
        if code == 401:
            return None, ModelGetUserBanV3Response.create_from_dict(content)
        if code == 403:
            return None, ModelGetUserBanV3Response.create_from_dict(content)
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
        active_only: Optional[bool] = None,
        ban_type: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> AdminGetBannedUsersV3:
        instance = cls()
        instance.namespace = namespace
        if active_only is not None:
            instance.active_only = active_only
        if ban_type is not None:
            instance.ban_type = ban_type
        if limit is not None:
            instance.limit = limit
        if offset is not None:
            instance.offset = offset
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminGetBannedUsersV3:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "activeOnly" in dict_ and dict_["activeOnly"] is not None:
            instance.active_only = bool(dict_["activeOnly"])
        elif include_empty:
            instance.active_only = bool()
        if "banType" in dict_ and dict_["banType"] is not None:
            instance.ban_type = str(dict_["banType"])
        elif include_empty:
            instance.ban_type = str()
        if "limit" in dict_ and dict_["limit"] is not None:
            instance.limit = int(dict_["limit"])
        elif include_empty:
            instance.limit = int()
        if "offset" in dict_ and dict_["offset"] is not None:
            instance.offset = int(dict_["offset"])
        elif include_empty:
            instance.offset = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "activeOnly": "active_only",
            "banType": "ban_type",
            "limit": "limit",
            "offset": "offset",
        }

    # endregion static methods
