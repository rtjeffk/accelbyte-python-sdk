# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-basic-service (1.35.0)

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


class UserProfilePrivateInfo(Model):
    """User profile private info (UserProfilePrivateInfo)

    Properties:
        avatar_large_url: (avatarLargeUrl) OPTIONAL str

        avatar_small_url: (avatarSmallUrl) OPTIONAL str

        avatar_url: (avatarUrl) OPTIONAL str

        custom_attributes: (customAttributes) OPTIONAL Dict[str, Any]

        date_of_birth: (dateOfBirth) OPTIONAL str

        first_name: (firstName) OPTIONAL str

        language: (language) OPTIONAL str

        last_name: (lastName) OPTIONAL str

        namespace: (namespace) OPTIONAL str

        private_custom_attributes: (privateCustomAttributes) OPTIONAL Dict[str, Any]

        status: (status) OPTIONAL str

        time_zone: (timeZone) OPTIONAL str

        user_id: (userId) OPTIONAL str

        zip_code: (zipCode) OPTIONAL str
    """

    # region fields

    avatar_large_url: str                                                                          # OPTIONAL
    avatar_small_url: str                                                                          # OPTIONAL
    avatar_url: str                                                                                # OPTIONAL
    custom_attributes: Dict[str, Any]                                                              # OPTIONAL
    date_of_birth: str                                                                             # OPTIONAL
    first_name: str                                                                                # OPTIONAL
    language: str                                                                                  # OPTIONAL
    last_name: str                                                                                 # OPTIONAL
    namespace: str                                                                                 # OPTIONAL
    private_custom_attributes: Dict[str, Any]                                                      # OPTIONAL
    status: str                                                                                    # OPTIONAL
    time_zone: str                                                                                 # OPTIONAL
    user_id: str                                                                                   # OPTIONAL
    zip_code: str                                                                                  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_avatar_large_url(self, value: str) -> UserProfilePrivateInfo:
        self.avatar_large_url = value
        return self

    def with_avatar_small_url(self, value: str) -> UserProfilePrivateInfo:
        self.avatar_small_url = value
        return self

    def with_avatar_url(self, value: str) -> UserProfilePrivateInfo:
        self.avatar_url = value
        return self

    def with_custom_attributes(self, value: Dict[str, Any]) -> UserProfilePrivateInfo:
        self.custom_attributes = value
        return self

    def with_date_of_birth(self, value: str) -> UserProfilePrivateInfo:
        self.date_of_birth = value
        return self

    def with_first_name(self, value: str) -> UserProfilePrivateInfo:
        self.first_name = value
        return self

    def with_language(self, value: str) -> UserProfilePrivateInfo:
        self.language = value
        return self

    def with_last_name(self, value: str) -> UserProfilePrivateInfo:
        self.last_name = value
        return self

    def with_namespace(self, value: str) -> UserProfilePrivateInfo:
        self.namespace = value
        return self

    def with_private_custom_attributes(self, value: Dict[str, Any]) -> UserProfilePrivateInfo:
        self.private_custom_attributes = value
        return self

    def with_status(self, value: str) -> UserProfilePrivateInfo:
        self.status = value
        return self

    def with_time_zone(self, value: str) -> UserProfilePrivateInfo:
        self.time_zone = value
        return self

    def with_user_id(self, value: str) -> UserProfilePrivateInfo:
        self.user_id = value
        return self

    def with_zip_code(self, value: str) -> UserProfilePrivateInfo:
        self.zip_code = value
        return self

    # endregion with_x methods

    # region is/has methods

    # noinspection PyMethodMayBeStatic
    def is_valid(self) -> bool:
        # pylint: disable=no-self-use
        # required checks
        # pattern checks
        return True

    # endregion is/has methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "avatar_large_url"):
            result["avatarLargeUrl"] = str(self.avatar_large_url)
        elif include_empty:
            result["avatarLargeUrl"] = str()
        if hasattr(self, "avatar_small_url"):
            result["avatarSmallUrl"] = str(self.avatar_small_url)
        elif include_empty:
            result["avatarSmallUrl"] = str()
        if hasattr(self, "avatar_url"):
            result["avatarUrl"] = str(self.avatar_url)
        elif include_empty:
            result["avatarUrl"] = str()
        if hasattr(self, "custom_attributes"):
            result["customAttributes"] = {str(k0): v0 for k0, v0 in self.custom_attributes.items()}
        elif include_empty:
            result["customAttributes"] = {}
        if hasattr(self, "date_of_birth"):
            result["dateOfBirth"] = str(self.date_of_birth)
        elif include_empty:
            result["dateOfBirth"] = str()
        if hasattr(self, "first_name"):
            result["firstName"] = str(self.first_name)
        elif include_empty:
            result["firstName"] = str()
        if hasattr(self, "language"):
            result["language"] = str(self.language)
        elif include_empty:
            result["language"] = str()
        if hasattr(self, "last_name"):
            result["lastName"] = str(self.last_name)
        elif include_empty:
            result["lastName"] = str()
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "private_custom_attributes"):
            result["privateCustomAttributes"] = {str(k0): v0 for k0, v0 in self.private_custom_attributes.items()}
        elif include_empty:
            result["privateCustomAttributes"] = {}
        if hasattr(self, "status"):
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "time_zone"):
            result["timeZone"] = str(self.time_zone)
        elif include_empty:
            result["timeZone"] = str()
        if hasattr(self, "user_id"):
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "zip_code"):
            result["zipCode"] = str(self.zip_code)
        elif include_empty:
            result["zipCode"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        avatar_large_url: Optional[str] = None,
        avatar_small_url: Optional[str] = None,
        avatar_url: Optional[str] = None,
        custom_attributes: Optional[Dict[str, Any]] = None,
        date_of_birth: Optional[str] = None,
        first_name: Optional[str] = None,
        language: Optional[str] = None,
        last_name: Optional[str] = None,
        namespace: Optional[str] = None,
        private_custom_attributes: Optional[Dict[str, Any]] = None,
        status: Optional[str] = None,
        time_zone: Optional[str] = None,
        user_id: Optional[str] = None,
        zip_code: Optional[str] = None,
    ) -> UserProfilePrivateInfo:
        instance = cls()
        if avatar_large_url is not None:
            instance.avatar_large_url = avatar_large_url
        if avatar_small_url is not None:
            instance.avatar_small_url = avatar_small_url
        if avatar_url is not None:
            instance.avatar_url = avatar_url
        if custom_attributes is not None:
            instance.custom_attributes = custom_attributes
        if date_of_birth is not None:
            instance.date_of_birth = date_of_birth
        if first_name is not None:
            instance.first_name = first_name
        if language is not None:
            instance.language = language
        if last_name is not None:
            instance.last_name = last_name
        if namespace is not None:
            instance.namespace = namespace
        if private_custom_attributes is not None:
            instance.private_custom_attributes = private_custom_attributes
        if status is not None:
            instance.status = status
        if time_zone is not None:
            instance.time_zone = time_zone
        if user_id is not None:
            instance.user_id = user_id
        if zip_code is not None:
            instance.zip_code = zip_code
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UserProfilePrivateInfo:
        instance = cls()
        if not dict_:
            return instance
        if "avatarLargeUrl" in dict_ and dict_["avatarLargeUrl"] is not None:
            instance.avatar_large_url = str(dict_["avatarLargeUrl"])
        elif include_empty:
            instance.avatar_large_url = str()
        if "avatarSmallUrl" in dict_ and dict_["avatarSmallUrl"] is not None:
            instance.avatar_small_url = str(dict_["avatarSmallUrl"])
        elif include_empty:
            instance.avatar_small_url = str()
        if "avatarUrl" in dict_ and dict_["avatarUrl"] is not None:
            instance.avatar_url = str(dict_["avatarUrl"])
        elif include_empty:
            instance.avatar_url = str()
        if "customAttributes" in dict_ and dict_["customAttributes"] is not None:
            instance.custom_attributes = {str(k0): v0 for k0, v0 in dict_["customAttributes"].items()}
        elif include_empty:
            instance.custom_attributes = {}
        if "dateOfBirth" in dict_ and dict_["dateOfBirth"] is not None:
            instance.date_of_birth = str(dict_["dateOfBirth"])
        elif include_empty:
            instance.date_of_birth = str()
        if "firstName" in dict_ and dict_["firstName"] is not None:
            instance.first_name = str(dict_["firstName"])
        elif include_empty:
            instance.first_name = str()
        if "language" in dict_ and dict_["language"] is not None:
            instance.language = str(dict_["language"])
        elif include_empty:
            instance.language = str()
        if "lastName" in dict_ and dict_["lastName"] is not None:
            instance.last_name = str(dict_["lastName"])
        elif include_empty:
            instance.last_name = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "privateCustomAttributes" in dict_ and dict_["privateCustomAttributes"] is not None:
            instance.private_custom_attributes = {str(k0): v0 for k0, v0 in dict_["privateCustomAttributes"].items()}
        elif include_empty:
            instance.private_custom_attributes = {}
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "timeZone" in dict_ and dict_["timeZone"] is not None:
            instance.time_zone = str(dict_["timeZone"])
        elif include_empty:
            instance.time_zone = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "zipCode" in dict_ and dict_["zipCode"] is not None:
            instance.zip_code = str(dict_["zipCode"])
        elif include_empty:
            instance.zip_code = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, UserProfilePrivateInfo]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[UserProfilePrivateInfo]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[UserProfilePrivateInfo, List[UserProfilePrivateInfo]]:
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
            "avatarLargeUrl": "avatar_large_url",
            "avatarSmallUrl": "avatar_small_url",
            "avatarUrl": "avatar_url",
            "customAttributes": "custom_attributes",
            "dateOfBirth": "date_of_birth",
            "firstName": "first_name",
            "language": "language",
            "lastName": "last_name",
            "namespace": "namespace",
            "privateCustomAttributes": "private_custom_attributes",
            "status": "status",
            "timeZone": "time_zone",
            "userId": "user_id",
            "zipCode": "zip_code",
        }

    # endregion static methods
