import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.cloudsave import get_player_public_record_handler_v1 as get_player_public_record_handler_v1_internal
from ....api.cloudsave.models import ModelsPlayerRecord
from ....api.cloudsave.models import ModelsResponseError


@click.command()
@click.argument("user_id", type=str)
@click.argument("key", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def get_player_public_record_handler_v1(
        user_id: str,
        key: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(get_player_public_record_handler_v1_internal.__doc__)
    result, error = get_player_public_record_handler_v1_internal(
        user_id=user_id,
        key=key,
        namespace=namespace,
    )
    if error:
        raise Exception(f"getPlayerPublicRecordHandlerV1 failed: {str(error)}")
    click.echo("getPlayerPublicRecordHandlerV1 success")