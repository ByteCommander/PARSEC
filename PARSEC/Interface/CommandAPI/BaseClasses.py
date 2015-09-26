__author__ = 'ByteCommander'
from PARSEC.Interface import _default_implementation


class CommandClassBase(object):

    def on_event(self, event, parsec_interface):
        _default_implementation(self, "on_event")


