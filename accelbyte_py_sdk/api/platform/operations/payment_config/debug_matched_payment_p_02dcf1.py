# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: justice_py_sdk_codegen/__main__.py

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

# justice-platform-service (4.12.0)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HeaderStr
from .....core import HttpResponse

from ...models import ErrorEntity
from ...models import PaymentProviderConfigInfo


class DebugMatchedPaymentProviderConfig(Operation):
    """Debug matched payment provider config(internal) (debugMatchedPaymentProviderConfig)

    Debug matched payment provider config.
    Other detail info:

      * Required permission : resource="ADMIN:PAYMENT:CONFIG", action=2 (READ)
      *  Returns : payment provider config

    Required Permission(s):
        - ADMIN:PAYMENT:CONFIG [READ]

    Properties:
        url: /platform/admin/payment/config/provider/matched

        method: GET

        tags: ["PaymentConfig"]

        consumes: []

        produces: ["application/json"]

        securities: [BEARER_AUTH] or [BEARER_AUTH]

        namespace: (namespace) OPTIONAL str in query

        region: (region) OPTIONAL str in query

    Responses:
        200: OK - PaymentProviderConfigInfo (successful operation)

        404: Not Found - ErrorEntity (33241: Payment provider config [{id}] does not exist)
    """

    # region fields

    _url: str = "/platform/admin/payment/config/provider/matched"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _securities: List[List[str]] = [["BEARER_AUTH"], ["BEARER_AUTH"]]
    _location_query: str = None

    namespace: str  # OPTIONAL in [query]
    region: str  # OPTIONAL in [query]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def securities(self) -> List[List[str]]:
        return self._securities

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "query": self.get_query_params(),
        }

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "region"):
            result["region"] = self.region
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> DebugMatchedPaymentProviderConfig:
        self.namespace = value
        return self

    def with_region(self, value: str) -> DebugMatchedPaymentProviderConfig:
        self.region = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = ""
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = ""
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(
        self, code: int, content_type: str, content: Any
    ) -> Tuple[
        Union[None, PaymentProviderConfigInfo], Union[None, ErrorEntity, HttpResponse]
    ]:
        """Parse the given response.

        200: OK - PaymentProviderConfigInfo (successful operation)

        404: Not Found - ErrorEntity (33241: Payment provider config [{id}] does not exist)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        pre_processed_response, error = self.pre_process_response(
            code=code, content_type=content_type, content=content
        )
        if error is not None:
            return None, None if error.is_no_content() else error
        code, content_type, content = pre_processed_response

        if code == 200:
            return PaymentProviderConfigInfo.create_from_dict(content), None
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)

        return None, self.handle_undocumented_response(
            code=code, content_type=content_type, content=content
        )

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: Optional[str] = None,
        region: Optional[str] = None,
    ) -> DebugMatchedPaymentProviderConfig:
        instance = cls()
        if namespace is not None:
            instance.namespace = namespace
        if region is not None:
            instance.region = region
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> DebugMatchedPaymentProviderConfig:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = ""
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = ""
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "region": "region",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "namespace": False,
            "region": False,
        }

    # endregion static methods
