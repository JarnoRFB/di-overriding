from dependency_injector import containers, providers

from . import components


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    component = providers.Selector(
        config.type,
        standard=providers.Factory(
            components.Component,
            param=config.param,
        ),
        all_caps=providers.Factory(
            components.AllCaps,
            param=config.param,
        ),
    )
