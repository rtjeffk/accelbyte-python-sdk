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

# justice-legal-service (1.19.0)

from __future__ import annotations
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse

from ...models import AcceptAgreementRequest
from ...models import AcceptAgreementResponse


class IndirectBulkAcceptVersionedPolicy(Operation):
    """Admin bulk accept Policy Versions (indirectBulkAcceptVersionedPolicy)

    Accepts many legal policy versions all at once. Supply with localized version policy id and userId to accept an agreement. Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:USER:{userId}:LEGAL", action=1 (CREATE)

    Required Permission(s):
        - ADMIN:NAMESPACE:{namespace}:USER:{userId}:LEGAL [CREATE]

    Properties:
        url: /agreement/admin/namespaces/{namespace}/users/{userId}/agreements/policies

        method: POST

        tags: ["Admin User Agreement"]

        consumes: []

        produces: ["application/json"]

        security_type: bearer

        body: (body) OPTIONAL List[AcceptAgreementRequest] in body

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        publisher_user_id: (publisherUserId) OPTIONAL str in query

        client_id: (clientId) REQUIRED str in query

        country_code: (countryCode) REQUIRED str in query

    Responses:
        200: OK - AcceptAgreementResponse (successful operation)
    """

    # region fields

    _url: str = "/agreement/admin/namespaces/{namespace}/users/{userId}/agreements/policies"
    _method: str = "POST"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: List[AcceptAgreementRequest]                                                             # OPTIONAL in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    publisher_user_id: str                                                                         # OPTIONAL in [query]
    client_id: str                                                                                 # REQUIRED in [query]
    country_code: str                                                                              # REQUIRED in [query]

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
            path_params=self.get_path_params(),
            query_params=self.get_query_params(),
        )

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
            "user_id",
            "client_id",
            "country_code",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_body_params(self) -> Any:
        if not hasattr(self, "body") or self.body is None:
            return None
        return [i.to_dict() for i in self.body]

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "publisher_user_id"):
            result["publisherUserId"] = self.publisher_user_id
        if hasattr(self, "client_id"):
            result["clientId"] = self.client_id
        if hasattr(self, "country_code"):
            result["countryCode"] = self.country_code
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        # required checks
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        if not hasattr(self, "client_id") or self.client_id is None:
            return False
        if not hasattr(self, "country_code") or self.country_code is None:
            return False
        # pattern checks
        if hasattr(self, "body") and any(not x.is_valid() for x in self.body):
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: List[AcceptAgreementRequest]) -> IndirectBulkAcceptVersionedPolicy:
        self.body = value
        return self

    def with_namespace(self, value: str) -> IndirectBulkAcceptVersionedPolicy:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> IndirectBulkAcceptVersionedPolicy:
        self.user_id = value
        return self

    def with_publisher_user_id(self, value: str) -> IndirectBulkAcceptVersionedPolicy:
        self.publisher_user_id = value
        return self

    def with_client_id(self, value: str) -> IndirectBulkAcceptVersionedPolicy:
        self.client_id = value
        return self

    def with_country_code(self, value: str) -> IndirectBulkAcceptVersionedPolicy:
        self.country_code = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = [i0.to_dict(include_empty=include_empty) for i0 in self.body]
        elif include_empty:
            result["body"] = []
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "publisher_user_id") and self.publisher_user_id:
            result["publisherUserId"] = str(self.publisher_user_id)
        elif include_empty:
            result["publisherUserId"] = str()
        if hasattr(self, "client_id") and self.client_id:
            result["clientId"] = str(self.client_id)
        elif include_empty:
            result["clientId"] = str()
        if hasattr(self, "country_code") and self.country_code:
            result["countryCode"] = str(self.country_code)
        elif include_empty:
            result["countryCode"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, AcceptAgreementResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - AcceptAgreementResponse (successful operation)

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        pre_processed_response, error = self.pre_process_response(code=code, content_type=content_type, content=content)
        if error is not None:
            return None, None if error.is_no_content() else error
        code, content_type, content = pre_processed_response

        if code == 200:
            return AcceptAgreementResponse.create_from_dict(content), None

        return None, self.handle_undocumented_response(code=code, content_type=content_type, content=content)

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        user_id: str,
        client_id: str,
        country_code: str,
        body: Optional[List[AcceptAgreementRequest]] = None,
        publisher_user_id: Optional[str] = None,
    ) -> IndirectBulkAcceptVersionedPolicy:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        instance.client_id = client_id
        instance.country_code = country_code
        if body is not None:
            instance.body = body
        if publisher_user_id is not None:
            instance.publisher_user_id = publisher_user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> IndirectBulkAcceptVersionedPolicy:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = [AcceptAgreementRequest.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["body"]]
        elif include_empty:
            instance.body = []
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "publisherUserId" in dict_ and dict_["publisherUserId"] is not None:
            instance.publisher_user_id = str(dict_["publisherUserId"])
        elif include_empty:
            instance.publisher_user_id = str()
        if "clientId" in dict_ and dict_["clientId"] is not None:
            instance.client_id = str(dict_["clientId"])
        elif include_empty:
            instance.client_id = str()
        if "countryCode" in dict_ and dict_["countryCode"] is not None:
            instance.country_code = str(dict_["countryCode"])
        elif include_empty:
            instance.country_code = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "userId": "user_id",
            "publisherUserId": "publisher_user_id",
            "clientId": "client_id",
            "countryCode": "country_code",
        }

    # endregion static methods
