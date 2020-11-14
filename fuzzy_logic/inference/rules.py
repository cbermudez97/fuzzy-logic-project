class Rule:
    def __init__(self, antecedent):
        self.antecedent = antecedent

    def eval(self):
        raise NotImplementedError()
    