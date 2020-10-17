from dependency_injector import containers, providers

from .main import Component, Container, cli


class AllCaps(Component):

    def __str__(self):
        return f"param={str(self.param).upper()}"


@containers.override(Container)
class AllCapsContainer(containers.DeclarativeContainer):
    component = providers.Factory(AllCaps, param=Container.config.param)


if __name__ == '__main__':
    cli()
