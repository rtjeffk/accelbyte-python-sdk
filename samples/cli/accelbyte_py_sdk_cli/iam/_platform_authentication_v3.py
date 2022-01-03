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
from accelbyte_py_sdk.api.iam import platform_authentication_v3 as platform_authentication_v3_internal


@click.command()
@click.argument("platform_id", type=str)
@click.argument("state", type=str)
@click.option("--code", "code", type=str)
@click.option("--error", "error", type=str)
@click.option("--openid_assoc_handle", "openid_assoc_handle", type=str)
@click.option("--openid_claimed_id", "openid_claimed_id", type=str)
@click.option("--openid_identity", "openid_identity", type=str)
@click.option("--openid_mode", "openid_mode", type=str)
@click.option("--openid_ns", "openid_ns", type=str)
@click.option("--openid_op_endpoint", "openid_op_endpoint", type=str)
@click.option("--openid_response_nonce", "openid_response_nonce", type=str)
@click.option("--openid_return_to", "openid_return_to", type=str)
@click.option("--openid_sig", "openid_sig", type=str)
@click.option("--openid_signed", "openid_signed", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def platform_authentication_v3(
        platform_id: str,
        state: str,
        code: Optional[str] = None,
        error: Optional[str] = None,
        openid_assoc_handle: Optional[str] = None,
        openid_claimed_id: Optional[str] = None,
        openid_identity: Optional[str] = None,
        openid_mode: Optional[str] = None,
        openid_ns: Optional[str] = None,
        openid_op_endpoint: Optional[str] = None,
        openid_response_nonce: Optional[str] = None,
        openid_return_to: Optional[str] = None,
        openid_sig: Optional[str] = None,
        openid_signed: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(platform_authentication_v3_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = platform_authentication_v3_internal(
        platform_id=platform_id,
        state=state,
        code=code,
        error=error,
        openid_assoc_handle=openid_assoc_handle,
        openid_claimed_id=openid_claimed_id,
        openid_identity=openid_identity,
        openid_mode=openid_mode,
        openid_ns=openid_ns,
        openid_op_endpoint=openid_op_endpoint,
        openid_response_nonce=openid_response_nonce,
        openid_return_to=openid_return_to,
        openid_sig=openid_sig,
        openid_signed=openid_signed,
    )
    if error:
        raise Exception(f"PlatformAuthenticationV3 failed: {str(error)}")
    click.echo("PlatformAuthenticationV3 success")
