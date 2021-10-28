import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.social import bulk_create_user_stat_items as bulk_create_user_stat_items_internal
from ....api.social.models import BulkStatItemCreate
from ....api.social.models import BulkStatItemOperationResult
from ....api.social.models import ValidationErrorEntity


@click.command()
@click.argument("user_id", type=str)
@click.option("--body", "body", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def bulk_create_user_stat_items(
        user_id: str,
        body: Optional[str] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(bulk_create_user_stat_items_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = [BulkStatItemCreate.create_from_dict(i0) for i0 in body_json]
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = bulk_create_user_stat_items_internal(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    if error:
        raise Exception(f"bulkCreateUserStatItems failed: {str(error)}")
    click.echo("bulkCreateUserStatItems success")