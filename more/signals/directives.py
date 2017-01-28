from uuid import uuid4

from blinker import Namespace
from dectate import Action


class SignalAction(Action):

    config = {
       'signal_registry': Namespace
    }

    def __init__(self, name):
        self.name = name

    def identifier(self, signal_registry):
        return (uuid4().hex, self.name)

    def perform(self, obj, signal_registry):
        pass  # pragma: no cover


class ConnectSignalAction(SignalAction):

    def perform(self, obj, signal_registry):
        signal_registry.signal(self.name).connect(obj)


class DisconnectSignalAction(SignalAction):

    def perform(self, obj, signal_registry):
        signal_registry.signal(self.name).disconnect(obj)
