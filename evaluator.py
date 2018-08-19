from ast import BinaryExpr as BE, UnaryExpr as UE
from tokenizer import TokenType, Token


class EvaluateError(Exception):
    pass

def evaluate(expr):
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
        elif op is TokenType.DIV:  #TODO sprawdzić czy nie ma dzielenia przez 0
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
