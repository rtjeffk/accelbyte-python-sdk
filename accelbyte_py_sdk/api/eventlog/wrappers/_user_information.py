# template file: justice_py_sdk_codegen/__main__.py

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
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

from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import get_namespace as get_services_namespace
from ....core import run_request
from ....core import run_request_async
from ....core import deprecated
from ....core import same_doc_as

from ..models import ModelsEventResponse
from ..models import ModelsUserLastActivity

from ..operations.user_information import DeleteUserActivitiesHandler
from ..operations.user_information import GetUserActivitiesHandler
from ..operations.user_information import LastUserActivityTimeHandler


@deprecated
@same_doc_as(DeleteUserActivitiesHandler)
def delete_user_activities_handler(user_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteUserActivitiesHandler.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers)


@deprecated
@same_doc_as(DeleteUserActivitiesHandler)
async def delete_user_activities_handler_async(user_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteUserActivitiesHandler.create(
        user_id=user_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers)


@deprecated
@same_doc_as(GetUserActivitiesHandler)
def get_user_activities_handler(page_size: float, user_id: str, offset: Optional[float] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetUserActivitiesHandler.create(
        page_size=page_size,
        user_id=user_id,
        offset=offset,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers)


@deprecated
@same_doc_as(GetUserActivitiesHandler)
async def get_user_activities_handler_async(page_size: float, user_id: str, offset: Optional[float] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetUserActivitiesHandler.create(
        page_size=page_size,
        user_id=user_id,
        offset=offset,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers)


@deprecated
@same_doc_as(LastUserActivityTimeHandler)
def last_user_activity_time_handler(user_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = LastUserActivityTimeHandler.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers)


@deprecated
@same_doc_as(LastUserActivityTimeHandler)
async def last_user_activity_time_handler_async(user_id: str, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = LastUserActivityTimeHandler.create(
        user_id=user_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers)
