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

from ...models import ModelLoginHistoriesResponse


class PublicGetUserLoginHistoriesV3(Operation):
    """Get User's Login Histories (PublicGetUserLoginHistoriesV3)

    Required valid user authorization.

    Notes for this endpoint:

      * This endpoint retrieve the first page of the data if `after` and `before` parameters is empty.
      * The maximum value of the limit is 100 and the minimum value of the limit is 1.
      * This endpoint retrieve the next page of the data if we provide `after` parameters with valid Unix timestamp.
      * This endpoint retrieve the previous page of the data if we provide `before` parameter with valid data Unix timestamp.


    Properties:
        url: /iam/v3/public/namespaces/{namespace}/users/{userId}/logins/histories

        method: GET

        tags: ["Users"]

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        before: (before) OPTIONAL float in query

        after: (after) OPTIONAL float in query

        limit: (limit) OPTIONAL float in query

    Responses:
        200: OK - ModelLoginHistoriesResponse (OK)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)
    """

    # region fields

    _url: str = "/iam/v3/public/namespaces/{namespace}/users/{userId}/logins/histories"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    before: float                                                                                  # OPTIONAL in [query]
    after: float                                                                                   # OPTIONAL in [query]
    limit: float                                                                                   # OPTIONAL in [query]

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

        # query params
        result += "?" + "&".join([f"{k}={v}" for k, v in self.get_query_params().items()])

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
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
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "before"):
            result["before"] = self.before
        if hasattr(self, "after"):
            result["after"] = self.after
        if hasattr(self, "limit"):
            result["limit"] = self.limit
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> PublicGetUserLoginHistoriesV3:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> PublicGetUserLoginHistoriesV3:
        self.user_id = value
        return self

    def with_before(self, value: float) -> PublicGetUserLoginHistoriesV3:
        self.before = value
        return self

    def with_after(self, value: float) -> PublicGetUserLoginHistoriesV3:
        self.after = value
        return self

    def with_limit(self, value: float) -> PublicGetUserLoginHistoriesV3:
        self.limit = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "before") and self.before:
            result["before"] = float(self.before)
        elif include_empty:
            result["before"] = float()
        if hasattr(self, "after") and self.after:
            result["after"] = float(self.after)
        elif include_empty:
            result["after"] = float()
        if hasattr(self, "limit") and self.limit:
            result["limit"] = float(self.limit)
        elif include_empty:
            result["limit"] = float()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelLoginHistoriesResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - ModelLoginHistoriesResponse (OK)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)
        """
        if code == 200:
            return ModelLoginHistoriesResponse.create_from_dict(content), None
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
        if code == 404:
            return None, HttpResponse.create(code, "Not Found")
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        user_id: str,
        before: Optional[float] = None,
        after: Optional[float] = None,
        limit: Optional[float] = None,
    ) -> PublicGetUserLoginHistoriesV3:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        if before is not None:
            instance.before = before
        if after is not None:
            instance.after = after
        if limit is not None:
            instance.limit = limit
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicGetUserLoginHistoriesV3:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "before" in dict_ and dict_["before"] is not None:
            instance.before = float(dict_["before"])
        elif include_empty:
            instance.before = float()
        if "after" in dict_ and dict_["after"] is not None:
            instance.after = float(dict_["after"])
        elif include_empty:
            instance.after = float()
        if "limit" in dict_ and dict_["limit"] is not None:
            instance.limit = float(dict_["limit"])
        elif include_empty:
            instance.limit = float()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "userId": "user_id",
            "before": "before",
            "after": "after",
            "limit": "limit",
        }

    # endregion static methods
