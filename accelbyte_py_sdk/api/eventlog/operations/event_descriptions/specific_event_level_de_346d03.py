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

# justice-event-log-service ()

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse
from .....core import clean_content_type
from .....core import try_convert_content_type
from .....core import deprecated

from ...models import ModelsMultipleEventLevel


@deprecated
class SpecificEventLevelDescriptionHandler(Operation):
    """Get specific list of event level and the descriptions by comma separated value of event levels (SpecificEventLevelDescriptionHandler)

    Properties:
        url: /event/descriptions/eventLevel/listByEventLevels

        method: GET

        tags: ["Event Descriptions"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        event_levels: (eventLevels) OPTIONAL str in query

    Responses:
        200: OK - ModelsMultipleEventLevel (OK)

        400: Bad Request - (Bad Request)

        404: Not Found - (Not Found)
    """

    # region fields

    _url: str = "/event/descriptions/eventLevel/listByEventLevels"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    event_levels: str                                                                              # OPTIONAL in [query]

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
        if hasattr(self, "event_levels"):
            result["eventLevels"] = self.event_levels
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        return True

    # endregion is/has methods

    # region with_x methods

    def with_event_levels(self, value: str) -> SpecificEventLevelDescriptionHandler:
        self.event_levels = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "event_levels") and self.event_levels:
            result["eventLevels"] = str(self.event_levels)
        elif include_empty:
            result["eventLevels"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsMultipleEventLevel], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - ModelsMultipleEventLevel (OK)

        400: Bad Request - (Bad Request)

        404: Not Found - (Not Found)

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
            return ModelsMultipleEventLevel.create_from_dict(content), None
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
        event_levels: Optional[str] = None,
    ) -> SpecificEventLevelDescriptionHandler:
        instance = cls()
        if event_levels is not None:
            instance.event_levels = event_levels
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> SpecificEventLevelDescriptionHandler:
        instance = cls()
        if "eventLevels" in dict_ and dict_["eventLevels"] is not None:
            instance.event_levels = str(dict_["eventLevels"])
        elif include_empty:
            instance.event_levels = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "eventLevels": "event_levels",
        }

    # endregion static methods
