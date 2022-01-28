# justice-legal-service (1.16.0)

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

from ...models import RetrieveLocalizedPolicyVersionResponse


class RetrieveLocalizedPolicyVersions(Operation):
    """Retrieve Versions from Country-Specific Policy (retrieveLocalizedPolicyVersions)

    Retrieve versions of a particular country-specific policy.<br>Other detail
    info: <ul><li><i>Required permission</i>: resource="ADMIN:NAMESPACE:*:LEGAL",
    action=2 (READ)</li></ul>


    Properties:
        url: /agreement/admin/localized-policy-versions/versions/{policyVersionId}

        method: GET

        tags: ["Localized Policy Versions"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        policy_version_id: (policyVersionId) REQUIRED str in path

    Responses:
        200: OK - List[RetrieveLocalizedPolicyVersionResponse] (successful operation)
    """

    # region fields

    _url: str = "/agreement/admin/localized-policy-versions/versions/{policyVersionId}"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    policy_version_id: str                                                                         # REQUIRED in [path]

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
            "policy_version_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "policy_version_id"):
            result["policyVersionId"] = self.policy_version_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "policy_version_id") or self.policy_version_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_policy_version_id(self, value: str) -> RetrieveLocalizedPolicyVersions:
        self.policy_version_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "policy_version_id") and self.policy_version_id:
            result["policyVersionId"] = str(self.policy_version_id)
        elif include_empty:
            result["policyVersionId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, List[RetrieveLocalizedPolicyVersionResponse]], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - List[RetrieveLocalizedPolicyVersionResponse] (successful operation)
        """
        if code == 200:
            return [RetrieveLocalizedPolicyVersionResponse.create_from_dict(i) for i in content], None
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
        policy_version_id: str,
    ) -> RetrieveLocalizedPolicyVersions:
        instance = cls()
        instance.policy_version_id = policy_version_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> RetrieveLocalizedPolicyVersions:
        instance = cls()
        if "policyVersionId" in dict_ and dict_["policyVersionId"] is not None:
            instance.policy_version_id = str(dict_["policyVersionId"])
        elif include_empty:
            instance.policy_version_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "policyVersionId": "policy_version_id",
        }

    # endregion static methods