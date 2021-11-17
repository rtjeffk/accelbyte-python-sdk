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


class AcceptAgreementResponse(Model):
    """Accept agreement response (AcceptAgreementResponse)

    Properties:
        comply: (comply) REQUIRED bool

        proceed: (proceed) REQUIRED bool

        ext: (ext) OPTIONAL Dict[str, Any]
    """

    # region fields

    comply: bool                                                                                   # REQUIRED
    proceed: bool                                                                                  # REQUIRED
    ext: Dict[str, Any]                                                                            # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_comply(self, value: bool) -> AcceptAgreementResponse:
        self.comply = value
        return self

    def with_proceed(self, value: bool) -> AcceptAgreementResponse:
        self.proceed = value
        return self

    def with_ext(self, value: Dict[str, Any]) -> AcceptAgreementResponse:
        self.ext = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "comply"):
            result["comply"] = bool(self.comply)
        elif include_empty:
            result["comply"] = bool()
        if hasattr(self, "proceed"):
            result["proceed"] = bool(self.proceed)
        elif include_empty:
            result["proceed"] = bool()
        if hasattr(self, "ext"):
            result["ext"] = {str(k0): v0 for k0, v0 in self.ext.items()}
        elif include_empty:
            result["ext"] = {}
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        comply: bool,
        proceed: bool,
        ext: Optional[Dict[str, Any]] = None,
    ) -> AcceptAgreementResponse:
        instance = cls()
        instance.comply = comply
        instance.proceed = proceed
        if ext is not None:
            instance.ext = ext
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AcceptAgreementResponse:
        instance = cls()
        if not dict_:
            return instance
        if "comply" in dict_ and dict_["comply"] is not None:
            instance.comply = bool(dict_["comply"])
        elif include_empty:
            instance.comply = bool()
        if "proceed" in dict_ and dict_["proceed"] is not None:
            instance.proceed = bool(dict_["proceed"])
        elif include_empty:
            instance.proceed = bool()
        if "ext" in dict_ and dict_["ext"] is not None:
            instance.ext = {str(k0): v0 for k0, v0 in dict_["ext"].items()}
        elif include_empty:
            instance.ext = {}
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "comply": "comply",
            "proceed": "proceed",
            "ext": "ext",
        }

    # endregion static methods