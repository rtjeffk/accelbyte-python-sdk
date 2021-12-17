# justice-seasonpass-service (1.5.0)

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
from accelbyte_py_sdk.api.seasonpass import query_seasons as query_seasons_internal
from accelbyte_py_sdk.api.seasonpass.models import ErrorEntity
from accelbyte_py_sdk.api.seasonpass.models import ListSeasonInfoPagingSlicedResult


@click.command()
@click.option("--limit", "limit", type=int)
@click.option("--offset", "offset", type=int)
@click.option("--status", "status", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def query_seasons(
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        status: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(query_seasons_internal.__doc__)
        return
    login_as_internal(login_as)
    try:
        status_json = json.loads(status)
        status = [str(i0) for i0 in status_json]
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'status'. {str(e)}") from e
    _, error = query_seasons_internal(
        limit=limit,
        offset=offset,
        status=status,
        namespace=namespace,
    )
    if error:
        raise Exception(f"querySeasons failed: {str(error)}")
    click.echo("querySeasons success")
