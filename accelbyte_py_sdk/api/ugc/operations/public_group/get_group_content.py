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

# justice-ugc-service (1.13.0)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse

from ...models import ModelsPaginatedContentDownloadResponse
from ...models import ResponseError


class GetGroupContent(Operation):
    """Get contents belong to a group (GetGroupContent)

    Required permission NAMESPACE:{namespace}:USER:{userId}:CONTENT [READ].

    Required Permission(s):
        - NAMESPACE:{namespace}:USER:{userId}:CONTENT [READ]

    Properties:
        url: /ugc/v1/public/namespaces/{namespace}/users/{userId}/groups/{groupId}/contents

        method: GET

        tags: ["Public Group"]

        consumes: ["application/json", "application/octet-stream"]

        produces: ["application/json"]

        security_type: bearer

        group_id: (groupId) REQUIRED str in path

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        limit: (limit) OPTIONAL str in query

        offset: (offset) OPTIONAL str in query

    Responses:
        200: OK - ModelsPaginatedContentDownloadResponse (OK)

        401: Unauthorized - ResponseError (Unauthorized)

        404: Not Found - ResponseError (Not Found)

        500: Internal Server Error - ResponseError (Internal Server Error)
    """

    # region fields

    _url: str = "/ugc/v1/public/namespaces/{namespace}/users/{userId}/groups/{groupId}/contents"
    _method: str = "GET"
    _consumes: List[str] = ["application/json", "application/octet-stream"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    group_id: str                                                                                  # REQUIRED in [path]
    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    limit: str                                                                                     # OPTIONAL in [query]
    offset: str                                                                                    # OPTIONAL in [query]

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
            "group_id",
            "namespace",
            "user_id",
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
        if hasattr(self, "group_id"):
            result["groupId"] = self.group_id
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "limit"):
            result["limit"] = self.limit
        if hasattr(self, "offset"):
            result["offset"] = self.offset
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "group_id") or self.group_id is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_group_id(self, value: str) -> GetGroupContent:
        self.group_id = value
        return self

    def with_namespace(self, value: str) -> GetGroupContent:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> GetGroupContent:
        self.user_id = value
        return self

    def with_limit(self, value: str) -> GetGroupContent:
        self.limit = value
        return self

    def with_offset(self, value: str) -> GetGroupContent:
        self.offset = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "group_id") and self.group_id:
            result["groupId"] = str(self.group_id)
        elif include_empty:
            result["groupId"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "limit") and self.limit:
            result["limit"] = str(self.limit)
        elif include_empty:
            result["limit"] = str()
        if hasattr(self, "offset") and self.offset:
            result["offset"] = str(self.offset)
        elif include_empty:
            result["offset"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsPaginatedContentDownloadResponse], Union[None, ResponseError]]:
        """Parse the given response.

        200: OK - ModelsPaginatedContentDownloadResponse (OK)

        401: Unauthorized - ResponseError (Unauthorized)

        404: Not Found - ResponseError (Not Found)

        500: Internal Server Error - ResponseError (Internal Server Error)
        """
        if code == 200:
            return ModelsPaginatedContentDownloadResponse.create_from_dict(content), None
        if code == 401:
            return None, ResponseError.create_from_dict(content)
        if code == 404:
            return None, ResponseError.create_from_dict(content)
        if code == 500:
            return None, ResponseError.create_from_dict(content)
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
        group_id: str,
        namespace: str,
        user_id: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> GetGroupContent:
        instance = cls()
        instance.group_id = group_id
        instance.namespace = namespace
        instance.user_id = user_id
        if limit is not None:
            instance.limit = limit
        if offset is not None:
            instance.offset = offset
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetGroupContent:
        instance = cls()
        if "groupId" in dict_ and dict_["groupId"] is not None:
            instance.group_id = str(dict_["groupId"])
        elif include_empty:
            instance.group_id = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "limit" in dict_ and dict_["limit"] is not None:
            instance.limit = str(dict_["limit"])
        elif include_empty:
            instance.limit = str()
        if "offset" in dict_ and dict_["offset"] is not None:
            instance.offset = str(dict_["offset"])
        elif include_empty:
            instance.offset = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "groupId": "group_id",
            "namespace": "namespace",
            "userId": "user_id",
            "limit": "limit",
            "offset": "offset",
        }

    # endregion static methods
