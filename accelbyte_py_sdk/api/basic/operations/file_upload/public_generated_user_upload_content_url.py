# justice-basic-service (1.23.0)

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

from ...models import ErrorEntity
from ...models import FileUploadUrlInfo
from ...models import ValidationErrorEntity


class PublicGeneratedUserUploadContentUrl(Operation):
    """Generate Upload URL For User Content (publicGeneratedUserUploadContentUrl)

    Generate an upload URL for user content. It's valid for 10 minutes.
    There are 2 kinds of storage limitation per user : maximum file count and
    maximum file size.
    Other detail info:

      * Required permission : resource = "NAMESPACE:{namespace}:USER:{userId}:FILEUPLOAD" , action=1 (CREATE)
      *  Action code : 11102
      *  Default maximum file count per user : 10 files
      *  Default maximum file size per user : 104857600 bytes
      *  Returns : URL data


    Properties:
        url: /basic/v1/public/namespaces/{namespace}/users/{userId}/files

        method: POST

        tags: ["FileUpload"]

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        file_type: (fileType) REQUIRED str in query

    Responses:
        200: OK - FileUploadUrlInfo (Successful operation)

        400: Bad Request - ValidationErrorEntity (20002: validation error | 11131: Unable to {action}: File type is not supported)

        401: Unauthorized - ErrorEntity (20001: unauthorized)

        403: Forbidden - ErrorEntity (20013: insufficient permission)

        409: Conflict - ErrorEntity (11132: Unable to {action}: file storage exceed limitation, user ID: {userId}, namespace: {namespace})

        500: Internal Server Error - ErrorEntity (20000: internal server error)
    """

    # region fields

    _url: str = "/basic/v1/public/namespaces/{namespace}/users/{userId}/files"
    _method: str = "POST"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    file_type: str                                                                                 # REQUIRED in [query]

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
            "file_type",
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
        if hasattr(self, "file_type"):
            result["fileType"] = self.file_type
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        if not hasattr(self, "file_type") or self.file_type is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> PublicGeneratedUserUploadContentUrl:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> PublicGeneratedUserUploadContentUrl:
        self.user_id = value
        return self

    def with_file_type(self, value: str) -> PublicGeneratedUserUploadContentUrl:
        self.file_type = value
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
        if hasattr(self, "file_type") and self.file_type:
            result["fileType"] = str(self.file_type)
        elif include_empty:
            result["fileType"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, FileUploadUrlInfo], Union[None, ErrorEntity, ValidationErrorEntity]]:
        """Parse the given response.

        200: OK - FileUploadUrlInfo (Successful operation)

        400: Bad Request - ValidationErrorEntity (20002: validation error | 11131: Unable to {action}: File type is not supported)

        401: Unauthorized - ErrorEntity (20001: unauthorized)

        403: Forbidden - ErrorEntity (20013: insufficient permission)

        409: Conflict - ErrorEntity (11132: Unable to {action}: file storage exceed limitation, user ID: {userId}, namespace: {namespace})

        500: Internal Server Error - ErrorEntity (20000: internal server error)
        """
        if code == 200:
            return FileUploadUrlInfo.create_from_dict(content), None
        if code == 400:
            return None, ValidationErrorEntity.create_from_dict(content)
        if code == 401:
            return None, ErrorEntity.create_from_dict(content)
        if code == 403:
            return None, ErrorEntity.create_from_dict(content)
        if code == 409:
            return None, ErrorEntity.create_from_dict(content)
        if code == 500:
            return None, ErrorEntity.create_from_dict(content)
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
        file_type: str,
    ) -> PublicGeneratedUserUploadContentUrl:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        instance.file_type = file_type
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicGeneratedUserUploadContentUrl:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "fileType" in dict_ and dict_["fileType"] is not None:
            instance.file_type = str(dict_["fileType"])
        elif include_empty:
            instance.file_type = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "userId": "user_id",
            "fileType": "file_type",
        }

    # endregion static methods
