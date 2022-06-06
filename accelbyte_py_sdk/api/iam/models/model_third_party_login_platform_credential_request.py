# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
# 
# Code generated. DO NOT EDIT!

# template file: justice_py_sdk_codegen/__main__.py

# justice-iam-service (5.9.0)

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

from ....core import Model


class ModelThirdPartyLoginPlatformCredentialRequest(Model):
    """Model third party login platform credential request (model.ThirdPartyLoginPlatformCredentialRequest)

    Properties:
        acsurl: (ACSURL) REQUIRED str

        app_id: (AppId) REQUIRED str

        aws_cognito_region: (AWSCognitoRegion) REQUIRED str

        aws_cognito_user_pool: (AWSCognitoUserPool) REQUIRED str

        client_id: (ClientId) REQUIRED str

        environment: (Environment) REQUIRED str

        federation_metadata_url: (FederationMetadataURL) REQUIRED str

        generic_oauth_flow: (GenericOauthFlow) REQUIRED bool

        is_active: (IsActive) REQUIRED bool

        issuer: (Issuer) REQUIRED str

        jwks_endpoint: (JWKSEndpoint) REQUIRED str

        key_id: (KeyID) REQUIRED str

        organization_id: (OrganizationId) REQUIRED str

        platform_name: (PlatformName) REQUIRED str

        redirect_uri: (RedirectUri) REQUIRED str

        secret: (Secret) REQUIRED str

        team_id: (TeamID) REQUIRED str

        token_authentication_type: (TokenAuthenticationType) REQUIRED str

        token_claims_mapping: (TokenClaimsMapping) REQUIRED Dict[str, str]
    """

    # region fields

    acsurl: str                                                                                    # REQUIRED
    app_id: str                                                                                    # REQUIRED
    aws_cognito_region: str                                                                        # REQUIRED
    aws_cognito_user_pool: str                                                                     # REQUIRED
    client_id: str                                                                                 # REQUIRED
    environment: str                                                                               # REQUIRED
    federation_metadata_url: str                                                                   # REQUIRED
    generic_oauth_flow: bool                                                                       # REQUIRED
    is_active: bool                                                                                # REQUIRED
    issuer: str                                                                                    # REQUIRED
    jwks_endpoint: str                                                                             # REQUIRED
    key_id: str                                                                                    # REQUIRED
    organization_id: str                                                                           # REQUIRED
    platform_name: str                                                                             # REQUIRED
    redirect_uri: str                                                                              # REQUIRED
    secret: str                                                                                    # REQUIRED
    team_id: str                                                                                   # REQUIRED
    token_authentication_type: str                                                                 # REQUIRED
    token_claims_mapping: Dict[str, str]                                                           # REQUIRED

    # endregion fields

    # region with_x methods

    def with_acsurl(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.acsurl = value
        return self

    def with_app_id(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.app_id = value
        return self

    def with_aws_cognito_region(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.aws_cognito_region = value
        return self

    def with_aws_cognito_user_pool(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.aws_cognito_user_pool = value
        return self

    def with_client_id(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.client_id = value
        return self

    def with_environment(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.environment = value
        return self

    def with_federation_metadata_url(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.federation_metadata_url = value
        return self

    def with_generic_oauth_flow(self, value: bool) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.generic_oauth_flow = value
        return self

    def with_is_active(self, value: bool) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.is_active = value
        return self

    def with_issuer(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.issuer = value
        return self

    def with_jwks_endpoint(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.jwks_endpoint = value
        return self

    def with_key_id(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.key_id = value
        return self

    def with_organization_id(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.organization_id = value
        return self

    def with_platform_name(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.platform_name = value
        return self

    def with_redirect_uri(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.redirect_uri = value
        return self

    def with_secret(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.secret = value
        return self

    def with_team_id(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.team_id = value
        return self

    def with_token_authentication_type(self, value: str) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.token_authentication_type = value
        return self

    def with_token_claims_mapping(self, value: Dict[str, str]) -> ModelThirdPartyLoginPlatformCredentialRequest:
        self.token_claims_mapping = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "acsurl"):
            result["ACSURL"] = str(self.acsurl)
        elif include_empty:
            result["ACSURL"] = ""
        if hasattr(self, "app_id"):
            result["AppId"] = str(self.app_id)
        elif include_empty:
            result["AppId"] = ""
        if hasattr(self, "aws_cognito_region"):
            result["AWSCognitoRegion"] = str(self.aws_cognito_region)
        elif include_empty:
            result["AWSCognitoRegion"] = ""
        if hasattr(self, "aws_cognito_user_pool"):
            result["AWSCognitoUserPool"] = str(self.aws_cognito_user_pool)
        elif include_empty:
            result["AWSCognitoUserPool"] = ""
        if hasattr(self, "client_id"):
            result["ClientId"] = str(self.client_id)
        elif include_empty:
            result["ClientId"] = ""
        if hasattr(self, "environment"):
            result["Environment"] = str(self.environment)
        elif include_empty:
            result["Environment"] = ""
        if hasattr(self, "federation_metadata_url"):
            result["FederationMetadataURL"] = str(self.federation_metadata_url)
        elif include_empty:
            result["FederationMetadataURL"] = ""
        if hasattr(self, "generic_oauth_flow"):
            result["GenericOauthFlow"] = bool(self.generic_oauth_flow)
        elif include_empty:
            result["GenericOauthFlow"] = False
        if hasattr(self, "is_active"):
            result["IsActive"] = bool(self.is_active)
        elif include_empty:
            result["IsActive"] = False
        if hasattr(self, "issuer"):
            result["Issuer"] = str(self.issuer)
        elif include_empty:
            result["Issuer"] = ""
        if hasattr(self, "jwks_endpoint"):
            result["JWKSEndpoint"] = str(self.jwks_endpoint)
        elif include_empty:
            result["JWKSEndpoint"] = ""
        if hasattr(self, "key_id"):
            result["KeyID"] = str(self.key_id)
        elif include_empty:
            result["KeyID"] = ""
        if hasattr(self, "organization_id"):
            result["OrganizationId"] = str(self.organization_id)
        elif include_empty:
            result["OrganizationId"] = ""
        if hasattr(self, "platform_name"):
            result["PlatformName"] = str(self.platform_name)
        elif include_empty:
            result["PlatformName"] = ""
        if hasattr(self, "redirect_uri"):
            result["RedirectUri"] = str(self.redirect_uri)
        elif include_empty:
            result["RedirectUri"] = ""
        if hasattr(self, "secret"):
            result["Secret"] = str(self.secret)
        elif include_empty:
            result["Secret"] = ""
        if hasattr(self, "team_id"):
            result["TeamID"] = str(self.team_id)
        elif include_empty:
            result["TeamID"] = ""
        if hasattr(self, "token_authentication_type"):
            result["TokenAuthenticationType"] = str(self.token_authentication_type)
        elif include_empty:
            result["TokenAuthenticationType"] = ""
        if hasattr(self, "token_claims_mapping"):
            result["TokenClaimsMapping"] = {str(k0): str(v0) for k0, v0 in self.token_claims_mapping.items()}
        elif include_empty:
            result["TokenClaimsMapping"] = {}
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        acsurl: str,
        app_id: str,
        aws_cognito_region: str,
        aws_cognito_user_pool: str,
        client_id: str,
        environment: str,
        federation_metadata_url: str,
        generic_oauth_flow: bool,
        is_active: bool,
        issuer: str,
        jwks_endpoint: str,
        key_id: str,
        organization_id: str,
        platform_name: str,
        redirect_uri: str,
        secret: str,
        team_id: str,
        token_authentication_type: str,
        token_claims_mapping: Dict[str, str],
    ) -> ModelThirdPartyLoginPlatformCredentialRequest:
        instance = cls()
        instance.acsurl = acsurl
        instance.app_id = app_id
        instance.aws_cognito_region = aws_cognito_region
        instance.aws_cognito_user_pool = aws_cognito_user_pool
        instance.client_id = client_id
        instance.environment = environment
        instance.federation_metadata_url = federation_metadata_url
        instance.generic_oauth_flow = generic_oauth_flow
        instance.is_active = is_active
        instance.issuer = issuer
        instance.jwks_endpoint = jwks_endpoint
        instance.key_id = key_id
        instance.organization_id = organization_id
        instance.platform_name = platform_name
        instance.redirect_uri = redirect_uri
        instance.secret = secret
        instance.team_id = team_id
        instance.token_authentication_type = token_authentication_type
        instance.token_claims_mapping = token_claims_mapping
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelThirdPartyLoginPlatformCredentialRequest:
        instance = cls()
        if not dict_:
            return instance
        if "ACSURL" in dict_ and dict_["ACSURL"] is not None:
            instance.acsurl = str(dict_["ACSURL"])
        elif include_empty:
            instance.acsurl = ""
        if "AppId" in dict_ and dict_["AppId"] is not None:
            instance.app_id = str(dict_["AppId"])
        elif include_empty:
            instance.app_id = ""
        if "AWSCognitoRegion" in dict_ and dict_["AWSCognitoRegion"] is not None:
            instance.aws_cognito_region = str(dict_["AWSCognitoRegion"])
        elif include_empty:
            instance.aws_cognito_region = ""
        if "AWSCognitoUserPool" in dict_ and dict_["AWSCognitoUserPool"] is not None:
            instance.aws_cognito_user_pool = str(dict_["AWSCognitoUserPool"])
        elif include_empty:
            instance.aws_cognito_user_pool = ""
        if "ClientId" in dict_ and dict_["ClientId"] is not None:
            instance.client_id = str(dict_["ClientId"])
        elif include_empty:
            instance.client_id = ""
        if "Environment" in dict_ and dict_["Environment"] is not None:
            instance.environment = str(dict_["Environment"])
        elif include_empty:
            instance.environment = ""
        if "FederationMetadataURL" in dict_ and dict_["FederationMetadataURL"] is not None:
            instance.federation_metadata_url = str(dict_["FederationMetadataURL"])
        elif include_empty:
            instance.federation_metadata_url = ""
        if "GenericOauthFlow" in dict_ and dict_["GenericOauthFlow"] is not None:
            instance.generic_oauth_flow = bool(dict_["GenericOauthFlow"])
        elif include_empty:
            instance.generic_oauth_flow = False
        if "IsActive" in dict_ and dict_["IsActive"] is not None:
            instance.is_active = bool(dict_["IsActive"])
        elif include_empty:
            instance.is_active = False
        if "Issuer" in dict_ and dict_["Issuer"] is not None:
            instance.issuer = str(dict_["Issuer"])
        elif include_empty:
            instance.issuer = ""
        if "JWKSEndpoint" in dict_ and dict_["JWKSEndpoint"] is not None:
            instance.jwks_endpoint = str(dict_["JWKSEndpoint"])
        elif include_empty:
            instance.jwks_endpoint = ""
        if "KeyID" in dict_ and dict_["KeyID"] is not None:
            instance.key_id = str(dict_["KeyID"])
        elif include_empty:
            instance.key_id = ""
        if "OrganizationId" in dict_ and dict_["OrganizationId"] is not None:
            instance.organization_id = str(dict_["OrganizationId"])
        elif include_empty:
            instance.organization_id = ""
        if "PlatformName" in dict_ and dict_["PlatformName"] is not None:
            instance.platform_name = str(dict_["PlatformName"])
        elif include_empty:
            instance.platform_name = ""
        if "RedirectUri" in dict_ and dict_["RedirectUri"] is not None:
            instance.redirect_uri = str(dict_["RedirectUri"])
        elif include_empty:
            instance.redirect_uri = ""
        if "Secret" in dict_ and dict_["Secret"] is not None:
            instance.secret = str(dict_["Secret"])
        elif include_empty:
            instance.secret = ""
        if "TeamID" in dict_ and dict_["TeamID"] is not None:
            instance.team_id = str(dict_["TeamID"])
        elif include_empty:
            instance.team_id = ""
        if "TokenAuthenticationType" in dict_ and dict_["TokenAuthenticationType"] is not None:
            instance.token_authentication_type = str(dict_["TokenAuthenticationType"])
        elif include_empty:
            instance.token_authentication_type = ""
        if "TokenClaimsMapping" in dict_ and dict_["TokenClaimsMapping"] is not None:
            instance.token_claims_mapping = {str(k0): str(v0) for k0, v0 in dict_["TokenClaimsMapping"].items()}
        elif include_empty:
            instance.token_claims_mapping = {}
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, ModelThirdPartyLoginPlatformCredentialRequest]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[ModelThirdPartyLoginPlatformCredentialRequest]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[ModelThirdPartyLoginPlatformCredentialRequest, List[ModelThirdPartyLoginPlatformCredentialRequest], Dict[Any, ModelThirdPartyLoginPlatformCredentialRequest]]:
        if many:
            if isinstance(any_, dict):
                return cls.create_many_from_dict(any_, include_empty=include_empty)
            elif isinstance(any_, list):
                return cls.create_many_from_list(any_, include_empty=include_empty)
            else:
                raise ValueError()
        else:
            return cls.create_from_dict(any_, include_empty=include_empty)

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "ACSURL": "acsurl",
            "AppId": "app_id",
            "AWSCognitoRegion": "aws_cognito_region",
            "AWSCognitoUserPool": "aws_cognito_user_pool",
            "ClientId": "client_id",
            "Environment": "environment",
            "FederationMetadataURL": "federation_metadata_url",
            "GenericOauthFlow": "generic_oauth_flow",
            "IsActive": "is_active",
            "Issuer": "issuer",
            "JWKSEndpoint": "jwks_endpoint",
            "KeyID": "key_id",
            "OrganizationId": "organization_id",
            "PlatformName": "platform_name",
            "RedirectUri": "redirect_uri",
            "Secret": "secret",
            "TeamID": "team_id",
            "TokenAuthenticationType": "token_authentication_type",
            "TokenClaimsMapping": "token_claims_mapping",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "ACSURL": True,
            "AppId": True,
            "AWSCognitoRegion": True,
            "AWSCognitoUserPool": True,
            "ClientId": True,
            "Environment": True,
            "FederationMetadataURL": True,
            "GenericOauthFlow": True,
            "IsActive": True,
            "Issuer": True,
            "JWKSEndpoint": True,
            "KeyID": True,
            "OrganizationId": True,
            "PlatformName": True,
            "RedirectUri": True,
            "Secret": True,
            "TeamID": True,
            "TokenAuthenticationType": True,
            "TokenClaimsMapping": True,
        }

    # endregion static methods
