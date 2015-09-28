__author__ = 'ByteCommander'


class EventBaseClass(object):

    def __init__(self, event_type_):

        if not type(event_type_) == str:
            raise TypeError("Invalid event_type argument. String required!")
        self.__event_type = event_type_

    @property
    def event_type(self):
        return self.__event_type

