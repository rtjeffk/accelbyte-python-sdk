# justice-platform-service (3.40.0)

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
from accelbyte_py_sdk.api.platform import query_codes as query_codes_internal
from accelbyte_py_sdk.api.platform.models import CodeInfoPagingSlicedResult


@click.command()
@click.argument("campaign_id", type=str)
@click.option("--active_only", "active_only", type=bool)
@click.option("--batch_no", "batch_no", type=int)
@click.option("--code", "code", type=str)
@click.option("--limit", "limit", type=int)
@click.option("--offset", "offset", type=int)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def query_codes(
        campaign_id: str,
        active_only: Optional[bool] = None,
        batch_no: Optional[int] = None,
        code: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(query_codes_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = query_codes_internal(
        campaign_id=campaign_id,
        active_only=active_only,
        batch_no=batch_no,
        code=code,
        limit=limit,
        offset=offset,
        namespace=namespace,
    )
    if error:
        raise Exception(f"queryCodes failed: {str(error)}")
    click.echo("queryCodes success")