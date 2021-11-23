# justice-iam-service (4.7.0)

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


class PlatformTokenGrantV3(Operation):
    """OAuth2 access token generation specific to platform (PlatformTokenGrantV3)

    <p>Platform token grant specifically used for performing token grant using
    platform, e.g. Steam, Justice, etc. The endpoint automatically create an
    account if the account associated with the platform is not exists yet. This
    endpoint requires all requests to have Authorization header set with Basic
    access authentication constructed from client id and client secret. For
    publisher-game namespace schema : Specify only either platform_token or
    device_id. Device token grant should be requested along with device_id
    parameter against game namespace. Another 3rd party platform token grant
    should be requested along with platform_token parameter against publisher
    namespace.</p> <h2>Supported platforms:</h2> <ul> <li><strong>steam</strong>:
    The platform_token’s value is the authentication code returned by Steam.</li>
    <li><strong>steamopenid</strong>: Steam's user authentication method using
    OpenID 2.0. The platform_token's value is URL generated by Steam on web
    authentication</li> <li><strong>facebook</strong>: The platform_token’s value
    is the authorization code returned by Facebook OAuth</li>
    <li><strong>google</strong>: The platform_token’s value is the authorization
    code returned by Google OAuth</li> <li><strong>oculus</strong>: The
    platform_token’s value is a string composed of Oculus's user ID and the nonce
    separated by a colon (:).</li> <li><strong>twitch</strong>: The
    platform_token’s value is the authorization code returned by Twitch
    OAuth.</li> <li><strong>discord</strong>: The platform_token’s value is the
    authorization code returned by Discord OAuth</li>
    <li><strong>android</strong>: The device_id is the Android’s device ID</li>
    <li><strong>ios</strong>: The device_id is the iOS’s device ID.</li>
    <li><strong>device</strong>: Every device that does’nt run Android and iOS is
    categorized as a device. The device_id is the device’s ID.</li>
    <li><strong>justice</strong>: The platform_token’s value is the designated
    user’s access token.</li> <li><strong>epicgames</strong>: The platform_token’s
    value is an access-token obtained from Epicgames EOS Account Service.</li>
    <li><strong>stadia</strong>: The platform_token's value is a JWT Token, which
    can be obtained after calling the Stadia SDK's function.</li>
    <li><strong>ps4</strong>: The platform_token’s value is the authorization code
    returned by Sony OAuth.</li> <li><strong>ps5</strong>: The platform_token’s
    value is the authorization code returned by Sony OAuth.</li>
    <li><strong>nintendo</strong>: The platform_token’s value is the authorization
    code(id_token) returned by Nintendo OAuth.</li>
    <li><strong>awscognito</strong>: The platform_token’s value is the aws cognito
    access token (JWT).</li> </ul> <h2>Account Group</h2> <p>Several platforms are
    grouped under account groups. The accounts on these platforms have the same
    platform user id. Login using one of these platform will returns the same IAM
    user. </p> <p>Following is the current registered account grouping: </p> <ul>
    <li> (psn) ps4web </li> <li> (psn) ps4 </li> <li> (psn) ps5 </li> </ul>
    <h2>Access Token Content</h2> <p>Following is the access token’s content:</p>
    <ul> <li> <p><strong>namespace</strong>. It is the namespace the token was
    generated from.</p> </li> <li> <p><strong>display_name</strong>. The display
    name of the sub. It is empty if the token is generated from the client
    credential</p> </li> <li> <p><strong>roles</strong>. The sub’s roles. It is
    empty if the token is generated from the client credential</p> </li> <li>
    <p><strong>namespace_roles</strong>. The sub’s roles scoped to namespace.
    Improvement from roles, which make the role scoped to specific namespace
    instead of global to publisher namespace</p> </li> <li>
    <p><strong>permissions</strong>. The sub or aud’ permissions</p> </li> <li>
    <p><strong>bans</strong>. The sub’s list of bans. It is used by the IAM client
    for validating the token.</p> </li> <li> <p><strong>jflgs</strong>. It stands
    for Justice Flags. It is a special flag used for storing additional status
    information regarding the sub. It is implemented as a bit mask. Following
    explains what each bit represents:</p> <ul> <li><p>1: Email Address
    Verified</p></li> <li><p>2: Phone Number Verified</p></li> <li><p>4:
    Anonymous</p></li> <li><p>8: Suspicious Login</p></li> </ul> </li> <li>
    <p><strong>aud</strong>. The aud is the client ID.</p> </li> <li>
    <p><strong>iat</strong>. The time the token issues at. It is in Epoch time
    format</p> </li> <li> <p><strong>exp</strong>. The time the token expires. It
    is in Epoch time format</p> </li> <li> <p><strong>sub</strong>. The UserID.
    The sub is omitted if the token is generated from client credential</p> </li>
    <h2>Bans</h2> <p>The JWT contains user's active bans with its expiry date.
    List of ban types can be obtained from /bans.</p> <br>action code : 10704


    Properties:
        url: /iam/v3/oauth/platforms/{platformId}/token

        method: POST

        tags: ["OAuth2.0"]

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        security: bearer

        client_id: (client_id) OPTIONAL str in form_data

        device_id: (device_id) OPTIONAL str in form_data

        platform_token: (platform_token) OPTIONAL str in form_data

        platform_id: (platformId) REQUIRED str in path

    Responses:
        200: OK - OauthmodelTokenResponse (Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)
    """

    # region fields

    _url: str = "/iam/v3/oauth/platforms/{platformId}/token"
    _method: str = "POST"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    client_id: str                                                                                 # OPTIONAL in [form_data]
    device_id: str                                                                                 # OPTIONAL in [form_data]
    platform_token: str                                                                            # OPTIONAL in [form_data]
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
        return self.create_full_url(
            url=self.url,
            base_url=base_url,
            path_params=self.get_path_params(),
            query_params=self.get_query_params(),
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
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
        if hasattr(self, "client_id"):
            result["client_id"] = self.client_id
        if hasattr(self, "device_id"):
            result["device_id"] = self.device_id
        if hasattr(self, "platform_token"):
            result["platform_token"] = self.platform_token
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

    def with_client_id(self, value: str) -> PlatformTokenGrantV3:
        self.client_id = value
        return self

    def with_device_id(self, value: str) -> PlatformTokenGrantV3:
        self.device_id = value
        return self

    def with_platform_token(self, value: str) -> PlatformTokenGrantV3:
        self.platform_token = value
        return self

    def with_platform_id(self, value: str) -> PlatformTokenGrantV3:
        self.platform_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "client_id") and self.client_id:
            result["client_id"] = str(self.client_id)
        elif include_empty:
            result["client_id"] = str()
        if hasattr(self, "device_id") and self.device_id:
            result["device_id"] = str(self.device_id)
        elif include_empty:
            result["device_id"] = str()
        if hasattr(self, "platform_token") and self.platform_token:
            result["platform_token"] = str(self.platform_token)
        elif include_empty:
            result["platform_token"] = str()
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
        client_id: Optional[str] = None,
        device_id: Optional[str] = None,
        platform_token: Optional[str] = None,
    ) -> PlatformTokenGrantV3:
        instance = cls()
        instance.platform_id = platform_id
        if client_id is not None:
            instance.client_id = client_id
        if device_id is not None:
            instance.device_id = device_id
        if platform_token is not None:
            instance.platform_token = platform_token
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PlatformTokenGrantV3:
        instance = cls()
        if "client_id" in dict_ and dict_["client_id"] is not None:
            instance.client_id = str(dict_["client_id"])
        elif include_empty:
            instance.client_id = str()
        if "device_id" in dict_ and dict_["device_id"] is not None:
            instance.device_id = str(dict_["device_id"])
        elif include_empty:
            instance.device_id = str()
        if "platform_token" in dict_ and dict_["platform_token"] is not None:
            instance.platform_token = str(dict_["platform_token"])
        elif include_empty:
            instance.platform_token = str()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "client_id": "client_id",
            "device_id": "device_id",
            "platform_token": "platform_token",
            "platformId": "platform_id",
        }

    # endregion static methods
