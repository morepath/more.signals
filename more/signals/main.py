from dectate import directive
import morepath

from .directives import (
    ConnectSignalAction,
    DisconnectSignalAction
)


class SignalApp(morepath.App):

    connect = directive(ConnectSignalAction)
    disconnect = directive(DisconnectSignalAction)

    @property
    def signals(self):
        return self.config.signal_registry

    def signal(self, event):
        return self.signals.signal(event)
