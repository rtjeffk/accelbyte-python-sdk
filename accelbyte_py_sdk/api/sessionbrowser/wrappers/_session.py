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
from ....core import same_doc_as

from ..models import ModelsActiveCustomGameResponse
from ..models import ModelsActiveMatchmakingGameResponse
from ..models import ModelsAddPlayerRequest
from ..models import ModelsAddPlayerResponse
from ..models import ModelsAdminSessionResponse
from ..models import ModelsCountActiveSessionResponse
from ..models import ModelsCreateSessionRequest
from ..models import ModelsJoinGameSessionRequest
from ..models import ModelsRecentPlayerQueryResponse
from ..models import ModelsSessionByUserIDsResponse
from ..models import ModelsSessionQueryResponse
from ..models import ModelsSessionResponse
from ..models import ModelsUpdateSessionRequest
from ..models import ResponseError
from ..models import RestapiErrorResponseV2

from ..operations.session import AddPlayerToSession
from ..operations.session import AdminGetSession
from ..operations.session import CreateSession
from ..operations.session import DeleteSession
from ..operations.session import DeleteSessionLocalDS
from ..operations.session import GetActiveCustomGameSessions
from ..operations.session import GetActiveMatchmakingGameSessions
from ..operations.session import GetRecentPlayer
from ..operations.session import GetSession
from ..operations.session import GetSessionByUserIDs
from ..operations.session import GetTotalActiveSession
from ..operations.session import JoinSession
from ..operations.session import QuerySession
from ..operations.session import RemovePlayerFromSession
from ..operations.session import UpdateSession


@same_doc_as(AddPlayerToSession)
def add_player_to_session(body: ModelsAddPlayerRequest, session_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AddPlayerToSession.create(
        body=body,
        session_id=session_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminGetSession)
def admin_get_session(session_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminGetSession.create(
        session_id=session_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(CreateSession)
def create_session(body: ModelsCreateSessionRequest, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateSession.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteSession)
def delete_session(session_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteSession.create(
        session_id=session_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteSessionLocalDS)
def delete_session_local_ds(session_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteSessionLocalDS.create(
        session_id=session_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetActiveCustomGameSessions)
def get_active_custom_game_sessions(session_id: Optional[str] = None, server_region: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetActiveCustomGameSessions.create(
        session_id=session_id,
        server_region=server_region,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetActiveMatchmakingGameSessions)
def get_active_matchmaking_game_sessions(session_id: Optional[str] = None, match_id: Optional[str] = None, server_region: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetActiveMatchmakingGameSessions.create(
        session_id=session_id,
        match_id=match_id,
        server_region=server_region,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetRecentPlayer)
def get_recent_player(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetRecentPlayer.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetSession)
def get_session(session_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetSession.create(
        session_id=session_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetSessionByUserIDs)
def get_session_by_user_i_ds(user_ids: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetSessionByUserIDs.create(
        user_ids=user_ids,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetTotalActiveSession)
def get_total_active_session(session_type: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetTotalActiveSession.create(
        session_type=session_type,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(JoinSession)
def join_session(body: ModelsJoinGameSessionRequest, session_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = JoinSession.create(
        body=body,
        session_id=session_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(QuerySession)
def query_session(session_type: str, user_id: Optional[str] = None, game_mode: Optional[str] = None, game_version: Optional[str] = None, joinable: Optional[str] = None, match_id: Optional[str] = None, match_exist: Optional[str] = None, server_status: Optional[str] = None, offset: Optional[str] = None, limit: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = QuerySession.create(
        session_type=session_type,
        user_id=user_id,
        game_mode=game_mode,
        game_version=game_version,
        joinable=joinable,
        match_id=match_id,
        match_exist=match_exist,
        server_status=server_status,
        offset=offset,
        limit=limit,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(RemovePlayerFromSession)
def remove_player_from_session(session_id: str, user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = RemovePlayerFromSession.create(
        session_id=session_id,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateSession)
def update_session(body: ModelsUpdateSessionRequest, session_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateSession.create(
        body=body,
        session_id=session_id,
        namespace=namespace,
    )
    return run_request(request)