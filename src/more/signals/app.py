from dectate import directive
import morepath

from .directives import ConnectSignalAction, DisconnectSignalAction


class App(morepath.App):

    connect = directive(ConnectSignalAction)
    disconnect = directive(DisconnectSignalAction)

    @property
    def signals(self):
        return self.config.signal_registry

    def signal(self, name, doc=None):
        return self.signals.signal(name, doc)
