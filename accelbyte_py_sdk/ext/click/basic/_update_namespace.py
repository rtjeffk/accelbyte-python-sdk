import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.basic import update_namespace as update_namespace_internal
from ....api.basic.models import ErrorEntity
from ....api.basic.models import NamespaceInfo
from ....api.basic.models import NamespaceUpdate
from ....api.basic.models import ValidationErrorEntity


@click.command()
@click.option("--body", "body", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def update_namespace(
        body: Optional[str] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(update_namespace_internal.__doc__)
    try:
        body_json = json.loads(body)
        body = NamespaceUpdate.create_from_dict(body_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'body'. {str(e)}")
    result, error = update_namespace_internal(
        body=body,
        namespace=namespace,
    )
    if error:
        raise Exception(f"updateNamespace failed: {str(error)}")
    click.echo("updateNamespace success")