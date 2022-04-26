# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-iam-service (5.8.0)

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


class AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4(Model):
    """Account upgrade headless account with verification code request V4 (account.upgradeHeadlessAccountWithVerificationCodeRequestV4)

    Properties:
        code: (code) REQUIRED str

        email_address: (emailAddress) REQUIRED str

        password: (password) REQUIRED str

        reach_minimum_age: (reachMinimumAge) REQUIRED bool

        username: (username) REQUIRED str

        validate_only: (validateOnly) REQUIRED bool

        country: (country) OPTIONAL str

        date_of_birth: (dateOfBirth) OPTIONAL str

        display_name: (displayName) OPTIONAL str
    """

    # region fields

    code: str                                                                                      # REQUIRED
    email_address: str                                                                             # REQUIRED
    password: str                                                                                  # REQUIRED
    reach_minimum_age: bool                                                                        # REQUIRED
    username: str                                                                                  # REQUIRED
    validate_only: bool                                                                            # REQUIRED
    country: str                                                                                   # OPTIONAL
    date_of_birth: str                                                                             # OPTIONAL
    display_name: str                                                                              # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_code(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.code = value
        return self

    def with_email_address(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.email_address = value
        return self

    def with_password(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.password = value
        return self

    def with_reach_minimum_age(self, value: bool) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.reach_minimum_age = value
        return self

    def with_username(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.username = value
        return self

    def with_validate_only(self, value: bool) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.validate_only = value
        return self

    def with_country(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.country = value
        return self

    def with_date_of_birth(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.date_of_birth = value
        return self

    def with_display_name(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.display_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "code"):
            result["code"] = str(self.code)
        elif include_empty:
            result["code"] = ""
        if hasattr(self, "email_address"):
            result["emailAddress"] = str(self.email_address)
        elif include_empty:
            result["emailAddress"] = ""
        if hasattr(self, "password"):
            result["password"] = str(self.password)
        elif include_empty:
            result["password"] = ""
        if hasattr(self, "reach_minimum_age"):
            result["reachMinimumAge"] = bool(self.reach_minimum_age)
        elif include_empty:
            result["reachMinimumAge"] = False
        if hasattr(self, "username"):
            result["username"] = str(self.username)
        elif include_empty:
            result["username"] = ""
        if hasattr(self, "validate_only"):
            result["validateOnly"] = bool(self.validate_only)
        elif include_empty:
            result["validateOnly"] = False
        if hasattr(self, "country"):
            result["country"] = str(self.country)
        elif include_empty:
            result["country"] = ""
        if hasattr(self, "date_of_birth"):
            result["dateOfBirth"] = str(self.date_of_birth)
        elif include_empty:
            result["dateOfBirth"] = ""
        if hasattr(self, "display_name"):
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = ""
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        code: str,
        email_address: str,
        password: str,
        reach_minimum_age: bool,
        username: str,
        validate_only: bool,
        country: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        display_name: Optional[str] = None,
    ) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        instance = cls()
        instance.code = code
        instance.email_address = email_address
        instance.password = password
        instance.reach_minimum_age = reach_minimum_age
        instance.username = username
        instance.validate_only = validate_only
        if country is not None:
            instance.country = country
        if date_of_birth is not None:
            instance.date_of_birth = date_of_birth
        if display_name is not None:
            instance.display_name = display_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        instance = cls()
        if not dict_:
            return instance
        if "code" in dict_ and dict_["code"] is not None:
            instance.code = str(dict_["code"])
        elif include_empty:
            instance.code = ""
        if "emailAddress" in dict_ and dict_["emailAddress"] is not None:
            instance.email_address = str(dict_["emailAddress"])
        elif include_empty:
            instance.email_address = ""
        if "password" in dict_ and dict_["password"] is not None:
            instance.password = str(dict_["password"])
        elif include_empty:
            instance.password = ""
        if "reachMinimumAge" in dict_ and dict_["reachMinimumAge"] is not None:
            instance.reach_minimum_age = bool(dict_["reachMinimumAge"])
        elif include_empty:
            instance.reach_minimum_age = False
        if "username" in dict_ and dict_["username"] is not None:
            instance.username = str(dict_["username"])
        elif include_empty:
            instance.username = ""
        if "validateOnly" in dict_ and dict_["validateOnly"] is not None:
            instance.validate_only = bool(dict_["validateOnly"])
        elif include_empty:
            instance.validate_only = False
        if "country" in dict_ and dict_["country"] is not None:
            instance.country = str(dict_["country"])
        elif include_empty:
            instance.country = ""
        if "dateOfBirth" in dict_ and dict_["dateOfBirth"] is not None:
            instance.date_of_birth = str(dict_["dateOfBirth"])
        elif include_empty:
            instance.date_of_birth = ""
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = ""
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4, List[AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4], Dict[Any, AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4]]:
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
            "code": "code",
            "emailAddress": "email_address",
            "password": "password",
            "reachMinimumAge": "reach_minimum_age",
            "username": "username",
            "validateOnly": "validate_only",
            "country": "country",
            "dateOfBirth": "date_of_birth",
            "displayName": "display_name",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "code": True,
            "emailAddress": True,
            "password": True,
            "reachMinimumAge": True,
            "username": True,
            "validateOnly": True,
            "country": False,
            "dateOfBirth": False,
            "displayName": False,
        }

    # endregion static methods
