import click
from dependency_injector import containers, providers


class Component:
    def __init__(self, param):
        if param is None:
            raise ValueError
        self.param = param

    def __str__(self):
        return f"param={self.param}"


class Container(containers.DeclarativeContainer):
    config = providers.Configuration("config")
    component = providers.Factory(Component, param=config.param)


@click.command()
@click.option("--param")
def cli(param):
    """Simple application that configures a component and prints it."""
    container = Container()
    # Configuration logic is here, because I want to reuse it and it
    # can be coupled with the cli.
    container.config.from_dict({"param": param})
    component = container.component()
    print(component)


if __name__ == '__main__':
    cli()
