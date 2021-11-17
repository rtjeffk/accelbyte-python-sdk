# justice-ugc-service (1.9.0)

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
from ....api.ugc import download_content_by_share_code as download_content_by_share_code_internal
from ....api.ugc.models import ModelsContentDownloadResponse
from ....api.ugc.models import ResponseError


@click.command()
@click.argument("share_code", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def download_content_by_share_code(
        share_code: str,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(download_content_by_share_code_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = download_content_by_share_code_internal(
        share_code=share_code,
        namespace=namespace,
    )
    if error:
        raise Exception(f"DownloadContentByShareCode failed: {str(error)}")
    click.echo("DownloadContentByShareCode success")