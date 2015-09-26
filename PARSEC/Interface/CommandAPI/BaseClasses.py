__author__ = 'ByteCommander'


def _default_implementation(instance, method_name):
    raise NotImplementedError("Function '{s}' not implemented by class '{s}.{s}' derived from {s}!".format(
        method_name, instance.__class__.__module__, instance.__class__.__name__, instance.__class__.__base__.__name__
    ))


class CommandClassBase(object):

    def on_event(self, event, parsec_interface):
        _default_implementation(self, "on_event")

