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


class CreateLocalizedPolicyVersionResponse(Model):
    """Create localized policy version response (CreateLocalizedPolicyVersionResponse)

    Properties:
        id_: (id) REQUIRED str

        created_at: (createdAt) OPTIONAL str

        description: (description) OPTIONAL str

        locale_code: (localeCode) OPTIONAL str

        updated_at: (updatedAt) OPTIONAL str
    """

    # region fields

    id_: str                                                                                       # REQUIRED
    created_at: str                                                                                # OPTIONAL
    description: str                                                                               # OPTIONAL
    locale_code: str                                                                               # OPTIONAL
    updated_at: str                                                                                # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_id(self, value: str) -> CreateLocalizedPolicyVersionResponse:
        self.id_ = value
        return self

    def with_created_at(self, value: str) -> CreateLocalizedPolicyVersionResponse:
        self.created_at = value
        return self

    def with_description(self, value: str) -> CreateLocalizedPolicyVersionResponse:
        self.description = value
        return self

    def with_locale_code(self, value: str) -> CreateLocalizedPolicyVersionResponse:
        self.locale_code = value
        return self

    def with_updated_at(self, value: str) -> CreateLocalizedPolicyVersionResponse:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "id_"):
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "created_at"):
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "description"):
            result["description"] = str(self.description)
        elif include_empty:
            result["description"] = str()
        if hasattr(self, "locale_code"):
            result["localeCode"] = str(self.locale_code)
        elif include_empty:
            result["localeCode"] = str()
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
        id_: str,
        created_at: Optional[str] = None,
        description: Optional[str] = None,
        locale_code: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> CreateLocalizedPolicyVersionResponse:
        instance = cls()
        instance.id_ = id_
        if created_at is not None:
            instance.created_at = created_at
        if description is not None:
            instance.description = description
        if locale_code is not None:
            instance.locale_code = locale_code
        if updated_at is not None:
            instance.updated_at = updated_at
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> CreateLocalizedPolicyVersionResponse:
        instance = cls()
        if not dict_:
            return instance
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "description" in dict_ and dict_["description"] is not None:
            instance.description = str(dict_["description"])
        elif include_empty:
            instance.description = str()
        if "localeCode" in dict_ and dict_["localeCode"] is not None:
            instance.locale_code = str(dict_["localeCode"])
        elif include_empty:
            instance.locale_code = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "id": "id_",
            "createdAt": "created_at",
            "description": "description",
            "localeCode": "locale_code",
            "updatedAt": "updated_at",
        }

    # endregion static methods