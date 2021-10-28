import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.group import update_single_group_v1 as update_single_group_v1_internal
from ....api.group.models import ModelsGroupResponseV1
from ....api.group.models import ModelsUpdateGroupRequestV1
from ....api.group.models import ResponseErrorResponse


@click.command()
@click.argument("body", type=str)
@click.argument("group_id", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def update_single_group_v1(
        body: str,
        group_id: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(update_single_group_v1_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = ModelsUpdateGroupRequestV1.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = update_single_group_v1_internal(
        body=body,
        group_id=group_id,
        namespace=namespace,
    )
    if error:
        raise Exception(f"updateSingleGroupV1 failed: {str(error)}")
    click.echo("updateSingleGroupV1 success")