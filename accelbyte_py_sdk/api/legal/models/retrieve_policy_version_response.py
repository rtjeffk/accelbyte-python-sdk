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

from ....core import Model

from ..models.localized_policy_version_object import LocalizedPolicyVersionObject


class RetrievePolicyVersionResponse(Model):
    """Retrieve policy version response (RetrievePolicyVersionResponse)

    Properties:
        display_version: (displayVersion) REQUIRED str

        id_: (id) REQUIRED str

        is_committed: (isCommitted) REQUIRED bool

        is_in_effect: (isInEffect) REQUIRED bool

        policy_id: (policyId) REQUIRED str

        base_policy_id: (basePolicyId) OPTIONAL str

        created_at: (createdAt) OPTIONAL str

        description: (description) OPTIONAL str

        localized_policy_versions: (localizedPolicyVersions) OPTIONAL List[LocalizedPolicyVersionObject]

        published_date: (publishedDate) OPTIONAL str

        status: (status) OPTIONAL str

        updated_at: (updatedAt) OPTIONAL str
    """

    # region fields

    display_version: str                                                                           # REQUIRED
    id_: str                                                                                       # REQUIRED
    is_committed: bool                                                                             # REQUIRED
    is_in_effect: bool                                                                             # REQUIRED
    policy_id: str                                                                                 # REQUIRED
    base_policy_id: str                                                                            # OPTIONAL
    created_at: str                                                                                # OPTIONAL
    description: str                                                                               # OPTIONAL
    localized_policy_versions: List[LocalizedPolicyVersionObject]                                  # OPTIONAL
    published_date: str                                                                            # OPTIONAL
    status: str                                                                                    # OPTIONAL
    updated_at: str                                                                                # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_display_version(self, value: str) -> RetrievePolicyVersionResponse:
        self.display_version = value
        return self

    def with_id(self, value: str) -> RetrievePolicyVersionResponse:
        self.id_ = value
        return self

    def with_is_committed(self, value: bool) -> RetrievePolicyVersionResponse:
        self.is_committed = value
        return self

    def with_is_in_effect(self, value: bool) -> RetrievePolicyVersionResponse:
        self.is_in_effect = value
        return self

    def with_policy_id(self, value: str) -> RetrievePolicyVersionResponse:
        self.policy_id = value
        return self

    def with_base_policy_id(self, value: str) -> RetrievePolicyVersionResponse:
        self.base_policy_id = value
        return self

    def with_created_at(self, value: str) -> RetrievePolicyVersionResponse:
        self.created_at = value
        return self

    def with_description(self, value: str) -> RetrievePolicyVersionResponse:
        self.description = value
        return self

    def with_localized_policy_versions(self, value: List[LocalizedPolicyVersionObject]) -> RetrievePolicyVersionResponse:
        self.localized_policy_versions = value
        return self

    def with_published_date(self, value: str) -> RetrievePolicyVersionResponse:
        self.published_date = value
        return self

    def with_status(self, value: str) -> RetrievePolicyVersionResponse:
        self.status = value
        return self

    def with_updated_at(self, value: str) -> RetrievePolicyVersionResponse:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "display_version"):
            result["displayVersion"] = str(self.display_version)
        elif include_empty:
            result["displayVersion"] = str()
        if hasattr(self, "id_"):
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "is_committed"):
            result["isCommitted"] = bool(self.is_committed)
        elif include_empty:
            result["isCommitted"] = bool()
        if hasattr(self, "is_in_effect"):
            result["isInEffect"] = bool(self.is_in_effect)
        elif include_empty:
            result["isInEffect"] = bool()
        if hasattr(self, "policy_id"):
            result["policyId"] = str(self.policy_id)
        elif include_empty:
            result["policyId"] = str()
        if hasattr(self, "base_policy_id"):
            result["basePolicyId"] = str(self.base_policy_id)
        elif include_empty:
            result["basePolicyId"] = str()
        if hasattr(self, "created_at"):
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "description"):
            result["description"] = str(self.description)
        elif include_empty:
            result["description"] = str()
        if hasattr(self, "localized_policy_versions"):
            result["localizedPolicyVersions"] = [i0.to_dict(include_empty=include_empty) for i0 in self.localized_policy_versions]
        elif include_empty:
            result["localizedPolicyVersions"] = []
        if hasattr(self, "published_date"):
            result["publishedDate"] = str(self.published_date)
        elif include_empty:
            result["publishedDate"] = str()
        if hasattr(self, "status"):
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "updated_at"):
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        display_version: str,
        id_: str,
        is_committed: bool,
        is_in_effect: bool,
        policy_id: str,
        base_policy_id: Optional[str] = None,
        created_at: Optional[str] = None,
        description: Optional[str] = None,
        localized_policy_versions: Optional[List[LocalizedPolicyVersionObject]] = None,
        published_date: Optional[str] = None,
        status: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> RetrievePolicyVersionResponse:
        instance = cls()
        instance.display_version = display_version
        instance.id_ = id_
        instance.is_committed = is_committed
        instance.is_in_effect = is_in_effect
        instance.policy_id = policy_id
        if base_policy_id is not None:
            instance.base_policy_id = base_policy_id
        if created_at is not None:
            instance.created_at = created_at
        if description is not None:
            instance.description = description
        if localized_policy_versions is not None:
            instance.localized_policy_versions = localized_policy_versions
        if published_date is not None:
            instance.published_date = published_date
        if status is not None:
            instance.status = status
        if updated_at is not None:
            instance.updated_at = updated_at
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> RetrievePolicyVersionResponse:
        instance = cls()
        if not dict_:
            return instance
        if "displayVersion" in dict_ and dict_["displayVersion"] is not None:
            instance.display_version = str(dict_["displayVersion"])
        elif include_empty:
            instance.display_version = str()
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "isCommitted" in dict_ and dict_["isCommitted"] is not None:
            instance.is_committed = bool(dict_["isCommitted"])
        elif include_empty:
            instance.is_committed = bool()
        if "isInEffect" in dict_ and dict_["isInEffect"] is not None:
            instance.is_in_effect = bool(dict_["isInEffect"])
        elif include_empty:
            instance.is_in_effect = bool()
        if "policyId" in dict_ and dict_["policyId"] is not None:
            instance.policy_id = str(dict_["policyId"])
        elif include_empty:
            instance.policy_id = str()
        if "basePolicyId" in dict_ and dict_["basePolicyId"] is not None:
            instance.base_policy_id = str(dict_["basePolicyId"])
        elif include_empty:
            instance.base_policy_id = str()
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "description" in dict_ and dict_["description"] is not None:
            instance.description = str(dict_["description"])
        elif include_empty:
            instance.description = str()
        if "localizedPolicyVersions" in dict_ and dict_["localizedPolicyVersions"] is not None:
            instance.localized_policy_versions = [LocalizedPolicyVersionObject.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["localizedPolicyVersions"]]
        elif include_empty:
            instance.localized_policy_versions = []
        if "publishedDate" in dict_ and dict_["publishedDate"] is not None:
            instance.published_date = str(dict_["publishedDate"])
        elif include_empty:
            instance.published_date = str()
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "displayVersion": "display_version",
            "id": "id_",
            "isCommitted": "is_committed",
            "isInEffect": "is_in_effect",
            "policyId": "policy_id",
            "basePolicyId": "base_policy_id",
            "createdAt": "created_at",
            "description": "description",
            "localizedPolicyVersions": "localized_policy_versions",
            "publishedDate": "published_date",
            "status": "status",
            "updatedAt": "updated_at",
        }

    # endregion static methods