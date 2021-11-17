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

from .....core import Operation
from .....core import HttpResponse

from ...models import ErrorEntity
from ...models import RetrievePolicyResponse


class RetrievePolicyCountry(Operation):
    """Retrieve a Base Legal Policy based on a Particular Country (retrievePolicyCountry)

    Retrieve a Base Legal Policy based on a Particular Country.<br>Other detail
    info: <ul><li><i>Required permission</i>: resource="ADMIN:NAMESPACE:*:LEGAL",
    action=2 (READ)</li></ul>


    Properties:
        url: /agreement/admin/base-policies/{basePolicyId}/countries/{countryCode}

        method: GET

        tags: ["Base Legal Policies"]

        consumes: []

        produces: ["application/json"]

        security: bearer

        base_policy_id: (basePolicyId) REQUIRED str in path

        country_code: (countryCode) REQUIRED str in path

    Responses:
        200: OK - RetrievePolicyResponse (successful operation)

        404: Not Found - ErrorEntity (40031: errors.net.accelbyte.platform.legal.base_policy_not_found)
    """

    # region fields

    _url: str = "/agreement/admin/base-policies/{basePolicyId}/countries/{countryCode}"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    base_policy_id: str                                                                            # REQUIRED in [path]
    country_code: str                                                                              # REQUIRED in [path]

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
    def security(self) -> Optional[str]:
        return self._security

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        result = base_url if base_url is not None else ""

        # path params
        url = self.url
        for k, v in self.get_path_params().items():
            url = url.replace(f"{{{k}}}", str(v))
        result += url

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "base_policy_id",
            "country_code",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "base_policy_id"):
            result["basePolicyId"] = self.base_policy_id
        if hasattr(self, "country_code"):
            result["countryCode"] = self.country_code
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "base_policy_id") or self.base_policy_id is None:
            return False
        if not hasattr(self, "country_code") or self.country_code is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_base_policy_id(self, value: str) -> RetrievePolicyCountry:
        self.base_policy_id = value
        return self

    def with_country_code(self, value: str) -> RetrievePolicyCountry:
        self.country_code = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "base_policy_id") and self.base_policy_id:
            result["basePolicyId"] = str(self.base_policy_id)
        elif include_empty:
            result["basePolicyId"] = str()
        if hasattr(self, "country_code") and self.country_code:
            result["countryCode"] = str(self.country_code)
        elif include_empty:
            result["countryCode"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, RetrievePolicyResponse], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - RetrievePolicyResponse (successful operation)

        404: Not Found - ErrorEntity (40031: errors.net.accelbyte.platform.legal.base_policy_not_found)
        """
        if code == 200:
            return RetrievePolicyResponse.create_from_dict(content), None
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        base_policy_id: str,
        country_code: str,
    ) -> RetrievePolicyCountry:
        instance = cls()
        instance.base_policy_id = base_policy_id
        instance.country_code = country_code
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> RetrievePolicyCountry:
        instance = cls()
        if "basePolicyId" in dict_ and dict_["basePolicyId"] is not None:
            instance.base_policy_id = str(dict_["basePolicyId"])
        elif include_empty:
            instance.base_policy_id = str()
        if "countryCode" in dict_ and dict_["countryCode"] is not None:
            instance.country_code = str(dict_["countryCode"])
        elif include_empty:
            instance.country_code = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "basePolicyId": "base_policy_id",
            "countryCode": "country_code",
        }

    # endregion static methods