# justice-basic-service (1.26.0)

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


class FileUploadUrlInfo(Model):
    """File upload url info (FileUploadUrlInfo)

    Properties:
        access_url: (accessUrl) OPTIONAL str

        content_type: (contentType) OPTIONAL str

        method: (method) OPTIONAL str

        url: (url) OPTIONAL str
    """

    # region fields

    access_url: str                                                                                # OPTIONAL
    content_type: str                                                                              # OPTIONAL
    method: str                                                                                    # OPTIONAL
    url: str                                                                                       # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_access_url(self, value: str) -> FileUploadUrlInfo:
        self.access_url = value
        return self

    def with_content_type(self, value: str) -> FileUploadUrlInfo:
        self.content_type = value
        return self

    def with_method(self, value: str) -> FileUploadUrlInfo:
        self.method = value
        return self

    def with_url(self, value: str) -> FileUploadUrlInfo:
        self.url = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "access_url"):
            result["accessUrl"] = str(self.access_url)
        elif include_empty:
            result["accessUrl"] = str()
        if hasattr(self, "content_type"):
            result["contentType"] = str(self.content_type)
        elif include_empty:
            result["contentType"] = str()
        if hasattr(self, "method"):
            result["method"] = str(self.method)
        elif include_empty:
            result["method"] = str()
        if hasattr(self, "url"):
            result["url"] = str(self.url)
        elif include_empty:
            result["url"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        access_url: Optional[str] = None,
        content_type: Optional[str] = None,
        method: Optional[str] = None,
        url: Optional[str] = None,
    ) -> FileUploadUrlInfo:
        instance = cls()
        if access_url is not None:
            instance.access_url = access_url
        if content_type is not None:
            instance.content_type = content_type
        if method is not None:
            instance.method = method
        if url is not None:
            instance.url = url
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> FileUploadUrlInfo:
        instance = cls()
        if not dict_:
            return instance
        if "accessUrl" in dict_ and dict_["accessUrl"] is not None:
            instance.access_url = str(dict_["accessUrl"])
        elif include_empty:
            instance.access_url = str()
        if "contentType" in dict_ and dict_["contentType"] is not None:
            instance.content_type = str(dict_["contentType"])
        elif include_empty:
            instance.content_type = str()
        if "method" in dict_ and dict_["method"] is not None:
            instance.method = str(dict_["method"])
        elif include_empty:
            instance.method = str()
        if "url" in dict_ and dict_["url"] is not None:
            instance.url = str(dict_["url"])
        elif include_empty:
            instance.url = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "accessUrl": "access_url",
            "contentType": "content_type",
            "method": "method",
            "url": "url",
        }

    # endregion static methods
