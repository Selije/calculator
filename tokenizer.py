from enum import Enum
import unittest


class TokenType(Enum):
    PLUS = 1
    MINUS = 2
    MUL = 3
    DIV = 4
    LPAR = 5
    RPAR = 6
    NUM = 7
    EOF = 8


class Token:
    def __init__(self, type: TokenType, value: str):
        self.type = type
        self.value = value

    def __repr__(self):
        """repr function is using for tests (like __str__)"""
        return f'token({self.type.name}, {self.value})'

    def __eq__(self, other):
        """ Makes possible to compare tokens with == """
        return self.type == other.type and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


def tokenize(input):
    return []


class Tests(unittest.TestCase):
    def test_string_tokenizing(self):
        input = '3 * 8 + ( 24 / 12 ) - 4'
        expected = [Token(TokenType.NUM, '3'),
                    Token(TokenType.MUL, '*'),
                    Token(TokenType.NUM, '8'),
                    Token(TokenType.PLUS, '+'),
                    Token(TokenType.LPAR, '('),
                    Token(TokenType.NUM, '24'),
                    Token(TokenType.DIV, '/'),
                    Token(TokenType.NUM, '12'),
                    Token(TokenType.RPAR, ')'),
                    Token(TokenType.MINUS, '-'),
                    Token(TokenType.NUM, '4'),
                    Token(TokenType.EOF, '')]

        self.assertEqual(expected, tokenize(input))

