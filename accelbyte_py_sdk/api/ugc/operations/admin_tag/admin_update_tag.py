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

# justice-ugc-service (1.14.0)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse
from .....core import clean_content_type
from .....core import try_convert_content_type

from ...models import ModelsCreateTagRequest
from ...models import ModelsCreateTagResponse
from ...models import ResponseError


class AdminUpdateTag(Operation):
    """Update tag (AdminUpdateTag)

    Required permission ADMIN:NAMESPACE:{namespace}:UGCCONFIG [UPDATE]
    updates a tag

    Required Permission(s):
        - ADMIN:NAMESPACE:{namespace}:UGCCONFIG [UPDATE]

    Properties:
        url: /ugc/v1/admin/namespaces/{namespace}/tags/{tagId}

        method: PUT

        tags: ["Admin Tag"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        body: (body) REQUIRED ModelsCreateTagRequest in body

        namespace: (namespace) REQUIRED str in path

        tag_id: (tagId) REQUIRED str in path

    Responses:
        200: OK - ModelsCreateTagResponse (OK)

        400: Bad Request - ResponseError (Bad Request)

        401: Unauthorized - ResponseError (Unauthorized)

        404: Not Found - ResponseError (Not Found)

        409: Conflict - ResponseError (Conflict)

        500: Internal Server Error - ResponseError (Internal Server Error)
    """

    # region fields

    _url: str = "/ugc/v1/admin/namespaces/{namespace}/tags/{tagId}"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelsCreateTagRequest                                                                   # REQUIRED in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    tag_id: str                                                                                    # REQUIRED in [path]

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
            "body",
            "namespace",
            "tag_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
        }

    def get_body_params(self) -> Any:
        if not hasattr(self, "body") or self.body is None:
            return None
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "tag_id"):
            result["tagId"] = self.tag_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "tag_id") or self.tag_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelsCreateTagRequest) -> AdminUpdateTag:
        self.body = value
        return self

    def with_namespace(self, value: str) -> AdminUpdateTag:
        self.namespace = value
        return self

    def with_tag_id(self, value: str) -> AdminUpdateTag:
        self.tag_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelsCreateTagRequest()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "tag_id") and self.tag_id:
            result["tagId"] = str(self.tag_id)
        elif include_empty:
            result["tagId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsCreateTagResponse], Union[None, ResponseError]]:
        """Parse the given response.

        200: OK - ModelsCreateTagResponse (OK)

        400: Bad Request - ResponseError (Bad Request)

        401: Unauthorized - ResponseError (Unauthorized)

        404: Not Found - ResponseError (Not Found)

        409: Conflict - ResponseError (Conflict)

        500: Internal Server Error - ResponseError (Internal Server Error)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        if content and content_type != "location":
            actual_content_type = clean_content_type(content_type)
            if actual_content_type not in self.produces:
                was_converted, converted_content = try_convert_content_type(actual_content_type, self.produces, content)
                if was_converted:
                    content = converted_content
                else:
                    return None, HttpResponse.create_unexpected_content_type_error(actual=actual_content_type, expected=self.produces)
        if code == 200:
            return ModelsCreateTagResponse.create_from_dict(content), None
        if code == 400:
            return None, ResponseError.create_from_dict(content)
        if code == 401:
            return None, ResponseError.create_from_dict(content)
        if code == 404:
            return None, ResponseError.create_from_dict(content)
        if code == 409:
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
        body: ModelsCreateTagRequest,
        namespace: str,
        tag_id: str,
    ) -> AdminUpdateTag:
        instance = cls()
        instance.body = body
        instance.namespace = namespace
        instance.tag_id = tag_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminUpdateTag:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelsCreateTagRequest.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelsCreateTagRequest()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "tagId" in dict_ and dict_["tagId"] is not None:
            instance.tag_id = str(dict_["tagId"])
        elif include_empty:
            instance.tag_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "tagId": "tag_id",
        }

    # endregion static methods
