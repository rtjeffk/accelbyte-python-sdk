# justice-seasonpass-service (1.6.0)

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

from ....core import Model

from ..models.image import Image
from ..models.localization import Localization


class PassInfo(Model):
    """A DTO object for pass info. (PassInfo)

    Properties:
        auto_enroll: (autoEnroll) REQUIRED bool

        code: (code) REQUIRED str

        created_at: (createdAt) REQUIRED str

        display_order: (displayOrder) REQUIRED str

        localizations: (localizations) REQUIRED Dict[str, Localization]

        namespace: (namespace) REQUIRED str

        pass_item_id: (passItemId) REQUIRED str

        pass_item_name: (passItemName) REQUIRED str

        season_id: (seasonId) REQUIRED str

        updated_at: (updatedAt) REQUIRED str

        images: (images) OPTIONAL List[Image]
    """

    # region fields

    auto_enroll: bool                                                                              # REQUIRED
    code: str                                                                                      # REQUIRED
    created_at: str                                                                                # REQUIRED
    display_order: str                                                                             # REQUIRED
    localizations: Dict[str, Localization]                                                         # REQUIRED
    namespace: str                                                                                 # REQUIRED
    pass_item_id: str                                                                              # REQUIRED
    pass_item_name: str                                                                            # REQUIRED
    season_id: str                                                                                 # REQUIRED
    updated_at: str                                                                                # REQUIRED
    images: List[Image]                                                                            # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_auto_enroll(self, value: bool) -> PassInfo:
        self.auto_enroll = value
        return self

    def with_code(self, value: str) -> PassInfo:
        self.code = value
        return self

    def with_created_at(self, value: str) -> PassInfo:
        self.created_at = value
        return self

    def with_display_order(self, value: str) -> PassInfo:
        self.display_order = value
        return self

    def with_localizations(self, value: Dict[str, Localization]) -> PassInfo:
        self.localizations = value
        return self

    def with_namespace(self, value: str) -> PassInfo:
        self.namespace = value
        return self

    def with_pass_item_id(self, value: str) -> PassInfo:
        self.pass_item_id = value
        return self

    def with_pass_item_name(self, value: str) -> PassInfo:
        self.pass_item_name = value
        return self

    def with_season_id(self, value: str) -> PassInfo:
        self.season_id = value
        return self

    def with_updated_at(self, value: str) -> PassInfo:
        self.updated_at = value
        return self

    def with_images(self, value: List[Image]) -> PassInfo:
        self.images = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "auto_enroll"):
            result["autoEnroll"] = bool(self.auto_enroll)
        elif include_empty:
            result["autoEnroll"] = bool()
        if hasattr(self, "code"):
            result["code"] = str(self.code)
        elif include_empty:
            result["code"] = str()
        if hasattr(self, "created_at"):
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "display_order"):
            result["displayOrder"] = str(self.display_order)
        elif include_empty:
            result["displayOrder"] = str()
        if hasattr(self, "localizations"):
            result["localizations"] = {str(k0): v0.to_dict(include_empty=include_empty) for k0, v0 in self.localizations.items()}
        elif include_empty:
            result["localizations"] = {}
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "pass_item_id"):
            result["passItemId"] = str(self.pass_item_id)
        elif include_empty:
            result["passItemId"] = str()
        if hasattr(self, "pass_item_name"):
            result["passItemName"] = str(self.pass_item_name)
        elif include_empty:
            result["passItemName"] = str()
        if hasattr(self, "season_id"):
            result["seasonId"] = str(self.season_id)
        elif include_empty:
            result["seasonId"] = str()
        if hasattr(self, "updated_at"):
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        if hasattr(self, "images"):
            result["images"] = [i0.to_dict(include_empty=include_empty) for i0 in self.images]
        elif include_empty:
            result["images"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        auto_enroll: bool,
        code: str,
        created_at: str,
        display_order: str,
        localizations: Dict[str, Localization],
        namespace: str,
        pass_item_id: str,
        pass_item_name: str,
        season_id: str,
        updated_at: str,
        images: Optional[List[Image]] = None,
    ) -> PassInfo:
        instance = cls()
        instance.auto_enroll = auto_enroll
        instance.code = code
        instance.created_at = created_at
        instance.display_order = display_order
        instance.localizations = localizations
        instance.namespace = namespace
        instance.pass_item_id = pass_item_id
        instance.pass_item_name = pass_item_name
        instance.season_id = season_id
        instance.updated_at = updated_at
        if images is not None:
            instance.images = images
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PassInfo:
        instance = cls()
        if not dict_:
            return instance
        if "autoEnroll" in dict_ and dict_["autoEnroll"] is not None:
            instance.auto_enroll = bool(dict_["autoEnroll"])
        elif include_empty:
            instance.auto_enroll = bool()
        if "code" in dict_ and dict_["code"] is not None:
            instance.code = str(dict_["code"])
        elif include_empty:
            instance.code = str()
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "displayOrder" in dict_ and dict_["displayOrder"] is not None:
            instance.display_order = str(dict_["displayOrder"])
        elif include_empty:
            instance.display_order = str()
        if "localizations" in dict_ and dict_["localizations"] is not None:
            instance.localizations = {str(k0): Localization.create_from_dict(v0, include_empty=include_empty) for k0, v0 in dict_["localizations"].items()}
        elif include_empty:
            instance.localizations = {}
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "passItemId" in dict_ and dict_["passItemId"] is not None:
            instance.pass_item_id = str(dict_["passItemId"])
        elif include_empty:
            instance.pass_item_id = str()
        if "passItemName" in dict_ and dict_["passItemName"] is not None:
            instance.pass_item_name = str(dict_["passItemName"])
        elif include_empty:
            instance.pass_item_name = str()
        if "seasonId" in dict_ and dict_["seasonId"] is not None:
            instance.season_id = str(dict_["seasonId"])
        elif include_empty:
            instance.season_id = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        if "images" in dict_ and dict_["images"] is not None:
            instance.images = [Image.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["images"]]
        elif include_empty:
            instance.images = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "autoEnroll": "auto_enroll",
            "code": "code",
            "createdAt": "created_at",
            "displayOrder": "display_order",
            "localizations": "localizations",
            "namespace": "namespace",
            "passItemId": "pass_item_id",
            "passItemName": "pass_item_name",
            "seasonId": "season_id",
            "updatedAt": "updated_at",
            "images": "images",
        }

    # endregion static methods