import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.lobby import get_user_incoming_friends as get_user_incoming_friends_internal
from ....api.lobby.models import ModelGetUserIncomingFriendsResponse
from ....api.lobby.models import RestapiErrorResponseV1


@click.command()
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def get_user_incoming_friends(
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(get_user_incoming_friends_internal.__doc__)
    result, error = get_user_incoming_friends_internal(
        namespace=namespace,
    )
    if error:
        raise Exception(f"getUserIncomingFriends failed: {str(error)}")
    click.echo("getUserIncomingFriends success")