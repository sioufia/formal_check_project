class Boolean_Exp:
    def __init__(self,evaluation, representation):
        self.evaluation=evaluation
        self.representation=representation

    def __repr__(self):
        return self.representation

    def evaluate(self, variables):
        return self.evaluation(variables)


if __name__=='__main__':
    B=Boolean_Exp(lambda vars : True, "true")
    print(B.evaluate({}))
    print(B)
    B1=Boolean_Exp(lambda vars:vars['X']>=0, "X>=0")
    print(B1.evaluate({"X":4}))
    print(B1)