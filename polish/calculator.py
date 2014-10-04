import operator

from stack import Stack

ADD = "+"
SUBTRACT = "-"
MULTIPLY = "*"
DIVIDE = "/"
MODULO = "%"

OPERATORS = {
    ADD: operator.add,
    SUBTRACT: operator.sub,
    MULTIPLY: operator.mul,
    DIVIDE: operator.div,
    MODULO: operator.mod,
}


class Expression(object):

    def __init__(self, operator, literals=[]):
        if operator not in OPERATORS:
            raise ValueError(
                'Attempted to create an invalid expression with operator %s',
                operator)

        if not isinstance(literals, list):
            raise TypeError(
                'Attempted to create an invalid expression with literals %s',
                literals)

        self.operator = operator
        self.literals = literals

    def evaluate(self):
        return reduce(OPERATORS[self.operator], self.literals)


class Calculator(object):
    def __init__(self, stream):
        if not isinstance(stream, basestring):
            raise TypeError(
                "Reverse Polish Notation Calculcator only takes "
                "strings as input"
            )

        self.stream = stream
        self.stack = Stack()

    def _tokenize(self):
        return self.stream.split()

    def _read_stack_literals(self):
        literals = []
        next_value = self.stack.peek()
        while next_value:
            if (next_value is None) or next_value in OPERATORS:
                break
            literals.append(self.stack.pop())
            next_value = self.stack.peek()

        # Stack output is LIFO but to preserve order of operations we want FIFO
        literals.reverse()
        return literals

    def run_calculator(self):
        for token in self._tokenize():
            if token not in OPERATORS:
                self.stack.push(float(token))
            else:
                literals = self._read_stack_literals()
                expression = Expression(operator=token, literals=literals)
                value = expression.evaluate()
                self.stack.push(value)

        return self.stack.pop()

    @classmethod
    def calculate(cls, stream):
        calculcator = cls(stream)
        return calculcator.run_calculator()
