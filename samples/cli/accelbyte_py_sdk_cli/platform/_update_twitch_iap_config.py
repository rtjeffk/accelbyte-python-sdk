# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template_file: python-cli-command.j2

# justice-platform-service (4.7.0)

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
import yaml
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from .._utils import to_dict
from accelbyte_py_sdk.api.platform import update_twitch_iap_config as update_twitch_iap_config_internal
from accelbyte_py_sdk.api.platform.models import TwitchIAPConfigInfo
from accelbyte_py_sdk.api.platform.models import TwitchIAPConfigRequest


@click.command()
@click.option("--body", "body", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--login_with_auth", type=str)
@click.option("--doc", type=bool)
def update_twitch_iap_config(
        body: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        login_with_auth: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(update_twitch_iap_config_internal.__doc__)
        return
    x_additional_headers = None
    if login_with_auth:
        x_additional_headers = {
            "Authorization": login_with_auth
        }
    else:
        login_as_internal(login_as)
    if body is not None:
        try:
            body_json = json.loads(body)
            body = TwitchIAPConfigRequest.create_from_dict(body_json)
        except ValueError as e:
            raise Exception(f"Invalid JSON for 'body'. {str(e)}") from e
    result, error = update_twitch_iap_config_internal(
        body=body,
        namespace=namespace,
        x_additional_headers=x_additional_headers,
    )
    if error:
        raise Exception(f"updateTwitchIAPConfig failed: {str(error)}")
    click.echo(yaml.safe_dump(to_dict(result), sort_keys=False))


update_twitch_iap_config.operation_id = "updateTwitchIAPConfig"
update_twitch_iap_config.is_deprecated = False
