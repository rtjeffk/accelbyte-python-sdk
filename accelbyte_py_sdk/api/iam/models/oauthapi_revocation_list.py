# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-iam-service (5.5.1)

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
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import Model

from ..models.bloom_filter_json import BloomFilterJSON
from ..models.oauthcommon_user_revocation_list_record import OauthcommonUserRevocationListRecord


class OauthapiRevocationList(Model):
    """Oauthapi revocation list (oauthapi.RevocationList)

    Properties:
        revoked_tokens: (revoked_tokens) REQUIRED BloomFilterJSON

        revoked_users: (revoked_users) REQUIRED List[OauthcommonUserRevocationListRecord]
    """

    # region fields

    revoked_tokens: BloomFilterJSON                                                                # REQUIRED
    revoked_users: List[OauthcommonUserRevocationListRecord]                                       # REQUIRED

    # endregion fields

    # region with_x methods

    def with_revoked_tokens(self, value: BloomFilterJSON) -> OauthapiRevocationList:
        self.revoked_tokens = value
        return self

    def with_revoked_users(self, value: List[OauthcommonUserRevocationListRecord]) -> OauthapiRevocationList:
        self.revoked_users = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "revoked_tokens") or self.revoked_tokens is None:
            return False
        if not hasattr(self, "revoked_users") or self.revoked_users is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "revoked_tokens"):
            result["revoked_tokens"] = self.revoked_tokens.to_dict(include_empty=include_empty)
        elif include_empty:
            result["revoked_tokens"] = BloomFilterJSON()
        if hasattr(self, "revoked_users"):
            result["revoked_users"] = [i0.to_dict(include_empty=include_empty) for i0 in self.revoked_users]
        elif include_empty:
            result["revoked_users"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        revoked_tokens: BloomFilterJSON,
        revoked_users: List[OauthcommonUserRevocationListRecord],
    ) -> OauthapiRevocationList:
        instance = cls()
        instance.revoked_tokens = revoked_tokens
        instance.revoked_users = revoked_users
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> OauthapiRevocationList:
        instance = cls()
        if not dict_:
            return instance
        if "revoked_tokens" in dict_ and dict_["revoked_tokens"] is not None:
            instance.revoked_tokens = BloomFilterJSON.create_from_dict(dict_["revoked_tokens"], include_empty=include_empty)
        elif include_empty:
            instance.revoked_tokens = BloomFilterJSON()
        if "revoked_users" in dict_ and dict_["revoked_users"] is not None:
            instance.revoked_users = [OauthcommonUserRevocationListRecord.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["revoked_users"]]
        elif include_empty:
            instance.revoked_users = []
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, OauthapiRevocationList]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[OauthapiRevocationList]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[OauthapiRevocationList, List[OauthapiRevocationList]]:
        if many:
            if isinstance(any_, dict):
                cls.create_many_from_dict(any_, include_empty=include_empty)
            elif isinstance(any_, list):
                cls.create_many_from_list(any_, include_empty=include_empty)
        else:
            return cls.create_from_dict(any_, include_empty=include_empty)

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "revoked_tokens": "revoked_tokens",
            "revoked_users": "revoked_users",
        }

    # endregion static methods
