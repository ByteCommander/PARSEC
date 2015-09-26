__author__ = 'ByteCommander'
from .. import _not_implemented
from . import CommandAPI
from ..Events import EventBase


class CommandBaseClass(object):
    """
    All methods this class provides can and will be called by PARSEC if you load any subclass of it as command module.

    You MUST override 'on_event(self, event, parsec_interface)' in your subclass, as this method raises a
    'NotImplementedError' by default.

    To add more functionality to your command you CAN override the other functions, which just are implemented
    with a 'pass' statement by default.
    """

    def on_event(self, event, parsec_interface):
        _not_implemented(self, "on_event")

    def on_enter(self, parsec_interface):
        pass

    def on_leave(self, parsec_interface):
        pass


class CommandBaseClassWithEventSwitch(CommandBaseClass):
    """
    This class overrides 'CommandBaseClass's 'on_event(...)' method to filter invalid argument types and split the
    requests up to the methods 'on_message_event(...)', 'on_ping_event(...)', 'on_reply_event(...)',
    'on_command_event(...)', 'on_room_event(...)', 'on_user_event(...)' and 'on_default_event(...)', which
    handles everything else.

    You should NOT override 'on_event(...)' any more, but ALL 'on_XXX_event(...)' methods, which raise a
    'NotImplementedException' by default. If you don't want to implement all different specialised handlers,
    you may add some event types (as string) to the 'default_events' attribute, which is a list.
    All events contained there and all with unknown 'event_type' attribute will be handled by the
    'on_default_event(...)' handler then.
    """

    def __init__(self):
        self.default_events = []

    def on_event(self, event, parsec_interface):
        if not issubclass(type(event), EventBase.EventBaseClass):
            raise TypeError("'on_event' requires as 'event' argument an instance of a subclass of "
                            "'PARSEC.Interface.Events.EventBase.EventBaseClass'!")
        if not isinstance(type(parsec_interface), CommandAPI.ParsecInterface):
            raise TypeError("'on_event' requires as 'parsec_interface' argument an instance of "
                            "'PARSEC.Interface.Commands.CommandAPI.ParsecInterface'!")

        if event.event_type in self.default_events:
            return self.on_default_event(event, parsec_interface)
        else:
            return (getattr(self, "on_{s}_event".format(event.event_type.lower()), self.on_default_event)
                    )(self, event, parsec_interface)

    def on_default_event(self, event, parsec_interface):
        _not_implemented(self, "on_default_event")

    def on_message_event(self, event, parsec_interface):
        _not_implemented(self, "on_message_event")

    def on_ping_event(self, event, parsec_interface):
        _not_implemented(self, "on_ping_event")

    def on_reply_event(self, event, parsec_interface):
        _not_implemented(self, "on_reply_event")

    def on_command_event(self, event, parsec_interface):
        _not_implemented(self, "on_command_event")

    def on_room_event(self, event, parsec_interface):
        _not_implemented(self, "on_room_event")

    def on_user_event(self, event, parsec_interface):
        _not_implemented(self, "on_user_event")
