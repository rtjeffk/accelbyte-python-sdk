# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

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

# justice-platform-service (4.3.2)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse
from .....core import clean_content_type
from .....core import try_convert_content_type

from ...models import StripeConfig
from ...models import TestResult


class TestStripeConfig(Operation):
    """Test stripe configuration (testStripeConfig)

    Test stripe configuration.

    #### Check List:

      * secretKey
      * allowedPaymentMethodTypes



    #### Non-check list:

      * publishableKey
      * webhookSecret

    Other detail info:
      * Required permission : resource="ADMIN:PAYMENT:CONFIG", action=4 (UPDATE)
      *  Returns : test adyen config

    Required Permission(s):
        - ADMIN:PAYMENT:CONFIG [UPDATE]

    Properties:
        url: /platform/admin/payment/config/merchant/stripeconfig/test

        method: POST

        tags: ["PaymentConfig"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        body: (body) OPTIONAL StripeConfig in body

        sandbox: (sandbox) OPTIONAL bool in query

    Responses:
        200: OK - TestResult (successful operation)
    """

    # region fields

    _url: str = "/platform/admin/payment/config/merchant/stripeconfig/test"
    _method: str = "POST"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: StripeConfig                                                                             # OPTIONAL in [body]
    sandbox: bool                                                                                  # OPTIONAL in [query]

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
    def security_type(self) -> Optional[str]:
        return self._security_type

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    def get_full_url(self, base_url: Union[None, str] = None, collection_format_map: Optional[Dict[str, Optional[str]]] = None) -> str:
        return self.create_full_url(
            url=self.url,
            base_url=base_url,
            query_params=self.get_query_params(),
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "query": self.get_query_params(),
        }

    def get_body_params(self) -> Any:
        if not hasattr(self, "body") or self.body is None:
            return None
        return self.body.to_dict()

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "sandbox"):
            result["sandbox"] = self.sandbox
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: StripeConfig) -> TestStripeConfig:
        self.body = value
        return self

    def with_sandbox(self, value: bool) -> TestStripeConfig:
        self.sandbox = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = StripeConfig()
        if hasattr(self, "sandbox") and self.sandbox:
            result["sandbox"] = bool(self.sandbox)
        elif include_empty:
            result["sandbox"] = bool()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, TestResult], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - TestResult (successful operation)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        if content and content_type != "location":
            actual_content_type = clean_content_type(content_type)
            if actual_content_type not in self.produces:
                was_converted, converted_content = try_convert_content_type(actual_content_type, self.produces, content)
                if was_converted:
                    content = converted_content
                else:
                    return None, HttpResponse.create_unexpected_content_type_error(actual=actual_content_type, expected=self.produces)
        if code == 200:
            return TestResult.create_from_dict(content), None
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            if undocumented_response.is_no_content():
                return None, None
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: Optional[StripeConfig] = None,
        sandbox: Optional[bool] = None,
    ) -> TestStripeConfig:
        instance = cls()
        if body is not None:
            instance.body = body
        if sandbox is not None:
            instance.sandbox = sandbox
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> TestStripeConfig:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = StripeConfig.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = StripeConfig()
        if "sandbox" in dict_ and dict_["sandbox"] is not None:
            instance.sandbox = bool(dict_["sandbox"])
        elif include_empty:
            instance.sandbox = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "sandbox": "sandbox",
        }

    # endregion static methods
