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

from ...models import ModelSSOPlatformCredentialRequest
from ...models import ModelSSOPlatformCredentialResponse
from ...models import RestErrorResponse


class AddSSOLoginPlatformCredential(Operation):
    """Add SSO Platform Credential (AddSSOLoginPlatformCredential)

    This is the API to Add SSO Platform Credential. It needs
    ADMIN:NAMESPACE:{namespace}:PLATFORM:{platformId}:SSO [CREATE]
    resource.<h2>Supported platforms:</h2><ul>
    <li><strong>discourse</strong></li>the ssoUrl of the discourse is the
    discourse forum url. example: https://forum.example.com <li><strong>azure with
    SAML</strong></li><b>appId</b> is an application identifier in IdP, in azure
    it's called EntityID <b>acsUrl</b> is an endpoint on the service provider
    where the identity provider will redirect to with its authentication response.
    example: /iam/v3/sso/saml/azuresaml/authenticate <b>federationMetadataUrl</b>
    is an endpoint on the Identity Provider(IdP) to get IdP federation metadata
    for service provider to build trust relationship </ul>


    Properties:
        url: /iam/v3/admin/namespaces/{namespace}/platforms/{platformId}/sso

        method: POST

        tags: ["SSO Credential"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        body: (body) REQUIRED ModelSSOPlatformCredentialRequest in body

        namespace: (namespace) REQUIRED str in path

        platform_id: (platformId) REQUIRED str in path

    Responses:
        201: Created - ModelSSOPlatformCredentialResponse (SSO Credential Created)

        400: Bad Request - RestErrorResponse (Bad Request)

        401: Unauthorized - (Unauthorized)

        403: Forbidden - (Forbidden)

        500: Internal Server Error - RestErrorResponse (Internal Server Error)
    """

    # region fields

    _url: str = "/iam/v3/admin/namespaces/{namespace}/platforms/{platformId}/sso"
    _method: str = "POST"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelSSOPlatformCredentialRequest                                                        # REQUIRED in [body]
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
            "body",
            "namespace",
            "platform_id",
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
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "platform_id") or self.platform_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelSSOPlatformCredentialRequest) -> AddSSOLoginPlatformCredential:
        self.body = value
        return self

    def with_namespace(self, value: str) -> AddSSOLoginPlatformCredential:
        self.namespace = value
        return self

    def with_platform_id(self, value: str) -> AddSSOLoginPlatformCredential:
        self.platform_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelSSOPlatformCredentialRequest()
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
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelSSOPlatformCredentialResponse], Union[None, HttpResponse, RestErrorResponse]]:
        """Parse the given response.

        201: Created - ModelSSOPlatformCredentialResponse (SSO Credential Created)

        400: Bad Request - RestErrorResponse (Bad Request)

        401: Unauthorized - (Unauthorized)

        403: Forbidden - (Forbidden)

        500: Internal Server Error - RestErrorResponse (Internal Server Error)
        """
        if code == 201:
            return ModelSSOPlatformCredentialResponse.create_from_dict(content), None
        if code == 400:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
        if code == 500:
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
        body: ModelSSOPlatformCredentialRequest,
        namespace: str,
        platform_id: str,
    ) -> AddSSOLoginPlatformCredential:
        instance = cls()
        instance.body = body
        instance.namespace = namespace
        instance.platform_id = platform_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AddSSOLoginPlatformCredential:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelSSOPlatformCredentialRequest.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelSSOPlatformCredentialRequest()
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
            "body": "body",
            "namespace": "namespace",
            "platformId": "platform_id",
        }

    # endregion static methods