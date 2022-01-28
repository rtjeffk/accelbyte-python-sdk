# justice-event-log-service ()

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
from .....core import deprecated

from ...models import ModelsMultipleEventType


@deprecated
class SpecificEventTypeDescriptionHandler(Operation):
    """Get specific list of event type and the descriptions by comma separated value of event types (SpecificEventTypeDescriptionHandler)

    Properties:
        url: /event/descriptions/eventType/listByEventTypes

        method: GET

        tags: ["Event Descriptions"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        event_types: (eventTypes) OPTIONAL str in query

    Responses:
        200: OK - ModelsMultipleEventType (OK)

        400: Bad Request - (Bad Request)

        404: Not Found - (Not Found)
    """

    # region fields

    _url: str = "/event/descriptions/eventType/listByEventTypes"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    event_types: str                                                                               # OPTIONAL in [query]

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
            "query": self.get_query_params(),
        }

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "event_types"):
            result["eventTypes"] = self.event_types
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        return True

    # endregion is/has methods

    # region with_x methods

    def with_event_types(self, value: str) -> SpecificEventTypeDescriptionHandler:
        self.event_types = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "event_types") and self.event_types:
            result["eventTypes"] = str(self.event_types)
        elif include_empty:
            result["eventTypes"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsMultipleEventType], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - ModelsMultipleEventType (OK)

        400: Bad Request - (Bad Request)

        404: Not Found - (Not Found)
        """
        if code == 200:
            return ModelsMultipleEventType.create_from_dict(content), None
        if code == 400:
            return None, HttpResponse.create(code, "Bad Request")
        if code == 404:
            return None, HttpResponse.create(code, "Not Found")
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
        event_types: Optional[str] = None,
    ) -> SpecificEventTypeDescriptionHandler:
        instance = cls()
        if event_types is not None:
            instance.event_types = event_types
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> SpecificEventTypeDescriptionHandler:
        instance = cls()
        if "eventTypes" in dict_ and dict_["eventTypes"] is not None:
            instance.event_types = str(dict_["eventTypes"])
        elif include_empty:
            instance.event_types = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "eventTypes": "event_types",
        }

    # endregion static methods