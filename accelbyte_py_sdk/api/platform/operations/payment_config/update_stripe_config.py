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

# justice-platform-service (4.5.1)

from __future__ import annotations
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse

from ...models import ErrorEntity
from ...models import PaymentMerchantConfigInfo
from ...models import StripeConfig


class UpdateStripeConfig(Operation):
    """Update stripe config (updateStripeConfig)

    Update stripe config.
    Other detail info:

      * Required permission : resource="ADMIN:PAYMENT:CONFIG", action=4 (UPDATE)
      *  Returns : updated payment merchant config

    Required Permission(s):
        - ADMIN:PAYMENT:CONFIG [UPDATE]

    Properties:
        url: /platform/admin/payment/config/merchant/{id}/stripeconfig

        method: PUT

        tags: ["PaymentConfig"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        body: (body) OPTIONAL StripeConfig in body

        id_: (id) REQUIRED str in path

        sandbox: (sandbox) OPTIONAL bool in query

        validate: (validate) OPTIONAL bool in query

    Responses:
        200: OK - PaymentMerchantConfigInfo (successful operation)

        404: Not Found - ErrorEntity (33242: Payment merchant config [{id}] does not exist | 33221: Update [{paymentProvider}] config in payment merchant config [{id}] failed with message [{errMsg}])
    """

    # region fields

    _url: str = "/platform/admin/payment/config/merchant/{id}/stripeconfig"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: StripeConfig                                                                             # OPTIONAL in [body]
    id_: str                                                                                       # REQUIRED in [path]
    sandbox: bool                                                                                  # OPTIONAL in [query]
    validate: bool                                                                                 # OPTIONAL in [query]

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
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "id_"):
            result["id"] = self.id_
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "sandbox"):
            result["sandbox"] = self.sandbox
        if hasattr(self, "validate"):
            result["validate"] = self.validate
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: StripeConfig) -> UpdateStripeConfig:
        self.body = value
        return self

    def with_id_(self, value: str) -> UpdateStripeConfig:
        self.id_ = value
        return self

    def with_sandbox(self, value: bool) -> UpdateStripeConfig:
        self.sandbox = value
        return self

    def with_validate(self, value: bool) -> UpdateStripeConfig:
        self.validate = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = StripeConfig()
        if hasattr(self, "id_") and self.id_:
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "sandbox") and self.sandbox:
            result["sandbox"] = bool(self.sandbox)
        elif include_empty:
            result["sandbox"] = bool()
        if hasattr(self, "validate") and self.validate:
            result["validate"] = bool(self.validate)
        elif include_empty:
            result["validate"] = bool()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, PaymentMerchantConfigInfo], Union[None, ErrorEntity, HttpResponse]]:
        """Parse the given response.

        200: OK - PaymentMerchantConfigInfo (successful operation)

        404: Not Found - ErrorEntity (33242: Payment merchant config [{id}] does not exist | 33221: Update [{paymentProvider}] config in payment merchant config [{id}] failed with message [{errMsg}])

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        pre_processed_response, error = self.pre_process_response(code=code, content_type=content_type, content=content)
        if error is not None:
            return None, None if error.is_no_content() else error
        code, content_type, content = pre_processed_response

        if code == 200:
            return PaymentMerchantConfigInfo.create_from_dict(content), None
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)

        return None, self.handle_undocumented_response(code=code, content_type=content_type, content=content)

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        id_: str,
        body: Optional[StripeConfig] = None,
        sandbox: Optional[bool] = None,
        validate: Optional[bool] = None,
    ) -> UpdateStripeConfig:
        instance = cls()
        instance.id_ = id_
        if body is not None:
            instance.body = body
        if sandbox is not None:
            instance.sandbox = sandbox
        if validate is not None:
            instance.validate = validate
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UpdateStripeConfig:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = StripeConfig.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = StripeConfig()
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "sandbox" in dict_ and dict_["sandbox"] is not None:
            instance.sandbox = bool(dict_["sandbox"])
        elif include_empty:
            instance.sandbox = bool()
        if "validate" in dict_ and dict_["validate"] is not None:
            instance.validate = bool(dict_["validate"])
        elif include_empty:
            instance.validate = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "id": "id_",
            "sandbox": "sandbox",
            "validate": "validate",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "body": False,
            "id": True,
            "sandbox": False,
            "validate": False,
        }

    # endregion static methods
