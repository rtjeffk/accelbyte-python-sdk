# Analytics Game Telemetry (0.0.1)

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
from accelbyte_py_sdk.api.gametelemetry import protected_save_events_game_telemetry_v1_protected_events_post as protected_save_events_game_telemetry_v1_protected_events_post_internal
from accelbyte_py_sdk.api.gametelemetry.models import HTTPValidationError
from accelbyte_py_sdk.api.gametelemetry.models import TelemetryBody


@click.command()
@click.argument("body", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def protected_save_events_game_telemetry_v1_protected_events_post(
        body: str,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(protected_save_events_game_telemetry_v1_protected_events_post_internal.__doc__)
        return
    login_as_internal(login_as)
    try:
        body_json = json.loads(body)
        body = [TelemetryBody.create_from_dict(i0) for i0 in body_json]
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}") from e
    _, error = protected_save_events_game_telemetry_v1_protected_events_post_internal(
        body=body,
    )
    if error:
        raise Exception(f"protected_save_events_game_telemetry_v1_protected_events_post failed: {str(error)}")
    click.echo("protected_save_events_game_telemetry_v1_protected_events_post success")
