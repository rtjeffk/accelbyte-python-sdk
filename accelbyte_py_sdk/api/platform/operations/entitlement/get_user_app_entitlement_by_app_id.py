# Auto-generated at 2021-09-21T14:10:39.007216+08:00
# from: Justice Platform Service (3.24.0)

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

from ...models import AppEntitlementInfo
from ...models import ErrorEntity


class GetUserAppEntitlementByAppId(Operation):
    """Get user app entitlement by appId (getUserAppEntitlementByAppId)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/entitlements/byAppId

        method: GET

        tags: Entitlement

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        app_id: (appId) REQUIRED str in query

        active_only: (activeOnly) OPTIONAL bool in query

    Responses:
        200: OK - AppEntitlementInfo (successful operation)

        404: Not Found - ErrorEntity (ErrorCode: 31142 | ErrorMessage: Entitlement with appId [{appId}] does not exist in namespace [{namespace}])
    """

    # region fields

    _url: str = "/platform/admin/namespaces/{namespace}/users/{userId}/entitlements/byAppId"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    app_id: str                                                                                    # REQUIRED in [query]
    active_only: bool                                                                              # OPTIONAL in [query]

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
            "app_id",
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
        if hasattr(self, "app_id"):
            result["appId"] = self.app_id
        if hasattr(self, "active_only"):
            result["activeOnly"] = self.active_only
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        if not hasattr(self, "app_id") or self.app_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> GetUserAppEntitlementByAppId:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> GetUserAppEntitlementByAppId:
        self.user_id = value
        return self

    def with_app_id(self, value: str) -> GetUserAppEntitlementByAppId:
        self.app_id = value
        return self

    def with_active_only(self, value: bool) -> GetUserAppEntitlementByAppId:
        self.active_only = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "app_id") and self.app_id:
            result["appId"] = str(self.app_id)
        elif include_empty:
            result["appId"] = str()
        if hasattr(self, "active_only") and self.active_only:
            result["activeOnly"] = bool(self.active_only)
        elif include_empty:
            result["activeOnly"] = bool()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, AppEntitlementInfo], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - AppEntitlementInfo (successful operation)

        404: Not Found - ErrorEntity (ErrorCode: 31142 | ErrorMessage: Entitlement with appId [{appId}] does not exist in namespace [{namespace}])
        """
        if code == 200:
            return AppEntitlementInfo.create_from_dict(content), None
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        user_id: str,
        app_id: str,
        active_only: Optional[bool] = None,
    ) -> GetUserAppEntitlementByAppId:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        instance.app_id = app_id
        if active_only is not None:
            instance.active_only = active_only
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetUserAppEntitlementByAppId:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "appId" in dict_ and dict_["appId"] is not None:
            instance.app_id = str(dict_["appId"])
        elif include_empty:
            instance.app_id = str()
        if "activeOnly" in dict_ and dict_["activeOnly"] is not None:
            instance.active_only = bool(dict_["activeOnly"])
        elif include_empty:
            instance.active_only = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "userId": "user_id",
            "appId": "app_id",
            "activeOnly": "active_only",
        }

    # endregion static methods
