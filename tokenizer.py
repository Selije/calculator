from enum import Enum
import re


class TokenizeError(Exception):
    pass


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


def tokenize(input: str):
    whitespaces=re.compile(r'^\s')     # ^ position 0, ^s+ whitespace 1 or more times
    num = re.compile(r'^\d+')
    result = []
    position = 0

    while position < len(input):
        current_char = input[position]
        if current_char == '+':
            result.append(Token(TokenType.PLUS, current_char))
            position += 1
        elif current_char == '-':
            result.append(Token(TokenType.MINUS, current_char))
            position += 1
        elif current_char == '*':
            result.append(Token(TokenType.MUL, current_char))
            position += 1
        elif current_char == '/':
            result.append(Token(TokenType.DIV, current_char))
            position += 1
        elif current_char == '(':
            result.append(Token(TokenType.LPAR, current_char))
            position += 1
        elif current_char == ')':
            result.append(Token(TokenType.RPAR, current_char))
            position += 1
        # elif current_char == ' ':
        #     result.append(Token(TokenType., current_char))
        #     position += 1
        elif whitespaces.match(current_char):
            position += 1
        else:
            match = num.match(input[position:])
            if match:
                num_literal = match.group(0)
                result.append(Token(TokenType.NUM, num_literal))
                position += len(num_literal)
            else:
                raise TokenizeError(f'Unexpected character at position {position}')

    result.append(Token(TokenType.EOF, ''))

    return result


# TESTS #

import unittest


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

    def test_invalid_input(self):
        input = '3* CHEESE + 18'
        self.assertRaises(TokenizeError, tokenize, input)
