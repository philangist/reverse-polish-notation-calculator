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

    def run_calculator(self):
        literals = []
        for token in self._tokenize():
            if token not in OPERATORS:
                literals.append(float(token))
            else:
                expression = Expression(operator=token, literals=literals)
                value = expression.evaluate()
                literals = [value]

        return literals[0]

    @classmethod
    def calculate(cls, stream):
        calculcator = cls(stream)
        return calculcator.run_calculator()
