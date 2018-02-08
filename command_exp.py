"""File containing the class representing the command expression"""

class Command_Exp:
    #need to specify a type of command in order to use it with some criterias
    TYPES=["skip","assign"]

    @staticmethod
    def identite(x):
        return x

    def __init__(self,function_to_execute,representation,type, reverse_fun=None):
        self.to_execute=function_to_execute
        self.representation=representation
        if type in Command_Exp.TYPES:
            self.type=type
        if reverse_fun is None:
            reverse_fun=Command_Exp.identite
        self.reverse_fun=reverse_fun


    def execute(self,variables):
        return self.to_execute(variables)

    def reverse_execute(self, variables):
        return self.reverse_fun(variables)

    def __repr__(self):
        return self.representation

if __name__=="__main__":
    def fun1(variables):
        variables['X']=variables['X']-variables['Y']
        return variables

    C=Command_Exp(fun1,"X:=X-Y")

    print({'X':3,'Y':2})
    print(C.execute({'X':3,'Y':2}))
    print(C)