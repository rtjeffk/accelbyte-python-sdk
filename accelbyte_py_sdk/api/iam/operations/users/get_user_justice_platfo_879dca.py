# justice-iam-service (5.1.1)

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
from .....core import deprecated

from ...models import ModelGetUserJusticePlatformAccountResponse


@deprecated
class GetUserJusticePlatformAccount(Operation):
    """Get the Justice linked accounts on the designated namespace (GetUserJusticePlatformAccount)

    <p>This endpoint requires the client access token as the bearer token.
    Required permission 'ADMIN:NAMESPACE:{namespace}:JUSTICE:USER:{userId}
    [UPDATE]'</p> <p><strong>It is going to be removed on November 26th,
    2018</strong></p> <p>The endpoint returns user Justice platform account linked
    with the given user. If the user Justice platform account doesn't exist in the
    designated namespace, the endpoint is going to <strong>create and return the
    new Justice platform account.</strong> The newly user Justice platform account
    is going to be forced to perform token grant through the given user and can't
    perform password update</p> <h3>Read Justice Platform Account UserID</h3>
    <p>In order to read the Justice platform account UserID, it is required to
    have the permission: <strong>NAMESPACE:{namespace}:JUSTICE:USER:{userId}
    [READ]</strong>, otherwise the UserID is going to be censored and replaced
    with “Redacted” text.</p>


    Properties:
        url: /iam/namespaces/{namespace}/users/{userId}/platforms/justice/{targetNamespace}

        method: POST

        tags: ["Users"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        namespace: (namespace) REQUIRED str in path

        target_namespace: (targetNamespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

    Responses:
        200: OK - ModelGetUserJusticePlatformAccountResponse (OK)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)
    """

    # region fields

    _url: str = "/iam/namespaces/{namespace}/users/{userId}/platforms/justice/{targetNamespace}"
    _method: str = "POST"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    target_namespace: str                                                                          # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]

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
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
            "target_namespace",
            "user_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "target_namespace"):
            result["targetNamespace"] = self.target_namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "target_namespace") or self.target_namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> GetUserJusticePlatformAccount:
        self.namespace = value
        return self

    def with_target_namespace(self, value: str) -> GetUserJusticePlatformAccount:
        self.target_namespace = value
        return self

    def with_user_id(self, value: str) -> GetUserJusticePlatformAccount:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "target_namespace") and self.target_namespace:
            result["targetNamespace"] = str(self.target_namespace)
        elif include_empty:
            result["targetNamespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelGetUserJusticePlatformAccountResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - ModelGetUserJusticePlatformAccountResponse (OK)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)
        """
        if code == 200:
            return ModelGetUserJusticePlatformAccountResponse.create_from_dict(content), None
        if code == 400:
            return None, HttpResponse.create(code, "Bad Request")
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
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
        target_namespace: str,
        user_id: str,
    ) -> GetUserJusticePlatformAccount:
        instance = cls()
        instance.namespace = namespace
        instance.target_namespace = target_namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetUserJusticePlatformAccount:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "targetNamespace" in dict_ and dict_["targetNamespace"] is not None:
            instance.target_namespace = str(dict_["targetNamespace"])
        elif include_empty:
            instance.target_namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "targetNamespace": "target_namespace",
            "userId": "user_id",
        }

    # endregion static methods