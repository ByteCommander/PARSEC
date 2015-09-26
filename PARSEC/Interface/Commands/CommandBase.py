__author__ = 'ByteCommander'
from PARSEC.Interface import _default_implementation
from PARSEC.Interface.Events import EventBase
from PARSEC.Interface.Commands import CommandAPI


class CommandBaseClass(object):

    def on_event(self, event, parsec_interface):
        _default_implementation(self, "on_event")


class CommandBaseClassWithEventSwitch(CommandBaseClass):

    def on_event(self, event, parsec_interface):
        if not issubclass(type(event), EventBase.EventBaseClass):
            raise TypeError("'on_event' requires as 'event' argument an instance of a subclass of "
                            "'PARSEC.Interface.Events.EventBase.EventBaseClass'!")
        if not isinstance(type(parsec_interface), CommandAPI.ParsecInterface):
            raise TypeError("'on_event' requires as 'parsec_interface' argument an instance of "
                            "'PARSEC.Interface.Commands.CommandAPI.ParsecInterface'!")

        return (getattr(self, "on_{s}_event".format(event.event_type.lower()), self.on_default_event)
                )(self, event, parsec_interface)

    def on_default_event(self, event, parsec_interface):
        _default_implementation(self, "on_default_event")

    def on_message_event(self, event, parsec_interface):
        _default_implementation(self, "on_message_event")

    def on_ping_event(self, event, parsec_interface):
        _default_implementation(self, "on_ping_event")

    def on_reply_event(self, event, parsec_interface):
        _default_implementation(self, "on_reply_event")

    def on_command_event(self, event, parsec_interface):
        _default_implementation(self, "on_command_event")

    def on_room_event(self, event, parsec_interface):
        _default_implementation(self, "on_room_event")

    def on_user_event(self, event, parsec_interface):
        _default_implementation(self, "on_user_event")
