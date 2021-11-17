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
from ....core import same_doc_as

from ..models import ModelsListTerminatedServersResponse
from ..models import ResponseError

from ..operations.terminated_servers import ListTerminatedServers


@same_doc_as(ListTerminatedServers)
def list_terminated_servers(deployment: Optional[str] = None, game_mode: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, party_id: Optional[str] = None, pod_name: Optional[str] = None, provider: Optional[str] = None, region: Optional[str] = None, session_id: Optional[str] = None, user_id: Optional[str] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListTerminatedServers.create(
        deployment=deployment,
        game_mode=game_mode,
        limit=limit,
        offset=offset,
        party_id=party_id,
        pod_name=pod_name,
        provider=provider,
        region=region,
        session_id=session_id,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request, additional_headers=x_additional_headers)


@same_doc_as(ListTerminatedServers)
async def list_terminated_servers_async(deployment: Optional[str] = None, game_mode: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, party_id: Optional[str] = None, pod_name: Optional[str] = None, provider: Optional[str] = None, region: Optional[str] = None, session_id: Optional[str] = None, user_id: Optional[str] = None, namespace: Optional[str] = None, x_additional_headers: Optional[Dict[str, str]] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListTerminatedServers.create(
        deployment=deployment,
        game_mode=game_mode,
        limit=limit,
        offset=offset,
        party_id=party_id,
        pod_name=pod_name,
        provider=provider,
        region=region,
        session_id=session_id,
        user_id=user_id,
        namespace=namespace,
    )
    return await run_request_async(request, additional_headers=x_additional_headers)