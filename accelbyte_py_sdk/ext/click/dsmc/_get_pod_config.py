import json
from typing import Optional

import click

from .._utils import login_as as login_as_internal
from ....api.dsmc import get_pod_config as get_pod_config_internal
from ....api.dsmc.models import ModelsPodConfigRecord
from ....api.dsmc.models import ResponseError


@click.command()
@click.argument("name", type=str)
@click.option("--namespace", type=str)
@click.option("--doc", type=bool)
@click.option("--login_as", type=click.Choice(["client", "user"], case_sensitive=False))
def get_pod_config(
        name: str,
        namespace: Optional[str] = None,
        doc: Optional[bool] = None,
        login_as: Optional[str] = None,
):
    login_as_internal(login_as)
    if doc:
        click.echo(get_pod_config_internal.__doc__)
    result, error = get_pod_config_internal(
        name=name,
        namespace=namespace,
    )
    if error:
        raise Exception(f"GetPodConfig failed: {str(error)}")
    click.echo("GetPodConfig success")