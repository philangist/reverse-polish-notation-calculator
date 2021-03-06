import logging

log = logging.getLogger(__name__)


class Stack(object):
    def __init__(self):
        self.values = []

    def push(self, val):
        if not val:
            return
        self.values.append(val)

    def pop(self):
        try:
            return self.values.pop(-1)
        except IndexError:
            log.exception('Could not pop value from stack')
            return None

    def peek(self):
        value = self.pop()
        if value is not None:
            self.push(value)
        return value
