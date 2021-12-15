# justice-dsm-controller-service (2.10.0)

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
from ....api.dsmc import list_session as list_session_internal
from ....api.dsmc.models import ModelsListSessionResponse
from ....api.dsmc.models import ResponseError


@click.command()
@click.option("--count", "count", type=int)
@click.option("--offset", "offset", type=int)
@click.option("--region", "region", type=str)
@click.option("--with_server", "with_server", type=bool)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def list_session(
        count: Optional[int] = None,
        offset: Optional[int] = None,
        region: Optional[str] = None,
        with_server: Optional[bool] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(list_session_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = list_session_internal(
        count=count,
        offset=offset,
        region=region,
        with_server=with_server,
        namespace=namespace,
    )
    if error:
        raise Exception(f"ListSession failed: {str(error)}")
    click.echo("ListSession success")
