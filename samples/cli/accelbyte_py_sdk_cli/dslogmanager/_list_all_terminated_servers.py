# justice-ds-log-manager-service (1.4.0)

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

import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from accelbyte_py_sdk.api.dslogmanager import list_all_terminated_servers as list_all_terminated_servers_internal
from accelbyte_py_sdk.api.dslogmanager.models import ModelsListTerminatedServersResponse
from accelbyte_py_sdk.api.dslogmanager.models import ResponseError


@click.command()
@click.option("--deployment", "deployment", type=str)
@click.option("--game_mode", "game_mode", type=str)
@click.option("--limit", "limit", type=int)
@click.option("--offset", "offset", type=int)
@click.option("--party_id", "party_id", type=str)
@click.option("--pod_name", "pod_name", type=str)
@click.option("--provider", "provider", type=str)
@click.option("--region", "region", type=str)
@click.option("--session_id", "session_id", type=str)
@click.option("--user_id", "user_id", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def list_all_terminated_servers(
        deployment: Optional[str] = None,
        game_mode: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        party_id: Optional[str] = None,
        pod_name: Optional[str] = None,
        provider: Optional[str] = None,
        region: Optional[str] = None,
        session_id: Optional[str] = None,
        user_id: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(list_all_terminated_servers_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = list_all_terminated_servers_internal(
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
    if error:
        raise Exception(f"listAllTerminatedServers failed: {str(error)}")
    click.echo("listAllTerminatedServers success")
