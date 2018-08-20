from tokenizer import TokenType, Token
from ast import BinaryExpr as BE, UnaryExpr as UE


class ParseError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def expr(self):
        return self.add()

    def add(self):
        result = self.mul()
        while self.current_token().type == TokenType.PLUS or self.current_token().type == TokenType.MINUS:
            op = self.advance()
            rh = self.mul()
            result = BE(result, op, rh)
        return result

    def mul(self):
        result = self.unary()
        while self.current_token().type == TokenType.MUL or self.current_token().type == TokenType.DIV:
            op = self.advance()
            rh = self.unary()
            result = BE(result, op, rh)
        return result

    def unary(self):
        if self.current_token().type == TokenType.MINUS:
            op = self.advance()
            rh = self.num()
            return UE(op, rh)
        else:
            return self.num()

    def num(self):
        if self.current_token().type == TokenType.NUM:  #is a number
            return float(self.advance().value)

        else:
            self.consume(TokenType.LPAR, 'Expect ( or number.') #is a LPAR or error when something else
            return self.paren()

    def paren(self):
        expr = self.expr()
        self.consume(TokenType.RPAR, 'Expect ).')
        return expr

    def consume(self, expected: TokenType, msg: str):
        if self.current_token().type == expected:
            self.position += 1
        else:
            raise ParseError(msg)

    def current_token(self) -> Token:
        return self.tokens[self.position]

    def advance(self):
        current_token = self.current_token()
        self.position += 1
        return current_token


def parse(tokens):
    return Parser(tokens).expr()


# TESTS #


import unittest
from tokenizer import tokenize


class Tests(unittest.TestCase):

    def test_adding_numbers(self):
        input = tokenize('3 + 45 + 8')
        expected = BE(BE(3.0, Token(TokenType.PLUS, '+'), 45.0), Token(TokenType.PLUS, '+'), 8.0)
        self.assertEqual(expected, Parser(input).expr())

    def test_subtracting_two_numbers(self):
        input = tokenize('33 - 5')
        expected = BE(33.0, Token(TokenType.MINUS, '-'), 5.0)
        self.assertEqual(expected, Parser(input).expr())

    def test_multiplying_two_numbers(self):
        input = tokenize('3 * 45')
        expected = BE(3.0, Token(TokenType.MUL, '*'), 45.0)
        self.assertEqual(expected, Parser(input).expr())

    def test_dividing_two_numbers(self):
        input = tokenize('30 / 5')
        expected = BE(30.0, Token(TokenType.DIV, '/'), 5.0)
        self.assertEqual(expected, Parser(input).expr())

    def test_negative_number(self):
        input = tokenize('-5')
        expected = UE(Token(TokenType.MINUS, '-'), 5.0)
        self.assertEqual(expected, Parser(input).expr())

    def test_negative_parenthesis(self):
        input = tokenize('-(18/5)')
        expected = UE(Token(TokenType.MINUS, '-'), BE(18.0, Token(TokenType.DIV, '/'), 5.0))
        self.assertEqual(expected, Parser(input).expr())

    def test_correctness_of_sequences(self):
        input = tokenize('3 + 45 * 8')
        expected = BE(3.0, Token(TokenType.PLUS, '+'), BE(45.0, Token(TokenType.MUL, '*'), 8.0))
        self.assertEqual(expected, Parser(input).expr())

    def test_correctness_of_sequences_with_parenthesis(self):
        input = tokenize('2 * (14 + 8)')
        expected = BE(2.0, Token(TokenType.MUL, '*'), BE(14.0, Token(TokenType.PLUS, '+'), 8.0))
        self.assertEqual(expected, Parser(input).expr())

    def test_lack_of_RPAR(self):
        input = tokenize('(3 + 45')
        self.assertRaises(ParseError, Parser(input).expr)

    def test_unexpected_RPAR(self):
        input = tokenize('8 + )9 + 2)')
        self.assertRaises(ParseError, Parser(input).expr)

    def test_too_many_symbols(self):
        input = tokenize('3 --- 8')
        self.assertRaises(ParseError, Parser(input).expr)


