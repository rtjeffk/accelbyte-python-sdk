# justice-iam-service (5.1.1)

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

from ...models import ModelInputValidationUpdatePayload
from ...models import RestErrorResponse


class AdminUpdateInputValidations(Operation):
    """Admin Update Input Validations (AdminUpdateInputValidations)

    <p>Required permission 'ADMIN:CONFIGURATION' [UPDATE]</p> <p>This endpoint is
    used to update input validation configuration.</p> Supported
    <code>field</code>:<br> <ul> <li>displayName</li> <li>password</li>
    <li>username</li> </ul> <p>If <code>isCustomRegex</code> is set to true,
    <code>regex</code> parameter will be used as input validation and the other
    parameters will be ignored. Otherwise, <code>regex</code> parameter will be
    ignored and regex for input validation will be generated based on the
    combination of the other parameters. </p> <p>If <code>allowUnicode</code> is
    set to true, unicode regex pattern will be use as the input validation and the
    other parameters will be ignored.</p> Supported <code>letterCase</code>:<br>
    <ul> <li>lowercase</li> <li>uppercase</li> <li>mixed: uppercase and
    lowercase</li> <li>mixed: uppercase and/or lowercase</li> </ul> Supported
    <code>specialCharacterLocation</code>:<br> <ul> <li>anywhere</li>
    <li>middle</li> </ul> <p>If <code>specialCharacters</code> is empty,
    <code>specialCharacterLocation</code> and
    <code>maxRepeatingSpecialCharacter</code> will be ignored.</p>
    <p><code>minCharType</code> is used to identify how many required criteria in
    the regex. The supported criteria are number, letter, special character, and
    letter case. If set to 0 or 1 means all criteria are optional. It can be set
    as much as the number of criteria enabled.</p>


    Properties:
        url: /iam/v3/admin/inputValidations

        method: PUT

        tags: ["InputValidations"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        body: (body) REQUIRED List[ModelInputValidationUpdatePayload] in body

    Responses:
        204: No Content - (No Content)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - RestErrorResponse
    """

    # region fields

    _url: str = "/iam/v3/admin/inputValidations"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: List[ModelInputValidationUpdatePayload]                                                  # REQUIRED in [body]

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
            "body",
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
        return [i.to_dict() for i in self.body]

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: List[ModelInputValidationUpdatePayload]) -> AdminUpdateInputValidations:
        self.body = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = [i0.to_dict(include_empty=include_empty) for i0 in self.body]
        elif include_empty:
            result["body"] = []
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[None, Union[None, HttpResponse, RestErrorResponse]]:
        """Parse the given response.

        204: No Content - (No Content)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - RestErrorResponse
        """
        if code == 204:
            return None, None
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
        if code == 404:
            return None, RestErrorResponse.create_from_dict(content)
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
        body: List[ModelInputValidationUpdatePayload],
    ) -> AdminUpdateInputValidations:
        instance = cls()
        instance.body = body
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminUpdateInputValidations:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = [ModelInputValidationUpdatePayload.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["body"]]
        elif include_empty:
            instance.body = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
        }

    # endregion static methods