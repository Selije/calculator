class BinaryExpr:

    def __init__(self, lh, op, rh):
        self.lh = lh
        self.op = op
        self.rh = rh


class Unary:

    def __init__(self, op, rh):
        self.op = op
        self.rh = rh
