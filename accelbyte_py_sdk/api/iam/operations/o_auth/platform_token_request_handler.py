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

# justice-iam-service (5.5.1)

from __future__ import annotations
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse
from .....core import deprecated

from ...models import OauthmodelErrorResponse
from ...models import OauthmodelTokenResponse


@deprecated
class PlatformTokenRequestHandler(Operation):
    """OAuth2 access token generation specific to platform (PlatformTokenRequestHandler)

    ## The endpoint is going to be deprecated at 2 July, 2018. Please use this instead: oauth/platforms/{platformId}/token





    This endpoint requires all requests to have Authorization header set with Basic access authentication
    constructed from client id and client secret. For publisher-game namespace schema : Specify only either platform_token or device_id. Device token grant
    should be requested along with device_id parameter against game namespace. Another 3rd party platform token grant should be requested
    along with platform_token parameter against publisher namespace.






    Supported platforms:





      1. steamopenid : Steam's user authentication method using OpenID 2.0. The expected value of the platform token is the URL generated by Steam on web authentication




    The JWT contains user's active bans with its expiry date. List of ban types can be obtained from /iam/bans.

    Properties:
        url: /iam/oauth/namespaces/{namespace}/platforms/{platformId}/token

        method: POST

        tags: ["OAuth"]

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        security_type: bearer

        device_id: (device_id) OPTIONAL str in form_data

        platform_token: (platform_token) OPTIONAL str in form_data

        namespace: (namespace) REQUIRED str in path

        platform_id: (platformId) REQUIRED str in path

    Responses:
        200: OK - OauthmodelTokenResponse (Access Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)
    """

    # region fields

    _url: str = "/iam/oauth/namespaces/{namespace}/platforms/{platformId}/token"
    _method: str = "POST"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    device_id: str                                                                                 # OPTIONAL in [form_data]
    platform_token: str                                                                            # OPTIONAL in [form_data]
    namespace: str                                                                                 # REQUIRED in [path]
    platform_id: str                                                                               # REQUIRED in [path]

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
            "platform_id",
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
        if hasattr(self, "device_id"):
            result["device_id"] = self.device_id
        if hasattr(self, "platform_token"):
            result["platform_token"] = self.platform_token
        return result

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        # required checks
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "platform_id") or self.platform_id is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region with_x methods

    def with_device_id(self, value: str) -> PlatformTokenRequestHandler:
        self.device_id = value
        return self

    def with_platform_token(self, value: str) -> PlatformTokenRequestHandler:
        self.platform_token = value
        return self

    def with_namespace(self, value: str) -> PlatformTokenRequestHandler:
        self.namespace = value
        return self

    def with_platform_id(self, value: str) -> PlatformTokenRequestHandler:
        self.platform_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "device_id") and self.device_id:
            result["device_id"] = str(self.device_id)
        elif include_empty:
            result["device_id"] = str()
        if hasattr(self, "platform_token") and self.platform_token:
            result["platform_token"] = str(self.platform_token)
        elif include_empty:
            result["platform_token"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "platform_id") and self.platform_id:
            result["platformId"] = str(self.platform_id)
        elif include_empty:
            result["platformId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, OauthmodelTokenResponse], Union[None, HttpResponse, OauthmodelErrorResponse]]:
        """Parse the given response.

        200: OK - OauthmodelTokenResponse (Access Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        pre_processed_response, error = self.pre_process_response(code=code, content_type=content_type, content=content)
        if error is not None:
            return None, None if error.is_no_content() else error
        code, content_type, content = pre_processed_response

        if code == 200:
            return OauthmodelTokenResponse.create_from_dict(content), None
        if code == 400:
            return None, OauthmodelErrorResponse.create_from_dict(content)
        if code == 401:
            return None, OauthmodelErrorResponse.create_from_dict(content)

        return None, self.handle_undocumented_response(code=code, content_type=content_type, content=content)

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        platform_id: str,
        device_id: Optional[str] = None,
        platform_token: Optional[str] = None,
    ) -> PlatformTokenRequestHandler:
        instance = cls()
        instance.namespace = namespace
        instance.platform_id = platform_id
        if device_id is not None:
            instance.device_id = device_id
        if platform_token is not None:
            instance.platform_token = platform_token
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PlatformTokenRequestHandler:
        instance = cls()
        if "device_id" in dict_ and dict_["device_id"] is not None:
            instance.device_id = str(dict_["device_id"])
        elif include_empty:
            instance.device_id = str()
        if "platform_token" in dict_ and dict_["platform_token"] is not None:
            instance.platform_token = str(dict_["platform_token"])
        elif include_empty:
            instance.platform_token = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "device_id": "device_id",
            "platform_token": "platform_token",
            "namespace": "namespace",
            "platformId": "platform_id",
        }

    # endregion static methods
