# Justice Matchmaking Service (2.13.2)

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

from ...models import ResponseError
from ...models import ResponseErrorV1


class DeleteUserFromSessionInChannel(Operation):
    """Delete user from the session in a channel (DeleteUserFromSessionInChannel)

    Required Permission: ADMIN:NAMESPACE:{namespace}:MATCHMAKING:CHANNEL [Delete]
    Required Scope: social Delete a user from a session in the channel.


    Properties:
        url: /matchmaking/v1/admin/namespaces/{namespace}/channels/{channelName}/sessions/{matchID}/users/{userID}

        method: DELETE

        tags: ["Matchmaking"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        channel_name: (channelName) REQUIRED str in path

        match_id: (matchID) REQUIRED str in path

        namespace: (namespace) REQUIRED str in path

        user_id: (userID) REQUIRED str in path

    Responses:
        200: OK - (Operation succeeded)

        204: No Content - (Operation succeeded)

        400: Bad Request - ResponseErrorV1 (20002: validation error | 20019: unable to parse request body)

        401: Unauthorized - ResponseErrorV1 (20001: unauthorized access)

        403: Forbidden - ResponseErrorV1 (20013: insufficient permissions | 20014: invalid audience | 20015: insufficient scope)

        404: Not Found - ResponseErrorV1 (510110: channel not found)

        500: Internal Server Error - ResponseError (20000: internal server error)
    """

    # region fields

    _url: str = "/matchmaking/v1/admin/namespaces/{namespace}/channels/{channelName}/sessions/{matchID}/users/{userID}"
    _method: str = "DELETE"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    channel_name: str                                                                              # REQUIRED in [path]
    match_id: str                                                                                  # REQUIRED in [path]
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
            "channel_name",
            "match_id",
            "namespace",
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
        if hasattr(self, "channel_name"):
            result["channelName"] = self.channel_name
        if hasattr(self, "match_id"):
            result["matchID"] = self.match_id
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userID"] = self.user_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "channel_name") or self.channel_name is None:
            return False
        if not hasattr(self, "match_id") or self.match_id is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_channel_name(self, value: str) -> DeleteUserFromSessionInChannel:
        self.channel_name = value
        return self

    def with_match_id(self, value: str) -> DeleteUserFromSessionInChannel:
        self.match_id = value
        return self

    def with_namespace(self, value: str) -> DeleteUserFromSessionInChannel:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> DeleteUserFromSessionInChannel:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "channel_name") and self.channel_name:
            result["channelName"] = str(self.channel_name)
        elif include_empty:
            result["channelName"] = str()
        if hasattr(self, "match_id") and self.match_id:
            result["matchID"] = str(self.match_id)
        elif include_empty:
            result["matchID"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userID"] = str(self.user_id)
        elif include_empty:
            result["userID"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, ResponseError, ResponseErrorV1]]:
        """Parse the given response.

        200: OK - (Operation succeeded)

        204: No Content - (Operation succeeded)

        400: Bad Request - ResponseErrorV1 (20002: validation error | 20019: unable to parse request body)

        401: Unauthorized - ResponseErrorV1 (20001: unauthorized access)

        403: Forbidden - ResponseErrorV1 (20013: insufficient permissions | 20014: invalid audience | 20015: insufficient scope)

        404: Not Found - ResponseErrorV1 (510110: channel not found)

        500: Internal Server Error - ResponseError (20000: internal server error)
        """
        if code == 200:
            return HttpResponse.create(code, "OK"), None
        if code == 204:
            return None, None
        if code == 400:
            return None, ResponseErrorV1.create_from_dict(content)
        if code == 401:
            return None, ResponseErrorV1.create_from_dict(content)
        if code == 403:
            return None, ResponseErrorV1.create_from_dict(content)
        if code == 404:
            return None, ResponseErrorV1.create_from_dict(content)
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
        channel_name: str,
        match_id: str,
        namespace: str,
        user_id: str,
    ) -> DeleteUserFromSessionInChannel:
        instance = cls()
        instance.channel_name = channel_name
        instance.match_id = match_id
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> DeleteUserFromSessionInChannel:
        instance = cls()
        if "channelName" in dict_ and dict_["channelName"] is not None:
            instance.channel_name = str(dict_["channelName"])
        elif include_empty:
            instance.channel_name = str()
        if "matchID" in dict_ and dict_["matchID"] is not None:
            instance.match_id = str(dict_["matchID"])
        elif include_empty:
            instance.match_id = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userID" in dict_ and dict_["userID"] is not None:
            instance.user_id = str(dict_["userID"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "channelName": "channel_name",
            "matchID": "match_id",
            "namespace": "namespace",
            "userID": "user_id",
        }

    # endregion static methods