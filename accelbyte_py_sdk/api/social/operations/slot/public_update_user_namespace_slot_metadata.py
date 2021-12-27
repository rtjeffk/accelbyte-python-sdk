# justice-social-service (1.22.0)

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
from ...models import SlotInfo
from ...models import SlotMetadataUpdate


class PublicUpdateUserNamespaceSlotMetadata(Operation):
    """Updates the slot metadata (publicUpdateUserNamespaceSlotMetadata)

    Updates the slot metadata.<br>Other detail info:<ul><li><i>Required
    permission</i>: resource="NAMESPACE:{namespace}:USER:{userId}:SLOTDATA",
    action=4 (UPDATE)</li><li><i>Returns</i>: updated slot</li></ul>


    Properties:
        url: /social/public/namespaces/{namespace}/users/{userId}/slots/{slotId}/metadata

        method: PUT

        tags: ["Slot"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        body: (body) OPTIONAL SlotMetadataUpdate in body

        namespace: (namespace) REQUIRED str in path

        slot_id: (slotId) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

    Responses:
        200: OK - SlotInfo (successful operation)

        404: Not Found - ErrorEntity (12141: Slot [{slotId}] not found in namespace [{namespace}])
    """

    # region fields

    _url: str = "/social/public/namespaces/{namespace}/users/{userId}/slots/{slotId}/metadata"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: SlotMetadataUpdate                                                                       # OPTIONAL in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    slot_id: str                                                                                   # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]

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
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
            "slot_id",
            "user_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
        }

    def get_body_params(self) -> Any:
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "slot_id"):
            result["slotId"] = self.slot_id
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "slot_id") or self.slot_id is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: SlotMetadataUpdate) -> PublicUpdateUserNamespaceSlotMetadata:
        self.body = value
        return self

    def with_namespace(self, value: str) -> PublicUpdateUserNamespaceSlotMetadata:
        self.namespace = value
        return self

    def with_slot_id(self, value: str) -> PublicUpdateUserNamespaceSlotMetadata:
        self.slot_id = value
        return self

    def with_user_id(self, value: str) -> PublicUpdateUserNamespaceSlotMetadata:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = SlotMetadataUpdate()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "slot_id") and self.slot_id:
            result["slotId"] = str(self.slot_id)
        elif include_empty:
            result["slotId"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, SlotInfo], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - SlotInfo (successful operation)

        404: Not Found - ErrorEntity (12141: Slot [{slotId}] not found in namespace [{namespace}])
        """
        if code == 200:
            return SlotInfo.create_from_dict(content), None
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
        slot_id: str,
        user_id: str,
        body: Optional[SlotMetadataUpdate] = None,
    ) -> PublicUpdateUserNamespaceSlotMetadata:
        instance = cls()
        instance.namespace = namespace
        instance.slot_id = slot_id
        instance.user_id = user_id
        if body is not None:
            instance.body = body
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicUpdateUserNamespaceSlotMetadata:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = SlotMetadataUpdate.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = SlotMetadataUpdate()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "slotId" in dict_ and dict_["slotId"] is not None:
            instance.slot_id = str(dict_["slotId"])
        elif include_empty:
            instance.slot_id = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "slotId": "slot_id",
            "userId": "user_id",
        }

    # endregion static methods
