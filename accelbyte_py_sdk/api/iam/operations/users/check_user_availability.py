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
from .....core import clean_content_type
from .....core import try_convert_content_type

from ...models import RestErrorResponse


class CheckUserAvailability(Operation):
    """Check user's account availability (CheckUserAvailability)

    Check user's account availability.
    Available field :
    - displayName

    If request include access token with user ID data, that user ID will be excluded from availability check.
    For example, in case user update his emailAddress, he can use his own emailAddress to update his account.

    Response Code :
    - Account Available : 404 (not found)
    - Account Not Available : 204 (no content)

    Properties:
        url: /iam/v3/public/namespaces/{namespace}/users/availability

        method: GET

        tags: ["Users"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        namespace: (namespace) REQUIRED str in path

        field: (field) REQUIRED str in query

        query: (query) REQUIRED str in query

    Responses:
        204: No Content - (No Content)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Not Found)

        422: Unprocessable Entity - RestErrorResponse (20002: validation error)
    """

    # region fields

    _url: str = "/iam/v3/public/namespaces/{namespace}/users/availability"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    field: str                                                                                     # REQUIRED in [query]
    query: str                                                                                     # REQUIRED in [query]

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
            "field",
            "query",
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
        if hasattr(self, "field"):
            result["field"] = self.field
        if hasattr(self, "query"):
            result["query"] = self.query
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "field") or self.field is None:
            return False
        if not hasattr(self, "query") or self.query is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> CheckUserAvailability:
        self.namespace = value
        return self

    def with_field(self, value: str) -> CheckUserAvailability:
        self.field = value
        return self

    def with_query(self, value: str) -> CheckUserAvailability:
        self.query = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "field") and self.field:
            result["field"] = str(self.field)
        elif include_empty:
            result["field"] = str()
        if hasattr(self, "query") and self.query:
            result["query"] = str(self.query)
        elif include_empty:
            result["query"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[None, Union[None, HttpResponse, RestErrorResponse]]:
        """Parse the given response.

        204: No Content - (No Content)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Not Found)

        422: Unprocessable Entity - RestErrorResponse (20002: validation error)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        if content:
            actual_content_type = clean_content_type(content_type)
            if actual_content_type not in self.produces:
                was_converted, converted_content = try_convert_content_type(actual_content_type, self.produces, content)
                if was_converted:
                    content = converted_content
                else:
                    return None, HttpResponse.create_unexpected_content_type_error(actual=actual_content_type, expected=self.produces)
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
        if code == 422:
            return None, RestErrorResponse.create_from_dict(content)
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
        field: str,
        query: str,
    ) -> CheckUserAvailability:
        instance = cls()
        instance.namespace = namespace
        instance.field = field
        instance.query = query
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> CheckUserAvailability:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "field" in dict_ and dict_["field"] is not None:
            instance.field = str(dict_["field"])
        elif include_empty:
            instance.field = str()
        if "query" in dict_ and dict_["query"] is not None:
            instance.query = str(dict_["query"])
        elif include_empty:
            instance.query = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "field": "field",
            "query": "query",
        }

    # endregion static methods
