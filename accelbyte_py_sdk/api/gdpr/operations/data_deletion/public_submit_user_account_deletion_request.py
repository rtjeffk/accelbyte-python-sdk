# justice-gdpr-service (1.11.1)

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

from ...models import ModelsRequestDeleteResponse
from ...models import ResponseError


class PublicSubmitUserAccountDeletionRequest(Operation):
    """Submit user's account deletion requests (PublicSubmitUserAccountDeletionRequest)

    <p>Requires valid user access token and password


    Properties:
        url: /gdpr/public/namespaces/{namespace}/users/{userId}/deletions

        method: POST

        tags: ["Data Deletion"]

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        security: bearer

        password: (password) REQUIRED str in form_data

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

    Responses:
        201: Created - ModelsRequestDeleteResponse (Created)

        400: Bad Request - ResponseError (Bad Request)

        401: Unauthorized - ResponseError (Unauthorized)

        403: Forbidden - ResponseError (Forbidden)

        404: Not Found - ResponseError (Not Found)

        500: Internal Server Error - ResponseError (Internal Server Error)
    """

    # region fields

    _url: str = "/gdpr/public/namespaces/{namespace}/users/{userId}/deletions"
    _method: str = "POST"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    password: str                                                                                  # REQUIRED in [form_data]
    namespace: str                                                                                 # REQUIRED in [path]
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
            "password",
            "namespace",
            "user_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "form_data": self.get_form_data_params(),
            "path": self.get_path_params(),
        }

    def get_form_data_params(self) -> dict:
        result = {}
        if hasattr(self, "password"):
            result["password"] = self.password
        return result

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "password") or self.password is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_password(self, value: str) -> PublicSubmitUserAccountDeletionRequest:
        self.password = value
        return self

    def with_namespace(self, value: str) -> PublicSubmitUserAccountDeletionRequest:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> PublicSubmitUserAccountDeletionRequest:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "password") and self.password:
            result["password"] = str(self.password)
        elif include_empty:
            result["password"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsRequestDeleteResponse], Union[None, ResponseError]]:
        """Parse the given response.

        201: Created - ModelsRequestDeleteResponse (Created)

        400: Bad Request - ResponseError (Bad Request)

        401: Unauthorized - ResponseError (Unauthorized)

        403: Forbidden - ResponseError (Forbidden)

        404: Not Found - ResponseError (Not Found)

        500: Internal Server Error - ResponseError (Internal Server Error)
        """
        if code == 201:
            return ModelsRequestDeleteResponse.create_from_dict(content), None
        if code == 400:
            return None, ResponseError.create_from_dict(content)
        if code == 401:
            return None, ResponseError.create_from_dict(content)
        if code == 403:
            return None, ResponseError.create_from_dict(content)
        if code == 404:
            return None, ResponseError.create_from_dict(content)
        if code == 500:
            return None, ResponseError.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        password: str,
        namespace: str,
        user_id: str,
    ) -> PublicSubmitUserAccountDeletionRequest:
        instance = cls()
        instance.password = password
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicSubmitUserAccountDeletionRequest:
        instance = cls()
        if "password" in dict_ and dict_["password"] is not None:
            instance.password = str(dict_["password"])
        elif include_empty:
            instance.password = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "password": "password",
            "namespace": "namespace",
            "userId": "user_id",
        }

    # endregion static methods