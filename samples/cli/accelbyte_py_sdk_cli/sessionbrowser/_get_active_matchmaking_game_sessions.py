# justice-session-browser-service ()

# Copyright (c) 2018 - 2022 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# template_file: python-cli-command.j2

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

import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from accelbyte_py_sdk.api.sessionbrowser import get_active_matchmaking_game_sessions as get_active_matchmaking_game_sessions_internal
from accelbyte_py_sdk.api.sessionbrowser.models import ModelsActiveMatchmakingGameResponse
from accelbyte_py_sdk.api.sessionbrowser.models import RestapiErrorResponseV2


@click.command()
@click.option("--match_id", "match_id", type=str)
@click.option("--server_region", "server_region", type=str)
@click.option("--session_id", "session_id", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def get_active_matchmaking_game_sessions(
        match_id: Optional[str] = None,
        server_region: Optional[str] = None,
        session_id: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(get_active_matchmaking_game_sessions_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = get_active_matchmaking_game_sessions_internal(
        match_id=match_id,
        server_region=server_region,
        session_id=session_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"GetActiveMatchmakingGameSessions failed: {str(error)}")
    click.echo("GetActiveMatchmakingGameSessions success")