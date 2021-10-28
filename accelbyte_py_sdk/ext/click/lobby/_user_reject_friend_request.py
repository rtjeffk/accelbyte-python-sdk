import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.lobby import user_reject_friend_request as user_reject_friend_request_internal
from ....api.lobby.models import ModelUserRejectFriendRequest
from ....api.lobby.models import RestapiErrorResponseV1


@click.command()
@click.argument("body", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def user_reject_friend_request(
        body: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(user_reject_friend_request_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = ModelUserRejectFriendRequest.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = user_reject_friend_request_internal(
        body=body,
        namespace=namespace,
    )
    if error:
        raise Exception(f"userRejectFriendRequest failed: {str(error)}")
    click.echo("userRejectFriendRequest success")