class MembershipFunc:
    def __init__(self, ipoints, func):
        self.ipoints = ipoints
        self.func = func

    def __call__(self, x):
        return self.func(x)
