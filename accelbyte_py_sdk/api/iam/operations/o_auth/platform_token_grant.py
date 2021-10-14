# Auto-generated at 2021-10-14T22:17:11.235037+08:00
# from: Justice Iam Service (4.1.0)

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

from ...models import OauthmodelErrorResponse
from ...models import OauthmodelTokenResponse


class PlatformTokenGrant(Operation):
    """OAuth2 access token generation specific to platform (PlatformTokenGrant)

    Platform token grant specifically used for performing token grant using
    platform, e.g. Steam, Justice, etc. The endpoint automatically create an
    account if the account associated with the platform is not exists yet. This
    endpoint requires all requests to have Authorization header set with Basic
    access authentication constructed from client id and client secret. For
    publisher-game namespace schema : Specify only either platform_token or
    device_id. Device token grant should be requested along with device_id
    parameter against game namespace. Another 3rd party platform token grant
    should be requested along with platform_token parameter against publisher
    namespace.

    ## Supported platforms:

      * steam : The platform_token’s value is the authentication code returned by Steam.
      * steamopenid : Steam's user authentication method using OpenID 2.0. The platform_token's value is URL generated by Steam on web authentication
      * facebook : The platform_token’s value is the authorization code returned by Facebook OAuth
      * google : The platform_token’s value is the authorization code returned by Google OAuth
      * oculus : The platform_token’s value is a string composed of Oculus's user ID and the nonce separated by a colon (:).
      * twitch : The platform_token’s value is the authorization code returned by Twitch OAuth.
      * discord : The platform_token’s value is the authorization code returned by Discord OAuth
      * android : The device_id is the Android’s device ID
      * ios : The device_id is the iOS’s device ID.
      * device : Every device that does’nt run Android and iOS is categorized as a device. The device_id is the device’s ID.
      * justice : The platform_token’s value is the designated user’s access token.

    ## Access Token Content

    Following is the access token’s content:

      * namespace. It is the namespace the token was generated from.

      * display_name. The display name of the sub. It is empty if the token is generated from the client credential

      * roles. The sub’s roles. It is empty if the token is generated from the client credential

      * namespace_roles. The sub’s roles scoped to namespace. Improvement from roles, which make the role scoped to specific namespace instead of global to publisher namespace

      * permissions. The sub or aud’ permissions

      * bans. The sub’s list of bans. It is used by the IAM client for validating the token.

      * jflgs. It stands for Justice Flags. It is a special flag used for storing additional status information regarding the sub. It is implemented as a bit mask. Following explains what each bit represents:

        * 1: Email Address Verified

        * 2: Phone Number Verified

        * 4: Anonymous

      * aud. The aud is the client ID.

      * iat. The time the token issues at. It is in Epoch time format

      * exp. The time the token expires. It is in Epoch time format

      * sub. The UserID. The sub is omitted if the token is generated from client credential

    ## Bans

    The JWT contains user's active bans with its expiry date. List of ban types
    can be obtained from /bans.

    ## Track Login History

    This endpoint will track login history to detect suspicious login activity,
    please provide "device_id" (alphanumeric) in request header parameter
    otherwise we will set to "unknown".

    Align with General Data Protection Regulation in Europe, user login history
    will be kept within 28 days by default"


    Properties:
        url: /iam/oauth/platforms/{platformId}/token

        method: POST

        tags: ["OAuth"]

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        security: bearer

        device_id: (Device-Id) OPTIONAL str in header

        platform_token: (platform_token) OPTIONAL str in form_data

        device_id: (device_id) OPTIONAL str in form_data

        namespace: (namespace) OPTIONAL str in form_data

        platform_id: (platformId) REQUIRED str in path

    Responses:
        200: OK - OauthmodelTokenResponse (Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)
    """

    # region fields

    _url: str = "/iam/oauth/platforms/{platformId}/token"
    _method: str = "POST"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    device_id: str                                                                                 # OPTIONAL in [header, form_data]
    platform_token: str                                                                            # OPTIONAL in [form_data]
    namespace: str                                                                                 # OPTIONAL in [form_data]
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
            "platform_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "header": self.get_header_params(),
            "form_data": self.get_form_data_params(),
            "path": self.get_path_params(),
        }

    def get_header_params(self) -> dict:
        result = {}
        if hasattr(self, "device_id"):
            result["Device-Id"] = self.device_id
        return result

    def get_form_data_params(self) -> dict:
        result = {}
        if hasattr(self, "platform_token"):
            result["platform_token"] = self.platform_token
        if hasattr(self, "device_id"):
            result["device_id"] = self.device_id
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "platform_id") or self.platform_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_device_id(self, value: str) -> PlatformTokenGrant:
        self.device_id = value
        return self

    def with_platform_token(self, value: str) -> PlatformTokenGrant:
        self.platform_token = value
        return self

    def with_namespace(self, value: str) -> PlatformTokenGrant:
        self.namespace = value
        return self

    def with_platform_id(self, value: str) -> PlatformTokenGrant:
        self.platform_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "device_id") and self.device_id:
            result["Device-Id"] = str(self.device_id)
        elif include_empty:
            result["Device-Id"] = str()
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
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, OauthmodelTokenResponse], Union[None, OauthmodelErrorResponse]]:
        """Parse the given response.

        200: OK - OauthmodelTokenResponse (Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)
        """
        if code == 200:
            return OauthmodelTokenResponse.create_from_dict(content), None
        if code == 400:
            return None, OauthmodelErrorResponse.create_from_dict(content)
        if code == 401:
            return None, OauthmodelErrorResponse.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        platform_id: str,
        device_id: Optional[str] = None,
        platform_token: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> PlatformTokenGrant:
        instance = cls()
        instance.platform_id = platform_id
        if device_id is not None:
            instance.device_id = device_id
        if platform_token is not None:
            instance.platform_token = platform_token
        if namespace is not None:
            instance.namespace = namespace
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PlatformTokenGrant:
        instance = cls()
        if "Device-Id" in dict_ and dict_["Device-Id"] is not None:
            instance.device_id = str(dict_["Device-Id"])
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
            "Device-Id": "device_id",
            "platform_token": "platform_token",
            "device_id": "device_id",
            "namespace": "namespace",
            "platformId": "platform_id",
        }

    # endregion static methods
