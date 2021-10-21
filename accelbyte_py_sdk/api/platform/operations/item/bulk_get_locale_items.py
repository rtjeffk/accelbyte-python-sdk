# justice-platform-service (3.34.0)

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
from ...models import ItemInfo


class BulkGetLocaleItems(Operation):
    """Bulk get locale items (bulkGetLocaleItems)

    This API is used to bulk get locale items. If item not exist in specific
    region, default region item will return.

    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:ITEM", action=2 (READ)
      *  Returns : the list of items info


    Properties:
        url: /platform/admin/namespaces/{namespace}/items/locale/byIds

        method: GET

        tags: ["Item"]

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        store_id: (storeId) OPTIONAL str in query

        item_ids: (itemIds) REQUIRED str in query

        region: (region) OPTIONAL str in query

        language: (language) OPTIONAL str in query

        active_only: (activeOnly) OPTIONAL bool in query

    Responses:
        200: OK - List[ItemInfo] (successful operation)

        404: Not Found - ErrorEntity (30141: Store [{storeId}] does not exist in namespace [{namespace}] | 30142: Published store does not exist in namespace [{namespace}])
    """

    # region fields

    _url: str = "/platform/admin/namespaces/{namespace}/items/locale/byIds"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    store_id: str                                                                                  # OPTIONAL in [query]
    item_ids: str                                                                                  # REQUIRED in [query]
    region: str                                                                                    # OPTIONAL in [query]
    language: str                                                                                  # OPTIONAL in [query]
    active_only: bool                                                                              # OPTIONAL in [query]

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
            url = url.replace(f"{{{k}}}", v)
        result += url

        # query params
        result += "?" + "&".join([f"{k}={v}" for k, v in self.get_query_params().items()])

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
            "item_ids",
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
        if hasattr(self, "store_id"):
            result["storeId"] = self.store_id
        if hasattr(self, "item_ids"):
            result["itemIds"] = self.item_ids
        if hasattr(self, "region"):
            result["region"] = self.region
        if hasattr(self, "language"):
            result["language"] = self.language
        if hasattr(self, "active_only"):
            result["activeOnly"] = self.active_only
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "item_ids") or self.item_ids is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> BulkGetLocaleItems:
        self.namespace = value
        return self

    def with_store_id(self, value: str) -> BulkGetLocaleItems:
        self.store_id = value
        return self

    def with_item_ids(self, value: str) -> BulkGetLocaleItems:
        self.item_ids = value
        return self

    def with_region(self, value: str) -> BulkGetLocaleItems:
        self.region = value
        return self

    def with_language(self, value: str) -> BulkGetLocaleItems:
        self.language = value
        return self

    def with_active_only(self, value: bool) -> BulkGetLocaleItems:
        self.active_only = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "store_id") and self.store_id:
            result["storeId"] = str(self.store_id)
        elif include_empty:
            result["storeId"] = str()
        if hasattr(self, "item_ids") and self.item_ids:
            result["itemIds"] = str(self.item_ids)
        elif include_empty:
            result["itemIds"] = str()
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = str()
        if hasattr(self, "language") and self.language:
            result["language"] = str(self.language)
        elif include_empty:
            result["language"] = str()
        if hasattr(self, "active_only") and self.active_only:
            result["activeOnly"] = bool(self.active_only)
        elif include_empty:
            result["activeOnly"] = bool()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, List[ItemInfo]], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - List[ItemInfo] (successful operation)

        404: Not Found - ErrorEntity (30141: Store [{storeId}] does not exist in namespace [{namespace}] | 30142: Published store does not exist in namespace [{namespace}])
        """
        if code == 200:
            return [ItemInfo.create_from_dict(i) for i in content], None
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
        namespace: str,
        item_ids: str,
        store_id: Optional[str] = None,
        region: Optional[str] = None,
        language: Optional[str] = None,
        active_only: Optional[bool] = None,
    ) -> BulkGetLocaleItems:
        instance = cls()
        instance.namespace = namespace
        instance.item_ids = item_ids
        if store_id is not None:
            instance.store_id = store_id
        if region is not None:
            instance.region = region
        if language is not None:
            instance.language = language
        if active_only is not None:
            instance.active_only = active_only
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> BulkGetLocaleItems:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "storeId" in dict_ and dict_["storeId"] is not None:
            instance.store_id = str(dict_["storeId"])
        elif include_empty:
            instance.store_id = str()
        if "itemIds" in dict_ and dict_["itemIds"] is not None:
            instance.item_ids = str(dict_["itemIds"])
        elif include_empty:
            instance.item_ids = str()
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = str()
        if "language" in dict_ and dict_["language"] is not None:
            instance.language = str(dict_["language"])
        elif include_empty:
            instance.language = str()
        if "activeOnly" in dict_ and dict_["activeOnly"] is not None:
            instance.active_only = bool(dict_["activeOnly"])
        elif include_empty:
            instance.active_only = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "storeId": "store_id",
            "itemIds": "item_ids",
            "region": "region",
            "language": "language",
            "activeOnly": "active_only",
        }

    # endregion static methods
