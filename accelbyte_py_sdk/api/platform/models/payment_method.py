# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template file: justice_py_sdk_codegen/__main__.py

# justice-platform-service (4.4.2)

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


class PaymentMethod(Model):
    """Payment method (PaymentMethod)

    Properties:
        name: (name) REQUIRED str

        payment_provider: (paymentProvider) REQUIRED str
    """

    # region fields

    name: str                                                                                      # REQUIRED
    payment_provider: str                                                                          # REQUIRED

    # endregion fields

    # region with_x methods

    def with_name(self, value: str) -> PaymentMethod:
        self.name = value
        return self

    def with_payment_provider(self, value: str) -> PaymentMethod:
        self.payment_provider = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "name"):
            result["name"] = str(self.name)
        elif include_empty:
            result["name"] = str()
        if hasattr(self, "payment_provider"):
            result["paymentProvider"] = str(self.payment_provider)
        elif include_empty:
            result["paymentProvider"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        name: str,
        payment_provider: str,
    ) -> PaymentMethod:
        instance = cls()
        instance.name = name
        instance.payment_provider = payment_provider
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PaymentMethod:
        instance = cls()
        if not dict_:
            return instance
        if "name" in dict_ and dict_["name"] is not None:
            instance.name = str(dict_["name"])
        elif include_empty:
            instance.name = str()
        if "paymentProvider" in dict_ and dict_["paymentProvider"] is not None:
            instance.payment_provider = str(dict_["paymentProvider"])
        elif include_empty:
            instance.payment_provider = str()
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, PaymentMethod]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[PaymentMethod]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[PaymentMethod, List[PaymentMethod]]:
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
            "name": "name",
            "paymentProvider": "payment_provider",
        }

    # endregion static methods
