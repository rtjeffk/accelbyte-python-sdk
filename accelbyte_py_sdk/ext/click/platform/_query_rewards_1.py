# justice-platform-service (3.37.1)

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
from ....api.platform import query_rewards_1 as query_rewards_1_internal
from ....api.platform.models import RewardPagingSlicedResult
from ....api.platform.models import ValidationErrorEntity


@click.command()
@click.option("--event_topic", "event_topic", type=str)
@click.option("--limit", "limit", type=int)
@click.option("--offset", "offset", type=int)
@click.option("--sort_by", "sort_by", type=str)
@click.option("--namespace", type=str)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
@click.option("--doc", type=bool)
def query_rewards_1(
        event_topic: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort_by: Optional[str] = None,
        namespace: Optional[str] = None,
        login_as: Optional[str] = None,
        doc: Optional[bool] = None,
):
    if doc:
        click.echo(query_rewards_1_internal.__doc__)
        return
    login_as_internal(login_as)
    _, error = query_rewards_1_internal(
        event_topic=event_topic,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        namespace=namespace,
    )
    if error:
        raise Exception(f"queryRewards_1 failed: {str(error)}")
    click.echo("queryRewards_1 success")
