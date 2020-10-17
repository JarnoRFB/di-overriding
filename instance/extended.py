from dependency_injector import containers, providers

from .main import Component, Container, main


class AllCaps(Component):

    def __str__(self):
        return f"param={str(self.param).upper()}"


class AllCapsContainer(containers.DeclarativeContainer):
    config = providers.Configuration("config")
    component = providers.Factory(AllCaps, param=Container.config.param)


if __name__ == '__main__':
    container = Container()
    container.override(AllCapsContainer())
    main(container)()
