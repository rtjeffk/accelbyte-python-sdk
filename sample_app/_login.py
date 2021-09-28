import click

from accelbyte_py_sdk.services.auth import login as acb_login


@click.command()
@click.argument("username")
@click.argument("password")
@click.option("--doc", type=bool)
def login(
        username,
        password,
        doc,
):
    if doc:
        click.echo(acb_login.__doc__)
    result, error = acb_login(
        username=username,
        password=password,
    )
    if error:
        raise Exception(str(error))
    click.echo("Login success.")