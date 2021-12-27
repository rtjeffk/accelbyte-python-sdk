# justice-iam-service (4.9.0)

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

from ...models import ModelUpdatePermissionScheduleRequest


class AddUserPermission(Operation):
    """Add User Permission (AddUserPermission)

    <p>Required permission 'ADMIN:NAMESPACE:{namespace}:PERMISSION:USER:{userId}
    [UPDATE]'</p> <p>This endpoint will update existing permission (bitwise OR the
    action) if found one with same resource, otherwise it will append a new
    permission</p> <p>Schedule contains cron string or date range (both are UTC,
    also in cron syntax) to indicate when a permission and action are in
    effect.</p> <p>Both schedule types accepts quartz compatible cron syntax e.g.
    * * * * * * *.</p> <p>In ranged schedule, first element will be start date,
    and second one will be end date</p> <p>If schedule is set, the scheduled
    action must be valid too, that is between 1 to 15, inclusive</p> <p>Syntax
    reference</p> <p>Fields:</p> <ol> <li>Seconds: 0-59 * / , -</li> <li>Minutes:
    0-59 * / , -</li> <li>Hours: 0-23 * / , -</li> <li>Day of month: 1-31 * / , -
    L W</li> <li>Month: 1-12 JAN-DEC * / , -</li> <li>Day of week: 0-6 SUN-SAT * /
    , - L #</li> <li>Year: 1970-2099 * / , -</li> </ol> <p>Special characters:</p>
    <ol> <li>*: all values in the fields, e.g. * in seconds fields indicates every
    second</li> <li>/: increments of ranges, e.g. 3-59/15 in the minute field
    indicate the third minute of the hour and every 15 minutes thereafter</li>
    <li>,: separate items of a list, e.g. MON,WED,FRI in day of week</li> <li>-:
    range, e.g. 2010-2018 indicates every year between 2010 and 2018,
    inclusive</li> <li>L: last, e.g. When used in the day-of-week field, it allows
    you to specify constructs such as "the last Friday" (5L) of a given month. In
    the day-of-month field, it specifies the last day of the month.</li> <li>W:
    business day, e.g. if you were to specify 15W as the value for the day-of-
    month field, the meaning is: "the nearest business day to the 15th of the
    month."</li> <li>#: must be followed by a number between one and five. It
    allows you to specify constructs such as "the second Friday" of a given
    month.</li> </ol>


    Properties:
        url: /iam/namespaces/{namespace}/users/{userId}/permissions/{resource}/{action}

        method: POST

        tags: ["Users"]

        consumes: ["application/json"]

        produces: ["application/json"]

        security_type: bearer

        body: (body) REQUIRED ModelUpdatePermissionScheduleRequest in body

        action: (action) REQUIRED int in path

        namespace: (namespace) REQUIRED str in path

        resource: (resource) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

    Responses:
        204: No Content - (Operation succeeded)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)
    """

    # region fields

    _url: str = "/iam/namespaces/{namespace}/users/{userId}/permissions/{resource}/{action}"
    _method: str = "POST"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security_type: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelUpdatePermissionScheduleRequest                                                     # REQUIRED in [body]
    action: int                                                                                    # REQUIRED in [path]
    namespace: str                                                                                 # REQUIRED in [path]
    resource: str                                                                                  # REQUIRED in [path]
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
            "body",
            "action",
            "namespace",
            "resource",
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
        if hasattr(self, "action"):
            result["action"] = self.action
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "resource"):
            result["resource"] = self.resource
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "action") or self.action is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "resource") or self.resource is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelUpdatePermissionScheduleRequest) -> AddUserPermission:
        self.body = value
        return self

    def with_action(self, value: int) -> AddUserPermission:
        self.action = value
        return self

    def with_namespace(self, value: str) -> AddUserPermission:
        self.namespace = value
        return self

    def with_resource(self, value: str) -> AddUserPermission:
        self.resource = value
        return self

    def with_user_id(self, value: str) -> AddUserPermission:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelUpdatePermissionScheduleRequest()
        if hasattr(self, "action") and self.action:
            result["action"] = int(self.action)
        elif include_empty:
            result["action"] = int()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "resource") and self.resource:
            result["resource"] = str(self.resource)
        elif include_empty:
            result["resource"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        204: No Content - (Operation succeeded)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)
        """
        if code == 204:
            return HttpResponse.create(code, "No Content"), None
        if code == 400:
            return None, HttpResponse.create(code, "Bad Request")
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
        if code == 404:
            return None, HttpResponse.create(code, "Not Found")
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: ModelUpdatePermissionScheduleRequest,
        action: int,
        namespace: str,
        resource: str,
        user_id: str,
    ) -> AddUserPermission:
        instance = cls()
        instance.body = body
        instance.action = action
        instance.namespace = namespace
        instance.resource = resource
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AddUserPermission:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelUpdatePermissionScheduleRequest.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelUpdatePermissionScheduleRequest()
        if "action" in dict_ and dict_["action"] is not None:
            instance.action = int(dict_["action"])
        elif include_empty:
            instance.action = int()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "resource" in dict_ and dict_["resource"] is not None:
            instance.resource = str(dict_["resource"])
        elif include_empty:
            instance.resource = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "action": "action",
            "namespace": "namespace",
            "resource": "resource",
            "userId": "user_id",
        }

    # endregion static methods
