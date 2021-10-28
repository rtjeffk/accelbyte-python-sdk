import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.social import public_create_user_namespace_slot as public_create_user_namespace_slot_internal
from ....api.social.models import ErrorEntity


@click.command()
@click.argument("user_id", type=str)
@click.option("--custom_attribute", "custom_attribute", type=str)
@click.option("--checksum", "checksum", type=str)
@click.option("--file", "file", type=str)
@click.option("--label", "label", type=str)
@click.option("--tags", "tags", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def public_create_user_namespace_slot(
        user_id: str,
        custom_attribute: Optional[str] = None,
        checksum: Optional[str] = None,
        file: Optional[str] = None,
        label: Optional[str] = None,
        tags: Optional[str] = None,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(public_create_user_namespace_slot_internal.__doc__)
    try:
        file_json = json.loads(file)
        file = Any.create_from_dict(file_json)
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'file'. {str(e)}")
    try:
        tags_json = json.loads(tags)
        tags = [str.create_from_dict(i0) for i0 in tags_json]
    except ValueError as e:
        raise Exception(f"Invalid JSON for 'tags'. {str(e)}")
    result, error = public_create_user_namespace_slot_internal(
        user_id=user_id,
        custom_attribute=custom_attribute,
        checksum=checksum,
        file=file,
        label=label,
        tags=tags,
        namespace=namespace,
    )
    if error:
        raise Exception(f"publicCreateUserNamespaceSlot failed: {str(error)}")
    click.echo("publicCreateUserNamespaceSlot success")