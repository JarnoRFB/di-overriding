import click

from .containers import Container


@click.command()
@click.option("--param")
@click.pass_context
def cli(ctx, param):
    """Simple application that configures a component and prints it."""
    container = Container(config={"type": ctx.obj["type"], "param": param})
    component = container.component()
    print(component)
