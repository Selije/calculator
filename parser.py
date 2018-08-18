from tokenizer import TokenType, Token
from ast import BinaryExpr, UnaryExpr

class ParseError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def expr(self):
        return self.add()

    def add(self):
        result = self.unary()
        while self.current_token().type == TokenType.PLUS or self.current_token().type == TokenType.MINUS:
            op = self.advance()
            rh = self.unary()
            result = BinaryExpr(result, op, rh)
        return result

    def unary(self):
        if self.current_token().type == TokenType.NUM:  #is a number
            return float(self.advance().value)

        else:
            self.consume(TokenType.LPAR, 'Expect ( or number.') #is a LPAR or sth else
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