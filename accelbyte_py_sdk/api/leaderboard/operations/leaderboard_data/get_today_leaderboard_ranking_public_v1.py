# justice-leaderboard-service (2.11.1)

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

from ...models import ModelsGetLeaderboardRankingResp
from ...models import ResponseErrorResponse


class GetTodayLeaderboardRankingPublicV1(Operation):
    """Get today leaderboard ranking data (GetTodayLeaderboardRankingPublicV1)

    <p>Get rankings in today leaderboard.</p>


    Properties:
        url: /leaderboard/v1/public/namespaces/{namespace}/leaderboards/{leaderboardCode}/today

        method: GET

        tags: ["LeaderboardData"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        leaderboard_code: (leaderboardCode) REQUIRED str in path

        namespace: (namespace) REQUIRED str in path

        limit: (limit) OPTIONAL int in query

        offset: (offset) OPTIONAL int in query

    Responses:
        200: OK - ModelsGetLeaderboardRankingResp (OK)

        400: Bad Request - ResponseErrorResponse (Bad Request)

        401: Unauthorized - ResponseErrorResponse (Unauthorized)

        403: Forbidden - ResponseErrorResponse (Forbidden)

        404: Not Found - ResponseErrorResponse (Not Found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
    """

    # region fields

    _url: str = "/leaderboard/v1/public/namespaces/{namespace}/leaderboards/{leaderboardCode}/today"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    leaderboard_code: str                                                                          # REQUIRED in [path]
    namespace: str                                                                                 # REQUIRED in [path]
    limit: int                                                                                     # OPTIONAL in [query]
    offset: int                                                                                    # OPTIONAL in [query]

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

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        return self.create_full_url(
            url=self.url,
            base_url=base_url,
            path_params=self.get_path_params(),
            query_params=self.get_query_params(),
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "leaderboard_code",
            "namespace",
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
        if hasattr(self, "leaderboard_code"):
            result["leaderboardCode"] = self.leaderboard_code
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "limit"):
            result["limit"] = self.limit
        if hasattr(self, "offset"):
            result["offset"] = self.offset
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "leaderboard_code") or self.leaderboard_code is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_leaderboard_code(self, value: str) -> GetTodayLeaderboardRankingPublicV1:
        self.leaderboard_code = value
        return self

    def with_namespace(self, value: str) -> GetTodayLeaderboardRankingPublicV1:
        self.namespace = value
        return self

    def with_limit(self, value: int) -> GetTodayLeaderboardRankingPublicV1:
        self.limit = value
        return self

    def with_offset(self, value: int) -> GetTodayLeaderboardRankingPublicV1:
        self.offset = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "leaderboard_code") and self.leaderboard_code:
            result["leaderboardCode"] = str(self.leaderboard_code)
        elif include_empty:
            result["leaderboardCode"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "limit") and self.limit:
            result["limit"] = int(self.limit)
        elif include_empty:
            result["limit"] = int()
        if hasattr(self, "offset") and self.offset:
            result["offset"] = int(self.offset)
        elif include_empty:
            result["offset"] = int()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsGetLeaderboardRankingResp], Union[None, ResponseErrorResponse]]:
        """Parse the given response.

        200: OK - ModelsGetLeaderboardRankingResp (OK)

        400: Bad Request - ResponseErrorResponse (Bad Request)

        401: Unauthorized - ResponseErrorResponse (Unauthorized)

        403: Forbidden - ResponseErrorResponse (Forbidden)

        404: Not Found - ResponseErrorResponse (Not Found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
        """
        if code == 200:
            return ModelsGetLeaderboardRankingResp.create_from_dict(content), None
        if code == 400:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 401:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 403:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 404:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 500:
            return None, ResponseErrorResponse.create_from_dict(content)
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
        leaderboard_code: str,
        namespace: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> GetTodayLeaderboardRankingPublicV1:
        instance = cls()
        instance.leaderboard_code = leaderboard_code
        instance.namespace = namespace
        if limit is not None:
            instance.limit = limit
        if offset is not None:
            instance.offset = offset
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetTodayLeaderboardRankingPublicV1:
        instance = cls()
        if "leaderboardCode" in dict_ and dict_["leaderboardCode"] is not None:
            instance.leaderboard_code = str(dict_["leaderboardCode"])
        elif include_empty:
            instance.leaderboard_code = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "limit" in dict_ and dict_["limit"] is not None:
            instance.limit = int(dict_["limit"])
        elif include_empty:
            instance.limit = int()
        if "offset" in dict_ and dict_["offset"] is not None:
            instance.offset = int(dict_["offset"])
        elif include_empty:
            instance.offset = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "leaderboardCode": "leaderboard_code",
            "namespace": "namespace",
            "limit": "limit",
            "offset": "offset",
        }

    # endregion static methods
