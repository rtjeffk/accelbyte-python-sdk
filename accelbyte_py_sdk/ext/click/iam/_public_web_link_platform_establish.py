# justice-iam-service (4.7.0)

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
from ....api.iam import public_web_link_platform_establish as public_web_link_platform_establish_internal


@click.command()
@click.argument("platform_id", type=str)
@click.argument("state", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def public_web_link_platform_establish(
        platform_id: str,
        state: str,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(public_web_link_platform_establish_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = public_web_link_platform_establish_internal(
        platform_id=platform_id,
        state=state,
        namespace=namespace,
    )
    if error:
        raise Exception(f"PublicWebLinkPlatformEstablish failed: {str(error)}")
    click.echo("PublicWebLinkPlatformEstablish success")
