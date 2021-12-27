# justice-platform-service (3.39.0)

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

from .....core import Operation
from .....core import HttpResponse

from ...models import TimedOwnership


class PublicGetMyEntitlementOwnershipBySku(Operation):
    """Get my entitlement ownership by sku (publicGetMyEntitlementOwnershipBySku)

    Get my entitlement ownership by sku.<p>Other detail info: <ul><li><i>Required
    permission</i>: resource="NAMESPACE:{namespace}:ENTITLEMENT", action=2
    (READ)</li><li><i>Path's namespace</i> : <ul><li>can be filled with
    <b>publisher namespace</b> in order to get <b>publisher namespace entitlement
    ownership by sku</b></li><li>can be filled with <b>game namespace</b> in order
    to get <b>game namespace entitlement ownership by sku</b></li></ul></li></ul>


    Properties:
        url: /platform/public/namespaces/{namespace}/users/me/entitlements/ownership/bySku

        method: GET

        tags: ["Entitlement"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        namespace: (namespace) REQUIRED str in path

        entitlement_clazz: (entitlementClazz) OPTIONAL str in query

        sku: (sku) REQUIRED str in query

    Responses:
        200: OK - TimedOwnership (successful operation)
    """

    # region fields

    _url: str = "/platform/public/namespaces/{namespace}/users/me/entitlements/ownership/bySku"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    entitlement_clazz: str                                                                         # OPTIONAL in [query]
    sku: str                                                                                       # REQUIRED in [query]

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

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        return self.create_full_url(
            url=self.url,
            base_url=base_url,
            path_params=self.get_path_params(),
            query_params=self.get_query_params(),
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
            "sku",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "entitlement_clazz"):
            result["entitlementClazz"] = self.entitlement_clazz
        if hasattr(self, "sku"):
            result["sku"] = self.sku
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "sku") or self.sku is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> PublicGetMyEntitlementOwnershipBySku:
        self.namespace = value
        return self

    def with_entitlement_clazz(self, value: str) -> PublicGetMyEntitlementOwnershipBySku:
        self.entitlement_clazz = value
        return self

    def with_sku(self, value: str) -> PublicGetMyEntitlementOwnershipBySku:
        self.sku = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "entitlement_clazz") and self.entitlement_clazz:
            result["entitlementClazz"] = str(self.entitlement_clazz)
        elif include_empty:
            result["entitlementClazz"] = str()
        if hasattr(self, "sku") and self.sku:
            result["sku"] = str(self.sku)
        elif include_empty:
            result["sku"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, TimedOwnership], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - TimedOwnership (successful operation)
        """
        if code == 200:
            return TimedOwnership.create_from_dict(content), None
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        sku: str,
        entitlement_clazz: Optional[str] = None,
    ) -> PublicGetMyEntitlementOwnershipBySku:
        instance = cls()
        instance.namespace = namespace
        instance.sku = sku
        if entitlement_clazz is not None:
            instance.entitlement_clazz = entitlement_clazz
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicGetMyEntitlementOwnershipBySku:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "entitlementClazz" in dict_ and dict_["entitlementClazz"] is not None:
            instance.entitlement_clazz = str(dict_["entitlementClazz"])
        elif include_empty:
            instance.entitlement_clazz = str()
        if "sku" in dict_ and dict_["sku"] is not None:
            instance.sku = str(dict_["sku"])
        elif include_empty:
            instance.sku = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "entitlementClazz": "entitlement_clazz",
            "sku": "sku",
        }

    # endregion static methods
