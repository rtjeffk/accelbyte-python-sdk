# justice-platform-service (3.37.1)

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

from ..models.currency_summary import CurrencySummary


class OrderSummary(Model):
    """Order summary (OrderSummary)

    Properties:
        currency: (currency) OPTIONAL CurrencySummary

        ext: (ext) OPTIONAL Dict[str, Any]

        free: (free) OPTIONAL bool
    """

    # region fields

    currency: CurrencySummary                                                                      # OPTIONAL
    ext: Dict[str, Any]                                                                            # OPTIONAL
    free: bool                                                                                     # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_currency(self, value: CurrencySummary) -> OrderSummary:
        self.currency = value
        return self

    def with_ext(self, value: Dict[str, Any]) -> OrderSummary:
        self.ext = value
        return self

    def with_free(self, value: bool) -> OrderSummary:
        self.free = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "currency"):
            result["currency"] = self.currency.to_dict(include_empty=include_empty)
        elif include_empty:
            result["currency"] = CurrencySummary()
        if hasattr(self, "ext"):
            result["ext"] = {str(k0): v0 for k0, v0 in self.ext.items()}
        elif include_empty:
            result["ext"] = {}
        if hasattr(self, "free"):
            result["free"] = bool(self.free)
        elif include_empty:
            result["free"] = bool()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        currency: Optional[CurrencySummary] = None,
        ext: Optional[Dict[str, Any]] = None,
        free: Optional[bool] = None,
    ) -> OrderSummary:
        instance = cls()
        if currency is not None:
            instance.currency = currency
        if ext is not None:
            instance.ext = ext
        if free is not None:
            instance.free = free
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> OrderSummary:
        instance = cls()
        if not dict_:
            return instance
        if "currency" in dict_ and dict_["currency"] is not None:
            instance.currency = CurrencySummary.create_from_dict(dict_["currency"], include_empty=include_empty)
        elif include_empty:
            instance.currency = CurrencySummary()
        if "ext" in dict_ and dict_["ext"] is not None:
            instance.ext = {str(k0): v0 for k0, v0 in dict_["ext"].items()}
        elif include_empty:
            instance.ext = {}
        if "free" in dict_ and dict_["free"] is not None:
            instance.free = bool(dict_["free"])
        elif include_empty:
            instance.free = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "currency": "currency",
            "ext": "ext",
            "free": "free",
        }

    # endregion static methods