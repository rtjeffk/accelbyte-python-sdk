# justice-iam-service (4.10.0)

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
from accelbyte_py_sdk.api.iam import token_grant_v3 as token_grant_v3_internal
from accelbyte_py_sdk.api.iam.models import OauthmodelErrorResponse
from accelbyte_py_sdk.api.iam.models import OauthmodelTokenResponseV3


@click.command()
@click.argument("grant_type", type=str)
@click.option("--device_id", "device_id", type=str)
@click.option("--client_id", "client_id", type=str)
@click.option("--code", "code", type=str)
@click.option("--code_verifier", "code_verifier", type=str)
@click.option("--redirect_uri", "redirect_uri", type=str)
@click.option("--refresh_token", "refresh_token", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def token_grant_v3(
        grant_type: str,
        device_id: Optional[str] = None,
        client_id: Optional[str] = None,
        code: Optional[str] = None,
        code_verifier: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        refresh_token: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(token_grant_v3_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = token_grant_v3_internal(
        grant_type=grant_type,
        device_id=device_id,
        client_id=client_id,
        code=code,
        code_verifier=code_verifier,
        redirect_uri=redirect_uri,
        refresh_token=refresh_token,
    )
    if error:
        raise Exception(f"TokenGrantV3 failed: {str(error)}")
    click.echo("TokenGrantV3 success")