from ast import BinaryExpr as BE, UnaryExpr as UE
from tokenizer import TokenType, tokenize


class EvaluateError(Exception):
    pass


def evaluate(expr) -> float:
    if type(expr) is float:
        return expr

    elif type(expr) is BE:
        lh = evaluate(expr.lh)
        rh = evaluate(expr.rh)
        op = expr.op.type

        if op is TokenType.PLUS:
            return lh + rh
        elif op is TokenType.MINUS:
            return lh - rh
        elif op is TokenType.MUL:
            return lh * rh
        elif op is TokenType.DIV:
            if rh == 0:
                raise EvaluateError('Must not divide by 0!')
            else:
                return lh / rh

        else:
            raise EvaluateError(f'Unknown binary operator {op}')

    elif type(expr) is UE:
        rh = evaluate(expr.rh)
        op = expr.op.type
        if op is TokenType.MINUS:
            return - rh
        else:
            raise EvaluateError(f'Unknown unary operator {op}')  #internal error (should never happen)


# TESTS #

from parser import parse
import unittest


class Tests(unittest.TestCase):

    def test_adding_numbers(self):
        input = parse(tokenize('3 + 45 + 8'))
        expected = 56.0
        self.assertEqual(expected, evaluate(input))

    def test_dividing_by_0(self):
        input = parse(tokenize('12/0'))
        self.assertRaises(EvaluateError, evaluate, input)

    def test_complex_dividing_by_0(self):
        input = parse(tokenize('12 / (6 - 6)'))
        self.assertRaises(EvaluateError, evaluate, input)

