# justice-lobby-server (1.33.0)

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

from ...models import ModelUpdateTopicRequest
from ...models import RestapiErrorResponseV1


class UpdateNotificationTopicV1Admin(Operation):
    """update topic information by topic name (updateNotificationTopicV1Admin)

    Required permission : `ADMIN:NAMESPACE:{namespace}:NOTIFICATION [UPDATE]` with
    scope `social`  
    update topic information by topic name.  
    topic should be alphabets, no special char except underscore, uppercase and no
    spacing. for example: TOPIC_TEST. Already existing topic can not be created  
    Action Code: 50216


    Properties:
        url: /lobby/v1/admin/notification/namespaces/{namespace}/topics/{topicName}

        method: PUT

        tags: ["notification"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        body: (body) REQUIRED ModelUpdateTopicRequest in body

        namespace: (namespace) REQUIRED str in path

        topic_name: (topicName) REQUIRED str in path

    Responses:
        204: No Content - (No Content)

        400: Bad Request - RestapiErrorResponseV1 (Bad Request)

        401: Unauthorized - RestapiErrorResponseV1 (Unauthorized)

        403: Forbidden - RestapiErrorResponseV1 (Forbidden)

        404: Not Found - RestapiErrorResponseV1 (Not Found)

        500: Internal Server Error - RestapiErrorResponseV1 (Internal Server Error)
    """

    # region fields

    _url: str = "/lobby/v1/admin/notification/namespaces/{namespace}/topics/{topicName}"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelUpdateTopicRequest                                                                  # REQUIRED in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    topic_name: str                                                                                # REQUIRED in [path]

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

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "body",
            "namespace",
            "topic_name",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
        }

    def get_body_params(self) -> Any:
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "topic_name"):
            result["topicName"] = self.topic_name
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "topic_name") or self.topic_name is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelUpdateTopicRequest) -> UpdateNotificationTopicV1Admin:
        self.body = value
        return self

    def with_namespace(self, value: str) -> UpdateNotificationTopicV1Admin:
        self.namespace = value
        return self

    def with_topic_name(self, value: str) -> UpdateNotificationTopicV1Admin:
        self.topic_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelUpdateTopicRequest()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "topic_name") and self.topic_name:
            result["topicName"] = str(self.topic_name)
        elif include_empty:
            result["topicName"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, RestapiErrorResponseV1]]:
        """Parse the given response.

        204: No Content - (No Content)

        400: Bad Request - RestapiErrorResponseV1 (Bad Request)

        401: Unauthorized - RestapiErrorResponseV1 (Unauthorized)

        403: Forbidden - RestapiErrorResponseV1 (Forbidden)

        404: Not Found - RestapiErrorResponseV1 (Not Found)

        500: Internal Server Error - RestapiErrorResponseV1 (Internal Server Error)
        """
        if code == 204:
            return HttpResponse.create(code, "No Content"), None
        if code == 400:
            return None, RestapiErrorResponseV1.create_from_dict(content)
        if code == 401:
            return None, RestapiErrorResponseV1.create_from_dict(content)
        if code == 403:
            return None, RestapiErrorResponseV1.create_from_dict(content)
        if code == 404:
            return None, RestapiErrorResponseV1.create_from_dict(content)
        if code == 500:
            return None, RestapiErrorResponseV1.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: ModelUpdateTopicRequest,
        namespace: str,
        topic_name: str,
    ) -> UpdateNotificationTopicV1Admin:
        instance = cls()
        instance.body = body
        instance.namespace = namespace
        instance.topic_name = topic_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UpdateNotificationTopicV1Admin:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelUpdateTopicRequest.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelUpdateTopicRequest()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "topicName" in dict_ and dict_["topicName"] is not None:
            instance.topic_name = str(dict_["topicName"])
        elif include_empty:
            instance.topic_name = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "topicName": "topic_name",
        }

    # endregion static methods
