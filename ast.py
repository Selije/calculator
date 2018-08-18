class BinaryExpr:

    def __init__(self, lh, op, rh):
        self.lh = lh
        self.op = op
        self.rh = rh

    def __repr__(self):
        """repr function is using for tests (like __str__)"""
        return f'({self.lh} {self.op} {self.rh})'

    def __eq__(self, other):
        """ Makes possible to compare tokens with == """
        return self.lh == other.lh and self.op == other.op and self.rh == other.rh

    def __ne__(self, other):
        return not self.__eq__(other)


class UnaryExpr:

    def __init__(self, op, rh):
        self.op = op
        self.rh = rh
