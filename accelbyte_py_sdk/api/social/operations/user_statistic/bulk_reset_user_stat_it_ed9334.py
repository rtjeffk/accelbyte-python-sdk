# justice-social-service (1.24.0)

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

from ...models import ADTOObjectForResettingUserStatItems
from ...models import BulkStatItemOperationResult
from ...models import ValidationErrorEntity


class BulkResetUserStatItemValues(Operation):
    """Bulk reset user's statitem values (bulkResetUserStatItemValues)

    Bulk reset user's statitem values for given namespace and user. Other detail
    info: + *Required permission*:
    resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:STATITEM", action=4
    (UPDATE) + *Returns*: bulk updated result


    Required Permission(s):
        - ADMIN:NAMESPACE:{namespace}:USER:{userId}:STATITEM [UPDATE]

    Properties:
        url: /social/v2/admin/namespaces/{namespace}/users/{userId}/statitems/value/reset/bulk

        method: PUT

        tags: ["UserStatistic"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        body: (body) OPTIONAL List[ADTOObjectForResettingUserStatItems] in body

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        additional_key: (additionalKey) OPTIONAL str in query

    Responses:
        200: OK - List[BulkStatItemOperationResult] (successful operation)

        422: Unprocessable Entity - ValidationErrorEntity (20002: validation error)
    """

    # region fields

    _url: str = "/social/v2/admin/namespaces/{namespace}/users/{userId}/statitems/value/reset/bulk"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: List[ADTOObjectForResettingUserStatItems]                                                # OPTIONAL in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    additional_key: str                                                                            # OPTIONAL in [query]

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
            "user_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_body_params(self) -> Any:
        if not hasattr(self, "body") or self.body is None:
            return None
        return [i.to_dict() for i in self.body]

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "additional_key"):
            result["additionalKey"] = self.additional_key
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

    def with_body(self, value: List[ADTOObjectForResettingUserStatItems]) -> BulkResetUserStatItemValues:
        self.body = value
        return self

    def with_namespace(self, value: str) -> BulkResetUserStatItemValues:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> BulkResetUserStatItemValues:
        self.user_id = value
        return self

    def with_additional_key(self, value: str) -> BulkResetUserStatItemValues:
        self.additional_key = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = [i0.to_dict(include_empty=include_empty) for i0 in self.body]
        elif include_empty:
            result["body"] = []
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "additional_key") and self.additional_key:
            result["additionalKey"] = str(self.additional_key)
        elif include_empty:
            result["additionalKey"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, List[BulkStatItemOperationResult]], Union[None, ValidationErrorEntity]]:
        """Parse the given response.

        200: OK - List[BulkStatItemOperationResult] (successful operation)

        422: Unprocessable Entity - ValidationErrorEntity (20002: validation error)
        """
        if code == 200:
            return [BulkStatItemOperationResult.create_from_dict(i) for i in content], None
        if code == 422:
            return None, ValidationErrorEntity.create_from_dict(content)
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
        user_id: str,
        body: Optional[List[ADTOObjectForResettingUserStatItems]] = None,
        additional_key: Optional[str] = None,
    ) -> BulkResetUserStatItemValues:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        if body is not None:
            instance.body = body
        if additional_key is not None:
            instance.additional_key = additional_key
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> BulkResetUserStatItemValues:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = [ADTOObjectForResettingUserStatItems.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["body"]]
        elif include_empty:
            instance.body = []
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "additionalKey" in dict_ and dict_["additionalKey"] is not None:
            instance.additional_key = str(dict_["additionalKey"])
        elif include_empty:
            instance.additional_key = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "userId": "user_id",
            "additionalKey": "additional_key",
        }

    # endregion static methods