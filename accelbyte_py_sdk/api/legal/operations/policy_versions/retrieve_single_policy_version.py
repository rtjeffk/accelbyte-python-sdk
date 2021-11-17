# justice-legal-service (1.14.0)

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
from ...models import RetrievePolicyVersionResponse


class RetrieveSinglePolicyVersion(Operation):
    """Retrieve a Version from Country-Specific Policy (retrieveSinglePolicyVersion)

    Retrieve a version of a particular country specific policy. If version is not
    provided, the Legal Service will assume caller requesting all versions from
    country-specific policy.<br>Other detail info: <ul><li><i>Required
    permission</i>: resource="ADMIN:NAMESPACE:*:LEGAL", action=2 (READ)</li></ul>


    Properties:
        url: /agreement/admin/policies/{policyId}/versions

        method: GET

        tags: ["Policy Versions"]

        consumes: []

        produces: ["application/json"]

        security: bearer

        policy_id: (policyId) REQUIRED str in path

        version_id: (versionId) OPTIONAL str in query

    Responses:
        200: OK - List[RetrievePolicyVersionResponse] (successful operation)

        404: Not Found - ErrorEntity (40035: errors.net.accelbyte.platform.legal.policy_version_not_found)
    """

    # region fields

    _url: str = "/agreement/admin/policies/{policyId}/versions"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    policy_id: str                                                                                 # REQUIRED in [path]
    version_id: str                                                                                # OPTIONAL in [query]

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
            url = url.replace(f"{{{k}}}", str(v))
        result += url

        # query params
        result += "?" + "&".join([f"{k}={v}" for k, v in self.get_query_params().items()])

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "policy_id",
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
        if hasattr(self, "policy_id"):
            result["policyId"] = self.policy_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "version_id"):
            result["versionId"] = self.version_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "policy_id") or self.policy_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_policy_id(self, value: str) -> RetrieveSinglePolicyVersion:
        self.policy_id = value
        return self

    def with_version_id(self, value: str) -> RetrieveSinglePolicyVersion:
        self.version_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "policy_id") and self.policy_id:
            result["policyId"] = str(self.policy_id)
        elif include_empty:
            result["policyId"] = str()
        if hasattr(self, "version_id") and self.version_id:
            result["versionId"] = str(self.version_id)
        elif include_empty:
            result["versionId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, List[RetrievePolicyVersionResponse]], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - List[RetrievePolicyVersionResponse] (successful operation)

        404: Not Found - ErrorEntity (40035: errors.net.accelbyte.platform.legal.policy_version_not_found)
        """
        if code == 200:
            return [RetrievePolicyVersionResponse.create_from_dict(i) for i in content], None
        if code == 404:
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
        policy_id: str,
        version_id: Optional[str] = None,
    ) -> RetrieveSinglePolicyVersion:
        instance = cls()
        instance.policy_id = policy_id
        if version_id is not None:
            instance.version_id = version_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> RetrieveSinglePolicyVersion:
        instance = cls()
        if "policyId" in dict_ and dict_["policyId"] is not None:
            instance.policy_id = str(dict_["policyId"])
        elif include_empty:
            instance.policy_id = str()
        if "versionId" in dict_ and dict_["versionId"] is not None:
            instance.version_id = str(dict_["versionId"])
        elif include_empty:
            instance.version_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "policyId": "policy_id",
            "versionId": "version_id",
        }

    # endregion static methods