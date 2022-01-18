# justice-platform-service (4.1.1)

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

from .....core import Operation
from .....core import HttpResponse

from ...models import FulfillmentScriptEvalTestRequest
from ...models import FulfillmentScriptEvalTestResult


class TestFulfillmentScriptEval(Operation):
    """Test eval fulfillment script (testFulfillmentScriptEval)

    <b>[TEST FACILITY ONLY]</b>Test eval fulfillment script.<br>Other detail info:
    <ul><li><i>Required permission</i>: resource="ADMIN:FULFILLMENT", action=2
    (READ)</li></ul>


    Properties:
        url: /platform/admin/fulfillment/scripts/tests/eval

        method: POST

        tags: ["FulfillmentScript"]

        consumes: []

        produces: []

        security_type: bearer

        body: (body) OPTIONAL FulfillmentScriptEvalTestRequest in body

    Responses:
        200: OK - FulfillmentScriptEvalTestResult (successful operation)
    """

    # region fields

    _url: str = "/platform/admin/fulfillment/scripts/tests/eval"
    _method: str = "POST"
    _consumes: List[str] = []
    _produces: List[str] = []
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: FulfillmentScriptEvalTestRequest                                                         # OPTIONAL in [body]

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
        }

    def get_body_params(self) -> Any:
        if not hasattr(self, "body") or self.body is None:
            return None
        return self.body.to_dict()

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: FulfillmentScriptEvalTestRequest) -> TestFulfillmentScriptEval:
        self.body = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = FulfillmentScriptEvalTestRequest()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, FulfillmentScriptEvalTestResult], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - FulfillmentScriptEvalTestResult (successful operation)
        """
        if code == 200:
            return FulfillmentScriptEvalTestResult.create_from_dict(content), None
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
        body: Optional[FulfillmentScriptEvalTestRequest] = None,
    ) -> TestFulfillmentScriptEval:
        instance = cls()
        if body is not None:
            instance.body = body
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> TestFulfillmentScriptEval:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = FulfillmentScriptEvalTestRequest.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = FulfillmentScriptEvalTestRequest()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
        }

    # endregion static methods
