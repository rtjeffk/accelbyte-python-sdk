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

from ..models.accountcommon_user_linked_platform import AccountcommonUserLinkedPlatform


class AccountcommonUserSearchByPlatformIDResult(Model):
    """Accountcommon user search by platform ID result (accountcommon.UserSearchByPlatformIDResult)

    Properties:
        display_name: (DisplayName) REQUIRED str

        email_address: (EmailAddress) REQUIRED str

        linked_platforms: (LinkedPlatforms) REQUIRED List[AccountcommonUserLinkedPlatform]

        phone_number: (PhoneNumber) REQUIRED str

        user_id: (UserId) REQUIRED str
    """

    # region fields

    display_name: str                                                                              # REQUIRED
    email_address: str                                                                             # REQUIRED
    linked_platforms: List[AccountcommonUserLinkedPlatform]                                        # REQUIRED
    phone_number: str                                                                              # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_display_name(self, value: str) -> AccountcommonUserSearchByPlatformIDResult:
        self.display_name = value
        return self

    def with_email_address(self, value: str) -> AccountcommonUserSearchByPlatformIDResult:
        self.email_address = value
        return self

    def with_linked_platforms(self, value: List[AccountcommonUserLinkedPlatform]) -> AccountcommonUserSearchByPlatformIDResult:
        self.linked_platforms = value
        return self

    def with_phone_number(self, value: str) -> AccountcommonUserSearchByPlatformIDResult:
        self.phone_number = value
        return self

    def with_user_id(self, value: str) -> AccountcommonUserSearchByPlatformIDResult:
        self.user_id = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        if not hasattr(self, "display_name") or self.display_name is None:
            return False
        if not hasattr(self, "email_address") or self.email_address is None:
            return False
        if not hasattr(self, "linked_platforms") or self.linked_platforms is None:
            return False
        if not hasattr(self, "phone_number") or self.phone_number is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "display_name"):
            result["DisplayName"] = str(self.display_name)
        elif include_empty:
            result["DisplayName"] = str()
        if hasattr(self, "email_address"):
            result["EmailAddress"] = str(self.email_address)
        elif include_empty:
            result["EmailAddress"] = str()
        if hasattr(self, "linked_platforms"):
            result["LinkedPlatforms"] = [i0.to_dict(include_empty=include_empty) for i0 in self.linked_platforms]
        elif include_empty:
            result["LinkedPlatforms"] = []
        if hasattr(self, "phone_number"):
            result["PhoneNumber"] = str(self.phone_number)
        elif include_empty:
            result["PhoneNumber"] = str()
        if hasattr(self, "user_id"):
            result["UserId"] = str(self.user_id)
        elif include_empty:
            result["UserId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        display_name: str,
        email_address: str,
        linked_platforms: List[AccountcommonUserLinkedPlatform],
        phone_number: str,
        user_id: str,
    ) -> AccountcommonUserSearchByPlatformIDResult:
        instance = cls()
        instance.display_name = display_name
        instance.email_address = email_address
        instance.linked_platforms = linked_platforms
        instance.phone_number = phone_number
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonUserSearchByPlatformIDResult:
        instance = cls()
        if not dict_:
            return instance
        if "DisplayName" in dict_ and dict_["DisplayName"] is not None:
            instance.display_name = str(dict_["DisplayName"])
        elif include_empty:
            instance.display_name = str()
        if "EmailAddress" in dict_ and dict_["EmailAddress"] is not None:
            instance.email_address = str(dict_["EmailAddress"])
        elif include_empty:
            instance.email_address = str()
        if "LinkedPlatforms" in dict_ and dict_["LinkedPlatforms"] is not None:
            instance.linked_platforms = [AccountcommonUserLinkedPlatform.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["LinkedPlatforms"]]
        elif include_empty:
            instance.linked_platforms = []
        if "PhoneNumber" in dict_ and dict_["PhoneNumber"] is not None:
            instance.phone_number = str(dict_["PhoneNumber"])
        elif include_empty:
            instance.phone_number = str()
        if "UserId" in dict_ and dict_["UserId"] is not None:
            instance.user_id = str(dict_["UserId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, AccountcommonUserSearchByPlatformIDResult]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[AccountcommonUserSearchByPlatformIDResult]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[AccountcommonUserSearchByPlatformIDResult, List[AccountcommonUserSearchByPlatformIDResult]]:
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
            "DisplayName": "display_name",
            "EmailAddress": "email_address",
            "LinkedPlatforms": "linked_platforms",
            "PhoneNumber": "phone_number",
            "UserId": "user_id",
        }

    # endregion static methods
