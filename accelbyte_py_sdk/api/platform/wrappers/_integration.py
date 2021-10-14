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

from ..models import ErrorEntity
from ..models import GameServerConfig

from ..operations.integration import GetGameServerConfig
from ..operations.integration import UpdateGameServerConfig


@same_doc_as(GetGameServerConfig)
def get_game_server_config(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGameServerConfig.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateGameServerConfig)
def update_game_server_config(body: Optional[GameServerConfig] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateGameServerConfig.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)