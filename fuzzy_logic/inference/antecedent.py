from ..sets.fuzzy_set import UMAX, USUM, UPRO, IMIN, IPRO, ISUB
from ..variables import Variable


class Antecedent:
    def __init__(self, norm=IMIN, conorm=UMAX):
        self.norm = norm
        self.conorm = conorm
    
    def __and__(self, other):
        return AndAntecedent(self, other, norm=self.norm, conorm=self.conorm)
    
    def __or__(self, other):
        return OrAntecedent(self, other, norm=self.norm, conorm=self.conorm)

    def eval(self, x):
        raise NotImplementedError()

class BinaryAntecedent(Antecedent):
    def __init__(self, left:Antecedent, right:Antecedent, norm=IMIN, conorm=UMAX):
        super(BinaryAntecedent, self).__init__(norm=norm, conorm=conorm)
        self.left = left
        self.right = right

class AndAntecedent(BinaryAntecedent):
    def eval(self, x):
        return self.norm(self.left.eval(x), self.right.eval(x))

class OrAntecedent(BinaryAntecedent):
    def eval(self, x):
        return self.conorm(self.left.eval(x), self.right.eval(x))

class IsStatementAntecedent(Antecedent):
    def __init__(self, var:Variable, descriptor:str, norm=IMIN, conorm=UMAX):
        super(IsStatementAntecedent, self).__init__(norm=norm, conorm=conorm)
        self.var = var
        self.desc = descriptor

    def eval(self, x):
        return self.var.fuzzify(x, self.desc)
