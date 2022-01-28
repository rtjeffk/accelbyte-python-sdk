# justice-iam-service (5.1.1)

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

from ...models import OauthcommonJWKSet


class GetJWKSV3(Operation):
    """JSON Web Key Set for verifying JWT (GetJWKSV3)

    <p>This endpoint serves public keys for verifying JWT access tokens generated
    by this service.</p> <p>When a client application wants to verify a JWT token,
    it needs to get the 'kid' value found in the JWT token header and use it to
    look up the corresponding public key from a set returned by this endpoint. The
    client application can then use that public key to verify the JWT.</p> <p>A
    client application might cache the keys so it doesn't need to do request every
    time it needs to verify a JWT token. If a client application caches the keys
    and a key with the same 'kid' cannot be found in the cache, it should then try
    to refresh the keys by making a request to this endpoint again.</p> <p>Please
    refer to the RFC for more information about JWK (JSON Web Key):
    https://tools.ietf.org/html/rfc7517</p> <br>action code : 10709


    Properties:
        url: /iam/v3/oauth/jwks

        method: GET

        tags: ["OAuth2.0"]

        consumes: [""]

        produces: ["application/json"]

        security_type: bearer

    Responses:
        200: OK - OauthcommonJWKSet (JWKS returned)
    """

    # region fields

    _url: str = "/iam/v3/oauth/jwks"
    _method: str = "GET"
    _consumes: List[str] = [""]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

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
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
        }

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        return True

    # endregion is/has methods

    # region with_x methods

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, OauthcommonJWKSet], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - OauthcommonJWKSet (JWKS returned)
        """
        if code == 200:
            return OauthcommonJWKSet.create_from_dict(content), None
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
    ) -> GetJWKSV3:
        instance = cls()
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetJWKSV3:
        instance = cls()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
        }

    # endregion static methods
