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

    def eval(self, values:dict):
        raise NotImplementedError()

class BinaryAntecedent(Antecedent):
    def __init__(self, left:Antecedent, right:Antecedent, norm=IMIN, conorm=UMAX):
        super(BinaryAntecedent, self).__init__(norm=norm, conorm=conorm)
        self.left = left
        self.right = right

class AndAntecedent(BinaryAntecedent):
    def eval(self, values:dict):
        return self.norm(self.left.eval(values), self.right.eval(values))

class OrAntecedent(BinaryAntecedent):
    def eval(self, values:dict):
        return self.conorm(self.left.eval(values), self.right.eval(values))

class IsStatementAntecedent(Antecedent):
    def __init__(self, var:Variable, descriptor:str, norm=IMIN, conorm=UMAX):
        super(IsStatementAntecedent, self).__init__(norm=norm, conorm=conorm)
        self.var = var
        self.desc = descriptor

    def eval(self, values:dict):
        return self.var.fuzzify(values[self.var.name], self.desc)
