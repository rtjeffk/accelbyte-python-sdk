# justice-social-service (1.22.0)

# template file: justice_py_sdk_codegen/__main__.py

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


class SlotInfo(Model):
    """Slot info (SlotInfo)

    Properties:
        checksum: (checksum) OPTIONAL str

        custom_attribute: (customAttribute) OPTIONAL str

        date_accessed: (dateAccessed) OPTIONAL str

        date_created: (dateCreated) OPTIONAL str

        date_modified: (dateModified) OPTIONAL str

        label: (label) OPTIONAL str

        mime_type: (mimeType) OPTIONAL str

        namespace: (namespace) OPTIONAL str

        original_name: (originalName) OPTIONAL str

        size: (size) OPTIONAL int

        slot_id: (slotId) OPTIONAL str

        stored_name: (storedName) OPTIONAL str

        tags: (tags) OPTIONAL List[str]

        user_id: (userId) OPTIONAL str
    """

    # region fields

    checksum: str                                                                                  # OPTIONAL
    custom_attribute: str                                                                          # OPTIONAL
    date_accessed: str                                                                             # OPTIONAL
    date_created: str                                                                              # OPTIONAL
    date_modified: str                                                                             # OPTIONAL
    label: str                                                                                     # OPTIONAL
    mime_type: str                                                                                 # OPTIONAL
    namespace: str                                                                                 # OPTIONAL
    original_name: str                                                                             # OPTIONAL
    size: int                                                                                      # OPTIONAL
    slot_id: str                                                                                   # OPTIONAL
    stored_name: str                                                                               # OPTIONAL
    tags: List[str]                                                                                # OPTIONAL
    user_id: str                                                                                   # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_checksum(self, value: str) -> SlotInfo:
        self.checksum = value
        return self

    def with_custom_attribute(self, value: str) -> SlotInfo:
        self.custom_attribute = value
        return self

    def with_date_accessed(self, value: str) -> SlotInfo:
        self.date_accessed = value
        return self

    def with_date_created(self, value: str) -> SlotInfo:
        self.date_created = value
        return self

    def with_date_modified(self, value: str) -> SlotInfo:
        self.date_modified = value
        return self

    def with_label(self, value: str) -> SlotInfo:
        self.label = value
        return self

    def with_mime_type(self, value: str) -> SlotInfo:
        self.mime_type = value
        return self

    def with_namespace(self, value: str) -> SlotInfo:
        self.namespace = value
        return self

    def with_original_name(self, value: str) -> SlotInfo:
        self.original_name = value
        return self

    def with_size(self, value: int) -> SlotInfo:
        self.size = value
        return self

    def with_slot_id(self, value: str) -> SlotInfo:
        self.slot_id = value
        return self

    def with_stored_name(self, value: str) -> SlotInfo:
        self.stored_name = value
        return self

    def with_tags(self, value: List[str]) -> SlotInfo:
        self.tags = value
        return self

    def with_user_id(self, value: str) -> SlotInfo:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "checksum"):
            result["checksum"] = str(self.checksum)
        elif include_empty:
            result["checksum"] = str()
        if hasattr(self, "custom_attribute"):
            result["customAttribute"] = str(self.custom_attribute)
        elif include_empty:
            result["customAttribute"] = str()
        if hasattr(self, "date_accessed"):
            result["dateAccessed"] = str(self.date_accessed)
        elif include_empty:
            result["dateAccessed"] = str()
        if hasattr(self, "date_created"):
            result["dateCreated"] = str(self.date_created)
        elif include_empty:
            result["dateCreated"] = str()
        if hasattr(self, "date_modified"):
            result["dateModified"] = str(self.date_modified)
        elif include_empty:
            result["dateModified"] = str()
        if hasattr(self, "label"):
            result["label"] = str(self.label)
        elif include_empty:
            result["label"] = str()
        if hasattr(self, "mime_type"):
            result["mimeType"] = str(self.mime_type)
        elif include_empty:
            result["mimeType"] = str()
        if hasattr(self, "namespace"):
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "original_name"):
            result["originalName"] = str(self.original_name)
        elif include_empty:
            result["originalName"] = str()
        if hasattr(self, "size"):
            result["size"] = int(self.size)
        elif include_empty:
            result["size"] = int()
        if hasattr(self, "slot_id"):
            result["slotId"] = str(self.slot_id)
        elif include_empty:
            result["slotId"] = str()
        if hasattr(self, "stored_name"):
            result["storedName"] = str(self.stored_name)
        elif include_empty:
            result["storedName"] = str()
        if hasattr(self, "tags"):
            result["tags"] = [str(i0) for i0 in self.tags]
        elif include_empty:
            result["tags"] = []
        if hasattr(self, "user_id"):
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        checksum: Optional[str] = None,
        custom_attribute: Optional[str] = None,
        date_accessed: Optional[str] = None,
        date_created: Optional[str] = None,
        date_modified: Optional[str] = None,
        label: Optional[str] = None,
        mime_type: Optional[str] = None,
        namespace: Optional[str] = None,
        original_name: Optional[str] = None,
        size: Optional[int] = None,
        slot_id: Optional[str] = None,
        stored_name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        user_id: Optional[str] = None,
    ) -> SlotInfo:
        instance = cls()
        if checksum is not None:
            instance.checksum = checksum
        if custom_attribute is not None:
            instance.custom_attribute = custom_attribute
        if date_accessed is not None:
            instance.date_accessed = date_accessed
        if date_created is not None:
            instance.date_created = date_created
        if date_modified is not None:
            instance.date_modified = date_modified
        if label is not None:
            instance.label = label
        if mime_type is not None:
            instance.mime_type = mime_type
        if namespace is not None:
            instance.namespace = namespace
        if original_name is not None:
            instance.original_name = original_name
        if size is not None:
            instance.size = size
        if slot_id is not None:
            instance.slot_id = slot_id
        if stored_name is not None:
            instance.stored_name = stored_name
        if tags is not None:
            instance.tags = tags
        if user_id is not None:
            instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> SlotInfo:
        instance = cls()
        if not dict_:
            return instance
        if "checksum" in dict_ and dict_["checksum"] is not None:
            instance.checksum = str(dict_["checksum"])
        elif include_empty:
            instance.checksum = str()
        if "customAttribute" in dict_ and dict_["customAttribute"] is not None:
            instance.custom_attribute = str(dict_["customAttribute"])
        elif include_empty:
            instance.custom_attribute = str()
        if "dateAccessed" in dict_ and dict_["dateAccessed"] is not None:
            instance.date_accessed = str(dict_["dateAccessed"])
        elif include_empty:
            instance.date_accessed = str()
        if "dateCreated" in dict_ and dict_["dateCreated"] is not None:
            instance.date_created = str(dict_["dateCreated"])
        elif include_empty:
            instance.date_created = str()
        if "dateModified" in dict_ and dict_["dateModified"] is not None:
            instance.date_modified = str(dict_["dateModified"])
        elif include_empty:
            instance.date_modified = str()
        if "label" in dict_ and dict_["label"] is not None:
            instance.label = str(dict_["label"])
        elif include_empty:
            instance.label = str()
        if "mimeType" in dict_ and dict_["mimeType"] is not None:
            instance.mime_type = str(dict_["mimeType"])
        elif include_empty:
            instance.mime_type = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "originalName" in dict_ and dict_["originalName"] is not None:
            instance.original_name = str(dict_["originalName"])
        elif include_empty:
            instance.original_name = str()
        if "size" in dict_ and dict_["size"] is not None:
            instance.size = int(dict_["size"])
        elif include_empty:
            instance.size = int()
        if "slotId" in dict_ and dict_["slotId"] is not None:
            instance.slot_id = str(dict_["slotId"])
        elif include_empty:
            instance.slot_id = str()
        if "storedName" in dict_ and dict_["storedName"] is not None:
            instance.stored_name = str(dict_["storedName"])
        elif include_empty:
            instance.stored_name = str()
        if "tags" in dict_ and dict_["tags"] is not None:
            instance.tags = [str(i0) for i0 in dict_["tags"]]
        elif include_empty:
            instance.tags = []
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "checksum": "checksum",
            "customAttribute": "custom_attribute",
            "dateAccessed": "date_accessed",
            "dateCreated": "date_created",
            "dateModified": "date_modified",
            "label": "label",
            "mimeType": "mime_type",
            "namespace": "namespace",
            "originalName": "original_name",
            "size": "size",
            "slotId": "slot_id",
            "storedName": "stored_name",
            "tags": "tags",
            "userId": "user_id",
        }

    # endregion static methods
